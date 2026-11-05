# Knowledge Graph Tooling and Map Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the validated YAML graph tooling and a single-file, offline, zoomable map, ready for course-by-course content production.

**Architecture:** YAML files are the only source of truth. A `kg` Python package loads them into pydantic models, validates them with one function per rule, and generates reports and a WebGL map page. The CLI is a thin layer over these modules.

**Tech Stack:** Python 3.11+ (developed on 3.14.6), pydantic 2, PyYAML with LibYAML where available, networkx, typer, pytest. Map page: sigma.js 3.0.2 and graphology 0.25.4. Dev only: pytest-playwright.

**Spec:** `docs/superpowers/specs/2026-11-05-knowledge-graph-tooling-and-map-design.md`. `CLAUDE.md` defines the model and rules.

## Global Constraints

- `validate` finishes in under 10 seconds on a synthetic 20,000-topic graph.
- The map is one offline HTML file, written to `build/map.html`, not committed. No Node.js is needed to build or open it.
- The map is read-only. Unmatched topics fade but stay in place. With no filters on, every topic shows.
- All YAML writes go through `store.py`. Graph YAML contains no comments.
- `split-topic`, `rename-id`, and `import-weights` validate first and write nothing if the result fails.
- Never set `status: reviewed`. Never loosen a rule to make a graph pass.
- No lessons, problems, or learner UI.
- Run Python as `.venv/Scripts/python` (Windows venv). All commands take `--root`, defaulting to `graph`.
- End commit messages with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Don't push unless the owner asks.
- Fetching the map libraries and installing `pytest-playwright` and Chromium each need the owner's approval at that step.

## Review Focus

1. **Topic text with markup or Unicode** (`</script>`, `<b>`, `&`, quotes, `π`): saved exactly, shown literally on the map, and never breaks the page. Tests in Tasks 2, 8, 9.
2. **YAML-sensitive values** (a topic named `No`, `1.5`, or `Force: a review`): survive a round trip as the same strings. Test in Task 2.
3. **Hand-edit mistakes** (malformed YAML, an unknown key, a missing field): `validate` lists every bad file with its name and exits non-zero, with no traceback. Tests in Tasks 2, 5.
4. **Sparse graphs and stale links** (no topics, stub-only courses, a stub selected, a saved URL naming a deleted topic, filters matching nothing): no crash, and the map shows a sensible empty or whole-graph state. Tests in Tasks 7, 8, 10.
5. **Weight CSVs edited in Excel** (BOM, CRLF, reordered rows, blank lines, omitted rows): import correctly, and omitted rows leave weights unchanged. Test in Task 14.

---

## File Structure

```
pyproject.toml, .gitattributes, .githooks/pre-commit
graph/courses.yaml, graph/id-history.yaml
src/kg/
  model.py       Topic, KnowledgePoint, Edge, Course, HistoryEntry
  store.py       load_graph, write_course, write_graph, GraphLoadError
  graph.py       KnowledgeGraph, GraphIndex, lineage queries
  limits.py      is_near_limits, course_closure
  checks/        base.py, structure.py, sequence.py, quality.py, __init__.py (run_checks)
  synthetic.py   generate(n_topics, seed)
  edits.py       rename_id, split_topic, apply_edit
  reports.py     stats, review_report, review_queue, find_duplicates
  weights.py     export_weights, import_weights
  map/           layout.py, data.py, export.py, template.html, app.js, vendor/
  cli.py
tests/           test_*.py, fixtures/sample/
```

## Stage 1: Foundation

### Task 1: Packaging and schema

**Files:** Create `pyproject.toml`, `.gitattributes`, `src/kg/__init__.py`, `src/kg/model.py`, `tests/test_model.py`

**Interfaces:**
- Produces, in `kg.model`:
  - `LEVELS: tuple[str, ...]` = `gk, g1 ... g12, uni-lower, uni-upper`; `level_rank(level: str) -> int`
  - `Edge(topic: str, encompassing: float, confidence: Literal["high","medium","low"])`
  - `KnowledgePoint(id: str, can_do: str, key_prerequisites: list[str] = [])`
  - `Topic(id, name, status: Literal["stub","draft","reviewed"], subject: str|None, course: str|None, level: str|None, justification: str|None, prerequisites: list[Edge], encompassed: list[Edge], knowledge_points: list[KnowledgePoint])`, with properties `is_stub` and `course_id` (the first two ID segments)
  - `Course(id, subject, levels: tuple[str,str], budget: int, follows: list[str] = [], view_topics: list[str]|None = None)`, property `is_view`
  - `HistoryEntry(op: Literal["rename","split"], source: str, targets: list[str])`

