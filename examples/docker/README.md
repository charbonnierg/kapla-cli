## Multi Platform Python Build Docker Image

This example illustrate how `kapla-cli` can be used to ease building docker images.

### Objectives

Let's build a docker image with:

- Python
- `poetry`
- some useful libraries often required to compile projects
- `scikit-build` also often needed on arm64 to build wheels

1. We want the docker image to be available for Python 3.7, 3.8 and 3.9.

2. We want to be able to specify poetry version

3. We want the docker image to run on:

- x64 processors (servers, desktop, laptop)
- arm64 processors
- armv7 processors (Raspberry Pi)

### The `builder.yml` file

Let's write those constraints in a file named `builder.yml`:

```yaml
---
name: python-build
registry: quara.azurecr.io

description: Python build image for QUARA project

platforms:
  - linux/amd64
  - linux/arm64

build:
  file: Dockerfile.build
  build_args:
    - name: base_image
      type: str
      default: python:3.8
    - name: poetry_version
      type: str
      default: "1.1.5"
```

### Writing the Dockerfile

You can find [the Dockerfile in the same directory as this README file](./Dockerfile).

## Building the images

- Using the default arguments

```bash
k builder build
```

- With different base images with custom tags

```bash
k builder build --base-image=python:3.7 --tags myregistry/myrepo:3.7 --push
k builder build --base-image=python:3.8 --tags myregistry/myrepo:3.8 --push
k builder build --base-image=python:3.9 --tags myregistry/myrepo:3.9 --push
```

- Using a different poetry version

```bash
k builder build --poetry-version=1.1.4 --tags myregistry/myrepo:poetry-1.1.4 --push
```
