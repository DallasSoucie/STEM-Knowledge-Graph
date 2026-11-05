"""Map data and the offline HTML export."""

import json
import re

from typer.testing import CliRunner

from conftest import add, course, topic
from kg.checks import run_checks
from kg.cli import app
from kg.graph import KnowledgeGraph
from kg.map.data import build_map_data
from kg.map.export import export_map
from kg.model import Topic

runner = CliRunner()


def export(kg, tmp_path):
    return export_map(kg, tmp_path / "map.html").read_text(encoding="utf-8")


def data_block(html):
    m = re.search(r'<script type="application/json" id="kg-data">(.*?)</script>', html, re.S)
    return m.group(1)


def strip_vendor(html):
    """Page minus the inlined libraries, which are third-party code."""
    html = re.sub(r"<script>/\*vendor:sigma\*/.*?</script>", "", html, flags=re.S)
    return re.sub(r"<script>/\*vendor:graphology\*/.*?</script>", "", html, flags=re.S)


def test_export_refuses_graph_with_errors(sample_copy, tmp_path):
    (sample_copy / "math" / "extra.yaml").write_text(
        "course: math.arith\ntopics:\n- {id: math.arith.dangling, name: D, status: draft,"
        " subject: math, course: math.arith, level: g4,"
        " prerequisites: [{topic: math.nope, encompassing: 0.5, confidence: high}]}\n",
        encoding="utf-8",
    )
    out = tmp_path / "out" / "map.html"
    result = runner.invoke(app, ["export-map", "--root", str(sample_copy), "--out", str(out)])
    assert result.exit_code == 1
    assert not out.exists()


def test_cli_exports_valid_graph(sample_copy, tmp_path):
    out = tmp_path / "out" / "map.html"
    result = runner.invoke(app, ["export-map", "--root", str(sample_copy), "--out", str(out)])
    assert result.exit_code == 0, result.output
    assert out.exists()


def test_page_makes_no_network_references(sample_graph, tmp_path):
    html = export(sample_graph, tmp_path)
    assert "http://" not in strip_vendor(html) and "https://" not in strip_vendor(html)
    assert "/*__" not in html  # every placeholder was filled


def test_markup_in_names_cannot_close_the_data_script(tmp_path):
    kg = KnowledgeGraph()
    kg.courses = {"math.a": course("math.a", 1)}
    t = topic("math.a.one", level="g4")
    add(kg, t.model_copy(update={"name": "</script><b>"}))
    html = export(kg, tmp_path)
    assert "<" not in data_block(html)
    assert json.loads(data_block(html))["topics"][0]["name"] == "</script><b>"


def test_edges_include_direct_and_encompassed(tmp_path):
    kg = KnowledgeGraph()
    kg.courses = {"math.a": course("math.a", 3)}
    add(
        kg,
        topic("math.a.one"),
        topic("math.a.two", ["math.a.one"], keys=["math.a.one"]),
        topic("math.a.three", ["math.a.two"], keys=["math.a.two"], encompassed=["math.a.one"]),
    )
    data = build_map_data(kg)
    idx = {t["id"]: i for i, t in enumerate(data["topics"])}
    edges = {tuple(e) for e in data["edges"]}
    assert (idx["math.a.one"], idx["math.a.two"], 0.5, "high", "direct") in edges
    assert (idx["math.a.one"], idx["math.a.three"], 0.3, "high", "encompassed") in edges
    assert len(edges) == 3


def test_stub_and_near_limit_flags_are_exported():
    kg = KnowledgeGraph()
    kg.courses = {"math.a": course("math.a", 2)}
    add(
        kg,
        topic("math.a.two_kp", n_kps=2),
        Topic(id="math.a.later", name="Later", status="stub"),
    )
    by_id = {t["id"]: t for t in build_map_data(kg)["topics"]}
    assert by_id["math.a.two_kp"]["near_limits"] is True
    assert by_id["math.a.two_kp"]["status"] == "draft"
    assert by_id["math.a.later"]["status"] == "stub"
    assert by_id["math.a.later"]["near_limits"] is False


def test_topic_record_shape(sample_graph):
    data = build_map_data(sample_graph)
    assert set(data) == {"levels", "subjects", "courses", "columns", "topics", "edges"}
    t = data["topics"][0]
    assert set(t) == {
        "id", "name", "subject", "course", "level", "status", "x", "y", "near_limits", "kps",
    }


def test_empty_graph_exports(tmp_path):
    html = export(KnowledgeGraph(), tmp_path)
    data = json.loads(data_block(html))
    assert data["topics"] == [] and data["edges"] == []


def test_sample_graph_is_valid_and_exports(sample_graph, tmp_path):
    assert not [i for i in run_checks(sample_graph) if i.severity == "error"]
    assert export(sample_graph, tmp_path).startswith("<!doctype html>")
