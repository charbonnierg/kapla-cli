# Kapla CLI Core

`kapla` cli is a tool to manage python mono repo easily using `poetry` and `git` and many other well known python tools. The `kapla-cli-core` package exposes two classes that can be used to manipulate monorepo within a Python application and is a dependency of `kapla-cli` package.

## Example usage:

```python
from kapla.cli import Project

# Find a pyproject named "my-project" recursively from the current directory
project = Project("my-project")
```

### Build the project (optionnally specify format, by defaults "sidst" and "wheel" are used)

```bash
project.build(format="wheel")
```

### Install the project (optionnaly specify extras)

```bash
project.install(extras=[])
```

### Lint the project

```bash
project.lint()
```

### Format the project

```bash
project.format()
```

### Run mypy against the project sources

```bash
project.typecheck()
```

### Test the project

```bash
project.test()
```

### Bump the project version

```bash
project.bump("new_version")
```
