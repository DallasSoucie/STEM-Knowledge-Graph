"""The pre-commit hook blocks commits whose graph fails validate."""

import os
import shutil
import subprocess
import sys
from pathlib import Path

from conftest import edge, valid_graph
from kg.store import write_graph

HOOK = Path(__file__).parent.parent / ".githooks" / "pre-commit"


def _git(repo: Path, *args: str, env_extra: dict | None = None):
    env = {**os.environ, "KG_PYTHON": sys.executable, **(env_extra or {})}
    return subprocess.run(
        ["git", "-c", "user.name=t", "-c", "user.email=t@t", *args],
        cwd=repo, capture_output=True, text=True, env=env,
    )


def _repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    (repo / ".githooks").mkdir(parents=True)
    shutil.copy(HOOK, repo / ".githooks" / "pre-commit")
    _git(repo, "init", "-q")
    _git(repo, "config", "core.hooksPath", ".githooks")
    _git(repo, "config", "core.autocrlf", "false")
    return repo


def _write(repo: Path, cyclic: bool) -> None:
    kg = valid_graph()
    kg.root = repo / "graph"
    if cyclic:
        kg.topics["math.a.one"].prerequisites = [edge("math.a.three")]
    write_graph(kg)


def test_hook_blocks_commit_with_invalid_graph(tmp_path):
    repo = _repo(tmp_path)
    _write(repo, cyclic=True)
    _git(repo, "add", "-A")
    result = _git(repo, "commit", "-m", "bad")
    assert result.returncode != 0
    assert "cycle" in result.stdout + result.stderr


def test_hook_allows_commit_with_clean_graph(tmp_path):
    repo = _repo(tmp_path)
    _write(repo, cyclic=False)
    _git(repo, "add", "-A")
    result = _git(repo, "commit", "-m", "good")
    assert result.returncode == 0, result.stdout + result.stderr


def test_hook_blocks_with_message_when_python_is_missing(tmp_path):
    repo = _repo(tmp_path)
    _write(repo, cyclic=False)
    _git(repo, "add", "-A")
    result = _git(repo, "commit", "-m", "x", env_extra={"KG_PYTHON": str(tmp_path / "nope")})
    assert result.returncode != 0
    assert "venv" in result.stdout + result.stderr