- [ ] **Step 1: Set up the environment.** `pyproject.toml` uses a `src` layout, script `kg = "kg.cli:app"`, `requires-python = ">=3.11"`, and a `dev` extra with pytest. `.gitattributes`: `graph/** text eol=lf`. Run `python -m venv .venv` and `.venv/Scripts/python -m pip install -e .[dev]`. Expected: installs without error.
- [ ] **Step 2: Write failing tests** in `tests/test_model.py`.

```python
def test_levels_are_ordered():
    assert level_rank("gk") < level_rank("g1") < level_rank("g12") < level_rank("uni-lower") < level_rank("uni-upper")

def test_unknown_keys_are_rejected():
    with pytest.raises(ValidationError):
        Topic.model_validate({"id": "math.k.a", "name": "A", "status": "stub", "statsu": "x"})

def test_stub_needs_only_id_name_status():
    t = Topic.model_validate({"id": "math.k.a", "name": "A", "status": "stub"})
    assert t.is_stub and t.course_id == "math.k"

def test_non_stub_requires_subject_course_level():
    with pytest.raises(ValidationError):
        Topic.model_validate({"id": "math.k.a", "name": "A", "status": "draft"})

def test_out_of_range_weight_loads_so_a_check_can_report_it():
    assert Edge(topic="x", encompassing=1.4, confidence="low").encompassing == 1.4
```

- [ ] **Step 3: Run tests.** `.venv/Scripts/python -m pytest tests/test_model.py -v`. Expected: FAIL on import.
- [ ] **Step 4: Implement `kg/model.py`.** Use `extra="forbid"` on every model. Models check types and required fields only; numeric limits belong to checks, so one run reports all of them.
- [ ] **Step 5: Run tests.** Expected: PASS.
- [ ] **Step 6: Commit** with `feat: add packaging and graph schema`.

### Task 2: YAML store

**Files:** Create `src/kg/graph.py` (dataclass only for now), `src/kg/store.py`, `tests/test_store.py`, `tests/fixtures/sample/` (small valid graph: `courses.yaml`, 2 math courses, 1 physics course, 12-15 topics with one stub and one `encompassed` entry)

**Interfaces:**
- Consumes: Task 1 models.
- Produces:
  - `kg.graph.KnowledgeGraph` dataclass: `topics: dict[str, Topic]` (insertion order is course order), `courses: dict[str, Course]`, `history: list[HistoryEntry]`, `duplicate_ids: list[str]`, `root: Path`
  - `kg.store.load_graph(root: Path) -> KnowledgeGraph`, raising `GraphLoadError(problems: list[tuple[Path, str]])` after reading every file
  - `kg.store.write_course(root, course_id, topics: list[Topic]) -> None`
  - `kg.store.write_graph(kg: KnowledgeGraph) -> None`, writing only files whose bytes changed

**File format:** `graph/<subject>/<short>.yaml` holds `course: math.alg1` and `topics: [...]`. Topic keys are in the order of the `CLAUDE.md` example, with `justification` after `status` and `encompassed` after `prerequisites`. Empty optional keys are omitted. `key_prerequisites` uses flow style. Line width is unlimited, `allow_unicode=True`, LF endings, UTF-8. Use `CSafeLoader` when importable, otherwise `SafeLoader`.

- [ ] **Step 1: Write failing tests.**

```python
def test_round_trip_is_byte_identical(sample_copy):
    before = snapshot(sample_copy)
    write_graph(load_graph(sample_copy))
    assert snapshot(sample_copy) == before

@pytest.mark.parametrize("text", ["No", "1.5", "Force: a review", "null", "</script>&<b>'\"π"])
def test_sensitive_strings_round_trip(tmp_graph, text):
    write_topic_named(tmp_graph, text)
    assert only_topic(load_graph(tmp_graph)).name == text

def test_all_bad_files_are_reported_with_names(tmp_graph):
    (tmp_graph / "math/a.yaml").write_text("course: [unclosed", encoding="utf-8")
    (tmp_graph / "math/b.yaml").write_text("course: math.b\ntopics:\n- {id: math.b.x, name: X, status: stub, bogus: 1}\n", encoding="utf-8")
    with pytest.raises(GraphLoadError) as e:
        load_graph(tmp_graph)
    assert {p.name for p, _ in e.value.problems} == {"a.yaml", "b.yaml"}

def test_duplicate_ids_are_recorded_not_lost(tmp_graph_with_duplicate):
    assert load_graph(tmp_graph_with_duplicate).duplicate_ids == ["math.a.x"]

def test_key_prerequisites_written_in_flow_style(sample_copy):
    assert "key_prerequisites: [" in read_any_course(sample_copy)
```

