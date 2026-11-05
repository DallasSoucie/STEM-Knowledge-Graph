"""Write the map as one offline HTML file: data, libraries and script all inlined."""

import json
from pathlib import Path

from kg.graph import KnowledgeGraph
from kg.map.data import build_map_data

_DIR = Path(__file__).parent
_LT = chr(92) + "u003c"  # backslash-u003c, the JSON escape for "<"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _inline_js(source: str, name: str) -> str:
    if "</script" in source.lower():
        raise ValueError(f"{name} contains a closing script tag and cannot be inlined")
    return source


def render_map(kg: KnowledgeGraph) -> str:
    # \u003c keeps markup in names from ever closing the data block; JSON.parse reads it back as "<"
    data = json.dumps(build_map_data(kg), ensure_ascii=False).replace("<", _LT)
    page = _read(_DIR / "template.html")
    parts = {
        "STYLE": "",
        "DATA": data,
        "SIGMA": "/*vendor:sigma*/" + _inline_js(_read(_DIR / "vendor" / "sigma.min.js"), "sigma"),
        "GRAPHOLOGY": "/*vendor:graphology*/"
        + _inline_js(_read(_DIR / "vendor" / "graphology.umd.min.js"), "graphology"),
        "APP": _inline_js(_read(_DIR / "app.js"), "app.js"),
    }
    for key, value in parts.items():
        page = page.replace(f"/*__{key}__*/", value)
    return page


def export_map(kg: KnowledgeGraph, out: Path) -> Path:
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_map(kg), encoding="utf-8", newline="\n")
    return out
