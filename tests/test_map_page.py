"""Browser tests: open the real exported map page and drive it through window.kgMap."""

import json
from urllib.parse import quote

import pytest

from conftest import add, course, edge, stub, topic
from kg.graph import KnowledgeGraph, lineage
from kg.map.export import export_map
from kg.model import Topic

pytest.importorskip("playwright")


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    # software GL so WebGL works in headless Chromium on any machine
    return {**browser_type_launch_args, "args": ["--use-gl=swiftshader", "--enable-unsafe-swiftshader"]}


def open_map(page, kg, tmp_path):
    out = export_map(kg, tmp_path / "map.html")
    errors = []
    page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.goto(out.as_uri())
    page.evaluate("window.kgMap.ready")
    return errors


@pytest.fixture
def sample_page(page, sample_graph, tmp_path):
    page.errors = open_map(page, sample_graph, tmp_path)
    return page


def select(page, topic_id):
    page.evaluate("id => window.kgMap.selectTopic(id)", topic_id)


def panel_text(page):
    return page.evaluate("window.kgMap.panelText()")


def test_all_topics_render_with_no_filters(sample_page, sample_graph):
    assert sample_page.evaluate("window.kgMap.topicCount()") == len(sample_graph.topics)


def test_search_finds_by_name_and_id(sample_page):
    by_name = sample_page.evaluate("window.kgMap.search('TWO-STEP')")
    assert by_name == ["math.alg1.solve-two-step-equations"]
    by_id = sample_page.evaluate("window.kgMap.search('physics.mech.')")
    assert len(by_id) == 3 and all(i.startswith("physics.mech.") for i in by_id)
    assert sample_page.evaluate("window.kgMap.search('no such topic')") == []


def test_search_shows_first_20_results(page, tmp_path):
    kg = KnowledgeGraph()
    kg.courses = {"math.a": course("math.a", 25)}
    add(kg, *[topic(f"math.a.t{i:02d}") for i in range(25)])
    open_map(page, kg, tmp_path)
    found = page.evaluate("window.kgMap.search('math.a')")
    assert found == [f"math.a.t{i:02d}" for i in range(20)]
    assert page.locator("#results button").count() == 20


def test_clicking_a_search_result_selects_and_centres_it(sample_page):
    sample_page.evaluate("window.kgMap.search('combine')")
    sample_page.locator("#results button").first.click()
    assert sample_page.evaluate("window.kgMap.selectedId()") == "math.alg1.combine-like-terms"
    sample_page.wait_for_function(
        """() => { const p = window.kgMap.nodeViewport('math.alg1.combine-like-terms');
                  const r = document.querySelector('#map').getBoundingClientRect();
                  return Math.abs(p.x - r.width / 2) < 3 && Math.abs(p.y - r.height / 2) < 3; }"""
    )


def test_clicking_a_panel_link_selects_that_topic(sample_page):
    select(sample_page, "math.alg1.combine-like-terms")
    sample_page.locator("#panel button", has_text="Evaluating algebraic expressions").first.click()
    assert sample_page.evaluate("window.kgMap.selectedId()") == "math.alg1.evaluate-expressions"
    assert "math.alg1.evaluate-expressions" in panel_text(sample_page)


def test_panel_shows_kps_weights_and_confidence(sample_page):
    select(sample_page, "math.alg1.evaluate-expressions")
    text = panel_text(sample_page)
    for expected in (
        "Evaluating algebraic expressions",
        "math.alg1.evaluate-expressions",
        "math.alg1",
        "g8",
        "draft",
        "Evaluate a one-variable expression at a whole number",
        "Adding fractions with unlike denominators",  # direct prerequisite
        "0.2",
        "medium",
        "Multiplying whole numbers",  # encompassed topic and key prerequisite
        "0.3",
        "Combining like terms",  # dependent
    ):
        assert expected in text, expected
    for heading in ("Prerequisites", "Encompassed", "Dependents", "Knowledge points"):
        assert heading.lower() in text.lower()  # headings are styled upper case


def test_markup_in_a_name_shows_literally(page, tmp_path):
    kg = KnowledgeGraph()
    kg.courses = {"math.k": course("math.k", 1)}
    t = topic("math.k.markup", level="g4")
    kg.topics[t.id] = t.model_copy(update={"name": "<b>x</b>"})
    open_map(page, kg, tmp_path)
    select(page, "math.k.markup")
    assert "<b>x</b>" in panel_text(page) and page.locator("#panel b").count() == 0
    page.evaluate("window.kgMap.search('<b>')")
    assert "<b>x</b>" in page.locator("#results").inner_text()
    assert page.locator("#results b").count() == 0


