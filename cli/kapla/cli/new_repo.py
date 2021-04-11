from pathlib import Path
import sys

import typer

from kapla.cli.projects import Monorepo
from kapla.cli.utils import run


def create_repo() -> Monorepo:
    yesno = typer.confirm("Do you want to create a new project ?")
    if not yesno:
        raise sys.exit(1)
    run("poetry init")
    repo = Monorepo(Path.cwd())
    repo.set_include_packages([])

    return repo
