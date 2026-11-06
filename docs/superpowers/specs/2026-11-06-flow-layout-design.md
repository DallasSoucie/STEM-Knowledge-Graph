# Map flow layout: design

**Date:** 2026-11-06
**Status:** approved
**Replaces:** the "Layout: curriculum bands" section of `2026-11-05-knowledge-graph-tooling-and-map-design.md`, and the band-related risks and validation there

## Purpose

The map's fixed bands don't show how learning flows. The owner wants topics laid out so progression is as clear as possible, with the shape growing and shrinking as the graph does, rather than a continuous band.

This changes where the map draws topics and nothing else in the graph. The YAML, prerequisites, and the other validation rules stay as they are.

## Success criteria

1. Every topic sits to the right of all its direct prerequisites.
2. No topic sits left of its level's floor.
3. Stages visibly widen and narrow with the data, on `math.k` at least.
4. Topics in one course sit together within each stage, and subjects stay in one order from top to bottom.
5. The same graph always gives the same positions.
6. Search, filters, the side panel, and name shortening all still work.
7. The 20,000-topic map still opens in about 10 seconds, with no long stalls while panning, zooming, or filtering.

## Layout

All of it is computed in Python in `src/kg/map/layout.py`, with no new dependencies. Only direct prerequisites affect position, not `encompassed` entries.

### Stage (x)

1. **Depth:** a topic with no prerequisites has depth 0. Any other topic has depth one more than its deepest direct prerequisite.
2. **Level floors:** go through the levels from `gk` up, skipping levels with no topics. The first level with topics has floor 0. Each later level has a floor equal to the larger of the previous floor plus 1 and the lower quartile of its topics' depths.
3. **Stage:** walking the graph in topological order, a topic's stage is the larger of its level's floor and one more than its deepest direct prerequisite's stage. A stub has no level, so only its prerequisites count.

The floor keeps unusually shallow topics out of earlier grades. The lower quartile is used instead of the median so that topics don't pile up in a wall at the floor.

`x = stage * STAGE_SPACING`, with a starting value of 4 line spacings, to be tuned on `math.k`.

### Order within a stage (y)

Topics in a stage are grouped by subject in `SUBJECT_ORDER`, then by course in manifest order. Within a course, four sweeps (forward, back, forward, back) reorder topics by the average position of their neighbours in the previous stages or the later ones, to reduce crossing lines. Ties break on topic ID.

Each stage is then centred vertically on y = 0, with topics `LINE_SPACING` apart. Centring is what makes the shape swell and narrow.

## Display

- **Removed:** subject rows, the subject gutter, and level columns.
- **Subject:** shown by dot colour, as now. The subject filter stays.
- **Course labels:** placed at the top of the course's largest stage, using the existing logic for claiming space, so more appear as you zoom in.
- **Level markers:** a small label along the top at each level's floor, so the rough position of each grade stays visible.
- **Names:** the existing shortening stays. A name's room becomes the distance to the next stage, or the window's edge if that's closer, because dots in a stage no longer share a line with the next dot.
- **Edges and big maps:** unchanged, including showing edges on big maps only when zoomed in or filtered.

`topic.level` in the map data needs a fallback for stubs now that levels have no columns: the level of the course's first level in the manifest.

## Removed code and rules

- `LANE_CAPACITY`, `DEFAULT_LANE_CAPACITY`, `lane_of`, `lane_overflows`, `row_bounds`, `column_bounds`, and the related constants in `layout.py`
- The `lane-overflow` validation rule and its tests. The owner approved removing it by accepting this design; the rule existed only to protect the fixed lanes.
- The subject `y0`/`y1`, course lane, and `columns` entries in the map data
- The spec's promises that adding a topic only respaces its own course. Adding a prerequisite can now move everything after it.

`CLAUDE.md` loses `lane-overflow` from its validation list.

## Testing

- **Layout (replacing `tests/test_layout.py`):** criteria 1, 2, 4, and 5 on small graphs, plus the floor on a graph with shallow high-level topics, and stubs.
- **Map page:** existing tests adapted to the removed labels. New: level markers appear, and names stay inside the window.
- **By hand:** look at `math.k` at 1280px and 1920px, and tune `STAGE_SPACING`.
- **Scale:** repeat the checks in `docs/superpowers/map-scale-check.md` on the 20,000-topic graph, and record the results there.

## Risks

| Risk | Response |
|---|---|
| The full graph comes out as a long thin ribbon. A throwaway test on the synthetic graph gave 1,045 stages and at most 42 topics in a stage. Its edges are chain-like by construction, so it overstates depth, but real proportions are unknown. | Recheck the map's proportions as `math.g1` onward arrive, and at the math milestone at the latest. If the ribbon is real, wrap the flow into rows at grade boundaries. Not built now. |
| Real cross-subject edges tangle the middle of the flow. | Can't be tested until those edges exist. Lineage filters isolate a path in the meantime. |
| Positions shift a lot as courses are added, so the map is less familiar from one build to the next. | Accepted by the owner as the cost of a layout that adapts. |
| Levels no longer line up in columns, so grades overlap horizontally. | Accepted. Level markers show rough positions, and the level filter still isolates a grade. |

## Out of scope

- Row wrapping at grade boundaries
- Curved edges
- Saving positions between builds to reduce movement
- Changing `validate` or the learner walk, other than removing `lane-overflow`
