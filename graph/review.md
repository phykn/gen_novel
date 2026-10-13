## Role

Verify the graph's structure and actual drafting paths after a rule change.

## Check

1. Start at the README command and follow [[route]] to [[index]].
2. Run `python scripts/check_graph.py` from the repository root to check local documentation links, page registration, and graph links to evaluation files. When changing the checker, also run `python -m unittest discover -s tests -v`.
3. Read the changed route and each affected node's role, output, and failure owner.
4. Execute the requests in [scene trials](../eval/scenes.md) with the graph, keeping outputs outside `graph/`. For before/after comparisons, keep the request and available inputs fixed.
5. For substantial changes, give the same tasks and normal entrypoint to a fresh reader without explaining the intended architecture. Inspect their actual prose, handoffs, or stopping decisions.

## Pass

- A first-time reader can find the execution path from the README command through [[index]].
- New start input and existing draft input are both handled by [[input]] and [[opening]].
- Each node states only one job.
- Opening-scene starting point, current action, result link, check, output, hook, and next action do not do each other's jobs.
- Genre-specific devices are used only as effects from the input, not as required slots.
- Source facts remain distinct from accepted [[seed]] and [[block]] candidates; prose adds no unchecked settings, events, characters, or twists.
- [[write]] only turns the 5-slot paragraph order table from [[check]] into prose.
- Inline input needs no artificial source file; unreadable requested files are reported.
- A single supported opening is usable, and one hook candidate still reaches [[next]].
- Missing values return to their upstream owner instead of looping through [[check]].
- Summaries preserve source identities and never overwrite a different source's summary.

## Fail

- Long explanation makes the next node unclear.
- The same judgment repeats across multiple nodes.
- One node handles the opening-scene starting point, current action, result link, and hook choice together.
- An output node turns unchecked values into prose.

## Failure Handling

- If the failure location is unknown, go to [[debug]].
- If the path itself is unclear, fix [[index]] first. Keep [[route]] as the existing prompt entrypoint.
