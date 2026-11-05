# Map check at 20,000 topics

Measured with Playwright and headless Chromium on `kg synth --topics 20000` (96,727 edges),
exported with `kg export-map`. Driver scripts and screenshots are under `build/` (not committed).

Software GL caveat: headless Chromium here used SwiftShader, a CPU rasteriser. It understates a
real GPU by a wide margin, so every frame time below is a conservative bound. The failures it
exposed (per-node and per-edge draw cost) are real in kind but will be far smaller on a GPU.

## Result

| | First attempt | After fallbacks |
|---|---|---|
| File size | 18.2 MB | 18.2 MB (13.9 MB topics and knowledge points, 4.0 MB edges) |
| Seconds to first render | 2.9 | 0.4 to 0.8 (three runs: 0.41, 0.41, 0.42; one full measure: 0.79) |
| Pan, zoomed out (median / worst frame) | 17 ms / 1150 ms | 16 ms / 24 ms |
| Zoom in with wheel (median / worst) | 640 ms / 930 ms | 17 ms / 22 ms |
| Pan, zoomed in (median / worst) | 17 ms / 660 ms | 16 ms / 27 ms |
| Zoom out (median / worst) | 640 ms / 970 ms | 17 ms / 50 ms |
| Subject filter (to second painted frame) | 1.4 s | 0.27 s |
| Lineage filter, both directions, no limit (4,293 topics) | 1.5 s | 0.27 s |
| Lineage filter, 2 steps | 1.0 s | 0.08 s |

Frames over 100 ms during any gesture: 0 after the fallbacks (the first attempt did not count them; most zoom frames were over 500 ms).

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
   zoomed in past camera ratio 0.15 (above the 0.12 that selecting a topic zooms to), only those with
   an end near the view, refreshed after 120 ms without camera movement. All topics stay drawn.
2. Nodes. Past 5,000 topics, topics draw as plain points when zoomed out; those near the view draw as
   circles once zoomed in past ratio 0.3. Circles for off-screen topics were the cost.
3. Zoom growth. Sigma's default sqrt growth turned topics into overlapping discs and, in point mode,
   a solid block when zoomed in, since topics sit about half a unit apart. Big maps now grow
   discs as ratio^-0.2, and label from a rendered size of 6 instead of 9.

Data size was not the cause, so the keys were not shortened. At 18 MB it opens fine from disk; it
would be slow to download. Knowledge-point text is 13.9 MB of it, if size ever matters.

Also fixed in this task (controller rulings): the `both` lineage is now the union of one walk up and one walk
down, with `maxSteps` per direction, in `kg.graph.lineage` and `app.js`; before, one walk went both
ways from every node and pulled in an ancestor's other dependents.

## What it looks like, honestly

Screenshots in `build/`: `synth-final-zoomout.png`, `synth-final-zoom1.png` to `zoom3.png`,
`synth-final-filter-subject.png`, `synth-final-filter-lineage.png`, `synth-final-lineage-zoomed.png`,
and for the real manifest layout `realfull-zoomout.png`, `realfull-final-zoom1.png` to `zoom3.png`.

What works: pans and zooms are smooth, filters respond at once, faded topics stay in place, selecting a
topic shows its edges.

What looks bad, and was not fixed because it comes from the layout rather than the renderer:

- At full zoom-out the whole map is a thin band, about 1,000 units wide and 150 tall, so it uses
  roughly a sixth of the window height and most of the window is blank. Rows are about 22 px apart.
- Lanes inside a row are under 1 px apart at full zoom-out, so the courses in a row read as one
  coloured bar. Subject labels sit on top of course labels, and course labels pile up in the two
  university columns, where most of the topics are.
- Every course's topics lie on one line about half a unit apart. Zoomed in until discs separate,
  topic labels on that line overlap each other (sigma's label grid does not keep a line of labels
  apart); zooming further clears it. Faded edges under a lineage filter add a lot of faint lines.
- Under a subject filter at full zoom-out the match is a thin line; fine, but easy to miss.

## Real manifest layout (ROW_LANES ruling)

Checked with every manifest course filled with synthetic chain topics at its real budget
(15,680 topics), in a scratch directory. With 30-lane rows, math uses 8 lanes, physics 4, chem 5,
bio 7, engr 26, so rows are partly empty, as the ruling anticipated.

I did not replace `ROW_LANES` with per-subject capacities. At full zoom-out the scale is set by the
width, so a lane is under 1 px either way, and capacities of 12, 8, 8, 12, 30 would pack the rows to
about 9 px apart and make the label collisions above worse. The blankness and the label pile-up come
from the band's aspect ratio (about 7 to 1) and from one-line courses. The likely fixes, not made
because they change the layout design: stretch y in the layout (or draw lanes taller than columns
are wide), and spread a course's topics over several lines. Owner decision at the final sign-off.
Real-manifest performance is like the synthetic run: worst frame 36 ms, filters 0.15 to 0.19 s.

## Reproduce

```
.venv/Scripts/kg synth --topics 20000 --out build/synth
.venv/Scripts/kg export-map --root build/synth --out build/synth-map.html
```

then open `build/synth-map.html`, or drive it with Playwright as in `tests/test_map_page.py`.
