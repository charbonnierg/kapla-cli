import pathlib

import pytest

from kapla.cli.projects import Project


@pytest.fixture
def kapla_cli_project() -> Project:
    return Project(pathlib.Path(__file__).parent.parent)
