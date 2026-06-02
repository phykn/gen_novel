## Current Purpose

Keep `graph` as an applied rule graph that can follow a draft-generation path from small input.

## Input Assumptions

- Chapter 1 may receive only a genre and rough idea.
- Later chapters may receive only an existing draft.
- Do not fill missing setting. Convert input only into the action to take now, what changed after the action, and the next first action.

## Current Path

[[route]] -> [[input]] -> [[opening]] -> [[choice]] -> [[result]] -> [[check]] -> [[write]]

If an unresolved problem remains at the end of a chapter, go through `[[hook]] -> [[next]]`.

If input is too small, read [[seed]]. If a genre or setup does not lead to action, read [[block]]. If the failure cause is unknown, read [[debug]].

## Current Structure

- [[route]] owns the first entry point and the next-reading path.
- [[input]] leaves the source input file list, output language, genre effect, and summary file locations.
- [[opening]] makes opening-scene starting point candidates.
- [[choice]] chooses one action the protagonist must take now.
- [[result]] turns the change after the action into material for the 5-slot paragraph order table.
- [[check]] makes the 5-slot paragraph order table.
- [[write]] turns only the 5-slot paragraph order table into draft prose.
- [[debug]] finds the first node where the failure appeared.

## Next Priority

- If repeated judgment appears again, first compare the path in [[route]] with each node's role.
- If input assumptions change, update this state node and [[route]] together.