def test_stub_can_be_selected(sample_page):
    select(sample_page, "math.trig.resolve-vector-components")
    text = panel_text(sample_page)
    assert "math.trig.resolve-vector-components" in text and "stub" in text
    assert sample_page.evaluate("window.kgMap.selectedId()") == "math.trig.resolve-vector-components"


def test_no_console_errors_on_load(sample_page):
    assert sample_page.errors == []


def test_webgl_failure_shows_message(page, sample_graph, tmp_path):
    page.add_init_script(
        """const g = HTMLCanvasElement.prototype.getContext;
           HTMLCanvasElement.prototype.getContext = function (t, ...a) {
             return /webgl/.test(t) ? null : g.call(this, t, ...a); };"""
    )
    out = export_map(sample_graph, tmp_path / "map.html")
    page.goto(out.as_uri())
    page.evaluate("window.kgMap.ready")
    assert "This map needs WebGL, which your browser couldn't start." in page.inner_text("#map")


# ---- filters ---------------------------------------------------------------------------------


def filter_graph() -> KnowledgeGraph:
    """A chain t1 -> t2 -> t3 -> t4 in math.a, a low-confidence physics link, a stub and a reviewed topic."""
    kg = KnowledgeGraph()
    kg.courses = {
        "math.a": course("math.a", 4, levels=("g4", "g7")),
        "math.b": course("math.b", 2, ["math.a"], levels=("g8", "g8")),
        "physics.p": course("physics.p", 1, ["math.a"], levels=("g11", "g11")),
    }
    f1 = topic("physics.p.f1", ["math.a.t3"], level="g11")
    f1 = f1.model_copy(update={"prerequisites": [edge("math.a.t3", 0.5, "low")], "status": "reviewed"})
    add(
        kg,
        topic("math.a.t1", level="g4"),
        topic("math.a.t2", ["math.a.t1"], level="g5"),
        topic("math.a.t3", ["math.a.t2"], level="g6"),
        topic("math.a.t4", ["math.a.t3"], level="g7", n_kps=5),  # five KPs: near the limits
        f1,
        stub("math.b.stub"),
        topic("math.b.u", ["math.b.stub", "math.a.t4"], level="g8"),
    )
    return kg


@pytest.fixture
def fpage(page, tmp_path):
    kg = filter_graph()
    page.kg = kg
    page.errors = open_map(page, kg, tmp_path)
    return page


def matched(page, filters):
    return sorted(page.evaluate("f => { window.kgMap.setFilters(f); return window.kgMap.matchedIds(); }", filters))


def ids(kg, pred):
    return sorted(t.id for t in kg.topics.values() if pred(t))


def test_no_filters_matches_everything(fpage):
    everything = sorted(fpage.kg.topics)
    assert matched(fpage, {}) == everything
    assert fpage.evaluate("window.kgMap.matchCount()") == len(everything)
    assert fpage.locator("#match-count").inner_text() == f"{len(everything)} of {len(everything)} topics"
    assert matched(fpage, {"subjects": [], "courses": [], "statuses": [], "lineage": None}) == everything
    assert fpage.locator("#clear-filters").is_hidden()


def test_subject_course_and_level_filters(fpage):
    kg = fpage.kg
    assert matched(fpage, {"subjects": ["physics"]}) == ["physics.p.f1"]
    assert matched(fpage, {"courses": ["math.b"]}) == ids(kg, lambda t: t.id.startswith("math.b."))
    assert matched(fpage, {"levelMin": "g5", "levelMax": "g7"}) == ["math.a.t2", "math.a.t3", "math.a.t4"]
    # a stub has no level of its own; it takes the one at its layout column
    assert matched(fpage, {"levelMin": "g8"}) == ["math.b.stub", "math.b.u", "physics.p.f1"]
    assert matched(fpage, {"levelMax": "g4"}) == ["math.a.t1"]


def test_status_confidence_and_near_limit_filters(fpage):
    assert matched(fpage, {"statuses": ["stub"]}) == ["math.b.stub"]
    assert matched(fpage, {"statuses": ["reviewed"]}) == ["physics.p.f1"]
    assert matched(fpage, {"statuses": ["stub", "reviewed"]}) == ["math.b.stub", "physics.p.f1"]
    # confidence matches a topic when any of its incoming edges has it
    assert matched(fpage, {"confidences": ["low"]}) == ["physics.p.f1"]
    assert matched(fpage, {"confidences": ["medium"]}) == []
    assert matched(fpage, {"confidences": ["high"]}) == ["math.a.t2", "math.a.t3", "math.a.t4", "math.b.u"]
    assert matched(fpage, {"nearLimits": True}) == ["math.a.t4"]


