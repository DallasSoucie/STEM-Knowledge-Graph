# Map Flow Layout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the map's fixed curriculum bands with a left-to-right flow driven by prerequisites, whose stages widen and narrow with the data.

**Architecture:** `src/kg/map/layout.py` computes each topic's stage and vertical order from the graph. `src/kg/map/data.py` passes positions, level markers, and stage spacing to `src/kg/map/app.js`, which drops the band labels. The YAML and all validation except `lane-overflow` stay as they are.

**Tech Stack:** Python 3.11+, networkx, pytest, pytest-playwright, sigma.js 3.0.2 (vendored).

**Spec:** `docs/superpowers/specs/2026-11-06-flow-layout-design.md`

## Global Constraints

- No new dependencies. Positions are computed in Python and are repeatable.
- Only direct prerequisites affect position, not `encompassed` entries.
- `LINE_SPACING = 1.0`. `STAGE_SPACING` starts at `4.0`, tuned by hand on `math.k` in Task 4.
- Floors: first level with topics is 0; each later level with topics is `max(previous floor + 1, lower quartile of its topics' depths)`.
- Four sweeps: forward, back, forward, back. Ties break on topic ID.
- Don't weaken or remove a test to make it pass, except tests of the removed bands and `lane-overflow`. If a test's graph relied on bands, give it edges or levels that exercise the same behaviour.
- Run tests with `.venv/Scripts/python -m pytest`. `kg validate --root graph` must stay green, with the pre-commit hook enabled.

## Review Focus

- A graph with no edges puts every topic in one stage: it must open as one column, without dividing by a zero width. (Task 3)
- A prerequisite at a higher level than its dependent: the dependent still sits to its right, even past its own level's floor. (Task 2)
- A stub with no level and a prerequisite pointing at it: the stub gets stage 0 and the dependent sits to its right. (Task 2)
- A topic whose course or subject isn't in the manifest or `SUBJECT_ORDER`: it gets a position, ordered after known ones. (Task 2)
- An empty graph, and a manifest with view courses: no error, and view courses add no positions. (Task 2)

---

### Task 1: Remove the `lane-overflow` rule

**Files:**
- Modify: `src/kg/checks/structure.py` (import on line 8, rule at lines 188-196)
- Modify: `CLAUDE.md` (validation paragraph, line 104)
- Test: `tests/test_checks.py` (lines 167-170, 210, 454-end of that test), `tests/test_cli.py` (test at line 96)

**Interfaces:**
- Produces: `kg.checks` no longer imports `kg.map.layout`.

- [ ] **Step 1: Delete the rule, its import, the `lane_overflow` fixture and its parametrize row, and both tests.** In `CLAUDE.md`, delete only the phrase `more courses in a subject than its map row has lanes (`lane-overflow`), `.

- [ ] **Step 2: Add a test to `tests/test_checks.py`**

```python
def test_validation_does_not_depend_on_the_map():
    import kg.checks.structure as s
    assert not hasattr(s, "lane_overflows")
```

- [ ] **Step 3: Run the checks and CLI tests**

Run: `.venv/Scripts/python -m pytest tests/test_checks.py tests/test_cli.py -q`
Expected: all pass.

- [ ] **Step 4: Commit**

```bash
git add src/kg/checks/structure.py CLAUDE.md tests/test_checks.py tests/test_cli.py
git commit -m "Remove the lane-overflow validation rule"
```

### Task 2: Compute stages and flow positions

**Files:**
- Modify: `src/kg/map/layout.py` (add alongside the band code, which Task 3 deletes)
- Test: `tests/test_flow_layout.py` (create)

**Interfaces:**
- Consumes: `KnowledgeGraph` (`.topics`, `.courses`), `LEVELS`, `conftest.add/course/stub/topic`.
- Produces:
  - `STAGE_SPACING: float = 4.0`
  - `topic_depths(kg) -> dict[str, int]`
  - `level_floors(kg, depths) -> dict[str, int]`, with only levels that have topics
  - `topic_stages(kg) -> dict[str, int]`
  - `flow_positions(kg) -> dict[str, tuple[float, float]]`

- [ ] **Step 1: Write the failing tests in `tests/test_flow_layout.py`**, building graphs with the `conftest` helpers:

