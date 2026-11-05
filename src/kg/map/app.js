// Map page: renders the kg-data graph with sigma.js, plus search and the topic panel.
// All user text goes through textContent. Read-only.
(function () {
  "use strict";

  const SUBJECT_COLOURS = {
    math: "#534AB7", physics: "#D85A30", chem: "#1D9E75", bio: "#639922", engr: "#378ADD",
  };
  const FALLBACK_COLOUR = "#888780";
  const MAX_RESULTS = 20;
  const SELECT_RATIO = 0.12; // camera zoom (smaller is closer) that selecting a topic zooms to
  const NODE_SIZE = 3.5;

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

  const mapEl = document.getElementById("map");
  const labelsEl = document.getElementById("labels");
  const panelEl = document.getElementById("panel");
  const searchEl = document.getElementById("search");
  const resultsEl = document.getElementById("results");

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
    return { color: colour, size: NODE_SIZE, label: t.name };
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
  const GraphCtor = window.graphology.Graph || window.graphology;

  const graph = new GraphCtor({ type: "directed" });
  for (const t of topics) {
    // sigma's y axis points up, the map's rows run downward
    graph.addNode(t.id, { x: t.x, y: -t.y, ...topicStyle(t) });
  }
  for (const e of data.edges) {
    const from = topics[e[0]].id, to = topics[e[1]].id;
    // a pair can be linked as both a direct and an encompassed edge; one drawn line is enough
    if (!graph.hasDirectedEdge(from, to)) graph.addDirectedEdge(from, to, { size: 0.5, color: theme().edge });
  }

  let sigma = null;
  let selected; // index of the selected topic, or undefined

  // The one reducer. Task 10 filters extend this, fading topics rather than moving or hiding them.
  function reduceNode(id, attrs) {
    if (selected !== undefined && topics[selected].id === id) {
      return { ...attrs, size: attrs.size * 1.6, highlighted: true, forceLabel: true, zIndex: 2 };
    }
    return attrs;
  }

  function drawHoverLabel(context, d, settings) {
    const size = settings.labelSize;
    context.font = settings.labelWeight + " " + size + "px " + settings.labelFont;
    const width = context.measureText(d.label).width + 10;
    context.fillStyle = theme().bg;
    context.shadowColor = "rgba(0,0,0,0.35)";
    context.shadowBlur = 6;
    context.fillRect(d.x + d.size + 2, d.y - size / 2 - 4, width, size + 8);
    context.shadowBlur = 0;
    context.fillStyle = theme().fg;
    context.fillText(d.label, d.x + d.size + 7, d.y + size / 3);
  }

  function drawLabel(context, d, settings) {
    context.font = settings.labelWeight + " " + settings.labelSize + "px " + settings.labelFont;
    context.fillStyle = theme().fg;
    context.fillText(d.label, d.x + d.size + 3, d.y + settings.labelSize / 3);
  }

  // ---- HTML label layer: subjects, courses and levels, positioned from the camera ----
  const overlay = [];
  function addOverlay(cls, text, colour, place) {
    const span = el("span", text, cls);
    labelsEl.appendChild(span);
    overlay.push({ span, place, colour });
  }

  function buildOverlay() {
    for (const s of data.subjects) {
      // pinned to the left edge, just above the subject's first (topmost) topic
      const own = topics.filter((t) => t.subject === s.id);
      const top = own.length ? Math.min(...own.map((t) => t.y)) : s.y0;
      addOverlay("lbl-subject", s.id, SUBJECT_COLOURS[s.id] || FALLBACK_COLOUR, () => ({
        x: 8, y: sigma.graphToViewport({ x: 0, y: -top }).y - 44, show: true,
      }));
    }
    const extent = new Map();
    for (const t of topics) {
      const c = extent.get(t.course) || { minX: Infinity, maxX: -Infinity, ySum: 0, n: 0 };
      c.minX = Math.min(c.minX, t.x);
      c.maxX = Math.max(c.maxX, t.x);
      c.ySum += t.y;
      c.n += 1;
      extent.set(t.course, c);
    }
    for (const [course, c] of extent) {
      const gy = -(c.ySum / c.n);
      addOverlay("lbl-course", course, null, (w) => {
        const left = sigma.graphToViewport({ x: c.minX, y: gy });
        const right = sigma.graphToViewport({ x: c.maxX, y: gy });
        return { x: Math.max(left.x, 4), y: left.y - 20, show: right.x > 0 && left.x < w };
      });
    }
    for (const col of data.columns) {
      addOverlay("lbl-level", col.level, null, () => {
        const a = sigma.graphToViewport({ x: col.x0, y: 0 }).x;
        const b = sigma.graphToViewport({ x: col.x1, y: 0 }).x;
        return { x: (a + b) / 2, y: 2, show: b - a > col.level.length * 7 + 6, center: true };
      });
    }
  }

  function updateOverlay() {
    const w = mapEl.clientWidth, h = mapEl.clientHeight;
    for (const o of overlay) {
      const p = o.place(w, h);
      const visible = p.show && p.y > -20 && p.y < h;
      o.span.style.display = visible ? "" : "none";
      if (o.colour) o.span.style.color = theme().lift ? mix(o.colour, theme().lift, 0.3) : o.colour;
      if (visible) {
        const dx = p.center ? -o.span.offsetWidth / 2 : 0;
        o.span.style.transform = "translate(" + Math.round(p.x + dx) + "px," + Math.round(p.y) + "px)";
      }
    }
  }

  function showNoWebGL() {
    const message = el("div", "This map needs WebGL, which your browser couldn't start.", "empty");
    message.id = "nowebgl";
    mapEl.replaceChildren(message);
    labelsEl.replaceChildren();
  }

  function start() {
    // frame the topics that exist, with a margin; empty columns and rows would only waste space
    const span = (values, pad) => (values.length ? [Math.min(...values) - pad, Math.max(...values) + pad] : [0, 1]);
    const xs = span(topics.map((t) => t.x), 8);
    const ys = span(topics.map((t) => t.y), 4);
    try {
      // when the browser has no WebGL, sigma's own script fails to load and leaves no global
      if (!window.Sigma) throw new Error("sigma did not load");
      const SigmaCtor = window.Sigma.Sigma || window.Sigma.default || window.Sigma;
      sigma = new SigmaCtor(graph, mapEl, {
        customBBox: { x: xs, y: [-ys[1], -ys[0]] },
        labelRenderedSizeThreshold: 9,
        labelDensity: 0.7,
        labelGridCellSize: 90,
        labelSize: 12,
        labelColor: { color: theme().fg },
        defaultDrawNodeLabel: drawLabel,
        defaultDrawNodeHover: drawHoverLabel,
        nodeReducer: reduceNode,
        zIndex: true,
        enableEdgeEvents: false,
      });
    } catch (err) {
      sigma = null;
      showNoWebGL();
      return Promise.resolve();
    }
    sigma.on("clickNode", ({ node }) => selectTopic(node));
    sigma.on("afterRender", updateOverlay);
    darkQuery.addEventListener("change", () => {
      for (const t of topics) graph.mergeNodeAttributes(t.id, topicStyle(t));
      graph.forEachEdge((e) => graph.setEdgeAttribute(e, "color", theme().edge));
      sigma.setSetting("labelColor", { color: theme().fg });
      sigma.refresh();
    });
    buildOverlay();
    return new Promise((resolve) => {
      sigma.once("afterRender", () => { updateOverlay(); resolve(); });
      sigma.refresh();
    });
  }

  // ---- selection -------------------------------------------------------
  function selectTopic(id) {
    const i = byId.get(id);
    if (i === undefined) return Promise.resolve();
    selected = i;
    renderPanel(i);
    if (!sigma) return Promise.resolve();
    sigma.refresh();
    const d = sigma.getNodeDisplayData(id);
    const camera = sigma.getCamera();
    return camera.animate(
      { x: d.x, y: d.y, ratio: Math.min(camera.ratio, SELECT_RATIO) },
      { duration: 250 }
    );
  }

  renderPanel(undefined);
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
    topicCount: () => (sigma ? graph.filterNodes((id) => !sigma.getNodeDisplayData(id).hidden).length : 0),
    // pixel position of a topic inside the map area (test hook for centring)
    nodeViewport: (id) => sigma.graphToViewport(graph.getNodeAttributes(id)),
  };
})();
