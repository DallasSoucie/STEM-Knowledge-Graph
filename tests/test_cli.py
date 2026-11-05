"""CLI behaviour through typer's CliRunner."""

from typer.testing import CliRunner

from conftest import FIXTURE, edge
from kg.cli import app
from kg.store import load_graph, write_graph

runner = CliRunner()


def run(*args):
    return runner.invoke(app, list(args))


def test_validate_clean_sample_exits_0():
    result = run("validate", "--root", str(FIXTURE))
    assert result.exit_code == 0, result.output
    assert "0 errors" in result.output


def test_validate_broken_graph_exits_1_and_names_rule(sample_copy):
    kg = load_graph(sample_copy)
    tid = next(iter(kg.topics))
    kg.topics[tid] = kg.topics[tid].model_copy(
        update={"prerequisites": [edge("math.nope.missing")]}
    )
    write_graph(kg)
    result = run("validate", "--root", str(sample_copy))
    assert result.exit_code == 1
    assert "error dangling-reference" in result.output
    assert tid in result.output


def test_validate_malformed_yaml_names_file_without_traceback(tmp_path):
    (tmp_path / "math").mkdir()
    (tmp_path / "math" / "a.yaml").write_text("course: [unclosed\n", encoding="utf-8")
    result = run("validate", "--root", str(tmp_path))
    assert result.exit_code == 1 and "a.yaml" in result.output and "Traceback" not in result.output


def test_validate_missing_root_exits_1_without_traceback(tmp_path):
    result = run("validate", "--root", str(tmp_path / "nope"))
    assert result.exit_code == 1 and "Traceback" not in result.output


def test_unknown_topic_query_exits_1_with_message():
    for cmd in ("ancestors", "descendants"):
        result = run(cmd, "math.zz.nothing", "--root", str(FIXTURE))
        assert result.exit_code == 1 and "unknown topic" in result.output
    result = run("path", "math.zz.nothing", "math.yy.nothing", "--root", str(FIXTURE))
    assert result.exit_code == 1 and "unknown topic" in result.output


def test_ancestors_descendants_and_path_on_sample(sample_graph):
    from kg.graph import GraphIndex

    index = GraphIndex(sample_graph)
    tid = next(t for t in sample_graph.topics if index.ancestors(t))
    anc = next(iter(index.ancestors(tid)))
    out = run("ancestors", tid, "--root", str(FIXTURE))
    assert out.exit_code == 0 and anc in out.output.split()
    out = run("descendants", anc, "--root", str(FIXTURE))
    assert out.exit_code == 0 and tid in out.output.split()
    out = run("path", anc, tid, "--root", str(FIXTURE))
    assert out.exit_code == 0 and out.output.split()[0] == anc and out.output.split()[-1] == tid
    out = run("path", tid, anc, "--root", str(FIXTURE))
    assert out.exit_code == 1 and "no path" in out.output


def test_synth_writes_a_graph_that_validates(tmp_path):
    out = tmp_path / "g"
    result = run("synth", "--topics", "300", "--out", str(out))
    assert result.exit_code == 0, result.output
    assert run("validate", "--root", str(out)).exit_code == 0
