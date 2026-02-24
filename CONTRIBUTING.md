# Contributing

## Add a missing package

1. Add the required package to `packages-0-base.txt`.
2. Run `uv run generator.py resolve` to regenerate `packages-1-resolved.txt`.
   This resolves all transitive dependencies of the base packages.
3. Run `uv run generator.py versions` to regenerate `packages-2-all.txt`.
   This expands each resolved package to all of its available stable versions.
4. Run `uv run generator.py generate` to generate stubs for all packages in `packages-2-all.txt`.
5. Commit `packages-0-base.txt`, `packages-1-resolved.txt`, `packages-2-all.txt`, and the generated stubs, then push to GitHub and open a pull request.
