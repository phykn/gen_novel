# gen_novel

`gen_novel` is a small starting point for writing a novel draft.

Writing a novel often gets stuck before the draft begins.
You may have a genre, a character, or one scene in mind, but not a full setting sheet, cast list, or chapter plan.
You may also have an existing draft and want the AI to continue from it without explaining the whole process again.

This project reduces that starting friction.
You give the AI the material you already have: genre, idea, protagonist, opening scene, or an existing draft file.
The AI then starts writing from that input.
It does not ask for a complete setting sheet before drafting.
The graph protects the smallest scene values that make prose possible: what is visible now, who must do what now, what is lost if that action does not happen, what changes after the action, and what must happen next.

Use it when you want to turn an idea into draft pages without rebuilding the instruction every time.
It can start a new draft from a short premise, or continue from an existing draft file.

## How To Start

Use an AI session that can read this repository, then copy the block below into the chat.
If the chat cannot access the repository, provide the files in `graph/` along with the message.
Fill in the lines you need with whatever you already know.
Leave unused lines blank or delete them.
If you have an existing draft, write its file name on the last line.
If not, delete the last line.
The message itself is source input; a file is optional.

```text
Read `graph/route.md`.

Genre and idea:
Protagonist:
Opening scene:
Existing draft file: (file name, if any)
```

The AI returns a scene draft in your input language, or the existing draft's language when continuing it, unless you request another language.
Continuation starts from the draft's current end state and preserves its viewpoint and tense unless you ask for a change.
You can add constraints such as paragraph count, viewpoint, or forbidden additions; no complete style sheet is needed.
The default response is the prose. Ask separately if you want the scene table, input organization, or a next-action handoff.
If you want a file, include its output path.
If the available material cannot support a physical action and its visible consequences, the AI identifies the missing scene value instead of inventing a new event to finish the prose.

## Maintaining The Graph

[`graph/index.md`](graph/index.md) owns the routes and page responsibilities.
The published `graph/route.md` starting command still leads there.
Follow [`graph/review.md`](graph/review.md) when changing the rules.

Check local links in the README, graph, and evaluation files, page registration, and links to each evaluation file from graph guidance.
Run from the repository root with Python 3; no extra packages are needed:

```text
python scripts/check_graph.py
```

Code examples are excluded from link checks. Fragment destinations within a file and external URLs are not checked.
When changing the checker, also run its regression tests:

```text
python -m unittest discover -s tests -v
```

Runtime summaries belong in `work/summary/`, outside the rule graph.