| Test | Assertion |
|---|---|
| `test_every_topic_is_right_of_its_prerequisites` | on `generate(500)`, every edge has `x(prereq) < x(topic)` |
| `test_depth_follows_the_deepest_prerequisite` | a chain a→b→c plus a→c gives depths 0, 1, 2 |
| `test_first_level_floor_is_zero` | `level_floors` for a gk chain gives `{"gk": 0}` |
| `test_floor_uses_the_lower_quartile` | four g3 topics at depths 4, 5, 6, 7 and gk at 0 to 7 give `floors["g3"] == 4` with quartile by `statistics.quantiles(d, n=4, method="inclusive")[0]`, rounded down |
| `test_floors_always_increase` | a g3 topic at depth 0 after a gk topic at depth 0 gives floors 0 and 1 |
| `test_shallow_high_level_topic_waits_for_its_floor` | that g3 topic's stage equals `floors["g3"]`, past its depth of 0 |
| `test_inverted_level_prerequisite_stays_ordered` | a g5 prerequisite of a g2 topic: dependent's stage is greater |
| `test_stub_has_stage_zero_and_dependent_follows` | stub with no level: stage 0, dependent's stage at least 1 |
| `test_unknown_course_and_subject_still_get_positions` | a topic in `bio.x` missing from the manifest, plus a `zzz.y` topic, get positions and sit after known courses in their stage |
| `test_stage_groups_by_subject_then_course` | in one stage, y order runs math, then physics; within math, manifest course order |
| `test_courses_stay_contiguous_within_a_stage` | on a stage holding two courses, no topic of one falls between topics of the other |
| `test_each_stage_is_centred` | every stage's mean y is 0, and neighbours are `LINE_SPACING` apart |
| `test_sweeps_reduce_crossings` | two parallel chains listed in crossed order end up with fewer crossings than with their ID order |
| `test_positions_are_repeatable` | two calls on `generate(500)` are equal |
| `test_no_two_topics_share_a_position` | on `generate(500)` |
| `test_empty_graph_gives_no_positions` | `flow_positions(KnowledgeGraph()) == {}` |
| `test_view_courses_add_no_positions` | a view course's listed topics each keep one position, and the count equals `len(kg.topics)` |

- [ ] **Step 2: Run to verify they fail**

Run: `.venv/Scripts/python -m pytest tests/test_flow_layout.py -q`
Expected: FAIL with `ImportError` on `flow_positions`.

- [ ] **Step 3: Implement in `layout.py`**

Build a `networkx.DiGraph` from direct prerequisites, skipping any that aren't in `kg.topics`, and walk `nx.lexicographical_topological_sort` for determinism. Group key per topic: `(subject rank, course rank)`, where subject rank is the index in `SUBJECT_ORDER` and then manifest order, course rank is manifest order, and unknown ones sort last by name.

The sweeps and centring:

```python
position = {id: index - (len(stage) - 1) / 2 for each stage, starting from sorted ID within group}
for neighbours in (prerequisites, dependents, prerequisites, dependents):
    for stage in stages, ascending when neighbours are prerequisites, else descending:
        key = (group, mean(position[n] for n in neighbours[id]) or position[id] if none, id)
        reassign position from stage sorted by key
x = stage * STAGE_SPACING
y = position * LINE_SPACING
```

- [ ] **Step 4: Run to verify they pass**

Run: `.venv/Scripts/python -m pytest tests/test_flow_layout.py -q`
Expected: all pass.

- [ ] **Step 5: Commit**

```bash
git add src/kg/map/layout.py tests/test_flow_layout.py
git commit -m "Add flow layout stages and positions"
```

### Task 3: Switch the map to the flow layout

**Files:**
- Modify: `src/kg/map/layout.py` (delete everything band-related; update the module docstring)
- Modify: `src/kg/map/data.py`
- Modify: `src/kg/map/app.js`, `src/kg/map/template.html`
- Delete: `tests/test_layout.py`
- Test: `tests/test_export.py`, `tests/test_map_page.py`

**Interfaces:**
- Consumes: `flow_positions`, `topic_stages`, `level_floors`, `topic_depths`, `STAGE_SPACING` from Task 2.
- Produces: `build_map_data` returns keys `levels`, `subjects` (`[{"id"}]`), `courses` (no `lane`), `level_markers` (`[{"level", "x"}]`), `stage_spacing`, `topics`, `edges`.
- Produces: `window.kgMap.nextStageRoom` is not added; label room is covered in Task 4.

- [ ] **Step 1: Update `tests/test_export.py:104`** to the new key set, and add:

```python
def test_level_markers_sit_at_each_floor(sample_graph):
    data = build_map_data(sample_graph)
    floors = level_floors(sample_graph, topic_depths(sample_graph))
    assert {m["level"]: m["x"] for m in data["level_markers"]} == {
        lv: f * STAGE_SPACING for lv, f in floors.items()
    }

def test_stub_level_falls_back_to_its_courses_first_level():
    ...  # stub in a course with levels ("g4", "g6") shows level "g4"; with no manifest entry, LEVELS[0]
```

- [ ] **Step 2: Add to `tests/test_map_page.py`** and remove the `.lbl-subject` assertion at line 448:

