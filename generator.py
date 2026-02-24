#!/usr/bin/env python3
"""
Chaquopy stub generation pipeline.

  generator.py resolve   – resolve transitive Maven dependencies
  generator.py versions  – enumerate all stable versions per package
  generator.py generate  – generate .pyi stubs for every coordinate

Usage:
    uv run generator.py resolve   [--base packages-0-base.txt]       [--out packages-1-resolved.txt]
    uv run generator.py versions  [--base packages-1-resolved.txt]   [--out packages-2-all.txt]
    uv run generator.py generate  [--packages packages-2-all.txt] [--clean]
"""

from __future__ import annotations

import argparse
import datetime
import importlib.metadata
import logging
import re
from dataclasses import dataclass
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import requests
from cookiecutter.main import cookiecutter as _cookiecutter
from lxml import etree

log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ROOT_DIR = Path(__file__).parent
CACHE_DIR = ROOT_DIR / ".cache" / "pom"
AUTOGEN_DIR = ROOT_DIR / "autogen"
TEMPLATE_DIR = ROOT_DIR / "template"

MAVEN_REPOS = [
    "https://repo1.maven.org/maven2",
    "https://dl.google.com/dl/android/maven2",
]

# ---------------------------------------------------------------------------
# Regexes
# ---------------------------------------------------------------------------

# Matches a concrete version in plain form (1.2.3) or an exact single-version
# range ([1.2.3], [1.2.3), (1.2.3], (1.2.3)). Does NOT match:
#   multi-ranges  [1.0,2.0)  → contains comma
#   unresolved    ${prop}    → contains $
_CONCRETE_VERSION = re.compile(r"^[\[(]?([^$,\[\]()]+)[\])]?$")

# Matches Android platform coordinates like "android-35"
_PLATFORM_COORD = re.compile(r"^android-(\d+)$")

# ---------------------------------------------------------------------------
# Coordinate types
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class PlatformCoord:
    """An Android platform coordinate, e.g. android-35."""
    api_level: int

    @property
    def name(self) -> str:
        return f"android-{self.api_level}"

    @property
    def version(self) -> str:
        return str(self.api_level)

    @property
    def stub_name(self) -> str:
        return "chaquopy-stubs-android"

    @property
    def readable_name(self) -> str:
        return f"Android API Level {self.api_level}"

    @property
    def stubgen_coord(self) -> str:
        return self.name


@dataclass(frozen=True)
class MavenCoord:
    """A Maven coordinate, e.g. com.example:artifact:1.0.0."""
    group_id: str
    artifact_id: str
    version: str

    @property
    def name(self) -> str:
        return f"{self.group_id}:{self.artifact_id}:{self.version}"

    @property
    def stub_name(self) -> str:
        group_slug = self.group_id.replace(".", "-")
        artifact_slug = self.artifact_id.replace(".", "-")
        return f"chaquopy-stubs-{group_slug}-{artifact_slug}"

    @property
    def readable_name(self) -> str:
        return f"{self.group_id}:{self.artifact_id}"

    @property
    def stubgen_coord(self) -> str:
        return self.name


Coordinate = PlatformCoord | MavenCoord

# ---------------------------------------------------------------------------
# Shared logging setup
# ---------------------------------------------------------------------------

def _setup_logging(verbose: bool) -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)-5s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG if verbose else logging.INFO,
        stream=sys.stderr,
    )

# ---------------------------------------------------------------------------
# Coordinate helpers
# ---------------------------------------------------------------------------

def is_stable(version: str) -> bool:
    """Return True if the version string looks like a stable release."""
    return "-" not in version


def parse_packages_file(path: Path) -> list[Coordinate]:
    """Parse a packages file and return a list of Coordinate objects.

    Supported line formats:
      android-35                      → PlatformCoord(api_level=35)
      group:artifact:version          → MavenCoord(group, artifact, version)
    """
    entries: list[Coordinate] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = _PLATFORM_COORD.match(line)
        if m:
            entries.append(PlatformCoord(api_level=int(m.group(1))))
            continue
        parts = line.split(":")
        if len(parts) == 3:
            entries.append(MavenCoord(parts[0], parts[1], parts[2]))
        else:
            log.warning("Skipping (expected 'android-N' or 'group:artifact:version'): %r", line)
    return entries

# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