- [ ] **Step 2: Run tests.** `.venv/Scripts/python -m pytest tests/test_store.py -v`. Expected: FAIL.
- [ ] **Step 3: Implement `store.py` and create the fixture.** A missing `id-history.yaml` means empty history.
- [ ] **Step 4: Run tests.** Expected: PASS.
- [ ] **Step 5: Commit** with `feat: add canonical YAML store`.

### Task 3: Graph index and queries

**Files:** Modify `src/kg/graph.py`. Create `src/kg/limits.py`, `tests/test_graph.py`

**Interfaces:**
- Produces:
  - `build_digraph(kg) -> nx.DiGraph`: edges run prerequisite to topic, from `prerequisites` only, skipping dangling targets
  - `GraphIndex(kg)`: `.cycles() -> list[list[str]]`, `.is_ancestor(a, b) -> bool`, `.ancestors(id) -> set[str]`, `.descendants(id) -> set[str]`
  - `lineage(kg, topic_id, direction: Literal["prerequisites","dependents","both"], max_steps: int|None) -> set[str]`, excluding the topic
  - `shortest_path(kg, a, b) -> list[str]|None`
  - `kg.limits.is_near_limits(topic: Topic) -> bool`, per the spec definition
  - `kg.limits.course_closure(kg, course_id) -> set[str]`, the course plus all `follows` transitively, safe against cycles and unknown IDs

- [ ] **Step 1: Write failing tests:** `test_is_ancestor_multi_hop`, `test_cycle_is_reported_and_ancestors_do_not_hang`, `test_lineage_respects_max_steps` (chain a→b→c→d: `lineage(kg,"d","prerequisites",1) == {"c"}`), `test_near_limits` (parametrized over each of the four spec conditions, and a clean topic returning False), `test_course_closure_survives_follows_cycle`.
- [ ] **Step 2: Run tests.** `.venv/Scripts/python -m pytest tests/test_graph.py -v`. Expected: FAIL.
- [ ] **Step 3: Implement.** `is_ancestor` must be cheap across 20,000 topics: compute closures once in topological order, using Python integers as bitsets.

```python
for t in topological_order:
    bits[t] = 0
    for p in direct_prereqs[t]:
        bits[t] |= bits[p] | (1 << index[p])
```

- [ ] **Step 4: Run tests.** Expected: PASS.
- [ ] **Step 5: Commit** with `feat: add graph index and lineage queries`.

### Task 4: Validation rules

**Files:** Create `src/kg/checks/{__init__,base,structure,sequence,quality}.py`, `tests/test_checks.py`, `tests/conftest.py` (builder helpers). Modify `CLAUDE.md` (add the encompassed-ancestry rule).

**Interfaces:**
- Consumes: `KnowledgeGraph`, `GraphIndex`, `course_closure`.
- Produces: `Issue(severity: Literal["error","warning"], rule: str, topic: str|None, file: str|None, message: str)`; decorator `@rule(name, severity)` over `fn(kg, index) -> Iterable[Issue]`; `run_checks(kg) -> list[Issue]`; `RULES: dict[str, ...]`.

| Rule | Severity | Fails when |
|---|---|---|
| `duplicate-id` | error | an ID is in `kg.duplicate_ids` |
| `id-format` | error | ID isn't `<subject>.<course>.<slug>` in lowercase slugs |
| `unknown-course` | error | a topic's `course_id` isn't in the manifest |
| `dangling-reference` | error | any prerequisite, encompassed, key prerequisite, `follows`, or view topic target is missing |
| `cycle` | error | prerequisites form a cycle; ancestor rules skip when this fires |
| `manifest-follows-cycle` | error | `follows` forms a cycle |
| `kp-count` | error | non-stub has under 2 or over 5 KPs |
| `direct-prereq-limit` | error | over 4 without `justification`, or over 5 at all |
| `key-prereq-limit` | error | a KP has over 4 key prerequisites |
| `weight-range` | error | any weight is outside 0-1 |
| `orphan` | error | non-stub has no prerequisites and no dependents |
| `stub-no-dependent` | error | a stub has no dependent |
| `key-prereq-not-ancestor` | error | a key prerequisite isn't an ancestor |
| `key-prereq-unweighted` | error | a key prerequisite is in neither `prerequisites` nor `encompassed` |
| `encompassed-not-ancestor` | error | an `encompassed` topic isn't an ancestor |
| `course-gap` | error | a prerequisite's course is outside `course_closure`, or a view course includes a topic whose prerequisite is neither in the view nor in the closure |
| `learner-walk` | error | walking a course in listed order reaches a topic whose prerequisite isn't yet known; known starts as all topics in the closure's other courses |
| `redundant-edge` | warning | a direct prerequisite is an ancestor of another direct prerequisite |
| `prereq-above-level` | warning | a prerequisite's level ranks above the topic's |
| `congested-topic` | warning | every KP has 3 or more key prerequisites |
| `no-prereq-above-gk` | warning | a non-stub above `gk` has no prerequisites |
| `weight-clustering` | warning | a course with 20+ weights has over 80% of them on its 3 most common values |
| `budget-variance` | warning | a course with non-stub topics is over 20% off its budget |