```python
def test_graph_with_no_edges_opens_as_one_column(page, tmp_path):
    errors = open_map(page, small_graph(60), tmp_path)
    assert page.evaluate("window.kgMap.topicCount()") == 60 and errors == []

def test_no_subject_gutter(sample_page):
    assert sample_page.locator("#gutter").count() == 0

def test_level_markers_show_and_never_overlap(page, tmp_path):
    ...  # a chain through gk, g1, g2: three .lbl-level spans visible, with no overlap via visible_rects

def test_course_label_sits_at_its_largest_stage(page, tmp_path):
    ...  # stages of sizes 1, 5, 2: the label's left edge is within one stage of the 5-topic stage's x
```

- [ ] **Step 3: Run to verify they fail**

Run: `.venv/Scripts/python -m pytest tests/test_export.py tests/test_map_page.py -q`
Expected: the new tests FAIL.

- [ ] **Step 4: Change `data.py`.** Use `flow_positions`. A topic's `level` is `t.level`, else the first level of its course in the manifest, else `LEVELS[0]`. Remove `_level_at`.

- [ ] **Step 5: Change `app.js` and `template.html`.**
- Remove `#gutter`, its CSS, `.lbl-subject`, `gutterEl`, `subjectLabels`, `paintSubject`, `placeSubjects`, and the `76px` insets on `#map` and `#labels`.
- `placeLevels(w)`: one label at each marker's x, at the same sticky y as now. Hide it when off-screen, or when it would overlap a marker already placed in this frame.
- `buildOverlay`: keep each course's full extent for deciding visibility, and add `anchorX` and `anchorY`: the x and top y of the stage holding most of its topics, with the leftmost winning a tie. `placeCourses` positions the label from the anchor instead of the block's top-left corner.

- [ ] **Step 6: Delete the band code and `tests/test_layout.py`.** `grep -rn "lane\|row_bounds\|column_bounds\|compute_positions\|_subject_rows" src tests` must return only `tests/fixtures` content and unrelated words.

- [ ] **Step 7: Run the full suite**

Run: `.venv/Scripts/python -m pytest -q`
Expected: all pass. Where a map test fails because its graph has no edges and now forms one column, give it a chain or levels that exercise the same behaviour, per Global Constraints.

- [ ] **Step 8: Commit**

```bash
git add -A src tests
git commit -m "Draw the map as a prerequisite flow"
```

### Task 4: Measure name room by stage, tune, and check at scale

**Files:**
- Modify: `src/kg/map/app.js` (`nextDotGap`, `fitLabel`)
- Modify: `src/kg/map/layout.py` (`STAGE_SPACING`, if tuning changes it)
- Modify: `docs/superpowers/map-scale-check.md`
- Modify: `docs/superpowers/specs/2026-11-05-knowledge-graph-tooling-and-map-design.md` (the "once that is built" note)
- Test: `tests/test_map_page.py`

**Interfaces:**
- Consumes: `data.stage_spacing` from Task 3.

- [ ] **Step 1: Change the name tests.** `named_course_graph` needs a chain so stages exist. Keep `test_small_course_names_every_topic_on_a_wide_window` and `test_small_course_labels_stay_inside_the_window`, and add:

```python
def test_a_name_never_reaches_the_next_stage(page, tmp_path):
    ...  # at 1920x1080, every topic rect's x1 - 12 stays left of the x of the next stage's dots, except in the last stage
```

- [ ] **Step 2: Run to verify the new test fails**

Run: `.venv/Scripts/python -m pytest tests/test_map_page.py -k "name" -q`
Expected: FAIL.

- [ ] **Step 3: Replace `nextDotGap`.** In `fitLabel`, room to the next stage is `data.stage_spacing * pxPerUnit - d.size - 9`, or `Infinity` when the topic is in the last stage. Delete `dotsByLine`.

- [ ] **Step 4: Run the tests**

Run: `.venv/Scripts/python -m pytest tests/test_map_page.py -q`
Expected: all pass.

- [ ] **Step 5: Tune by hand.** Run `.venv/Scripts/kg export-map --root graph`, look at `math.k` at 1280px and 1920px, and change `STAGE_SPACING` if names are too short or the flow too flat. Rerun the suite after any change.

- [ ] **Step 6: Check scale.** Run `kg synth --topics 20000` into a scratch folder, export it, and measure file size, seconds to first render, pan and zoom frame times, and filter times, as in `map-scale-check.md`. Record them there, with stage count, tallest stage, and overview proportions. Expected: opens in about 10 seconds, with no frame over 100 ms under software GL apart from those the doc already explains. If that fails, stop and report rather than adding fallbacks.

- [ ] **Step 7: Update the old spec's note** to "Replaced by `2026-11-06-flow-layout-design.md`."

- [ ] **Step 8: Run everything and commit**

Run: `.venv/Scripts/python -m pytest -q` and `.venv/Scripts/kg validate --root graph`
Expected: all pass; 0 errors, 0 warnings.

```bash
git add src tests docs
git commit -m "Fit topic names to the flow's stages and record the scale check"
```
