# Knowledge graph tooling and map: design

**Date:** 2026-11-05
**Status:** awaiting owner review
**Repo:** https://github.com/DallasSoucie/STEM-Knowledge-Graph

## Purpose

Build the tooling for a Kindergarten-to-university STEM knowledge graph, and a zoomable map for navigating it. The owner uses the map to explore and review the graph as it grows to about 15,700 topics. It is an authoring tool, not the learner-facing app.

`CLAUDE.md` is the source of truth for the graph model, validation rules, and workflow. `KG_PROMPT.md` holds the size targets, course catalog, and authoring heuristics. This spec covers how to build the tools and how content production runs on top of them.

## Success criteria

1. `validate` catches every rule in `CLAUDE.md` and finishes in under 10 seconds on a synthetic 20,000-topic graph.
2. The map opens as one offline HTML file, and shows every topic with no filters on.
3. From any topic, the owner can reach its prerequisites, dependents, knowledge points, and weights in a few clicks.
4. Curriculum, lineage, and review-state filters narrow the view without moving any topic.
5. The map stays usable on the 20,000-topic synthetic graph.
6. A repeatable course procedure produces validated, reviewable courses, proven on `math.k`.

## Out of scope

- Lessons, problems, and learner UI
- Editing from the map
- A server or database
- A map filter for edge attributes such as weight range (possible later version)
- A force-directed map view (possible later version)
- Student data and recalibration, beyond keeping the CSV round trip and stable IDs ready

## Architecture

The YAML files are the only source of truth. Everything else, including the map, is generated from them.

```
graph/
  courses.yaml            manifest: course sequence, levels, budgets, view courses
  id-history.yaml         old-to-new IDs from splits and renames
  <subject>/<course>.yaml topics in course order
src/kg/
  model.py                pydantic schema: Topic, KnowledgePoint, edges, Course
  store.py                load and write YAML in one canonical format
  graph.py                build the networkx graph and answer lineage queries
  checks/                 one small function per rule, each returning issues
  edits.py                split-topic and rename-id
  reports.py              stats, review-report, review-queue, find-duplicates
  weights.py              CSV export and import
  map/                    layout, data export, page template, pinned JS libraries
  cli.py                  thin typer commands that call the modules above
tests/
```

**Stack:** as in `CLAUDE.md`, plus PyYAML with the LibYAML parser. `pytest-playwright` is a proposed development-only dependency; it needs a Chromium download, so ask the owner before installing it.

### Storage rules

- All writes go through `store.py`, which always produces the same key order and layout, so tool edits show up as small diffs.
- Graph YAML contains no comments, because tools rewrite whole files. Notes belong in real fields such as `justification`.
- `graph/courses.yaml` lists each course's subject, level range, topic budget, and the courses it follows, plus view courses as lists of existing topic IDs.
- `graph/id-history.yaml` records each rename and split, so that student records can follow them later.
- Knowledge point order comes from list position. A new knowledge point takes the next unused ID, so per-KP data stays attached when a rung is inserted.

### Validation

Each rule is a function that takes the loaded graph and returns issues. An issue has a severity (`error` or `warning`), a file, a topic ID, a rule name, and a message. `validate` runs every rule, prints all issues, and exits non-zero if any is an error.

The rules are those in the `CLAUDE.md` validation section, plus:

- **Learner walk (error):** starting from nothing, walk each course sequence in order and confirm every topic becomes reachable. This stands in for Math Academy's practice of running the real model build until we have a model.
- **Encompassed ancestry (error, new rule):** every `encompassed` topic must be an ancestor of the topic. Otherwise a student could get review credit for a topic they were never required to learn. Approving this spec approves this rule, and `CLAUDE.md` is updated to match.
- **Lane overflow (error):** the map gives each subject row a fixed number of lanes. A manifest that needs more lanes than the row holds fails `validate`, so `export-map` never meets it.
- **Level outside course (error):** a non-stub topic whose level lies outside its course's level range in the manifest.

If LibYAML parsing alone breaks the 10-second target, add a cache of parsed files, keyed on file hash. Build the cache only if the speed test fails.

### Commands

All commands run as `kg <command>`:

| Command | Purpose |
|---|---|
| `validate` | The gate for all content changes |
| `stats` | Counts and distributions, including budget variance |
| `ancestors`, `descendants`, `path` | Graph queries |
| `split-topic`, `rename-id` | Safe structural edits |
| `export-map` | Generate the map (replaces `export` in `CLAUDE.md`; Graphviz output is dropped) |
| `review-report` | Low-confidence edges, topics near limits, cross-subject edges |
| `review-queue` | Review items ranked by low confidence, then descendant count, then cross-subject |
| `find-duplicates` | Likely duplicate topics, from names and `can_do` text across courses |
| `export-weights`, `import-weights` | Round-trip all weights through CSV |

`split-topic`, `rename-id`, and `import-weights` validate the result first and write nothing if it fails. A pre-commit hook runs `validate`. Update the Commands section of `CLAUDE.md` as each command is built.

A topic is **near the limits** if it has 4 or more direct prerequisites, has a KP with 4 key prerequisites, has 2 or 5 KPs, or has every KP at 3 or more key prerequisites.

## The map

### Layout: curriculum bands

