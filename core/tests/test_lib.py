from kapla.cli.projects import Project


def test_repo_name(kapla_cli_project: Project) -> None:
    assert kapla_cli_project.pyproject.name == "kapla-cli-core"
