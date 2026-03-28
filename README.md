# chaquopy-stubs
Python type stubs for Android/Maven libraries, generated with [chaquopy-stubgen](https://github.com/timrid/chaquopy-stubgen).

Each stub package corresponds to a Maven artifact and provides `.pyi` type annotations for use with [Chaquopy](https://chaquo.com/chaquopy/) — the Python SDK for Android.

## Installation

### Android platform stubs
To install the stubs for the Android SDK (API Level 35):

```bash
pip install chaquopy-stubs-android==35.*
```

A build date is appended to each version, so packages are published under a scheme like `35.20260325`. The build date indicates which version of chaquopy-stubgen was used to generate the stubs.

### Maven artifact stubs
Stub packages are named after their Maven coordinate:

```
chaquopy-stubs-{group_id}-{artifact_id}
```

For example, if your Android app depends on `com.google.android.material:material:1.12.0`, install the matching stubs:

```bash
pip install chaquopy-stubs-com-google-android-material-material==1.12.*
```

Stubs are only published for the latest patch release of each minor version. For example, if `1.12.4` is the latest patch of the `1.12.x` series, only `1.12.4` is available — not `1.12.0`, `1.12.1`, etc. Therefore, always use `==1.12.*` in your requirements to automatically pick the latest available patch.

Additionally, a build date is appended to each version, so packages are published under a scheme like `1.12.4.20260325`. The build date indicates which version of `chaquopy-stubgen` was used to generate the stubs.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for instructions on how to add missing packages.