def test_lineage_direction_and_step_limit(fpage):
    kg = fpage.kg
    for direction in ("prerequisites", "dependents", "both"):
        for steps in (None, 1, 2):
            want = sorted(lineage(kg, "math.a.t3", direction, steps))
            got = matched(fpage, {"lineage": {"topic": "math.a.t3", "direction": direction, "maxSteps": steps}})
            assert got == want, (direction, steps)
    assert matched(fpage, {"lineage": {"topic": "math.a.t3", "direction": "prerequisites"}}) == [
        "math.a.t1",
        "math.a.t2",
    ]


def test_lineage_both_excludes_an_ancestors_other_dependents(page, tmp_path):
    kg = KnowledgeGraph()
    kg.courses = {"math.a": course("math.a", 5, levels=("g4", "g8"))}
    add(
        kg,
        topic("math.a.a", level="g4"),
        topic("math.a.b", ["math.a.a"], level="g5"),
        topic("math.a.c", ["math.a.b"], level="g6"),
        topic("math.a.d", ["math.a.c"], level="g7"),
        topic("math.a.x", ["math.a.a"], level="g8"),  # another dependent of the ancestor a
    )
    open_map(page, kg, tmp_path)
    for steps in (None, 1, 2):
        got = matched(page, {"lineage": {"topic": "math.a.c", "direction": "both", "maxSteps": steps}})
        assert got == sorted(lineage(kg, "math.a.c", "both", steps)), steps
        assert "math.a.x" not in got


def test_edge_is_drawn_normally_only_when_both_ends_match(fpage):
    def colour(a, b):
        return fpage.evaluate("([a, b]) => window.kgMap.edgeDisplay(a, b).color", [a, b])

    normal = colour("math.a.t3", "math.a.t4")
    assert colour("math.a.t3", "physics.p.f1") == normal  # no filter: everything normal
    fpage.evaluate("window.kgMap.setFilters({courses: ['math.a']})")
    assert colour("math.a.t3", "math.a.t4") == normal  # both ends match
    faded = colour("math.a.t4", "math.b.u")  # one end matches
    assert faded != normal
    assert colour("math.a.t3", "physics.p.f1") == faded
    fpage.evaluate("window.kgMap.setFilters({subjects: ['physics']})")
    assert colour("math.a.t1", "math.a.t2") == faded  # neither end matches
    assert colour("math.a.t3", "physics.p.f1") == faded  # only one end matches


def test_filters_combine_as_and(fpage):
    both = {"lineage": {"topic": "math.a.t2", "direction": "dependents"}, "levelMin": "g7", "statuses": ["draft"]}
    assert matched(fpage, both) == ["math.a.t4", "math.b.u"]
    assert matched(fpage, {**both, "nearLimits": True}) == ["math.a.t4"]
    assert matched(fpage, {**both, "subjects": ["physics"]}) == []
    assert matched(fpage, {"subjects": ["math"], "courses": ["physics.p"]}) == []


def test_filtering_never_moves_topics(fpage):
    before = fpage.evaluate("window.kgMap.positions()")
    assert len(before) == len(fpage.kg.topics)
    fpage.evaluate("window.kgMap.setFilters({subjects: ['physics'], nearLimits: true})")
    fpage.evaluate("window.kgMap.selectTopic('math.a.t2')")
    assert fpage.evaluate("window.kgMap.positions()") == before
    assert fpage.evaluate("window.kgMap.topicCount()") == len(fpage.kg.topics)  # faded, never hidden


def test_zero_matches_shows_count_and_clear(fpage):
    total = len(fpage.kg.topics)
    assert matched(fpage, {"subjects": ["physics"], "nearLimits": True}) == []
    assert fpage.locator("#match-count").inner_text() == f"0 of {total} topics"
    clear = fpage.get_by_role("button", name="Clear filters")
    clear.click()
    assert fpage.evaluate("window.kgMap.matchCount()") == total
    assert fpage.locator("#match-count").inner_text() == f"{total} of {total} topics"
    assert clear.is_hidden()
    assert fpage.evaluate("location.hash") in ("", "#")


def test_controls_drive_the_filters(fpage):
    fpage.get_by_label("physics", exact=True).check()
    assert fpage.evaluate("window.kgMap.matchedIds()") == ["physics.p.f1"]
    assert fpage.locator("#match-count").inner_text() == f"1 of {len(fpage.kg.topics)} topics"
    fpage.get_by_role("button", name="Clear filters").click()
    fpage.get_by_label("Near the size limits").check()
    assert fpage.evaluate("window.kgMap.matchedIds()") == ["math.a.t4"]
    fpage.get_by_role("button", name="Clear filters").click()
    fpage.get_by_label("Stub", exact=True).check()
    assert fpage.evaluate("window.kgMap.matchedIds()") == ["math.b.stub"]
    fpage.get_by_role("button", name="Clear filters").click()
    fpage.get_by_label("Lowest level").select_option("g8")
    assert sorted(fpage.evaluate("window.kgMap.matchedIds()")) == ["math.b.stub", "math.b.u", "physics.p.f1"]