- [ ] **Step 1: Write failing tests.** Parametrize one test over every rule, with a graph builder that breaks exactly that rule. Add the guard test below so no rule can ship without a case.

```python
@pytest.mark.parametrize("rule_name,build", CASES)
def test_rule_fires_on_its_broken_graph(rule_name, build):
    assert rule_name in {i.rule for i in run_checks(build())}

def test_every_registered_rule_has_a_case():
    assert {name for name, _ in CASES} == set(RULES)

def test_clean_graph_has_no_errors(sample_graph):
    assert [i for i in run_checks(sample_graph) if i.severity == "error"] == []

def test_empty_graph_is_clean(empty_graph):
    assert run_checks(empty_graph) == []

def test_stub_is_exempt_from_kp_count(graph_with_used_stub):
    assert "kp-count" not in {i.rule for i in run_checks(graph_with_used_stub)}
```

- [ ] **Step 2: Run tests.** `.venv/Scripts/python -m pytest tests/test_checks.py -v`. Expected: FAIL.
- [ ] **Step 3: Implement the rules.** `structure.py`: IDs, references, cycles, limits. `sequence.py`: gap, walk, follows. `quality.py`: warnings. Issues carry the source file name where known.
- [ ] **Step 4: Run tests.** Expected: PASS.
- [ ] **Step 5: Add the encompassed-ancestry rule to the Validation section of `CLAUDE.md`.**
- [ ] **Step 6: Commit** with `feat: add validation rules`.

### Task 5: Core CLI, synthetic graph, and speed test

**Files:** Create `src/kg/cli.py`, `src/kg/synthetic.py`, `tests/test_cli.py`, `tests/test_speed.py`

**Interfaces:**
- Produces:
  - `synthetic.generate(n_topics: int, seed: int = 0, root: Path = Path("graph")) -> KnowledgeGraph`: valid and deterministic, with `root` setting where `write_graph` saves it, about 3.4 KPs and 5 weighted relationships per topic, five subjects, realistic course sizes
  - Commands: `validate`, `ancestors ID`, `descendants ID`, `path A B`, `synth --topics N --out DIR`
- `validate` output is one line per issue, `severity rule file topic: message`, then a count line. Exit 1 on any error or `GraphLoadError`.

- [ ] **Step 1: Write failing tests.**

```python
def test_validate_clean_sample_exits_0(): ...      # CliRunner, --root fixtures/sample
def test_validate_broken_graph_exits_1_and_names_rule(): ...
def test_validate_malformed_yaml_names_file_without_traceback(tmp_path):
    result = run("validate", "--root", bad_root(tmp_path))
    assert result.exit_code == 1 and "a.yaml" in result.output and "Traceback" not in result.output
def test_unknown_topic_query_exits_1_with_message(): ...

def test_synthetic_graph_has_no_errors_and_hits_density():
    kg = generate(2000, seed=1)
    assert not errors(run_checks(kg))
    assert 3.2 <= mean_kps(kg) <= 3.6 and 4.5 <= mean_weighted_edges(kg) <= 5.5

def test_validate_under_10_seconds_on_20000_topics(tmp_path):
    write_graph(generate(20000, seed=1, root=tmp_path))
    start = time.perf_counter()
    run_checks(load_graph(tmp_path))
    assert time.perf_counter() - start < 10
```

- [ ] **Step 2: Run tests.** `.venv/Scripts/python -m pytest tests/test_cli.py tests/test_speed.py -v`. Expected: FAIL.
- [ ] **Step 3: Implement `synthetic.py`, then `cli.py`.** In `synthetic.py`, draw prerequisites only from earlier topics or `follows` courses, and add non-direct weights to `encompassed` from ancestors.
- [ ] **Step 4: Run tests.** Expected: PASS. If only the speed test fails, profile first; add the file-hash parse cache from the spec only if parsing is the cause.
- [ ] **Step 5: Commit** with `feat: add core CLI and synthetic graph with speed test`.

### Task 6: Course manifest

**Files:** Create `graph/courses.yaml`, `tests/test_manifest.py`

