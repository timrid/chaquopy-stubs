# chaquopy-stubs

Python type stubs for Android/Maven libraries, generated with [chaquopy-stubgen](https://github.com/timrid/chaquopy-stubgen).

Each stub package corresponds to a Maven artifact and provides `.pyi` type annotations for use with [Chaquopy](https://chaquo.com/chaquopy/) — the Python SDK for Android.

## Installation

### Android platform stubs

To install the stubs for the Android SDK (API Level 35):

```bash
pip install chaquopy-stubs-android==35
```

### Maven artifact stubs

Stub packages are named after their Maven coordinate:

```
chaquopy-stubs-{group_id}-{artifact_id}
```

For example, if your Android app depends on `com.google.android.material:material:1.13.0`, install the matching stubs:

```bash
pip install chaquopy-stubs-com-google-android-material-material==1.13.0
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for instructions on how to add missing packages.