Replaced by `2026-11-06-flow-layout-design.md`, once that is built.

Positions are computed in Python and are repeatable.

- **Columns:** the x axis has one column per level, from `gk` to `uni-upper`. Column width comes from the topic budgets in the manifest, not from current topic counts, so a growing course doesn't shift the columns.
- **Rows:** the y axis has one row per subject: math, physics, chemistry, biology, engineering. Each row has a fixed lane capacity (math 12, physics 8, chem 8, bio 12, engr 30), so rows never move each other. A subject needing more lanes is an error.
- **Lanes:** lanes have one fixed height and are assigned to courses in manifest order. Courses with non-overlapping level ranges can share a lane. Courses at the same level get separate lanes, which keeps them from piling up.
- **Topic position:** a course's topics at one level form a block inside its column and lane, wrapped into 8 lines like text, in listed order. Line length comes from the course's budget; past budget the lines tighten and never grow taller.

Adding a topic respaces only its own course. Adding a course can shift lanes within its own subject row, but not other rows. A new course whose per-level budget share exceeds the largest share at any level it spans widens that column, which shifts the x positions of every row from that level on. View courses add no positions.

### Display

- Zoomed out: every topic and edge, with subject and course labels. Edges are very faint. Topics are coloured by subject.
- Zoomed in: topic names appear.
- Stubs appear as a pale tint of their subject colour, since the renderer draws filled dots only.
- Fallback: if the 20,000-topic test shows all edges can't stay usable, draw edges only past a zoom threshold or when a filter is on. Topics always show.

### Interaction

- **Search:** by name or ID. Selecting a result centres the map on that topic and opens its panel.
- **Side panel:** a topic's name, ID, course, level, and status; its knowledge points with `can_do` and key prerequisites; and its prerequisites, encompassed topics, and dependents, with weights and confidence. Clicking any linked topic jumps to it.
- **Filters:**
  - Curriculum: subject, course, level range
  - Lineage: from the selected topic, its prerequisites, dependents, or both, with an optional step limit
  - Review state: status, edge confidence, topics near the limits
- Filters combine, so a topic must match all of them. Unmatched topics fade but stay in place, and a count shows how many match.
- Filter state lives in the URL, so a saved link restores the view.

The map is read-only.

### Build

`kg export-map` writes a single offline `build/map.html`, which is not committed. The page embeds the graph data and pinned copies of sigma.js and graphology, which are committed under `src/kg/map/`. Fetching those files needs the owner's approval when they are first added. No Node.js is needed to build or open the map.

`export-map` refuses to run if `validate` reports errors. If the browser can't start WebGL, the page says so rather than showing a blank canvas.

## Testing

- **Tooling:** test-first with pytest. Each validation rule has one graph that passes and one that fails.
- **Synthetic generator:** produces 20,000 topics at the target distributions of about 3.4 KPs and 5 weighted relationships per topic, as valid data. Used for the `validate` speed test and the map test.
- **Map data:** Python tests cover layout repeatability, the stability rules above, and the exported data.
- **Map behaviour:** browser tests open the real page and check search, filter counts, and lineage. If `pytest-playwright` isn't approved, these become a written manual checklist.
- **Map usability:** checked by hand in a browser on the synthetic graph. Usable means it opens in under about 10 seconds, and panning, zooming, and filtering respond without long stalls.

## Build stages

| Stage | Builds | Done when |
|---|---|---|
| 1. Foundation | Packaging, schema, store, manifest, validation rules, core CLI, sample graph, synthetic generator | Tests pass, every rule is shown failing on a broken graph, and the speed test passes |
| 2. Map | Layout, `export-map`, page, search, panel, filters | The sample graph is navigable, and the synthetic graph meets the usability bar |
| 3. Remaining tools | Edits, reports, weights CSV, pre-commit hook | Each has tests, and a rename or split leaves the graph valid |
| 4. Pilot course | `math.k` through the course procedure | The owner accepts it, and lessons are folded back into the docs |
| 5. All courses | Remaining courses, in `KG_PROMPT.md` order | Pauses at math, core graph, and full graph |

The detailed implementation plan covers stages 1-3. Stages 4 and 5 use the course procedure below.

## Course procedure

Phase 2 of `KG_PROMPT.md` defines this procedure. In short, for each course: present the topic list and stop for approval, write it in validated batches of 20-40 topics, self-review, then present reports and the regenerated map. Each course needs the owner's acceptance, and content will span many sessions.

## Risks

| Risk | Response |
|---|---|
| 78,000 edges draw as a smear or lag | Test on the synthetic graph in stage 2, and use the edge fallback |
| Long edges between subject rows add clutter | Faint edges by default, and lineage filters to isolate a path |
| Data makes `map.html` very large | Measure on the synthetic graph, and shorten the embedded keys if needed |
| `validate` slows down as rules grow | The speed test runs in the test suite, so a slowdown fails visibly |
| Synthetic data hides real-world layout problems | Re-check the map at the pilot course and at each milestone |
| The owner can't review everything | `review-queue` sends attention to the highest-leverage edges first |

## Repository

- Remote: `origin` at the repo above
- Ignored: `build/`, `.superpowers/`, `refs/` (4.2 GB of reference material), and the two Math Academy transcripts
