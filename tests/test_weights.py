"""Weight CSV export and import."""

import csv
import hashlib

import pytest
from typer.testing import CliRunner

from kg.cli import app
from kg.store import load_graph
from kg.weights import WeightImportError, export_weights, import_weights

HEADER = "topic,kind,prerequisite,encompassing,confidence"
T = "math.alg1.solve-multi-step-equations"
P = "math.alg1.solve-two-step-equations"
E = "math.alg1.combine-like-terms"


def snapshot(root):
    return {
        str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(root.rglob("*"))
        if p.is_file() and ".kg-cache" not in p.parts
    }


def edge_of(kg, topic, kind, target):
    edges = kg.topics[topic].prerequisites if kind == "direct" else kg.topics[topic].encompassed
    return next(e for e in edges if e.topic == target)


def write_csv(path, *rows, header=HEADER):
    path.write_text("\n".join([header, *rows]) + "\n", encoding="utf-8")
    return path


def test_round_trip_changes_nothing(sample_copy, tmp_path):
    before = snapshot(sample_copy)
    kg = load_graph(sample_copy)
    out = tmp_path / "w.csv"
    export_weights(kg, out)
    rows = list(csv.DictReader(out.open(encoding="utf-8")))
    assert {r["kind"] for r in rows} == {"direct", "encompassed"}
    import_weights(kg, out)
    result = CliRunner().invoke(app, ["import-weights", str(out), "--root", str(sample_copy)])
    assert result.exit_code == 0, result.output
    assert snapshot(sample_copy) == before


def test_excel_style_file_imports(sample_copy, tmp_path):
    kg = load_graph(sample_copy)
    path = tmp_path / "x.csv"
    path.write_bytes(
        f"\ufeff{HEADER}\r\n{T},direct,{P},0.5,low\r\n\r\n".encode()
    )
    new = import_weights(kg, path)
    assert edge_of(new, T, "direct", P).encompassing == 0.5
    assert edge_of(new, T, "direct", P).confidence == "low"


def test_rows_may_be_reordered(sample_copy, tmp_path):
    kg = load_graph(sample_copy)
    out = tmp_path / "w.csv"
    export_weights(kg, out)
    lines = out.read_text(encoding="utf-8").splitlines()
    path = tmp_path / "r.csv"
    path.write_text("\n".join([lines[0], *reversed(lines[1:])]) + "\n", encoding="utf-8")
    new = import_weights(kg, path)
    assert new.topics == kg.topics


def test_omitted_rows_leave_weights_unchanged(sample_copy, tmp_path):
    kg = load_graph(sample_copy)
    before = edge_of(kg, T, "direct", E)
    path = write_csv(tmp_path / "x.csv", f"{T},direct,{P},0.9,medium")
    new = import_weights(kg, path)
    assert edge_of(new, T, "direct", P).encompassing == 0.9
    assert edge_of(new, T, "direct", E) == before
    assert edge_of(new, T, "encompassed", E) == edge_of(kg, T, "encompassed", E)


def test_direct_and_encompassed_rows_are_independent(sample_copy, tmp_path):
    kg = load_graph(sample_copy)
    path = write_csv(tmp_path / "x.csv", f"{T},encompassed,{E},0.8,low")
    new = import_weights(kg, path)
    assert edge_of(new, T, "encompassed", E).encompassing == 0.8
    assert edge_of(new, T, "direct", E) == edge_of(kg, T, "direct", E)


def test_unknown_edge_out_of_range_and_bad_number_are_all_reported(sample_copy, tmp_path):
    kg = load_graph(sample_copy)
    path = write_csv(
        tmp_path / "x.csv",
        f"{T},direct,math.alg1.nope,0.5,high",
        f"{T},direct,{P},1.5,high",
        f"{T},direct,{E},abc,high",
        f"{T},sideways,{E},0.5,high",
        f"{T},encompassed,{E},0.5,certain",
    )
    with pytest.raises(WeightImportError) as exc:
        import_weights(kg, path)
    assert len(exc.value.problems) == 5
    assert all(p.startswith("row ") for p in exc.value.problems)


def test_bad_header_is_reported(sample_copy, tmp_path):
    kg = load_graph(sample_copy)
    path = write_csv(tmp_path / "x.csv", header="topic,prerequisite")
    with pytest.raises(WeightImportError):
        import_weights(kg, path)


def test_failed_import_writes_nothing(sample_copy, tmp_path):
    before = snapshot(sample_copy)
    path = write_csv(
        tmp_path / "x.csv", f"{T},direct,{P},0.9,high", f"{T},direct,{E},2,high"
    )
    result = CliRunner().invoke(app, ["import-weights", str(path), "--root", str(sample_copy)])
    assert result.exit_code == 1
    assert "row 3" in result.output
    assert snapshot(sample_copy) == before


def test_import_changes_only_weight_and_confidence(sample_copy, tmp_path):
    path = write_csv(tmp_path / "x.csv", f"{T},direct,{P},0.9,low")
    result = CliRunner().invoke(app, ["import-weights", str(path), "--root", str(sample_copy)])
    assert result.exit_code == 0, result.output
    new = load_graph(sample_copy)
    assert edge_of(new, T, "direct", P).encompassing == 0.9
