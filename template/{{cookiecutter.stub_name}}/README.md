# {{ cookiecutter.stub_name }}

Python type stubs for {% if cookiecutter.maven_url %}[`{{ cookiecutter.readable_name }}`]({{ cookiecutter.maven_url }}){% else %}{{ cookiecutter.readable_name }}{% endif %}, generated with [chaquopy-stubgen](https://github.com/chaquo/chaquopy) `{{ cookiecutter.stubgen_version }}`.

## Usage

These are stub-only packages ([PEP 561](https://peps.python.org/pep-0561/)). Install them alongside your project to get type checking support for `{{ cookiecutter.readable_name }}` when using [Chaquopy](https://chaquo.com/chaquopy/).

```bash
pip install {{ cookiecutter.stub_name }}=={{ cookiecutter.version }}
```