**Interfaces:** Consumes the `Course` schema. IDs are `<subject>.<short>`, using catalog names and the subject prefixes `math`, `physics`, `chem`, `bio`, `engr`.

- [ ] **Step 1: Write failing tests:** `test_manifest_has_103_courses`; `test_budgets_total_15680`; `test_subject_totals` (math 4370, physics 1880, chem 1850, bio 2310, engr 5270); `test_real_graph_validates` (`kg validate` exits 0 on the empty `graph/`).
- [ ] **Step 2: Run tests.** `.venv/Scripts/python -m pytest tests/test_manifest.py -v`. Expected: FAIL.
- [ ] **Step 3: Transcribe the `KG_PROMPT.md` catalog.** Levels: each grade course is its own grade. `alg1` is g8-g9, `geom` g9-g10, `alg2` g10-g11, `precalc` g11-g12, `stats` g11-g12. `elem` is gk-g5 and `ms` g6-g8; `hs1` is g9-g11 and `hs2` g11-g12. Introductory and common-core university courses are `uni-lower`; the rest are `uni-upper`. Set `follows` from the real dependencies, including cross-subject ones such as `physics.mechanics` following `math.calc1`.
- [ ] **Step 4: Run tests.** Expected: PASS.
- [ ] **Step 5: Commit** with `feat: add provisional course manifest`.

## Stage 2: Map

### Task 7: Layout

**Files:** Create `src/kg/map/__init__.py`, `src/kg/map/layout.py`, `tests/test_layout.py`

**Interfaces:** Produces `compute_positions(kg) -> dict[str, tuple[float, float]]`, `column_bounds(kg) -> dict[str, tuple[float,float]]`, `lane_of(kg) -> dict[str, tuple[str,int]]`.

**Pinned rules:**
- Subject row order: math, physics, chem, bio, engr.
- Each row has a fixed height of `ROW_LANES = 30` lanes, so a new lane can't move other rows. Raise a clear error if a subject needs more.
- Lanes are first-fit in manifest order, sharing a lane only when level ranges don't overlap. View courses get no lane.
- Column width is proportional to the largest per-level budget share at that level, where share = budget ÷ the number of levels the course spans, with a minimum width. Budgets, not counts, so growing a course moves nothing else.
- Topic x: `col_start + (i + 0.5) / n * col_width`, where `i` and `n` count that course's topics at that level, in listed order.
- A stub without a level takes its course's first level.

**Spec note:** adding a course whose budget share exceeds its level's current maximum widens that column, which shifts x positions across all rows. The stability test covers courses within the current maximum, which is the usual case.

- [ ] **Step 1: Write failing tests:** `test_positions_are_repeatable`; `test_lower_levels_are_left_of_higher`; `test_subjects_occupy_separate_rows`; `test_same_level_courses_get_separate_lanes`; `test_nonoverlapping_courses_share_a_lane`; `test_adding_topic_moves_only_its_course`; `test_adding_course_within_budget_max_leaves_other_rows_unmoved`; `test_empty_graph_gives_no_positions`; `test_stub_without_level_gets_position`.
- [ ] **Step 2: Run tests.** `.venv/Scripts/python -m pytest tests/test_layout.py -v`. Expected: FAIL.
- [ ] **Step 3: Implement `layout.py`.**
- [ ] **Step 4: Run tests.** Expected: PASS.
- [ ] **Step 5: Commit** with `feat: add curriculum bands layout`.

### Task 8: Map data and export

**Files:** Create `src/kg/map/data.py`, `src/kg/map/export.py`, `src/kg/map/template.html`, `src/kg/map/vendor/{sigma.min.js,graphology.umd.min.js,VERSIONS.txt}`, `tests/test_export.py`. Modify `cli.py`, `pyproject.toml` (package data).

**Interfaces:**
- Produces:
  - `build_map_data(kg) -> dict`: keys `levels`, `subjects`, `courses`, `columns`, `topics` (`id, name, subject, course, level, status, x, y, near_limits, kps`), and `edges` (`[source_index, target_index, weight, confidence, kind]`, kind being `direct` or `encompassed`)
  - `export_map(kg, out: Path) -> Path`
  - Command: `kg export-map [--out build/map.html]`, which exits 1 without writing if `run_checks` reports errors
- Embed the data in `<script type="application/json" id="kg-data">`, replacing every `<` with `<` in the JSON. Inline the vendor files and `app.js` so the page makes no network requests.

- [ ] **Step 1: Ask the owner to approve fetching the libraries,** then save `https://cdn.jsdelivr.net/npm/sigma@3.0.2/dist/sigma.min.js` and `https://cdn.jsdelivr.net/npm/graphology@0.25.4/dist/graphology.umd.min.js` to `vendor/`, recording versions, URLs, and SHA-256 in `VERSIONS.txt`.
- [ ] **Step 2: Write failing tests.**

