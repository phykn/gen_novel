## Role

Verify the graph's structure and actual drafting paths after a rule change.

## Check

1. Start at the README command and follow [[route]] to [[index]].
2. Run `python scripts/check_graph.py` from the repository root to check local documentation links, page registration, and graph links to evaluation files. When changing the checker, also run `python -m unittest discover -s tests -v`.
3. Read the changed route and each affected node's role, output, and failure owner.
4. Execute [scene trials](../eval/scenes.md) and [prompt boundary trials](../eval/prompts.md) with the graph, keeping outputs outside `graph/`. For before/after comparisons, keep the request and available inputs fixed.
5. For substantial changes, give the same tasks and normal entrypoint to a fresh reader without explaining the intended architecture. Inspect their actual prose, handoffs, or stopping decisions.

## Pass

- A first-time reader can find the execution path from the README command through [[index]].
- New start input and existing draft input are both handled by [[input]] and [[opening]].
- Each node states only one job.
- [[core]] owns allowed working values; [[input]] owns intake and summaries; [[check]] owns the scene table.
- Opening-scene starting point, current action, result link, check, output, hook, and next action do not do each other's jobs.
- Genre-specific devices are used only as effects from the input, not as required slots.
- Source facts remain distinct from accepted [[seed]] and [[block]] candidates; prose adds no unchecked settings, events, characters, or twists.
- [[write]] renders the 5-slot scene table from [[check]] under the constraints from [[input]]; slot order does not force five paragraphs.
- Actor, causality, urgency, loss, and completed versus pending status survive every handoff. A deadline for a completed action does not become a new deadline.
- Continuation retains the current state, viewpoint, tense, and output language unless the user requests changes; it does not repeat the earlier draft.
- Unknown effects and source conflicts cause a focused stop, not an invented success or a silently chosen version.
- Input-only requests end after organization. Default prose delivery excludes working tables and validation notes.
- Inline input needs no artificial source file; unreadable requested files are reported.
- A single supported opening is usable, and one hook candidate still reaches [[next]].
- Missing values return to their upstream owner instead of looping through [[check]].
- Summaries preserve source identities, supplied files, and earlier summaries, including across repeated runs.

## Fail

- Long explanation makes the next node unclear.
- The same judgment repeats across multiple nodes.
- One node handles the opening-scene starting point, current action, result link, and hook choice together.
- An output node turns unchecked values into prose.

## Failure Handling

- If the failure location is unknown, go to [[debug]].
- If the path itself is unclear, fix [[index]] first. Keep [[route]] as the existing prompt entrypoint.