def http_get(url: str) -> bytes | None:
    """GET a URL; return body bytes, or None on 404 / error."""
    log.debug("GET %s", url)
    try:
        r = requests.get(url, timeout=30)
        if r.status_code == 404:
            return None
        r.raise_for_status()
        return r.content
    except requests.HTTPError as e:
        log.warning("HTTP %s: %s", e.response.status_code, url)
        return None
    except requests.RequestException as e:
        log.error("Request failed (%s): %s", e, url)
        return None

# ---------------------------------------------------------------------------
# POM parsing
# ---------------------------------------------------------------------------

def _parse_pom(raw: bytes) -> etree._Element:
    """Parse POM XML and strip all namespace prefixes for simple tag access."""
    root = etree.fromstring(raw)
    for elem in root.iter():
        if elem.tag and isinstance(elem.tag, str) and elem.tag[0] == "{":
            elem.tag = elem.tag.split("}", 1)[1]
    return root


def _text(elem: etree._Element | None) -> str:
    """Safely return stripped text of an element, or empty string."""
    return (elem.text or "").strip() if elem is not None else ""


def fetch_pom(group_id: str, artifact_id: str, version: str) -> etree._Element | None:
    """Fetch and cache a POM from Maven Central or Google Maven."""
    group_path = group_id.replace(".", "/")
    pom_file = f"{artifact_id}-{version}.pom"
    cache_path = CACHE_DIR / group_path / artifact_id / version / pom_file

    if cache_path.exists():
        log.debug("POM cache hit: %s:%s:%s", group_id, artifact_id, version)
        return _parse_pom(cache_path.read_bytes())

    for repo in MAVEN_REPOS:
        url = f"{repo}/{group_path}/{artifact_id}/{version}/{pom_file}"
        raw = http_get(url)
        if raw is not None:
            log.debug("Fetched POM %s:%s:%s from %s", group_id, artifact_id, version, repo)
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            cache_path.write_bytes(raw)
            log.debug("Cached POM to %s", cache_path.relative_to(ROOT_DIR))
            return _parse_pom(raw)

    log.warning("POM not found in any repo: %s:%s:%s", group_id, artifact_id, version)
    return None

# ---------------------------------------------------------------------------
# Version queries
# ---------------------------------------------------------------------------

def maven_latest_stable_version(group_id: str, artifact_id: str) -> str | None:
    """Return the latest stable version via maven-metadata.xml."""
    log.debug("Looking up latest stable version for %s:%s", group_id, artifact_id)
    versions = fetch_all_stable_versions(group_id, artifact_id)
    if versions:
        log.debug(" → %s:%s:%s", group_id, artifact_id, versions[0])
        return versions[0]
    log.warning("Could not determine latest stable version for %s:%s", group_id, artifact_id)
    return None


def fetch_all_stable_versions(group_id: str, artifact_id: str) -> list[str]:
    """Return all stable versions (newest first) via maven-metadata.xml."""
    group_path = group_id.replace(".", "/")
    for repo in MAVEN_REPOS:
        meta_url = f"{repo}/{group_path}/{artifact_id}/maven-metadata.xml"
        raw = http_get(meta_url)
        if raw is None:
            continue
        try:
            root = etree.fromstring(raw)
            versions = [v.text for v in root.findall(".//version") if v.text]
            stable = [v for v in reversed(versions) if is_stable(v)]
            if stable:
                return stable
        except etree.XMLSyntaxError:
            continue

    return []


# ===========================================================================
# Stage 1 – resolve
# ===========================================================================

def resolve_pom_deps(
    group_id: str,
    artifact_id: str,
    version: str,
    resolved: dict[str, str],
    visited_poms: set[str],
    depth: int = 0,
) -> None:
    """Recursively resolve compile/runtime dependencies from POM files."""
    coord_key = f"{group_id}:{artifact_id}:{version}"
    if coord_key in visited_poms:
        log.debug("[cached] %s", coord_key)
        return
    visited_poms.add(coord_key)

    indent = " " * depth
    log.info("%s→ %s", indent, coord_key)

    pom = fetch_pom(group_id, artifact_id, version)
    if pom is None:
        return

    # Collect <properties> for variable substitution
    props: dict[str, str] = {
        "project.groupId": group_id,
        "project.artifactId": artifact_id,
        "project.version": version,
    }
    for prop in pom.findall("./properties/*"):
        if prop.text:
            props[prop.tag] = prop.text.strip()

    def resolve_val(val: str) -> str:
        for k, v in props.items():
            val = val.replace(f"${{{k}}}", v)
        return val

    # Only direct <dependencies>, NOT <dependencyManagement/dependencies>
    for dep in pom.findall("./dependencies/dependency"):
        dep_group    = resolve_val(_text(dep.find("groupId")))
        dep_artifact = resolve_val(_text(dep.find("artifactId")))
        dep_version  = resolve_val(_text(dep.find("version")))
        dep_scope    = _text(dep.find("scope")) or "compile"
        dep_optional = _text(dep.find("optional"))

        if not dep_group or not dep_artifact:
            continue
        if dep_scope not in ("compile", "runtime"):
            log.debug("Skipping %s:%s (scope=%s)", dep_group, dep_artifact, dep_scope)
            continue
        if dep_optional == "true":
            continue

        ga = f"{dep_group}:{dep_artifact}"
        m = _CONCRETE_VERSION.match(dep_version)
        if m:
            effective_version = m.group(1)
            if effective_version != dep_version:
                log.debug("Resolved version spec %s → %s", dep_version, effective_version)
            resolved.setdefault(ga, effective_version)
            resolve_pom_deps(dep_group, dep_artifact, effective_version, resolved, visited_poms, depth + 1)
        else:
            log.info("%s  unresolvable version %r for %s, skipping…", indent, dep_version, ga)


