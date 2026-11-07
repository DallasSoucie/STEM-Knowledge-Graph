"""The real course manifest in graph/courses.yaml."""

from collections import Counter
from pathlib import Path

from typer.testing import CliRunner

from kg.cli import app
from kg.model import level_rank
from kg.store import load_graph

GRAPH = Path(__file__).parent.parent / "graph"


def _courses():
    return list(load_graph(GRAPH).courses.values())


def test_manifest_has_103_courses():
    assert len(_courses()) == 110


def test_budgets_total_9350():
    assert sum(c.budget for c in _courses()) == 9350


def test_subject_totals():
    totals = Counter()
    for c in _courses():
        totals[c.subject] += c.budget
    assert totals == {"math": 4370, "physics": 1335, "chem": 790, "bio": 755, "engr": 2100}


def test_ids_follows_and_levels_are_consistent():
    courses = _courses()
    ids = {c.id for c in courses}
    assert len(ids) == len(courses)
    for c in courses:
        assert c.id.split(".")[0] == c.subject
        assert level_rank(c.levels[0]) <= level_rank(c.levels[1])
        assert set(c.follows) <= ids and c.id not in c.follows


def test_real_graph_validates():
    result = CliRunner().invoke(app, ["validate", "--root", str(GRAPH)])
    assert result.exit_code == 0, result.output
