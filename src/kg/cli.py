"""Command-line interface. Errors are printed as messages, never tracebacks."""

from pathlib import Path

import typer

from kg.checks import run_checks
from kg.edits import EditError, apply_edit, rename_id, split_topic
from kg.graph import GraphIndex, KnowledgeGraph, shortest_path
from kg.map.export import export_map
from kg.store import GraphLoadError, load_graph, write_graph
from kg.synthetic import generate

app = typer.Typer(add_completion=False, no_args_is_help=True)

RootOption = typer.Option(Path("graph"), "--root", help="Graph directory.")


def _fail(message: str) -> typer.Exit:
    typer.echo(message)
    return typer.Exit(1)


def _load(root: Path) -> KnowledgeGraph:
    try:
        return load_graph(root)
    except GraphLoadError as exc:
        for file, message in exc.problems:
            typer.echo(f"error load-error {file} -: {message}")
        raise _fail(f"{len(exc.problems)} errors, 0 warnings") from exc


def _known(kg: KnowledgeGraph, *ids: str) -> None:
    for tid in ids:
        if tid not in kg.topics:
            raise _fail(f"unknown topic: {tid}")


@app.command()
def validate(root: Path = RootOption) -> None:
    """Run every rule. Exit 1 if any error."""
    kg = _load(root)
    issues = run_checks(kg)
    for i in issues:
        typer.echo(f"{i.severity} {i.rule} {i.file or '-'} {i.topic or '-'}: {i.message}")
    errors = sum(i.severity == "error" for i in issues)
    typer.echo(f"{errors} errors, {len(issues) - errors} warnings")
    if errors:
        raise typer.Exit(1)


@app.command()
def ancestors(topic_id: str, root: Path = RootOption) -> None:
    """List every topic the given topic depends on, directly or not."""
    kg = _load(root)
    _known(kg, topic_id)
    for t in sorted(GraphIndex(kg).ancestors(topic_id)):
        typer.echo(t)


@app.command()
def descendants(topic_id: str, root: Path = RootOption) -> None:
    """List every topic that depends on the given topic, directly or not."""
    kg = _load(root)
    _known(kg, topic_id)
    for t in sorted(GraphIndex(kg).descendants(topic_id)):
        typer.echo(t)


@app.command()
def path(a: str, b: str, root: Path = RootOption) -> None:
    """Shortest prerequisite chain from topic A up to topic B."""
    kg = _load(root)
    _known(kg, a, b)
    chain = shortest_path(kg, a, b)
    if chain is None:
        raise _fail(f"no path from {a} to {b}")
    for t in chain:
        typer.echo(t)


@app.command()
def synth(
    topics: int = typer.Option(..., "--topics", help="Number of topics."),
    out: Path = typer.Option(..., "--out", help="Directory to write."),
    seed: int = typer.Option(0, "--seed"),
) -> None:
    """Write a synthetic valid graph (for testing, not content)."""
    if topics < 5:
        raise _fail("--topics must be at least 5")
    write_graph(generate(topics, seed=seed, root=out))
    typer.echo(f"wrote {topics} topics to {out}")


@app.command("export-map")
def export_map_command(
    root: Path = RootOption,
    out: Path = typer.Option(Path("build/map.html"), "--out", help="HTML file to write."),
) -> None:
    """Write the offline curriculum map. Exit 1, writing nothing, if validation has errors."""
    kg = _load(root)
    errors = [i for i in run_checks(kg) if i.severity == "error"]
    if errors:
        for i in errors:
            typer.echo(f"error {i.rule} {i.file or '-'} {i.topic or '-'}: {i.message}")
        raise _fail(f"{len(errors)} errors; map not written")
    typer.echo(f"wrote {export_map(kg, out)}")


def _commit(new_kg: KnowledgeGraph) -> None:
    """Validate then write; on errors print them, write nothing and exit 1."""
    errors = apply_edit(new_kg)
    if errors:
        for i in errors:
            typer.echo(f"error {i.rule} {i.file or '-'} {i.topic or '-'}: {i.message}")
        raise _fail(f"{len(errors)} errors; nothing written")


@app.command("rename-id")
def rename_id_command(old: str, new: str, root: Path = RootOption) -> None:
    """Rename a topic ID and every reference to it, recording the change in id-history."""
    kg = _load(root)
    try:
        edited = rename_id(kg, old, new)
    except EditError as exc:
        raise _fail(str(exc)) from exc
    _commit(edited)
    typer.echo(f"renamed {old} -> {new}")


@app.command("split-topic")
def split_topic_command(
    topic_id: str,
    new_id: str = typer.Option(..., "--new-id", help="ID of the new topic."),
    new_name: str = typer.Option(..., "--new-name", help="Name of the new topic."),
    move_kps: str = typer.Option(..., "--move-kps", help="Comma-separated KP ids to move."),
    keep_kp: list[str] = typer.Option([], "--keep-kp", help="New KP text added to the original."),
    new_kp: list[str] = typer.Option([], "--new-kp", help="New KP text added to the new topic."),
    root: Path = RootOption,
) -> None:
    """Split a topic in two. The new topic follows the original and takes the moved KPs."""
    kg = _load(root)
    moved = [k.strip() for k in move_kps.split(",") if k.strip()]
    try:
        edited = split_topic(kg, topic_id, new_id, new_name, moved, keep_kp, new_kp)
    except EditError as exc:
        raise _fail(str(exc)) from exc
    _commit(edited)
    typer.echo(f"split {topic_id} -> {topic_id}, {new_id}")
