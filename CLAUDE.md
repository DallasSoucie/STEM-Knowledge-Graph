# CLAUDE.md

## Project

A knowledge graph for a Math Academy-style adaptive learning app covering roughly Kindergarten through university-level **math, physics, chemistry, biology, and engineering**. Engineering is a common core first, then discipline courses (civil, chemical, mechanical, electrical, computer/software). Earth and space science is out of scope; home only what a topic genuinely needs in physics or chemistry. The graph (topics, knowledge points, prerequisites, encompassing weights) will later drive task selection, spaced review, and course sequencing. `KG_PROMPT.md` holds the size targets and course catalog.

**Scope of this repo: the graph and its tooling only.** No lesson text, no practice problems, no UI. If a task seems to require those, stop and ask.

## Hard constraints

- Everything here must be original. Build from general knowledge of standards and typical curricula (Common Core, NGSS, AP, standard university course sequences).
- **Never copy or closely mirror any specific textbook's table of contents, chapter structure, section titles, or wording.** Do not paste text from OpenStax or any other source. Prerequisite relationships are ideas and fine to derive; expression is not.
- Topic names are short, generic, and descriptive (e.g. "Solving two-step linear equations").
- Do not invent edges to make the graph look connected. A weak or uncertain link is marked `confidence: low`, not dressed up.

## Graph model

- **Topic**: one lesson-sized skill chunk. If it tries to do too much, split it.
- **Knowledge points (KPs)**: 3-4 per topic (2 or 5 only in rare cases), a ladder from the most basic version, to a twist (e.g. negatives), to another twist (e.g. fractions), to the pieces combined. Each KP has a one-line `can_do` statement.
- **Direct prerequisites** (topic to topic): typically 1-3, up to 4, hard cap 5. More than 4 requires a written `justification`.
- **Key prerequisites** (per KP): specific topics that KP leans on, which may sit many steps back. Keep to about 3-4 per KP; more means overload, so split or restructure.
- **Encompassing weight** (0.0-1.0, on each prerequisite edge and `encompassed` entry): the fraction of the prerequisite topic exercised, on average, by solving a problem in this topic. 0 means required first but not practiced. Used later to give implicit review credit.
- **Encompassed topics** (optional `encompassed` list): weighted topics that are not direct prerequisites, such as a key prerequisite several steps back. They carry review credit without adding a direct edge.
- **Cross-subject edges** are ordinary prerequisites between topics in different subjects (e.g. kinematics requires derivatives, stoichiometry requires ratios and unit conversion, statics requires vectors and trig). Math is the spine. Whether an edge is cross-subject is derived from the `subject` fields, not stored.
- **Level**: coarse ordinal `gk < g1 < g2 < ... < g12 < uni-lower < uni-upper`. Warn when a prerequisite's level is above the topic's level.
- **Stubs**: a prerequisite in a course not built yet gets a `status: stub` node (id and name only) so the graph stays valid. Fill stubs in later.
- **Status values**: `stub`, `draft`, `reviewed`. Only the human sets `reviewed`.
- **Confidence**: every prerequisite edge and `encompassed` entry carries `confidence: high|medium|low`. Encompassing weights are initial estimates to be recalibrated from real student data later, so keep them easy to bulk-update.

## Course sizing

- School courses: roughly year-long. University courses: roughly one semester, at most about 200 topics.
- Cover the common ground of what most strong universities teach for that course. Leave out idiosyncratic topics. Put second-course material (e.g. PDEs) in a separate course.
- K-8 science is split by subject into `elem` and `ms` courses (e.g. `physics.elem`, `physics.ms`), not one integrated course.

## Data format and conventions

- One YAML file per course under `graph/<subject>/<course>.yaml`.
- `graph/courses.yaml` is the course manifest and defines the intended course sequence: each course's subject, level range, topic budget, and the courses it follows, plus any view courses (lists of existing topic IDs that add no new topics).
- **IDs are readable slugs**: `<subject>.<course>.<topic-slug>`, e.g. `math.alg1.solve-two-step-equations`. Never numeric IDs, so a typo becomes a dangling reference that validation catches. IDs are stable; use `rename-id` rather than hand-editing references.
- Keep YAML diff-friendly: one key per line, stable key order, topics in course order.

Each course file wraps its topics in a `course:` / `topics:` mapping; the example below is one entry of `topics:`.

```yaml
course: math.alg1
topics:
  - id: math.alg1.solve-two-step-equations
    name: Solving two-step linear equations
    subject: math
    course: math.alg1
    level: g8
    status: draft
    prerequisites:
      - topic: math.alg1.solve-one-step-equations
        encompassing: 0.6
        confidence: high
    encompassed:
      - topic: math.g6.fraction-operations
        encompassing: 0.15
        confidence: medium
    knowledge_points:
      - id: kp1
        can_do: Solve ax + b = c with positive integer coefficients
        key_prerequisites: [math.alg1.solve-one-step-equations]
      - id: kp2
        can_do: Solve two-step equations with fractional coefficients
        key_prerequisites: [math.g6.fraction-operations]
```

