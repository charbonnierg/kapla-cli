#!/usr/bin/env bash

set -eu

CI=${CI:-"0"}

if [[ "$CI" -eq "0" ]]; then
    . $(dirname "$0")/env.sh
fi

# Go to core package
cd core
echo -e "Installing core package using poetry install"
poetry install
cd -

# Install cli package
cd cli
echo -e "Installing cli using poetry install"
poetry install
cd -

# Install pre-commit hooks
echo -e "Installing pre-commit hooks"
pre-commit install

# Install pre-commit commit-msg hooks
pre-commit install --hook-type commit-msg
