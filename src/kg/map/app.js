// Map page: renders the kg-data graph with sigma.js, plus search, the topic panel and filters.
// All user text goes through textContent. Read-only.
(function () {
  "use strict";

  const SUBJECT_COLOURS = {
    math: "#534AB7", physics: "#D85A30", chem: "#1D9E75", bio: "#639922", engr: "#378ADD",
  };
  const FALLBACK_COLOUR = "#888780";
  const MAX_RESULTS = 20;
  const SELECT_LINE_PX = 20; // selecting a topic zooms until a block's lines are this many pixels apart
  const MAX_DOT = 3.5; // topic radius in pixels at full zoom-out; dense maps use less, down to MIN_DOT
  const MIN_DOT = 1;
  const LINE_SPACING = 1; // graph units between a course block's lines, from layout.py
  const LABEL_LINE_PX = 6; // topic labels start once a block's lines are this many pixels apart
  const COURSE_LABEL_HEIGHT = 16;
  const TOPIC_LABEL_HALF = 8; // half a topic label's height, so course labels clear the first line's names
  const STAGE_PADDING = 30; // sigma's default margin around the dots
  const LABEL_ROOM_PX = 90; // kept free right of the dots on maps that show names at once
  const MIN_LABEL_PX = 56; // below this a shortened name says too little to be worth drawing
  // Sigma's grid only limits which topics may try for a label, and picks them by ID within a cell, so
  // it is kept loose once labels are on: drawLabel below does the real work of keeping them apart.
  const LABEL_GRID_CELL = 24;
  const LABEL_GRID_DENSITY = 3;
  // Big maps keep edges out of the graph until they are wanted: while zoomed in past EDGE_ZOOM (a
  // camera ratio, smaller is closer), and then only those near the view, or while a filter is on
  // (only edges touching a matching topic). Every topic stays drawn. Small maps always draw all edges.
  // Edges are removed from sigma, not just hidden: hidden edges still cost a draw call each.
  const EDGE_LIMIT = 10000;
  const EDGE_ZOOM = 0.08;
  const EDGE_IDLE_MS = 120;
  // Big maps draw topics as plain points, and only those near the view as smooth circles once zoomed
  // in past POINT_ZOOM: every node costs a draw call in the circle shader whether or not it is on
  // screen, and with 20,000 of them that dominates every frame.
  const POINT_LIMIT = 5000;
  const POINT_ZOOM = 0.1;

  const data = JSON.parse(document.getElementById("kg-data").textContent);
  const topics = data.topics;
  const byId = new Map(topics.map((t, i) => [t.id, i]));
  const incoming = topics.map(() => []); // edges whose target is this topic: prerequisites
  const outgoing = topics.map(() => []); // edges whose source is this topic: dependents
  for (const [src, dst, weight, confidence, kind] of data.edges) {
    const e = { src, dst, weight, confidence, kind };
    incoming[dst].push(e);
    outgoing[src].push(e);
  }

  // ---- filters: pure functions over the data, no sigma and no DOM ------------------------
  const LEVELS = data.levels;
  const LEVEL_RANK = new Map(LEVELS.map((l, i) => [l, i]));
  const STATUSES = ["stub", "draft", "reviewed"];
  const CONFIDENCES = ["high", "medium", "low"];
  const DIRECTIONS = ["prerequisites", "dependents", "both"];
  const SUBJECT_IDS = new Set(topics.map((t) => t.subject));
  for (const s of data.subjects) SUBJECT_IDS.add(s.id);
  const COURSE_IDS = new Set(topics.map((t) => t.course));
  for (const c of data.courses) COURSE_IDS.add(c.id);
  const topicRank = Int16Array.from(topics, (t) => (LEVEL_RANK.has(t.level) ? LEVEL_RANK.get(t.level) : -1));

  const known = (values, allowed) =>
    Array.isArray(values)
      ? Array.from(new Set(values.filter((v) => typeof v === "string" && allowed.has(v))))
      : [];

  // Anything that isn't a recognised, still-existing value is dropped, so a stale or hand-edited
  // link degrades to "no constraint" instead of an empty map. Always returns the full shape.
  function normalizeFilters(raw) {
    const r = raw && typeof raw === "object" && !Array.isArray(raw) ? raw : {};
    const level = (v) => (typeof v === "string" && LEVEL_RANK.has(v) ? v : null);
    let lineage = null;
    const l = r.lineage;
    if (l && typeof l === "object" && byId.has(l.topic) && DIRECTIONS.includes(l.direction)) {
      const steps = Number.isInteger(l.maxSteps) && l.maxSteps >= 1 ? l.maxSteps : null;
      lineage = { topic: l.topic, direction: l.direction, maxSteps: steps };
    }
    return {
      subjects: known(r.subjects, SUBJECT_IDS),
      courses: known(r.courses, COURSE_IDS),
      levelMin: level(r.levelMin),
      levelMax: level(r.levelMax),
      statuses: known(r.statuses, new Set(STATUSES)),
      confidences: known(r.confidences, new Set(CONFIDENCES)),
      nearLimits: r.nearLimits === true,
      lineage,
    };
  }

  const isActive = (f) =>
    f.subjects.length > 0 || f.courses.length > 0 || f.levelMin !== null || f.levelMax !== null ||
    f.statuses.length > 0 || f.confidences.length > 0 || f.nearLimits || f.lineage !== null;

  // Only the fields that are set, so the URL stays short.
  function compactFilters(f) {
    const out = {};
    for (const k of ["subjects", "courses", "statuses", "confidences"]) if (f[k].length) out[k] = f[k];
    if (f.levelMin !== null) out.levelMin = f.levelMin;
    if (f.levelMax !== null) out.levelMax = f.levelMax;
    if (f.nearLimits) out.nearLimits = true;
    if (f.lineage) out.lineage = f.lineage;
    return out;
  }

  // Breadth-first over direct prerequisite edges, like kg.graph.lineage: the topic itself is excluded.
  // "both" is the union of two walks, one up and one down, each with its own step limit.
  function walkMask(mask, rootIndex, edgesOf, end, maxSteps) {
    const n = topics.length;
    const seen = new Uint8Array(n);
    const depth = new Int32Array(n);
    const queue = new Int32Array(n);
    let head = 0, tail = 0;
    queue[tail++] = rootIndex;
    seen[rootIndex] = 1;
    while (head < tail) {
      const node = queue[head++];
      if (maxSteps !== null && depth[node] >= maxSteps) continue;
      for (const e of edgesOf[node]) {
        if (e.kind !== "direct") continue;
        const next = e[end];
        if (seen[next]) continue;
        seen[next] = 1;
        mask[next] = 1;
        depth[next] = depth[node] + 1;
        queue[tail++] = next;
      }
    }
  }

  function lineageMask(rootIndex, direction, maxSteps) {
    const mask = new Uint8Array(topics.length);
    if (direction !== "dependents") walkMask(mask, rootIndex, incoming, "src", maxSteps);
    if (direction !== "prerequisites") walkMask(mask, rootIndex, outgoing, "dst", maxSteps);
    mask[rootIndex] = 0;
    return mask;
  }

  // One pass over the topics. Returns { mask, count }, or null when no filter is set.
  function computeMatches(f) {
    if (!isActive(f)) return null;
    const subjects = f.subjects.length ? new Set(f.subjects) : null;
    const courses = f.courses.length ? new Set(f.courses) : null;
    const statuses = f.statuses.length ? new Set(f.statuses) : null;
    const confidences = f.confidences.length ? new Set(f.confidences) : null;
    const lo = f.levelMin === null ? -1 : LEVEL_RANK.get(f.levelMin);
    const hi = f.levelMax === null ? LEVELS.length : LEVEL_RANK.get(f.levelMax);
    const limitLevels = f.levelMin !== null || f.levelMax !== null;
    const lineage = f.lineage ? lineageMask(byId.get(f.lineage.topic), f.lineage.direction, f.lineage.maxSteps) : null;
    const mask = new Uint8Array(topics.length);
    let count = 0;
    for (let i = 0; i < topics.length; i++) {
      const t = topics[i];
      if (subjects && !subjects.has(t.subject)) continue;
      if (courses && !courses.has(t.course)) continue;
      if (limitLevels && (topicRank[i] < lo || topicRank[i] > hi)) continue;
      if (statuses && !statuses.has(t.status)) continue;
      if (f.nearLimits && !t.near_limits) continue;
      if (lineage && !lineage[i]) continue;
      if (confidences && !incoming[i].some((e) => confidences.has(e.confidence))) continue;
      mask[i] = 1;
      count++;
    }
    return { mask, count };
  }

  function minMax(items, pick) {
    let lo = Infinity, hi = -Infinity;
    for (const item of items) {
      const v = pick(item);
      if (v < lo) lo = v;
      if (v > hi) hi = v;
    }
    return [lo, hi];
  }

  const mapEl = document.getElementById("map");
  const labelsEl = document.getElementById("labels");
  const panelEl = document.getElementById("panel");
  const searchEl = document.getElementById("search");
  const resultsEl = document.getElementById("results");
  const countEl = document.getElementById("match-count");
  const clearEl = document.getElementById("clear-filters");

  // ---- theme -----------------------------------------------------------
  const darkQuery = window.matchMedia("(prefers-color-scheme: dark)");
  // Edge colours are opaque, pre-blended with the background: sigma's WebGL output is not
  // premultiplied, so an rgba edge colour washes out to white instead of fading.
  const theme = () =>
    darkQuery.matches
      ? { bg: "#16161a", fg: "#ececf0", edge: mix("#9a9ab0", "#16161a", 0.75), lift: "#ffffff" }
      : { bg: "#ffffff", fg: "#1d1d1f", edge: mix("#6a6a80", "#ffffff", 0.72), lift: null };

  function mix(hex, otherHex, amount) {
    const a = parseInt(hex.slice(1), 16), b = parseInt(otherHex.slice(1), 16);
    const ch = (shift) => Math.round(((a >> shift) & 255) * (1 - amount) + ((b >> shift) & 255) * amount);
    return "#" + [16, 8, 0].map((s) => ch(s).toString(16).padStart(2, "0")).join("");
  }

  // ---- single place that decides how a topic looks (Task 10 filters hook in via reducers) ----
  function topicStyle(t) {
    const base = SUBJECT_COLOURS[t.subject] || FALLBACK_COLOUR;
    // sigma draws filled dots only, so a stub is a pale tint of its subject colour
    const colour = t.status === "stub" ? mix(base, theme().bg, 0.7) : base;
    return { color: colour, size: dotSize, label: t.name };
  }

  // ---- search ----------------------------------------------------------
  function searchTopics(text) {
    const q = text.trim().toLowerCase();
    if (!q) return [];
    const found = [];
    for (const t of topics) {
      if (t.name.toLowerCase().includes(q) || t.id.toLowerCase().includes(q)) {
        found.push(t.id);
        if (found.length === MAX_RESULTS) break;
      }
    }
    return found;
  }

  function el(tag, text, className) {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    if (className) node.className = className;
    return node;
  }

  function topicButton(id) {
    const i = byId.get(id);
    if (i === undefined) return el("span", id);
    const b = el("button", topics[i].name);
    b.type = "button";
    b.title = id;
    b.addEventListener("click", () => selectTopic(id));
    return b;
  }

  function renderResults(ids) {
    resultsEl.replaceChildren();
    for (const id of ids) {
      const t = topics[byId.get(id)];
      const b = el("button", t.name);
      b.type = "button";
      b.appendChild(el("span", id, "sub"));
      b.addEventListener("click", () => {
        resultsEl.replaceChildren();
        selectTopic(id);
      });
      resultsEl.appendChild(b);
    }
  }

  function runSearch(text) {
    const ids = searchTopics(text);
    renderResults(ids);
    return ids;
  }

  searchEl.addEventListener("input", () => runSearch(searchEl.value));
  searchEl.addEventListener("keydown", (ev) => {
    if (ev.key === "Enter") {
      const first = resultsEl.querySelector("button");
      if (first) first.click();
    } else if (ev.key === "Escape") {
      resultsEl.replaceChildren();
    }
  });

  // ---- panel -----------------------------------------------------------
  function edgeList(heading, edges, otherEnd) {
    const section = el("section");
    section.appendChild(el("h3", heading));
    if (!edges.length) {
      section.appendChild(el("div", "None.", "empty"));
      return section;
    }
    const list = el("ul");
    for (const e of edges) {
      const li = el("li");
      li.appendChild(topicButton(topics[otherEnd(e)].id));
      li.appendChild(el("span", "weight " + e.weight + ", confidence " + e.confidence, "meta"));
      list.appendChild(li);
    }
    section.appendChild(list);
    return section;
  }

  function renderPanel(i) {
    panelEl.replaceChildren();
    if (i === undefined) {
      panelEl.appendChild(el("div", "Select a topic, or search for one, to see its details.", "empty"));
      return;
    }
    const t = topics[i];
    panelEl.appendChild(el("h2", t.name));
    panelEl.appendChild(el("div", t.id, "id"));
    const facts = el("dl");
    const rows = [["Course", t.course], ["Level", t.level], ["Status", t.status]];
    if (t.near_limits) rows.push(["Note", "Near the size limits"]);
    for (const [k, v] of rows) {
      facts.appendChild(el("dt", k));
      facts.appendChild(el("dd", v));
    }
    panelEl.appendChild(facts);

    const kps = el("section");
    kps.appendChild(el("h3", "Knowledge points"));
    if (!t.kps.length) kps.appendChild(el("div", "None yet.", "empty"));
    const kpList = el("ul");
    for (const kp of t.kps) {
      const li = el("li");
      li.appendChild(el("span", kp.id + ": " + kp.can_do));
      if (kp.key_prerequisites.length) {
        const keys = el("span", "Key prerequisites: ", "keys");
        kp.key_prerequisites.forEach((id, n) => {
          if (n) keys.appendChild(document.createTextNode(", "));
          keys.appendChild(topicButton(id));
        });
        li.appendChild(keys);
      }
      kpList.appendChild(li);
    }
    kps.appendChild(kpList);
    panelEl.appendChild(kps);

    const prereqs = incoming[i].filter((e) => e.kind === "direct");
    const encompassed = incoming[i].filter((e) => e.kind === "encompassed");
    panelEl.appendChild(edgeList("Prerequisites", prereqs, (e) => e.src));
    panelEl.appendChild(edgeList("Encompassed topics", encompassed, (e) => e.src));
    panelEl.appendChild(edgeList("Dependents", outgoing[i], (e) => e.dst));
    panelEl.scrollTop = 0;
  }

  // ---- graph and sigma -------------------------------------------------
  // sigma fits the view to the topics that exist; empty columns and rows would only waste space
  const extent = (pick) => (topics.length ? minMax(topics, pick) : [0, 1]);
  const spanX = extent((t) => t.x);
  const spanY = extent((t) => t.y);
  const lineSpacingPx = Math.max(
    0,
    LINE_SPACING *
      Math.min(
        (mapEl.clientWidth - 2 * STAGE_PADDING) / (spanX[1] - spanX[0]),
        (mapEl.clientHeight - 2 * STAGE_PADDING) / (spanY[1] - spanY[0]),
      ),
  );
  // Dots stay small enough at full zoom-out that a course reads as a block, not a smear; sigma grows them on zoom.
  const dotSize = Math.min(MAX_DOT, Math.max(MIN_DOT, lineSpacingPx * 0.45));
  // Dots grow as 1 / sqrt(ratio), so this is the size they reach when lines are LABEL_LINE_PX apart.
  const labelThreshold = dotSize * 0.99 * Math.max(1, Math.sqrt(LABEL_LINE_PX / lineSpacingPx));

  // Graph distance from each topic to the next dot on its line, which is the room its name has.
  const nextDotGap = new Float64Array(topics.length).fill(Infinity);
  const dotsByLine = new Map();
  topics.forEach((t, i) => {
    if (!dotsByLine.has(t.y)) dotsByLine.set(t.y, []);
    dotsByLine.get(t.y).push(i);
  });
  for (const line of dotsByLine.values()) {
    line.sort((a, b) => topics[a].x - topics[b].x);
    for (let n = 0; n + 1 < line.length; n++) nextDotGap[line[n]] = topics[line[n + 1]].x - topics[line[n]].x;
  }

  const GraphCtor = window.graphology.Graph || window.graphology;

  const graph = new GraphCtor({ type: "directed" });
  for (const t of topics) {
    // sigma's y axis points up, the map's rows run downward
    graph.addNode(t.id, { x: t.x, y: -t.y, idx: byId.get(t.id), ...topicStyle(t) });
  }
  function addEdge(e) {
    const from = topics[e[0]].id, to = topics[e[1]].id;
    // a pair can be linked as both a direct and an encompassed edge; one drawn line is enough
    if (!graph.hasDirectedEdge(from, to)) graph.addDirectedEdge(from, to, { size: 0.5, color: theme().edge, si: e[0], di: e[1] });
  }
  if (data.edges.length <= EDGE_LIMIT) for (const e of data.edges) addEdge(e);

  let sigma = null;
  let selected; // index of the selected topic, or undefined

  // ---- filter state and fading ----
  let filters = normalizeFilters(null);
  let matches = null; // { mask, count } while any filter is set, else null
  const fadeCache = new Map();

  // The lineage's starting topic always stays drawn: it is the thing being looked at.
  const isShown = (i) =>
    matches === null || matches.mask[i] === 1 || (filters.lineage !== null && i === byId.get(filters.lineage.topic));

  function faded(colour) {
    const key = (darkQuery.matches ? "d" : "l") + colour;
    let out = fadeCache.get(key);
    if (out === undefined) {
      out = mix(colour, theme().bg, 0.86);
      fadeCache.set(key, out);
    }
    return out;
  }

  // Filters fade topics here, and never move or hide them.
  const pointGated = topics.length > POINT_LIMIT;
  let anyCircle = false;
  let circleMask = pointGated ? new Uint8Array(topics.length) : null; // 1: draw as a circle

  function reduceNode(id, attrs) {
    if (circleMask !== null && circleMask[attrs.idx] === 0 && !(selected !== undefined && topics[selected].id === id)) {
      attrs = { ...attrs, type: "point" };
    }
    if (selected !== undefined && topics[selected].id === id) {
      return { ...attrs, size: attrs.size * 1.6, highlighted: true, forceLabel: true, zIndex: 2 };
    }
    if (matches !== null && !isShown(attrs.idx)) {
      return { ...attrs, color: faded(attrs.color), label: null, zIndex: 0 };
    }
    return attrs;
  }

  const edgeGated = data.edges.length > EDGE_LIMIT;
  let drawnEdges = null; // Uint8Array over data.edges while gated: 1 when the edge is in the graph
  let edgeTimer = 0;

  // The graph-space rectangle on screen, padded a quarter on every side; null when zoomed out past `zoom`.
  function viewRect(zoom) {
    if (sigma.getCamera().ratio >= zoom) return null;
    const a = sigma.viewportToGraph({ x: 0, y: 0 });
    const b = sigma.viewportToGraph({ x: mapEl.clientWidth, y: mapEl.clientHeight });
    const padX = Math.abs(b.x - a.x) * 0.25, padY = Math.abs(b.y - a.y) * 0.25;
    return {
      x0: Math.min(a.x, b.x) - padX, x1: Math.max(a.x, b.x) + padX,
      y0: Math.min(a.y, b.y) - padY, y1: Math.max(a.y, b.y) + padY,
    };
  }

  const inRect = (r, i) => topics[i].x >= r.x0 && topics[i].x <= r.x1 && -topics[i].y >= r.y0 && -topics[i].y <= r.y1;

  function wantedEdges() {
    const want = new Uint8Array(data.edges.length);
    const r = viewRect(EDGE_ZOOM);
    if (matches !== null) {
      for (let k = 0; k < data.edges.length; k++) want[k] = isShown(data.edges[k][0]) || isShown(data.edges[k][1]) ? 1 : 0;
    } else if (r !== null) {
      for (let k = 0; k < data.edges.length; k++) want[k] = inRect(r, data.edges[k][0]) || inRect(r, data.edges[k][1]) ? 1 : 0;
    }
    return want;
  }

  // Which topics are drawn as circles. Returns true when that changed, so sigma needs a refresh.
  function syncCircles() {
    if (!pointGated) return false;
    const r = viewRect(POINT_ZOOM);
    const next = new Uint8Array(topics.length);
    if (r !== null) for (let i = 0; i < topics.length; i++) next[i] = inRect(r, i) ? 1 : 0;
    let same = true;
    for (let i = 0; same && i < next.length; i++) if (next[i] !== circleMask[i]) same = false;
    circleMask = next;
    anyCircle = r !== null;
    return !same;
  }

  function syncEdges() {
    clearTimeout(edgeTimer);
    if (!sigma) return;
    const circlesChanged = syncCircles();
    if (!edgeGated) {
      if (circlesChanged) sigma.refresh();
      return;
    }
    const want = wantedEdges();
    let same = drawnEdges !== null;
    for (let k = 0; same && k < want.length; k++) if (want[k] !== drawnEdges[k]) same = false;
    if (same) {
      if (circlesChanged) sigma.refresh();
      return;
    }
    drawnEdges = want;
    graph.clearEdges();
    for (let k = 0; k < want.length; k++) if (want[k]) addEdge(data.edges[k]);
    if (circlesChanged) sigma.refresh();
  }

  const syncEdgesSoon = () => {
    clearTimeout(edgeTimer);
    edgeTimer = setTimeout(syncEdges, EDGE_IDLE_MS);
  };

  // An edge is drawn normally only when both of its ends are.
  function reduceEdge(id, attrs) {
    if (matches !== null && !(isShown(attrs.si) && isShown(attrs.di))) {
      return { ...attrs, color: faded(attrs.color), zIndex: 0 };
    }
    return attrs;
  }

  function drawHoverLabel(context, d, settings) {
    const size = settings.labelSize;
    const name = topics[byId.get(d.key)].name; // not d.label: a faded topic has none, and still names itself on hover
    context.font = settings.labelWeight + " " + size + "px " + settings.labelFont;
    const width = context.measureText(name).width + 10;
    context.fillStyle = theme().bg;
    context.shadowColor = "rgba(0,0,0,0.35)";
    context.shadowBlur = 6;
    context.fillRect(d.x + d.size + 2, d.y - size / 2 - 4, width, size + 8);
    context.shadowBlur = 0;
    context.fillStyle = theme().fg;
    context.fillText(name, d.x + d.size + 7, d.y + size / 3);
  }

  // ---- labels share one list of claimed space, per frame: the selected topic, then course labels
  // nearest the view centre, then topic labels. First to claim its space wins. ----
  let labelRects = [];
  let labelsClaimed = false;
  const labelWidths = new Map();
  let drawnLabels = new Map(); // id -> the text drawn this frame (test hook)
  let pxPerUnit = 0; // screen pixels per graph unit this frame

  function labelWidth(context, key, label, settings) {
    let width = labelWidths.get(key);
    if (width === undefined) {
      context.font = settings.labelWeight + " " + settings.labelSize + "px " + settings.labelFont;
      width = context.measureText(label).width;
      labelWidths.set(key, width);
    }
    return width;
  }

  function labelRect(context, key, label, x, y, size, settings, width = labelWidth(context, key, label, settings)) {
    const half = settings.labelSize / 2 + 2;
    return { text: key, x0: x + size + 2, x1: x + size + width + 12, y0: y - half, y1: y + half };
  }

  const rectsOverlap = (a, b) => a.x0 < b.x1 && b.x0 < a.x1 && a.y0 < b.y1 && b.y0 < a.y1;

  // Runs once a frame, as late as possible: sigma updates its camera matrix after "beforeRender", so
  // this waits for the first topic label of the frame, or for the end of a frame without any.
  function claimLabels() {
    if (labelsClaimed || !sigma) return; // sigma draws its first frame inside its constructor
    labelsClaimed = true;
    labelRects = [];
    drawnLabels = new Map();
    pxPerUnit = Math.abs(sigma.graphToViewport({ x: 1, y: 0 }).x - sigma.graphToViewport({ x: 0, y: 0 }).x);
    if (selected !== undefined) {
      const t = topics[selected];
      const p = sigma.graphToViewport(graph.getNodeAttributes(t.id));
      const size = sigma.scaleSize(dotSize * 1.6);
      const context = sigma.getCanvases().labels.getContext("2d");
      labelRects.push(labelRect(context, t.id, t.name, p.x, p.y, size, sigma.getSettings()));
    }
    updateOverlay();
  }

  // The name to draw and its width: whole if it fits before the next dot and the window's edge, shortened
  // if enough room is left, and otherwise whole only if the edge would not cut it. Null means no label.
  function fitLabel(context, d, settings) {
    const width = labelWidth(context, d.key, d.label, settings);
    if (!sigma) return { text: d.label, width };
    const toEdge = sigma.getDimensions().width - (d.x + d.size + 3);
    const toNextDot = nextDotGap[byId.get(d.key)] * pxPerUnit - d.size - 9;
    const room = Math.min(toEdge, toNextDot);
    if (width <= room) return { text: d.label, width };
    if (room >= MIN_LABEL_PX) {
      const chars = Math.floor(((room - 8) * d.label.length) / width);
      return { text: d.label.slice(0, chars).trimEnd() + "\u2026", width: room };
    }
    return width <= toEdge ? { text: d.label, width } : null;
  }

  function drawLabel(context, d, settings) {
    if (!d.label) return;
    claimLabels();
    const isSelected = selected !== undefined && topics[selected].id === d.key;
    let text = d.label;
    if (!isSelected) {
      const fit = fitLabel(context, d, settings);
      if (fit === null) return;
      text = fit.text;
      const rect = labelRect(context, d.key, d.label, d.x, d.y, d.size, settings, fit.width);
      if (labelRects.some((other) => rectsOverlap(rect, other))) return;
      labelRects.push(rect);
    }
    drawnLabels.set(d.key, text);
    context.font = settings.labelWeight + " " + settings.labelSize + "px " + settings.labelFont;
    const x = d.x + d.size + 3, y = d.y + settings.labelSize / 3;
    // a halo in the background colour keeps the text readable over the dots of the lines around it
    context.lineJoin = "round";
    context.lineWidth = 3;
    context.strokeStyle = theme().bg;
    context.strokeText(text, x, y);
    context.fillStyle = theme().fg;
    context.fillText(text, x, y);
  }

  // ---- HTML label layers: levels and courses over the map ----
  const levelLabels = [];
  const courseLabels = [];

  function addLabel(parent, cls, text) {
    const span = el("span", text, cls);
    parent.appendChild(span);
    return { span, shown: true, moved: "" };
  }

  // Style writes are skipped when nothing changed, so a frame touches only what moved.
  function place(label, x, y) {
    if (!label.shown) {
      label.span.style.display = "";
      label.shown = true;
    }
    const moved = "translate(" + Math.round(x) + "px," + Math.round(y) + "px)";
    if (moved !== label.moved) {
      label.span.style.transform = moved;
      label.moved = moved;
    }
  }

  function hide(label) {
    if (label.shown) {
      label.span.style.display = "none";
      label.shown = false;
    }
  }

  function buildOverlay() {
    for (const m of data.level_markers) {
      const label = addLabel(labelsEl, "lbl-level", m.level);
      levelLabels.push({ ...label, x: m.x, width: label.span.offsetWidth });
    }
    const extent = new Map();
    for (const t of topics) {
      const c = extent.get(t.course) || { x0: Infinity, x1: -Infinity, y0: Infinity, y1: -Infinity, stages: new Map() };
      if (t.x < c.x0) c.x0 = t.x;
      if (t.x > c.x1) c.x1 = t.x;
      if (t.y < c.y0) c.y0 = t.y;
      if (t.y > c.y1) c.y1 = t.y;
      const stage = c.stages.get(t.x) || { x: t.x, y: t.y, n: 0 };
      stage.n++;
      if (t.y < stage.y) stage.y = t.y;
      c.stages.set(t.x, stage);
      extent.set(t.course, c);
    }
    for (const [course, { stages, ...c }] of extent) {
      // the label sits over the stage holding most of the course; the leftmost wins a tie
      let anchor = null;
      for (const stage of stages.values()) {
        if (!anchor || stage.n > anchor.n || (stage.n === anchor.n && stage.x < anchor.x)) anchor = stage;
      }
      const label = addLabel(labelsEl, "lbl-course", course);
      courseLabels.push({ ...label, ...c, anchorX: anchor.x, anchorY: anchor.y, width: label.span.offsetWidth, order: courseLabels.length });
    }
  }

  const clamp = (v, lo, hi) => Math.min(Math.max(v, lo), Math.max(lo, hi));

  // Levels sit just above the map, sticking to the top of the window once zoomed in. Returns the y
  // below which course labels have to stay.
  function placeLevels(w) {
    const y = Math.max(2, sigma.graphToViewport({ x: 0, y: -spanY[0] }).y - COURSE_LABEL_HEIGHT * 2 - TOPIC_LABEL_HALF);
    const placed = [];
    for (const m of levelLabels) {
      const x = sigma.graphToViewport({ x: m.x, y: 0 }).x;
      const right = x + m.width + 1;
      if (right < 0 || x > w || placed.some((p) => x < p.right && p.x < right)) {
        hide(m);
        continue;
      }
      placed.push({ x, right });
      place(m, x, y);
    }
    return y + COURSE_LABEL_HEIGHT;
  }

  // Greedy: courses nearest the view centre claim space first, so more appear as you zoom in.
  function placeCourses(w, h, top) {
    const wanted = [];
    for (const c of courseLabels) {
      const a = sigma.graphToViewport({ x: c.x0, y: -c.y0 });
      const b = sigma.graphToViewport({ x: c.x1, y: -c.y1 });
      if (b.x < 0 || a.x > w || b.y < top || a.y > h) {
        hide(c);
        continue;
      }
      const dx = Math.max(a.x - w / 2, w / 2 - b.x, 0);
      const dy = Math.max(a.y - h / 2, h / 2 - b.y, 0);
      c.dist = dx * dx + dy * dy;
      // above its block, or kept in view while the block fills the window
      const anchor = sigma.graphToViewport({ x: c.anchorX, y: -c.anchorY });
      c.px = clamp(anchor.x, 4, w - c.width - 4);
      c.py = clamp(anchor.y - COURSE_LABEL_HEIGHT - TOPIC_LABEL_HALF - 1, top, Math.min(b.y, h) - COURSE_LABEL_HEIGHT);
      wanted.push(c);
    }
    wanted.sort((p, q) => p.dist - q.dist || p.order - q.order);
    for (const c of wanted) {
      const rect = { text: c.span.textContent, x0: c.px, x1: c.px + c.width + 1, y0: c.py, y1: c.py + COURSE_LABEL_HEIGHT };
      if (labelRects.some((other) => rectsOverlap(rect, other))) {
        hide(c);
      } else {
        labelRects.push(rect);
        place(c, c.px, c.py);
      }
    }
  }

  function updateOverlay() {
    const w = mapEl.clientWidth, h = mapEl.clientHeight;
    placeCourses(w, h, placeLevels(w));
  }

  function webglAvailable() {
    const canvas = document.createElement("canvas");
    return Boolean(canvas.getContext("webgl2") || canvas.getContext("webgl"));
  }

  function showStartFailure(err) {
    const noWebGL = !webglAvailable();
    const text = noWebGL ? "This map needs WebGL, which your browser couldn't start." : "The map couldn't start: " + err.message;
    const message = el("div", text, "empty");
    if (noWebGL) message.id = "nowebgl";
    mapEl.replaceChildren(message);
    labelsEl.replaceChildren();
  }

  // Dots are kept clear of the right edge only where names show at once; big overviews need the width.
  function reserveLabelRoom() {
    const dx = spanX[1] - spanX[0];
    const usable = mapEl.clientWidth - 2 * STAGE_PADDING - LABEL_ROOM_PX;
    if (lineSpacingPx < LABEL_LINE_PX || dx === 0 || usable <= 0) return;
    sigma.setCustomBBox({ x: [spanX[0], spanX[1] + (LABEL_ROOM_PX * dx) / usable], y: [-spanY[1], -spanY[0]] });
  }

  function start() {
    try {
      // when the browser has no WebGL, sigma's own script fails to load and leaves no global
      if (!window.Sigma) throw new Error("sigma did not load");
      const SigmaCtor = window.Sigma.Sigma || window.Sigma.default || window.Sigma;
      sigma = new SigmaCtor(graph, mapEl, {
        labelRenderedSizeThreshold: labelThreshold,
        labelDensity: LABEL_GRID_DENSITY,
        labelGridCellSize: LABEL_GRID_CELL,
        labelSize: 12,
        labelColor: { color: theme().fg },
        defaultDrawNodeLabel: drawLabel,
        defaultDrawNodeHover: drawHoverLabel,
        nodeProgramClasses: { point: window.Sigma.rendering.NodePointProgram },
        nodeReducer: reduceNode,
        edgeReducer: reduceEdge,
        zIndex: true,
        enableEdgeEvents: false,
      });
    } catch (err) {
      console.error(err);
      sigma = null;
      showStartFailure(err);
      return Promise.resolve();
    }
    reserveLabelRoom();
    sigma.on("clickNode", ({ node }) => selectTopic(node));
    sigma.on("beforeRender", () => { labelsClaimed = false; });
    sigma.on("afterRender", claimLabels);
    sigma.getCamera().on("updated", () => {
      // zooming out past the threshold must drop the circles at once; everything else waits for a pause
      if (pointGated && sigma.getCamera().ratio >= POINT_ZOOM && anyCircle) syncEdges();
      else syncEdgesSoon();
    });
    darkQuery.addEventListener("change", () => {
      fadeCache.clear();
      for (const t of topics) graph.mergeNodeAttributes(t.id, topicStyle(t));
      graph.forEachEdge((e) => graph.setEdgeAttribute(e, "color", theme().edge));
      sigma.setSetting("labelColor", { color: theme().fg });
      sigma.refresh();
    });
    buildOverlay();
    syncEdges();
    return new Promise((resolve) => {
      sigma.once("afterRender", resolve);
      sigma.refresh();
    });
  }

  // ---- selection -------------------------------------------------------
  // Relative to the map's density, so a sparse map keeps the topic's neighbours in view. Never out past
  // the full map, and on a big map close enough to bring in the selected topic's edges.
  function selectRatio() {
    const ratio = Math.min(1, lineSpacingPx / SELECT_LINE_PX);
    return edgeGated ? Math.min(ratio, EDGE_ZOOM * 0.75) : ratio;
  }

  function selectTopic(id) {
    const i = byId.get(id);
    if (i === undefined) return Promise.resolve();
    selected = i;
    renderPanel(i);
    // an active lineage follows the selection; that call refreshes sigma itself
    if (lineageOn()) applyFilters(readControls(), { fromControls: true });
    else if (sigma) sigma.refresh();
    updateLineageHint();
    if (!sigma) return Promise.resolve();
    const d = sigma.getNodeDisplayData(id);
    const camera = sigma.getCamera();
    return camera.animate(
      { x: d.x, y: d.y, ratio: Math.min(camera.ratio, selectRatio()) },
      { duration: 250 }
    );
  }

  // ---- filter controls --------------------------------------------------------------------
  const ctl = {
    subjects: document.getElementById("f-subjects"),
    courses: document.getElementById("f-courses"),
    statuses: document.getElementById("f-statuses"),
    confidences: document.getElementById("f-confidences"),
    levelMin: document.getElementById("f-level-min"),
    levelMax: document.getElementById("f-level-max"),
    direction: document.getElementById("f-direction"),
    steps: document.getElementById("f-steps"),
    near: document.getElementById("f-near"),
    hint: document.getElementById("f-lineage-topic"),
  };

  function checkbox(container, value, text) {
    const label = el("label");
    const box = document.createElement("input");
    box.type = "checkbox";
    box.value = value;
    label.append(box, document.createTextNode(text));
    container.appendChild(label);
  }

  function buildControls() {
    for (const s of data.subjects) checkbox(ctl.subjects, s.id, s.id);
    for (const c of Array.from(COURSE_IDS).sort()) checkbox(ctl.courses, c, c);
    for (const s of STATUSES) checkbox(ctl.statuses, s, s[0].toUpperCase() + s.slice(1));
    for (const c of CONFIDENCES) checkbox(ctl.confidences, c, c[0].toUpperCase() + c.slice(1));
    for (const sel of [ctl.levelMin, ctl.levelMax]) {
      const any = el("option", "Any");
      any.value = "";
      sel.appendChild(any);
      for (const l of LEVELS) {
        const o = el("option", l);
        o.value = l;
        sel.appendChild(o);
      }
    }
  }

  const checkedValues = (container) =>
    Array.from(container.querySelectorAll("input:checked"), (b) => b.value);

  const lineageOn = () => ctl.direction.value !== "";

  function readControls() {
    const steps = parseInt(ctl.steps.value, 10);
    return {
      subjects: checkedValues(ctl.subjects),
      courses: checkedValues(ctl.courses),
      levelMin: ctl.levelMin.value || null,
      levelMax: ctl.levelMax.value || null,
      statuses: checkedValues(ctl.statuses),
      confidences: checkedValues(ctl.confidences),
      nearLimits: ctl.near.checked,
      lineage:
        lineageOn() && selected !== undefined
          ? { topic: topics[selected].id, direction: ctl.direction.value, maxSteps: Number.isNaN(steps) ? null : steps }
          : null,
    };
  }

  function syncControls() {
    const set = (container, values) => {
      for (const b of container.querySelectorAll("input")) b.checked = values.includes(b.value);
    };
    set(ctl.subjects, filters.subjects);
    set(ctl.courses, filters.courses);
    set(ctl.statuses, filters.statuses);
    set(ctl.confidences, filters.confidences);
    ctl.levelMin.value = filters.levelMin || "";
    ctl.levelMax.value = filters.levelMax || "";
    ctl.near.checked = filters.nearLimits;
    ctl.direction.value = filters.lineage ? filters.lineage.direction : "";
    ctl.steps.value = filters.lineage && filters.lineage.maxSteps !== null ? String(filters.lineage.maxSteps) : "";
  }

  function updateLineageHint() {
    ctl.hint.textContent =
      selected === undefined ? "Select a topic on the map, then choose a direction." : "From: " + topics[selected].name;
  }

  function updateCount() {
    const total = topics.length;
    const n = matches === null ? total : matches.count;
    countEl.textContent = total === 0 ? "No topics yet" : n + " of " + total + " topics";
    countEl.classList.toggle("none", matches !== null && n === 0);
    clearEl.hidden = !isActive(filters);
  }

  function writeHash() {
    const base = location.pathname + location.search;
    const hash = isActive(filters) ? "#f=" + encodeURIComponent(JSON.stringify(compactFilters(filters))) : "";
    try {
      history.replaceState(null, "", base + hash);
    } catch (err) {
      // a browser that refuses replaceState still filters correctly, the link just isn't shareable
    }
  }

  function readHash() {
    if (!location.hash.startsWith("#f=")) return null;
    try {
      return JSON.parse(decodeURIComponent(location.hash.slice(3)));
    } catch (err) {
      return null;
    }
  }

  // The one entry point for changing filters. fromControls skips rewriting the controls, so a
  // half-typed step limit is left alone.
  function applyFilters(raw, opts) {
    filters = normalizeFilters(raw);
    matches = computeMatches(filters);
    if (filters.lineage) {
      // the lineage always starts from the selected topic
      const i = byId.get(filters.lineage.topic);
      if (selected !== i) {
        selected = i;
        renderPanel(i);
      }
    }
    if (!(opts && opts.fromControls)) syncControls();
    updateLineageHint();
    updateCount();
    writeHash();
    syncEdges();
    if (sigma) sigma.refresh();
  }

  function matchedIds() {
    if (matches === null) return topics.map((t) => t.id);
    const out = [];
    for (let i = 0; i < topics.length; i++) if (matches.mask[i]) out.push(topics[i].id);
    return out;
  }

  if (topics.length === 0) {
    const note = document.createElement("div");
    note.className = "empty-note";
    note.textContent = "No topics yet. Add course files under the graph folder and export again.";
    document.getElementById("map-wrap").appendChild(note);
  }

  buildControls();
  for (const node of document.querySelectorAll("#filters input, #filters select")) {
    node.addEventListener("change", () => applyFilters(readControls(), { fromControls: true }));
  }
  ctl.steps.addEventListener("input", () => applyFilters(readControls(), { fromControls: true }));
  clearEl.addEventListener("click", () => applyFilters(null));
  window.addEventListener("hashchange", () => applyFilters(readHash()));
  renderPanel(undefined);
  applyFilters(readHash());

  const ready = new Promise((resolve) => {
    // wait for layout, so the container has a size before sigma measures it
    requestAnimationFrame(() => start().then(resolve));
  });

  window.kgMap = {
    ready,
    selectTopic,
    selectedId: () => (selected === undefined ? null : topics[selected].id),
    search: (text) => {
      searchEl.value = text;
      return runSearch(text);
    },
    panelText: () => panelEl.innerText,
    setFilters: (raw) => applyFilters(raw),
    matchCount: () => (matches === null ? topics.length : matches.count),
    matchedIds,
    positions: () => {
      const out = {};
      graph.forEachNode((id, a) => { out[id] = { x: a.x, y: a.y }; });
      return out;
    },
    topicCount: () => (sigma ? graph.filterNodes((id) => !sigma.getNodeDisplayData(id).hidden).length : 0),
    // edges currently in the graph, and in the data (they differ on big maps)
    edgeCount: () => graph.size,
    totalEdges: () => data.edges.length,
    // sigma's display data for the edge between two topics (test hook for edge fading)
    edgeDisplay: (from, to) => sigma.getEdgeDisplayData(graph.directedEdge(from, to)),
    // pixel position of a topic inside the map area (test hook for centring)
    nodeViewport: (id) => sigma.graphToViewport(graph.getNodeAttributes(id)),
    // the selected, course and topic labels of the last frame, in map pixels (test hook for overprinting)
    labelRects: () => labelRects,
    // the text of each topic label drawn in the last frame (test hook for shortening)
    labelTexts: () => Object.fromEntries(drawnLabels),
  };
})();
