from typing import Callable, Generator

import pytest
from typer.testing import Result

from kapla.cli.app import app

K = Callable[..., Result]


@pytest.fixture
def k() -> Generator[K, None, None]:
    from typer.testing import CliRunner, Result

    runner = CliRunner()

    def func(*args: str) -> Result:
        return runner.invoke(app, args)

    yield func
