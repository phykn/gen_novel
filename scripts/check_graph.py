"""Check local graph links and index registration without extra dependencies."""

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
GRAPH = ROOT / "graph"
WIKI_LINK = re.compile(r"\[\[([^\]|#]+)(?:[^\]]*)\]\]")
MARKDOWN_LINK = re.compile(r"\[[^\]\n]+\]\(([^)\s]+)\)")


def check_graph():
    pages = {path.stem: path for path in GRAPH.glob("*.md")}
    errors = []
    links = {}

    for path in [ROOT / "README.md", *pages.values()]:
        text = path.read_text(encoding="utf-8")
        targets = set(WIKI_LINK.findall(text))
        links[path.stem] = targets
        for name in sorted(targets - pages.keys()):
            errors.append(f"{path.relative_to(ROOT)}: missing graph page [[{name}]]")
        for target in MARKDOWN_LINK.findall(text):
            if ":" in target or target.startswith("#"):
                continue
            dst = path.parent / target.split("#", 1)[0]
            if not dst.is_file():
                errors.append(f"{path.relative_to(ROOT)}: missing file {target}")

    if "index" not in pages:
        errors.append("graph/index.md: missing entrypoint")
    else:
        text = pages["index"].read_text(encoding="utf-8")
        sections = dict(re.findall(r"^## ([^\n]+)\n(.*?)(?=^## |\Z)", text, re.M | re.S))
        for heading in ("Route", "Pages"):
            if heading not in sections:
                errors.append(f"graph/index.md: missing {heading} section")
                continue
            registered = set(WIKI_LINK.findall(sections[heading]))
            for name in sorted(pages.keys() - {"index"} - registered):
                errors.append(f"graph/index.md: [[{name}]] is absent from {heading}")

    if "index" not in links.get("route", set()):
        errors.append("graph/route.md: published entrypoint must link to [[index]]")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"OK: {len(pages)} graph pages; local links and index registration pass.")
    return 0


if __name__ == "__main__":
    sys.exit(check_graph())