def cmd_resolve(args: argparse.Namespace) -> None:
    base_file = Path(args.base)
    out_file = Path(args.out)

    if not base_file.exists():
        log.error("File not found: %s", base_file)
        sys.exit(1)

    base_packages = parse_packages_file(base_file)
    platform = [c for c in base_packages if isinstance(c, PlatformCoord)]
    maven    = [c for c in base_packages if isinstance(c, MavenCoord)]
    log.info("Base packages (%d): %d platform, %d Maven",
             len(base_packages), len(platform), len(maven))

    resolved: dict[str, str] = {f"{c.group_id}:{c.artifact_id}": c.version for c in maven}
    visited_poms: set[str] = set()

    for c in maven:
        log.info("")
        log.info("=== Resolving %s ===", c.name)
        resolve_pom_deps(c.group_id, c.artifact_id, c.version, resolved, visited_poms)

    platform_lines = sorted(c.name for c in platform)
    maven_lines    = sorted(f"{ga}:{ver}" for ga, ver in resolved.items())
    all_lines = platform_lines + maven_lines
    out_file.write_text("\n".join(all_lines) + "\n", encoding="utf-8")
    log.info("")
    log.info("Wrote %d packages to %s (%d platform, %d Maven)",
             len(all_lines), out_file, len(platform_lines), len(maven_lines))


# ===========================================================================
# Stage 2 – versions
# ===========================================================================

def cmd_versions(args: argparse.Namespace) -> None:
    base_file = Path(args.base)
    out_file = Path(args.out)

    if not base_file.exists():
        log.error("File not found: %s", base_file)
        sys.exit(1)

    packages = parse_packages_file(base_file)
    log.info("Packages (%d) loaded from %s", len(packages), base_file)

    lines: list[str] = []
    for i, coord in enumerate(packages, 1):
        if isinstance(coord, PlatformCoord):
            # Platform entries have no Maven versions — pass through as-is
            log.info("[%d/%d] %s (platform, pass-through)", i, len(packages), coord.name)
            lines.append(coord.name)
            continue
        log.info("[%d/%d] Fetching versions for %s:%s…", i, len(packages), coord.group_id, coord.artifact_id)
        versions = fetch_all_stable_versions(coord.group_id, coord.artifact_id)
        log.info(" → %d stable versions found", len(versions))
        for v in versions:
            lines.append(f"{coord.group_id}:{coord.artifact_id}:{v}")

    out_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
    log.info("")
    log.info("Wrote %d coordinates to %s", len(lines), out_file)


# ===========================================================================
# Stage 3 – generate
# ===========================================================================

def render_template(
    coord: Coordinate,
    stub_version: str,
    stubgen_version: str,
    target_dir: Path,
) -> None:
    """Render the cookiecutter template into target_dir."""
    if isinstance(coord, PlatformCoord):
        group_id, artifact_id = "", coord.name
    else:
        group_id, artifact_id = coord.group_id, coord.artifact_id
    with tempfile.TemporaryDirectory() as tmp:
        _cookiecutter(
            str(TEMPLATE_DIR),
            no_input=True,
            extra_context={
                "stub_name": coord.stub_name,
                "group_id": group_id,
                "artifact_id": artifact_id,
                "readable_name": coord.readable_name,
                "version": coord.version,
                "stub_version": stub_version,
                "stubgen_version": stubgen_version,
            },
            output_dir=tmp,
            overwrite_if_exists=True,
        )
        src = Path(tmp) / coord.stub_name
        shutil.copytree(src, target_dir, dirs_exist_ok=True)
    log.debug("Rendered template → %s", target_dir.relative_to(ROOT_DIR))


