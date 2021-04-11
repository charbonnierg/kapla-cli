#!/usr/bin/env bash

set -eu

ROOT=$(realpath $(dirname $(dirname $(echo "$0"))))
PYTHON="${PYTHON:-"python3"}"

# Create virtual environment if it does not exist yet
function createVenv {
  cd $ROOT
  if [ ! -d ".venv/" ]; then
    echo -e "Creating virtual environment in $ROOT/.venv directory"
    $PYTHON -m venv .venv
  fi
  cd -
}

function activateVenv {
  cd $ROOT
  # Activate virtual environment
  echo -e "Activating virtual environment"
  . .venv/bin/activate
  cd -
}

# First make sure virtual environment exists
createVenv
# Then activate virtual environment
activateVenv
