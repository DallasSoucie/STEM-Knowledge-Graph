# Map check at 20,000 topics

Measured with Playwright and headless Chromium on `kg synth --topics 20000` (96,727 edges),
exported with `kg export-map`. Driver scripts and screenshots are under `build/` (not committed).

Software GL caveat: headless Chromium here used SwiftShader, a CPU rasteriser. It understates a
real GPU by a wide margin, so every frame time below is a conservative bound. The failures it
exposed (per-node and per-edge draw cost) are real in kind but will be far smaller on a GPU.

## Result

| | First attempt | After fallbacks | After layout fix (two runs) |
|---|---|---|---|
| File size | 18.2 MB | 18.2 MB (13.9 MB topics and knowledge points, 4.0 MB edges) | 18.3 MB |
| Seconds to first render | 2.9 | 0.4 to 0.8 (three runs: 0.41, 0.41, 0.42; one full measure: 0.79) | 0.42, 0.45 |
| Pan, zoomed out (median / worst frame) | 17 ms / 1150 ms | 16 ms / 24 ms | 17 ms / 24 ms |
| Zoom in with wheel (median / worst) | 640 ms / 930 ms | 17 ms / 22 ms | 17 ms / 25 ms |
| Pan, zoomed in (median / worst) | 17 ms / 660 ms | 16 ms / 27 ms | 17 ms / 25 ms |
| Zoom out (median / worst) | 640 ms / 970 ms | 17 ms / 50 ms | 17 ms / 44 ms |
| Subject filter (to second painted frame) | 1.4 s | 0.27 s | 0.26 s |
| Lineage filter, both directions, no limit (4,293 topics) | 1.5 s | 0.27 s | 0.20 s, 0.21 s |
| Lineage filter, 2 steps | 1.0 s | 0.08 s | 0.05 s |

Frames over 100 ms during any gesture: 0 after the fallbacks and 0 after the layout fix (the first attempt did not count them; most zoom frames were over 500 ms).

Method note: the first-attempt "median 17 ms" for pans only looks fine because Playwright sends the
mouse events in a burst and the page then idles; the worst-frame column is the honest one. A second
method, setting the camera each frame, gave 840 ms per frame at full zoom-out in the first
attempt and 18 ms after.

Passing bar (opens in about 10 s, no long stalls while panning, zooming and filtering): met, with
the caveat above.

## What was slow and what changed

Profiling by removing parts of the scene, under software GL:

- 97k edges: about 500 ms per frame. Sigma's `hidden` flag only zeroes an edge's buffer entry; the
  instanced draw still covers it, so hiding is not enough.
- 20,000 circle nodes: about 300 ms per frame at any zoom. The circle shader costs per node whether
  or not the node is on screen. The same nodes as plain points: about 1 ms.
- Labels, the HTML overlay and the data size were not the cause.

Fixes in `src/kg/map/app.js`, all applying only to big maps so small ones are unchanged:

