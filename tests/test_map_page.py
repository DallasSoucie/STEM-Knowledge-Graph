"""Browser tests: open the real exported map page and drive it through window.kgMap."""

import pytest

from conftest import add, course, topic
from kg.graph import KnowledgeGraph
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
