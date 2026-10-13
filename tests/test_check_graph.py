"""Exercise the documented checker command against isolated repositories."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_graph.py"


class CheckGraphTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.write("README.md", "Read [index](graph/index.md).\n")
        self.write("graph/index.md", "## Route\n[[route]] [[review]]\n## Pages\n[[route]] [[review]]\n")
        self.write("graph/route.md", "Continue at [[index]].\n")
        self.write("graph/review.md", "Run [trials](../eval/scenes.md).\n")
        self.write("eval/scenes.md", "Start from [README](../README.md).\n")
        (self.root / "scripts").mkdir()
        shutil.copyfile(SCRIPT, self.root / "scripts" / SCRIPT.name)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def check(self, *errors):
        result = subprocess.run(
            [sys.executable, str(self.root / "scripts" / SCRIPT.name)],
            cwd=self.root.parent,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, int(bool(errors)), result.stdout + result.stderr)
        if errors:
            self.assertEqual(result.stdout, "")
            for error in errors:
                self.assertIn(error, result.stderr)
            self.assertNotIn("Traceback", result.stderr)
        else:
            self.assertIn("OK: 3 graph pages", result.stdout)
            self.assertEqual(result.stderr, "")

    def test_valid_graph_from_another_working_directory(self):
        self.check()

    def test_missing_wiki_page(self):
        self.write("README.md", "Read [[missing]].\n")
        self.check("README.md: missing graph page [[missing]]")

    def test_missing_markdown_target(self):
        self.write("graph/route.md", "[[index]] and [source](missing.md#part).\n")
        self.check("graph/route.md: missing file missing.md#part")

    def test_broken_eval_links(self):
        self.write("eval/scenes.md", "Use [source](missing.md) and [[missing]].\n")
        self.check("eval/scenes.md: missing file missing.md", "eval/scenes.md: missing graph page [[missing]]")

    def test_eval_requires_graph_link(self):
        self.write("graph/review.md", "Run the trials.\n")
        self.write("README.md", "[trials](eval/scenes.md)\n")
        self.check("eval/scenes.md: no link from graph maintenance guidance")

    def test_nested_eval_requires_its_own_link(self):
        self.write("eval/more/trial.md", "Try another scene.\n")
        self.check("eval/more/trial.md: no link from graph maintenance guidance")

    def test_registration_is_required_in_each_index_section(self):
        for section in ("Route", "Pages"):
            with self.subTest(section=section):
                sections = {"Route": "[[route]] [[review]]", "Pages": "[[route]] [[review]]"}
                sections[section] = "[[route]]"
                self.write("graph/index.md", "\n".join(f"## {key}\n{value}" for key, value in sections.items()))
                self.check(f"graph/index.md: [[review]] is absent from {section}")

    def test_missing_index_section(self):
        self.write("graph/index.md", "## Route\n[[route]] [[review]]\n")
        self.check("graph/index.md: missing Pages section")

    def test_missing_entrypoints(self):
        (self.root / "graph/index.md").unlink()
        (self.root / "graph/route.md").unlink()
        self.check("graph/index.md: missing entrypoint", "graph/route.md: published entrypoint must link to [[index]]")

    def test_missing_readme(self):
        (self.root / "README.md").unlink()
        self.check("README.md: cannot read file")

    def test_non_utf8_source(self):
        (self.root / "graph/review.md").write_bytes(b"\xff")
        self.check("graph/review.md: cannot read file")

    def test_code_examples_are_not_links(self):
        self.write("README.md", """An inline `[[example]]` and ``[example](missing.md)``.
```text
[[example]]
[example](missing.md)
````
~~~markdown
[[another-example]]
~~~
Read [index](graph/index.md).
""")
        self.check()

    def test_code_examples_cannot_register_pages(self):
        self.write("graph/index.md", "## Route\n[[route]] `[[review]]`\n## Pages\n[[route]] [[review]]\n")
        self.check("graph/index.md: [[review]] is absent from Route")

    def test_code_formatted_link_labels_keep_their_targets(self):
        self.write("README.md", "Read [`missing.md`](missing.md).\n")
        self.check("README.md: missing file missing.md")

    def test_code_examples_cannot_supply_entrypoint_or_eval_link(self):
        self.write("graph/route.md", "Example: `[[index]]`\n")
        self.write("graph/review.md", "```md\n[trial](../eval/scenes.md)\n```\n")
        self.check("graph/route.md: published entrypoint must link to [[index]]", "eval/scenes.md: no link from graph maintenance guidance")

    def test_aliases_fragments_and_external_links(self):
        self.write("README.md", "[[index#Route|start]] [route](graph/route.md#role) [local](#start) [web](https://example.com)\n")
        self.check()

    def test_crlf_index_and_subheadings(self):
        (self.root / "graph/index.md").write_bytes(b"## Route\r\n### Start\r\n[[route]] [[review]]\r\n## Pages\r\n[[route]] [[review]]\r\n")
        self.check()


if __name__ == "__main__":
    unittest.main()
