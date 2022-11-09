"""Blog management tasks."""

# Work around https://github.com/pyinvoke/invoke/issues/833
import inspect

if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec

import pathlib
import shutil
from typing import List

import invoke


JEKYLL_VERSION = "3.8"


def get_repo_root() -> pathlib.Path:
    """Returns git repository root."""
    return pathlib.Path(__file__).parent.absolute()


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


@invoke.task
def serve(ctx):
    """Serves auto-reloading blog via Docker."""
    docker_command = get_base_docker_command()
    docker_command.extend(["jekyll", "serve", "--drafts", "--incremental"])
    ctx.run(" ".join(docker_command))


@invoke.task
def test(ctx):
    """Runs blog tests."""
    docker_command = get_base_docker_command()
    docker_command.extend(["/bin/bash", "-ctx", "'script/install && script/htmlproofer && script/github-pages-health-check'"])
    ctx.run(" ".join(docker_command))


@invoke.task
def clean(ctx):
    """Cleans build and vendor directories."""
    shutil.rmtree(get_repo_root() / "_site", ignore_errors=True)
    shutil.rmtree(get_repo_root() / "vendor", ignore_errors=True)


@invoke.task
def new_post(ctx):
    """Creates a new draft post."""
    ctx.run("script/new-post")


@invoke.task
def update_dependencies(ctx):
    """Updates blog's Ruby Gems."""
    docker_command = get_base_docker_command()
    docker_command.extend(["/bin/bash", "-ctx", "'bundle update'"])
    ctx.run(" ".join(docker_command))