def run_stubgen(coordinate: str, output_dir: Path) -> bool:
    """Invoke chaquopy-stubgen for the given coordinate. Returns True on success."""
    cmd = [
        sys.executable,
        "-m", "chaquopy_stubgen",
        coordinate,
        "--output-dir", str(output_dir),
    ]
    log.debug("Running: %s", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        log.error(
            "chaquopy-stubgen failed for %s (exit %d)\n%s",
            coordinate, result.returncode,
            (result.stderr or result.stdout).strip(),
        )
        return False
    if result.stdout.strip():
        log.debug(result.stdout.strip())
    return True


def process_coordinate(
    coord: Coordinate,
    build_date: str,
    stubgen_version: str,
    index: int,
    total: int,
) -> bool:
    """Generate stubs + template files for one coordinate. Returns True on success."""
    version_dir = AUTOGEN_DIR / coord.stub_name / coord.version

    log.info("[%d/%d] %s", index, total, coord.name)

    if version_dir.exists() and any(version_dir.iterdir()):
        log.info("  → already exists, skipping")
        return True

    version_dir.mkdir(parents=True, exist_ok=True)
    src_dir = version_dir / "src"

    success = run_stubgen(coord.stubgen_coord, src_dir)
    if not success:
        return False

    # stubgen may delete+recreate output_dir; ensure it exists before writing template
    src_dir.mkdir(parents=True, exist_ok=True)
    stub_version = f"{coord.version}.{build_date}"
    render_template(coord, stub_version, stubgen_version, version_dir)
    log.debug("  → done: %s", version_dir.relative_to(ROOT_DIR))
    return True


def cmd_generate(args: argparse.Namespace) -> None:
    if args.clean and AUTOGEN_DIR.exists():
        log.info("Deleting %s …", AUTOGEN_DIR)
        shutil.rmtree(AUTOGEN_DIR)

    packages_file = Path(args.packages)
    if not packages_file.exists():
        log.error("Packages file not found: %s", packages_file)
        sys.exit(1)

    entries = parse_packages_file(packages_file)
    if not entries:
        log.warning("No entries found in %s", packages_file)
        sys.exit(0)

    total = len(entries)
    log.info("Generating stubs for %d coordinates from %s", total, packages_file.name)

    build_date = datetime.date.today().strftime("%Y%m%d")
    stubgen_version = importlib.metadata.version("chaquopy-stubgen")
    log.info("Build date: %s, chaquopy-stubgen: %s", build_date, stubgen_version)

    failed: list[str] = []
    for i, coord in enumerate(entries, 1):
        ok = process_coordinate(coord, build_date, stubgen_version, i, total)
        if not ok:
            failed.append(coord.name)

    if failed:
        log.warning("%d coordinate(s) failed:", len(failed))
        for coord in failed:
            log.warning("  %s", coord)
    else:
        log.info("All %d coordinates processed successfully.", total)


# ===========================================================================
# CLI
# ===========================================================================

def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable debug logging")
    sub = parser.add_subparsers(dest="command", required=True)

    # resolve
    p_resolve = sub.add_parser("resolve", help="Resolve transitive deps → packages-1-resolved.txt")
    p_resolve.add_argument("--base", default=str(ROOT_DIR / "packages-0-base.txt"))
    p_resolve.add_argument("--out",  default=str(ROOT_DIR / "packages-1-resolved.txt"))

    # versions
    p_versions = sub.add_parser("versions", help="Enumerate stable versions → packages-2-all.txt")
    p_versions.add_argument("--base", default=str(ROOT_DIR / "packages-1-resolved.txt"))
    p_versions.add_argument("--out",  default=str(ROOT_DIR / "packages-2-all.txt"))

    # generate
    p_generate = sub.add_parser("generate", help="Generate stubs → autogen/")
    p_generate.add_argument("--packages", default=str(ROOT_DIR / "packages-2-all.txt"),
                            help="Input file (default: packages-2-all.txt)")
    p_generate.add_argument("--clean", action="store_true",
                            help="Delete autogen/ before generating")

    args = parser.parse_args()
    _setup_logging(args.verbose)

    if args.command == "resolve":
        cmd_resolve(args)
    elif args.command == "versions":
        cmd_versions(args)
    elif args.command == "generate":
        cmd_generate(args)


if __name__ == "__main__":
    main()