```python
def test_export_refuses_graph_with_errors(): ...   # exit 1, no file written
def test_page_makes_no_network_references(tmp_path):
    html = export(sample, tmp_path)
    assert "http://" not in strip_vendor(html) and "https://" not in strip_vendor(html)
def test_markup_in_names_cannot_close_the_data_script(tmp_path):
    html = export(graph_with_name("</script><b>"), tmp_path)
    assert json.loads(data_block(html))["topics"][0]["name"] == "</script><b>"
def test_edges_include_direct_and_encompassed(): ...
def test_stub_and_near_limit_flags_are_exported(): ...
def test_empty_graph_exports(): ...
```

- [ ] **Step 3: Run tests.** `.venv/Scripts/python -m pytest tests/test_export.py -v`. Expected: FAIL.
- [ ] **Step 4: Implement, with a template that renders only a heading for now.**
- [ ] **Step 5: Run tests.** Expected: PASS.
- [ ] **Step 6: Commit** with `feat: add map data export`.

### Task 9: Map page: rendering, search, panel

**Files:** Create `src/kg/map/app.js`, `tests/test_map_page.py`. Modify `template.html`, `pyproject.toml` (`map` dev extra).

**Interfaces:**
- Consumes: the `kg-data` shape from Task 8.
- Produces: `window.kgMap` test hook: `selectTopic(id)`, `selectedId()`, `search(text) -> string[]`, `panelText() -> string`, `topicCount()`, `ready: Promise`.

**Pinned rules:**
- Colours match the mockup: math `#534AB7`, physics `#D85A30`, chem `#1D9E75`, bio `#639922`, engr `#378ADD`. Edges are very faint.
- Topic labels appear on zoom through sigma's label threshold. Subject and course labels are drawn as a positioned HTML layer over the canvas, updated from the camera.
- Sigma's bundled renderer draws filled dots, so stubs use a pale tint of the subject colour instead of the spec's hollow dot. This keeps them distinct without another dependency.
- Render all user text with `textContent`, never `innerHTML`.
- Search matches a case-insensitive substring of name or ID, showing the first 20 results. Selecting a topic centres the camera and opens the panel.
- The panel shows the fields listed in the spec. Every linked topic is a button that selects it. Style the page with plain inline CSS, supporting light and dark modes.
- If WebGL fails, replace the canvas with: "This map needs WebGL, which your browser couldn't start."

- [ ] **Step 1: Ask the owner to approve `pytest-playwright` and the Chromium download.** If approved, install them with a `map` extra, launching Chromium with `--use-gl=swiftshader`. If declined, turn each test below into a written item in `tests/manual_map_checklist.md` and run it by hand.
- [ ] **Step 2: Write failing tests** against the sample graph.

```python
def test_all_topics_render_with_no_filters(page): assert topic_count(page) == len(sample.topics)
def test_search_finds_by_name_and_id(page): ...
def test_clicking_a_panel_link_selects_that_topic(page): ...
def test_panel_shows_kps_weights_and_confidence(page): ...
def test_markup_in_a_name_shows_literally(page):      # graph containing "<b>x</b>"
    select(page, "math.k.markup")
    assert "<b>x</b>" in panel_text(page) and page.locator("#panel b").count() == 0
def test_stub_can_be_selected(page): ...
def test_no_console_errors_on_load(page): ...
```

- [ ] **Step 3: Run tests.** `.venv/Scripts/python -m pytest tests/test_map_page.py -v`. Expected: FAIL.
- [ ] **Step 4: Implement `app.js` and the page.**
- [ ] **Step 5: Run tests.** Expected: PASS.
- [ ] **Step 6: Commit** with `feat: add map rendering, search, and topic panel`.

### Task 10: Map filters

**Files:** Modify `src/kg/map/app.js`, `template.html`, `tests/test_map_page.py`

**Interfaces:** Adds `kgMap.setFilters(obj)`, `kgMap.matchCount() -> int`, `kgMap.matchedIds() -> string[]`, and `kgMap.positions() -> object`.

**Pinned rules:**
- Filter shape: `{subjects: [], courses: [], levelMin, levelMax, statuses: [], confidences: [], nearLimits: bool, lineage: {topic, direction, maxSteps}}`. Empty or absent means no constraint. A topic must match every set filter.
- Confidence matches a topic if any of its incoming edges has that confidence.
- Fading uses sigma reducers only, so positions never change. An edge is drawn normally only when both ends match.
- The count reads `N of M topics`. Zero matches shows the count with a "Clear filters" action.
- Filter state is stored in the URL hash as encoded JSON and restored on load. Unknown topics, courses, or malformed hashes are ignored, and the whole graph shows.

