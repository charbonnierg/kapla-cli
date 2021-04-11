# Kapla CLI

This repository contains a tool to manage python mono repo easily using `poetry` and `git`.

It can build and distribute python packages independently from each other.

Run the `k` command to learm more about its features:

```bash
k --help
```

### Installing the packages for development

In order to install all packages, run the following command:

```bash
k install
```

### Running the tests

Tests are ran using `pytest` using the following command:

```bash
k test
```

> Note: You can optionnally specify pytest markers: `k test -m "databases"` or `k test -m "not databases"` for example.

### Linting the code

Code is linted using `flake8` using the following command:

```bash
k lint
```

### Formatting the code

Code is formatted using `black` using the following command:

```bash
k format
```

### Adding a new package

In order to add a new package, use the `repo` tool:

- In order to create a library:

```bash
k new library my-library
```

- In order to create a plugin:

```bash
k new plugin my-plugin
```

- In order to create an application:

```bash
k new application my-app
```
