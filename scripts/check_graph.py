"""Check graph routes and local documentation links without extra dependencies."""

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WIKI_LINK = re.compile(r"\[\[([^\]|#]+)(?:[^\]]*)\]\]")
MARKDOWN_LINK = re.compile(r"\[[^\]\n]+\]\(([^)\s]+)\)")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
INLINE_CODE = re.compile(r"(`+).*?\1(?!`)", re.S)


def strip_code(text):
    """Exclude code examples while preserving lines for section matching."""
    lines = []
    fence = ""
    for line in text.splitlines(keepends=True):
        match = FENCE.match(line.rstrip("\r\n"))
        if fence:
            if (
                match and match[1][0] == fence[0]
                and len(match[1]) >= len(fence) and not match[2].strip()
            ):
                fence = ""
            lines.append("\n")
        elif match:
            fence = match[1]
            lines.append("\n")
        else:
            lines.append(line)
    return INLINE_CODE.sub(lambda match: re.sub(r"[^\n]", " ", match[0]), "".join(lines))


def check_graph(root):
    """Return validation errors for a repository, without printing or writing."""
    pages = {path.stem: path for path in sorted((root / "graph").glob("*.md"))}
    trials = sorted((root / "eval").rglob("*.md"))
    errors = []
    texts = {}
    linked_files = set()

    for path in [root / "README.md", *pages.values(), *trials]:
        label = path.relative_to(root).as_posix()
        try:
            text = strip_code(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as exc:
            errors.append(f"{label}: cannot read file: {exc}")
            continue
        texts[path] = text
        targets = set(WIKI_LINK.findall(text))
        for name in sorted(targets - pages.keys()):
            errors.append(f"{label}: missing graph page [[{name}]]")
        for target in MARKDOWN_LINK.findall(text):
            if ":" in target or target.startswith("#"):
                continue
            dst = path.parent / target.split("#", 1)[0]
            if not dst.is_file():
                errors.append(f"{label}: missing file {target}")
            elif path.parent == root / "graph":
                linked_files.add(dst.resolve())

    for path in trials:
        if path.resolve() not in linked_files:
            errors.append(f"{path.relative_to(root).as_posix()}: no link from graph maintenance guidance")

    if "index" not in pages:
        errors.append("graph/index.md: missing entrypoint")
    else:
        text = texts.get(pages["index"], "")
        sections = dict(re.findall(r"^## ([^\n]+)\n(.*?)(?=^## |\Z)", text, re.M | re.S))
        for heading in ("Route", "Pages"):
            if heading not in sections:
                errors.append(f"graph/index.md: missing {heading} section")
                continue
            registered = set(WIKI_LINK.findall(sections[heading]))
            for name in sorted(pages.keys() - {"index"} - registered):
                errors.append(f"graph/index.md: [[{name}]] is absent from {heading}")

    route = texts.get(root / "graph" / "route.md", "")
    if "index" not in WIKI_LINK.findall(route):
        errors.append("graph/route.md: published entrypoint must link to [[index]]")

    return errors


def main():
    errors = check_graph(ROOT)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    count = len(list((ROOT / "graph").glob("*.md")))
    print(f"OK: {count} graph pages; local links, index registration, and eval coverage pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
