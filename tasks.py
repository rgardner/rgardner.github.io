"""Blog management tasks."""

from pathlib import Path
import shutil
import subprocess
from typing import List

from invoke import task


JEKYLL_VERSION = "3.8"


def get_repo_root() -> Path:
    """Returns git repository root."""
    return Path(__file__).parent.absolute()


def get_base_docker_command() -> List[str]:
    repo_root = get_repo_root()
    return [
        "docker",
        "run",
        "--rm",
        f"--volume={repo_root}:/srv/jekyll",
        f"--volume={repo_root}/vendor/bundle:/usr/local/bundle",
        "--publish",
        "4000:4000",
        f"jekyll/jekyll:{JEKYLL_VERSION}",
    ]


@task
def serve(c):
    """Serves auto-reloading blog via Docker."""
    repo_root = get_repo_root()
    docker_command = get_base_docker_command()
    docker_command.extend(["jekyll", "serve", "--drafts", "--incremental"])
    c.run(" ".join(docker_command))


@task
def test(c):
    """Runs blog tests."""
    repo_root = get_repo_root()
    docker_command = get_base_docker_command()
    docker_command.extend(["/bin/bash", "-c", "'script/install && script/run-tests'"])
    c.run(" ".join(docker_command))


@task
def clean(c):
    """Cleans build and vendor directories."""
    shutil.rmtree(get_repo_root() / "_site", ignore_errors=True)
    shutil.rmtree(get_repo_root() / "vendor", ignore_errors=True)


@task
def new_post(c):
    """Creates a new draft post."""
    c.run("script/new-post")


@task
def update_dependencies(c):
    """Updates blog's Ruby Gems."""
    repo_root = get_repo_root()
    docker_command = get_base_docker_command()
    docker_command.extend(["/bin/bash", "-c", "'bundle update'"])
    c.run(" ".join(docker_command))
