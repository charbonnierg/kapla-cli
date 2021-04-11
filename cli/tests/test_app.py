from typing import Callable

from typer.testing import Result

K = Callable[..., Result]


def test_k(k: K) -> None:
    result = k()
    assert result.exit_code == 0
    assert "Python monorepo toolkit" in result.stdout
    assert "Options:" in result.stdout
    assert "Commands:" in result.stdout


def test_lint(k: K) -> None:
    result = k("lint")
    assert result.exit_code == 0


def test_format(k: K) -> None:
    result = k("format")
    assert result.exit_code == 0


def test_typecheck(k: K) -> None:
    result = k("typecheck")
    assert result.exit_code == 0


def test_install(k: K) -> None:
    result = k("install")
    assert result.exit_code == 0


def test_build(k: K) -> None:
    result = k("build")
    assert result.exit_code == 0


def test_clean(k: K) -> None:
    result = k("clean")
    assert result.exit_code == 0