1. Edges (brief's fallback). Past 10,000 edges they are removed from the sigma graph, not hidden.
   They are added back (a) when a filter is on, only those touching a matching topic, and (b) when
   zoomed in past camera ratio 0.08 (selecting a topic always zooms past it on such a map), only those with
   an end near the view, refreshed after 120 ms without camera movement. All topics stay drawn.
2. Nodes. Past 5,000 topics, topics draw as plain points when zoomed out; those near the view draw as
   circles once zoomed in past ratio 0.1. Circles for off-screen topics were the cost.
Data size was not the cause, so the keys were not shortened. At 18 MB it opens fine from disk; it
would be slow to download. Knowledge-point text is 13.9 MB of it, if size ever matters.

Also fixed in this task (controller rulings): the `both` lineage is now the union of one walk up and one walk
down, with `maxSteps` per direction, in `kg.graph.lineage` and `app.js`; before, one walk went both
ways from every node and pulled in an ancestor's other dependents.

## Layout fix: readable at real scale

The first layout failed at the real manifest's size: a 7:1 band using a sixth of the window, each course
a solid bar, course and subject labels colliding, topic labels overprinting. That was the layout, so it changed:

- A course's topics at a level now wrap into a block of 8 lines inside its column, with line length
  from its budget. Growing within budget only fills its own block; past budget, its lines tighten
  instead of growing taller, so no other course ever moves.
- Lanes are one fixed height, and rows have fixed capacities: math 12, physics 8, chem 8, bio 12, engr 30.
  `ROW_LANES` is gone. Filled to budget, the real manifest is 1044 by 697 units, a ratio of 1.50.
- Dots scale with how dense the map is, down to radius 1 px at full zoom-out, and grow as zoom
  increases. Big maps no longer need the slower growth curve from the earlier fallback.
- Subject labels moved to their own gutter left of the map, as colour strips spanning each row. The name stays
  at the top of the strip's visible part.
- Course labels are placed greedily each frame, nearest the view centre first, skipping any that would
  overlap. Level labels sit above the map and stick to the top of the window when zoomed in.
- Topic labels share that list of claimed space, after the selected topic and course labels, so none
  overprint. A hovered topic's label is drawn on top in an opaque box, and may cover a neighbour's.
- Point and edge gates tightened for the new density: circles past ratio 0.1, edges past 0.08.

### What I saw

Screenshots in `build/`, viewports 1400x850 unless noted. `t11r-*` is the real manifest filled to budget
(15,680 topics, synthetic names and chain-like edges), `t11s-*` the 20,000-topic synthetic graph. Each set
has `-a-zoomout`, `-b-zoom1` to `zoom4` and `-c-selected`. Also `t11x-1920-zoomout.png`, `-selected`, `-hover`, `-lineage`
at 1920x1080, and `t11x-dark.png`.

- Full zoom-out, real manifest: reads as a table. All 15 level labels are shown, the five subject strips
  line up with their rows, and about 40 course labels show with no overlaps. At 1400x850 the map fills
  about 60 percent of the window height because the map area is 750 px wide; at 1920x1080 about 80 percent.
- Mid zoom: course names fill in as you zoom in, one per block, and the current subject and level stay visible.
- Zoomed in: topic names are readable and none printed over another. At lines about 20 px apart most topics
  in view are named. Selecting a topic then zoomed until lines were about 20 px apart (now 25 px, see the flow check below), capped at the full map, so
  a sparse map keeps the neighbours in view. Tests cover that on one course of 8 (at least 7 in view) and of 150 topics (at least 30 in view at 20 px, 24 at 25 px), and the line gap on the real manifest with 40 topics per course. I looked at the result on `t11p-*`
  (one course of 150) and `t11r-c-selected` (filled manifest). It does not promise neighbouring names on every
  graph: labels are still culled, and on a dense map only the ones that fit show.
- Lineage filter when zoomed in: matched names stand out against faded dots. Dark theme at zoom-out looks the same.

What still looks weak:

- The engr row is 30 lanes that are only used in the two university columns, so about a third of the map's
  area, lower left, is blank. It comes from the manifest and fixed capacities.
- Small school science courses (`physics.elem`, 40 topics over 6 levels) are sparse ticks at zoom-out.
  They are visible and labelled but look thin next to math.
- At full zoom-out a block's lines merge, so a block reads as hatching rather than separate dots.
- At the zoom where topic labels first appear (lines about 6 px apart), labels sit over neighbouring dots.
  The halo keeps them legible, but it is busy until you zoom further.
- Real edges are unknown: the fill uses synthetic edges, so edge clutter on the real graph is unmeasured.

### Timings on the real manifest (two runs, same method)

First render 0.35 s and 0.36 s. Worst frame: pan zoomed out 24 ms, zoom in 25 ms, pan zoomed in 45 ms, zoom
out 54 ms, none over 100 ms. Before this fix it was a worst frame of 36 ms, on the old layout's views, so this
worst case is higher. Subject filter 0.08 to 0.10 s (was 0.15 to 0.19 s), lineage 0.04 to 0.05 s.

A second method moves the camera every frame at a fixed ratio, centred on a dense topic, under software GL.
The worst frames were at ratios 0.09 to 0.06, where circles and nearby edges both draw: real 70 ms and synthetic 66 ms
at most, and 35 ms or less at every ratio above 0.1. The earlier concern of about 190 ms at ratio 0.15 to 0.1 is gone.
Removing labels and course labels in turn did not make frames measurably faster, so the label work is not
the cost; drawing dots and edges under software GL is. None of this has been measured on a real GPU.

## Flow layout check (2026-11-06)

The map now draws a left-to-right prerequisite flow (`2026-11-06-flow-layout-design.md`), so the layout
sections above describe the old table. Same method as the first table: `kg synth --topics 20000`, exported,
driven with Playwright and software GL at 1400x850, two runs. Frame times are conservative bounds as before.

| | Flow layout (two runs) |
|---|---|
| File size | 18.1 MB |
| Seconds to first render | 0.42, 0.42 |
| Pan, zoomed out (median / worst frame) | 17 ms / 22 ms, 18 ms / 22 ms |
| Zoom in with wheel (median / worst) | 17 ms / 21 ms, 17 ms / 19 ms |
| Pan, zoomed in (median / worst) | 17 ms / 19 ms, 17 ms / 20 ms |
| Zoom out (median / worst) | 17 ms / 22 ms, 17 ms / 20 ms |
| Subject filter (to second painted frame) | 0.26 s, 0.26 s |
| Lineage filter, both directions, no limit (4,293 topics) | 0.22 s, 0.22 s |
| Lineage filter, 2 steps | 0.05 s, 0.05 s |

Frames over 100 ms: 0. Passing bar met.

Shape: 927 stages, the tallest holding 46 topics, `STAGE_SPACING` 3.0, so the whole map is about 2778 by 45
units (about 62:1). At 1920x1080 the overview is a thin coloured band across the middle of the window with
course and level labels above it; it reads as a flow only once zoomed in. The synthetic graph is chain-like,
which makes it far longer than a real one is likely to be, so this is the worst case for proportions.
Topic names get `stage_spacing` graph units of room before the next stage. A name that fits is drawn whole;
with at least 40 px of room it is shortened with an ellipsis; with less, no name is drawn, so a name never
runs past the next stage. Selecting a topic zooms until lines are about 25 px apart (`SELECT_LINE_PX`), so
neighbours in a stage have room for names. On the real graph at full zoom-out (71 topics, `math.k` and the
course after it) the stage gap is 62 px at 1280x720 and every name is cut to about 6 to 8 letters, which says
little; at 1920x1080 68 of 71 are cut but most show enough to read. Whole names need zooming in.

## Reproduce

```
.venv/Scripts/kg synth --topics 20000 --out build/synth
.venv/Scripts/kg export-map --root build/synth --out build/synth-map.html
```

then open `build/synth-map.html`, or drive it with Playwright as in `tests/test_map_page.py`.
