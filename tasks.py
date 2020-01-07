"""Blog management tasks."""

from pathlib import Path
import shutil
import subprocess
from subprocess import PIPE

from invoke import task


def get_repo_root() -> Path:
    """Returns git repository root."""
    proc = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], stdout=PIPE, check=True, text=True,
    )
    return Path(proc.stdout.strip())


@task
def serve(c):
    """Serves auto-reloading blog via Docker."""
    repo_root = get_repo_root()
    c.run(
        f"docker run --volume={repo_root}:/srv/jekyll --publish 4000:4000 jekyll/jekyll jekyll serve --drafts --incremental",
    )


@task
def test(c):
    """Runs blog tests."""
    repo_root = get_repo_root()
    c.run(
        f"docker run --volume={repo_root}:/srv/jekyll jekyll/jekyll /bin/bash -c 'script/install && script/run-tests'"
    )


@task
def clean(c):
    """Cleans build directory."""
    site_dir = get_repo_root() / "_site"
    shutil.rmtree(site_dir, ignore_errors=True)


@task
def new_post(c):
    """Creates a new draft post."""
    c.run("script/new-post")


@task
def update_dependencies(c):
    """Updates blog's Ruby Gems."""
    repo_root = get_repo_root()
    c.run("docker run --volume={repo_root}:/src/jekyll bundle update")
