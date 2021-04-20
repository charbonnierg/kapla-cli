from kapla.cli.projects import Monorepo, Project


def test_project_name(kapla_cli_core_project: Project) -> None:
    assert kapla_cli_core_project.pyproject.name == "kapla-cli-core"


def test_repo_name(kapla_cli_repo: Monorepo) -> None:
    assert kapla_cli_repo.pyproject.name == "kapla-cli-monorepo"


def test_repo_package(kapla_cli_repo: Monorepo) -> None:
    assert [project.pyproject.name for project in kapla_cli_repo.get_packages()] == [
        "kapla-cli-monorepo",
        "kapla-cli",
        "kapla-cli-core",
    ]