- [ ] **Step 1: Write failing tests:** `test_no_filters_matches_everything`; `test_subject_course_and_level_filters`; `test_status_confidence_and_near_limit_filters`; `test_lineage_direction_and_step_limit` (expected sets from `lineage()` in Python); `test_filters_combine_as_and`; `test_filtering_never_moves_topics` (`positions()` identical before and after); `test_zero_matches_shows_count_and_clear`; `test_url_restores_filters`; `test_stale_hash_shows_whole_graph` (deleted topic, malformed JSON).
- [ ] **Step 2: Run tests.** Expected: FAIL.
- [ ] **Step 3: Implement.** Keep matching in pure functions over the data, separate from sigma.
- [ ] **Step 4: Run tests.** Expected: PASS.
- [ ] **Step 5: Commit** with `feat: add map filters and shareable URLs`.

### Task 11: Map check at full size

**Files:** Create `docs/superpowers/map-scale-check.md`. Possibly modify `app.js` for the edge fallback.

- [ ] **Step 1: Generate the page.** `.venv/Scripts/kg synth --topics 20000 --out build/synth`, then `.venv/Scripts/kg export-map --root build/synth --out build/synth-map.html`. Expected: writes the file.
- [ ] **Step 2: Open it in a browser and record** file size, seconds to first render, and how panning, zooming, a subject filter, and a lineage filter behave. Passing means it opens in under about 10 seconds, and panning, zooming, and filtering respond without long stalls.
- [ ] **Step 3: If edges cause the failure, apply the spec's fallback:** draw edges only past a zoom threshold or when a filter is on, leaving all topics visible. If the data size is the cause, shorten the embedded keys. Re-check.
- [ ] **Step 4: Show the owner the result on the synthetic graph,** and record it in `map-scale-check.md`. Done when the owner agrees the map is usable.
- [ ] **Step 5: Commit** with `docs: record map check at 20,000 topics`.

## Stage 3: Remaining tools

### Task 12: Safe edits

**Files:** Create `src/kg/edits.py`, `tests/test_edits.py`. Modify `cli.py`.

**Interfaces:**
- Produces:
  - `rename_id(kg, old, new) -> KnowledgeGraph`
  - `split_topic(kg, topic_id, new_id, new_name, move_kps: list[str], keep_new_kps: list[str] = [], new_kps: list[str] = []) -> KnowledgeGraph`
  - `apply_edit(new_kg) -> list[Issue]`, which writes only if `run_checks` has no errors and otherwise returns the errors
  - Commands: `rename-id OLD NEW`; `split-topic ID --new-id --new-name --move-kps kp3,kp4 [--keep-kp TEXT]... [--new-kp TEXT]...`
- All edit functions return new graphs and don't mutate their input. Each appends a `HistoryEntry`.

**Split rules:**
- The original keeps its ID and unmoved KPs. The new topic sits right after it and takes the moved KPs, which keep their IDs. `--keep-kp` and `--new-kp` add KPs with the next unused ID, which is how a 3-KP topic becomes two valid topics.
- The new topic's prerequisite is the original, at weight 0.5 and `confidence: low`.
- Dependents' direct prerequisites, encompassed entries, and key prerequisites pointing at the original are re-pointed to the new topic, because a dependent needed the whole topic. Re-pointed edges get `confidence: low` so they appear in the review queue.

- [ ] **Step 1: Write failing tests:** `test_rename_updates_every_reference` (direct, encompassed, key, view list); `test_rename_records_history`; `test_rename_to_existing_id_writes_nothing`; `test_split_moves_kps_and_repoints_dependents`; `test_split_result_validates`; `test_split_marks_changed_edges_low_confidence`; `test_split_leaving_one_kp_writes_nothing_and_exits_1` (files unchanged byte for byte); `test_split_three_kp_topic_with_added_kps_validates`; `test_kp_ids_stay_stable_after_inserting`.
- [ ] **Step 2: Run tests.** `.venv/Scripts/python -m pytest tests/test_edits.py -v`. Expected: FAIL.
- [ ] **Step 3: Implement.**
- [ ] **Step 4: Run tests.** Expected: PASS.
- [ ] **Step 5: Commit** with `feat: add rename-id and split-topic`.

### Task 13: Reports

**Files:** Create `src/kg/reports.py`, `tests/test_reports.py`. Modify `cli.py`.