## Stack

Python 3.11+, pydantic (schema), PyYAML (with LibYAML), networkx (graph logic), typer (CLI), pytest. If the plan proposes a better fit, get approval before switching, then update this section.

## Setup

```
python -m venv .venv
.venv/Scripts/python -m pip install -e .[dev,map]
.venv/Scripts/python -m playwright install chromium
git config core.hooksPath .githooks
```

The `.githooks/pre-commit` hook runs `kg validate` and blocks the commit on failure. Run commands as `.venv/Scripts/kg <command>` or `.venv/Scripts/python -m kg.cli <command>`. Every graph command takes `--root` (default `graph`). The hook validates the working tree, not just the staged files.

## Commands

Update this section as the tooling is built, and keep it accurate.

- `validate` - the gate for all content changes (see below)
- `stats` - counts by subject/course/level, prerequisite, KP and weight distributions, depth
- `ancestors` / `descendants` / `path` - graph queries
- `split-topic`, `rename-id` - safe structural edits (rename updates every reference and records `id-history.yaml`)
- `export-weights` / `import-weights` - round-trip edge weights and confidences through CSV
- `review-report` - low-confidence edges, topics near limits, all cross-subject edges (direct and encompassed edges, labelled by kind)
- `review-queue` - prerequisite and encompassed edges ranked by review risk
- `find-duplicates` - topic pairs in different courses that look like the same skill
- `export-map` - write the offline curriculum map to `build/map.html` (not committed; refuses if validation fails)
- `synth` - write a synthetic valid graph, for testing only
- `pytest` - run tests (`.venv/Scripts/python -m pytest`)

## Validation (must stay green)

`validate` fails on: cycles, dangling references, duplicate IDs, KP count outside 2-5, more than 4 direct prerequisites without `justification`, more than 4 key prerequisites per KP, weights outside 0-1, orphan nodes, gaps (a prerequisite missing from the course sequence in `graph/courses.yaml`), a key prerequisite that is neither a direct prerequisite nor an ancestor, a key prerequisite missing from both `prerequisites` and `encompassed`, an `encompassed` topic that is not an ancestor, a stub with no dependent, an ID that is not `<subject>.<course>.<slug>` in lowercase (`id-format`), a topic in a course missing from the manifest or in a view course (`unknown-course`), courses whose `follows` form a cycle (`manifest-follows-cycle`), a topic whose prerequisite is not yet known when its course sequence reaches it (`learner-walk`), more courses in a subject than its map row has lanes (`lane-overflow`), a non-stub topic whose level is outside its course's level range (`level-outside-course`), and duplicates: a repeated ID, a repeated prerequisite or `encompassed` entry or KP ID within one topic, or a repeated course in `courses.yaml` (`duplicate-id`). A course file that is not at the path its `course:` names is a load error. Stubs are exempt from the KP count. It warns on: redundant edges implied transitively, prerequisites above the topic's level, a topic where every KP has 3 or more key prerequisites, a topic above `gk` with no prerequisites, weights in a course clustering on a few values, a course more than 20% off its budget.

**Run `validate` after every batch of content and before every commit. Never leave the graph in an invalid state.**

## Workflow rules

1. **Plan before generating.** For any new course, propose its topic list (with estimated count and level range) and wait for approval before writing it.
2. **Work course by course**, math first (it is the spine), then physics, chemistry, biology, engineering, linking back to math.
3. **Self-review each course before presenting it**: look for overloaded topics, large conceptual jumps (insert a stepping-stone topic or split), missing prerequisites, and weak or invented links. Then run `review-report`.
4. **Prefer small steps.** A key prerequisite is something the student genuinely needs, not something merely related.
5. **Small commits**, one logical batch each (e.g. "Add math.g4 fractions topics"), validation passing.
6. **When unsure, say so**: mark `confidence: low` and surface it in the review report instead of guessing silently. Ask before making structural decisions (renaming a course, changing the schema, changing scope).

## Don't

- Don't write lessons, problems, or explanations of content.
- Don't copy from or closely follow any textbook structure or text.
- Don't set `status: reviewed`.
- Don't change the schema, validation rules, or sizing limits without approval.
- Don't silently drop or loosen a validation failure to make the graph pass; fix the data, or ask.

## Reference Materials

- Reference materials are available
- References should not be strictly followed, especially curriculum. This is just to help in decision making.
- Relevant BC Curriculum: "C:\AI\Learn STEM\refs\bc-curriculum"
- Textbooks: "C:\AI\Learn STEM\refs\Textbooks" 
- Uni course descriptions with prerequisites: "C:\AI\Learn STEM\refs\uni_course_descriptions"
- Common Core math standards: "C:\AI\Learn STEM\refs\common-core-standards\Math_Standards1.pdf". Compare against the BC curriculum and use best judgement where they differ.
