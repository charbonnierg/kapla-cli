#!/usr/bin/env bash

set -eu

CI=${CI:-"0"}
SCRIPTS=$(dirname "$0")
ROOT=$(dirname $SCRIPTS)

if [[ "$CI" -eq "0" ]]; then
    . $(dirname "$0")/env.sh
fi



# Remove packagess
pip freeze | grep kapla | cut -f1 -d "=" | xargs pip uninstall -y 2> /dev/null || true
pip freeze | grep kapla | cut -f1 -d "=" | xargs pip uninstall -y 2> /dev/null || true
rm -f ./**/poetry.lock

# Go to core package
cd "$ROOT/core"
echo -e "Installing core package using poetry install"
poetry install
cd -

# Install cli package
cd "$ROOT/cli"
echo -e "Installing cli using poetry install"
poetry install
cd -

cd "$ROOT"
# Install pre-commit hooks
echo -e "Installing pre-commit hooks"
pre-commit install

# Install pre-commit commit-msg hooks
pre-commit install --hook-type commit-msg
cd -