**Interfaces:**
- Produces:
  - `stats(kg) -> dict`: counts by subject, course, and level; prerequisite-count, KP-count, weight, and depth distributions; confidence mix and budget variance per course
  - `review_report(kg) -> dict`: `low_confidence`, `near_limits`, `cross_subject`
  - `review_queue(kg, limit: int|None = None) -> list[QueueItem]`, with `QueueItem(topic, prerequisite, confidence, descendants, cross_subject)`, sorted by low confidence first, then descendant count descending, then cross-subject first, then ID
  - `find_duplicates(kg, threshold: float = 0.8) -> list[tuple[str, str, float]]`: Jaccard similarity on lowercased word sets of name plus `can_do` text, comparing only topics in different courses, and using an inverted word index rather than all pairs
  - Commands: `stats`, `review-report`, `review-queue [--limit N]`, `find-duplicates`, each with `--course` where meaningful and readable text output

- [ ] **Step 1: Write failing tests:** `test_stats_counts_match_a_known_graph`; `test_cross_subject_derived_from_subject_fields`; `test_queue_order` (asserting the full tie-break order on a small graph); `test_find_duplicates_flags_same_skill_in_two_courses`; `test_find_duplicates_ignores_same_course_and_unrelated`; `test_reports_handle_empty_graph`; `test_find_duplicates_under_30_seconds_on_20000_topics`.
- [ ] **Step 2: Run tests.** `.venv/Scripts/python -m pytest tests/test_reports.py -v`. Expected: FAIL.
- [ ] **Step 3: Implement.**
- [ ] **Step 4: Run tests.** Expected: PASS.
- [ ] **Step 5: Commit** with `feat: add stats, review reports, and duplicate detection`.

### Task 14: Weight CSV round trip

**Files:** Create `src/kg/weights.py`, `tests/test_weights.py`. Modify `cli.py`.

**Interfaces:** `export_weights(kg, out: Path)`; `import_weights(kg, csv_path: Path) -> KnowledgeGraph`, raising `WeightImportError(problems: list[str])`; commands `export-weights --out`, `import-weights FILE`, the latter using `apply_edit`. Columns: `topic,kind,prerequisite,encompassing,confidence`, with `kind` being `direct` or `encompassed`.

- [ ] **Step 1: Write failing tests.**

```python
def test_round_trip_changes_nothing(sample_copy): ...      # files byte-identical
def test_excel_style_file_imports(tmp_path):
    path.write_bytes("﻿topic,kind,prerequisite,encompassing,confidence\r\n...\r\n\r\n".encode())
    assert edge(import_weights(kg, path), ...).encompassing == 0.5
def test_rows_may_be_reordered(): ...
def test_omitted_rows_leave_weights_unchanged(): ...
def test_unknown_edge_out_of_range_and_bad_number_are_all_reported(): ...
def test_failed_import_writes_nothing(): ...
```

- [ ] **Step 2: Run tests.** `.venv/Scripts/python -m pytest tests/test_weights.py -v`. Expected: FAIL.
- [ ] **Step 3: Implement,** reading with `utf-8-sig`. Import may change only `encompassing` and `confidence`.
- [ ] **Step 4: Run tests.** Expected: PASS.
- [ ] **Step 5: Commit** with `feat: add weight CSV export and import`.

### Task 15: Commit gate and docs

**Files:** Create `.githooks/pre-commit`. Modify `CLAUDE.md`, `KG_PROMPT.md`. Test: `tests/test_hook.py`.

- [ ] **Step 1: Write failing test** `test_hook_blocks_commit_with_invalid_graph`: in a temp repo using the hook, committing a graph with a cycle exits non-zero, and a clean graph commits.
- [ ] **Step 2: Run test.** Expected: FAIL.
- [ ] **Step 3: Implement.** Make `kg.cli` runnable as a module. The POSIX `sh` hook runs `.venv/Scripts/python -m kg.cli validate` and blocks on non-zero, with a message if the venv is missing. Enable it with `git config core.hooksPath .githooks`.
- [ ] **Step 4: Run the full suite.** `.venv/Scripts/python -m pytest`. Expected: all pass.
- [ ] **Step 5: Update the docs.** In `CLAUDE.md`, list every command as actually built, including setup steps, and replace `export` with `export-map`. In `KG_PROMPT.md`, mark Phases 0 and 1 as done, and add showing the regenerated map to step 4 of the course procedure.
- [ ] **Step 6: Commit** with `feat: add validation commit hook and update docs`.

## After this plan

Stages 4 and 5 follow Phase 2 of `KG_PROMPT.md`, one course at a time, starting with `math.k` as the pilot. The pilot's topic list goes to the owner for approval before any content is written. After the pilot, re-check the map, and fold what it taught us back into `KG_PROMPT.md` and `CLAUDE.md`.