def test_lineage_controls_follow_the_selected_topic(fpage):
    select(fpage, "math.a.t3")
    fpage.get_by_label("Direction").select_option("prerequisites")
    assert sorted(fpage.evaluate("window.kgMap.matchedIds()")) == ["math.a.t1", "math.a.t2"]
    fpage.get_by_label("Step limit").fill("1")
    assert fpage.evaluate("window.kgMap.matchedIds()") == ["math.a.t2"]
    select(fpage, "math.a.t4")  # the lineage re-anchors on the new selection
    assert fpage.evaluate("window.kgMap.matchedIds()") == ["math.a.t3"]


def test_url_restores_filters(page, tmp_path):
    kg = filter_graph()
    out = export_map(kg, tmp_path / "map.html")
    filters = {"subjects": ["math"], "levelMin": "g6", "lineage": {"topic": "math.a.t3", "direction": "dependents"}}
    page.goto(out.as_uri() + "#f=" + quote(json.dumps(filters)))
    page.evaluate("window.kgMap.ready")
    assert sorted(page.evaluate("window.kgMap.matchedIds()")) == ["math.a.t4", "math.b.u"]
    assert page.locator("#match-count").inner_text() == f"2 of {len(kg.topics)} topics"
    assert page.get_by_label("math", exact=True).is_checked()
    # changing a filter writes the state back to the URL, and that link round-trips
    page.evaluate("window.kgMap.setFilters({statuses: ['stub']})")
    url = page.evaluate("location.href")
    page.goto("about:blank")
    page.goto(url)
    page.evaluate("window.kgMap.ready")
    assert page.evaluate("window.kgMap.matchedIds()") == ["math.b.stub"]


@pytest.mark.parametrize(
    "bad",
    [
        "#f=" + quote(json.dumps({"lineage": {"topic": "math.a.gone", "direction": "both"}})),
        "#f=" + quote(json.dumps({"courses": ["math.zzz"], "subjects": ["nope"], "statuses": ["bogus"]})),
        "#f=" + quote("{not json"),
        "#f=%E0%A4%A",
        "#f=" + quote("[1,2]"),
        "#f=" + quote("null"),
        "#unrelated",
    ],
)
def test_stale_hash_shows_whole_graph(page, tmp_path, bad):
    kg = filter_graph()
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    out = export_map(kg, tmp_path / "map.html")
    page.goto(out.as_uri() + bad)
    page.evaluate("window.kgMap.ready")
    assert page.evaluate("window.kgMap.matchCount()") == len(kg.topics)
    assert page.locator("#match-count").inner_text() == f"{len(kg.topics)} of {len(kg.topics)} topics"
    assert errors == []


def test_filtered_view_screenshot(fpage, tmp_path):
    select(fpage, "math.a.t3")
    fpage.get_by_label("Direction").select_option("both")
    fpage.wait_for_timeout(400)
    shot = tmp_path / "filters.png"
    fpage.screenshot(path=str(shot))
    assert shot.stat().st_size > 0


# ---- big maps ----------------------------------------------------------------------------------


def test_big_map_draws_edges_only_when_zoomed_in_or_filtered(page, tmp_path):
    kg = KnowledgeGraph()
    kg.courses = {"math.a": course("math.a", 5200, levels=("g4", "g8"))}
    n = 5200  # past the point limit; 4 prerequisites each puts the edges past the edge limit
    add(
        kg,
        *[
            topic(f"math.a.t{i:05d}", [f"math.a.t{j:05d}" for j in range(max(0, i - 4), i)], level="g8" if i >= 4000 else "g5")
            for i in range(n)
        ],
    )
    open_map(page, kg, tmp_path)
    assert page.evaluate("window.kgMap.topicCount()") == n  # every topic is drawn at full zoom-out
    assert page.evaluate("window.kgMap.edgeCount()") == 0
    page.evaluate("window.kgMap.setFilters({levelMin: 'g8'})")
    filtered = page.evaluate("window.kgMap.edgeCount()")
    assert 0 < filtered < page.evaluate("window.kgMap.totalEdges()")  # only edges touching a match
    assert page.evaluate("window.kgMap.topicCount()") == n
    page.evaluate("window.kgMap.setFilters({})")
    assert page.evaluate("window.kgMap.edgeCount()") == 0
    page.evaluate("window.kgMap.selectTopic('math.a.t02500')")  # zooms in on it
    page.wait_for_function("window.kgMap.edgeCount() > 0")
