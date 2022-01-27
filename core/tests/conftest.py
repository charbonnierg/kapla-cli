import pathlib

import pytest
from kapla.cli.projects import Monorepo, Project


@pytest.fixture
def kapla_cli_core_project() -> Project:
    return Project(pathlib.Path(__file__).parent.parent)


@pytest.fixture
def kapla_cli_repo() -> Project:
    return Monorepo(pathlib.Path(__file__).parent.parent.parent)
