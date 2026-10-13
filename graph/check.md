## Role
Validate the values from [[result]] and put them in a 5-slot scene table.

## Table

| Slot | Required value |
| --- | --- |
| 1 | Pre-action image and existing problem, including urgency and immediate loss |
| 2 | Executed current action and actor |
| 3 | Visible change caused by that action |
| 4 | Who sees or hears that change, with supported access within the narrative viewpoint |
| 5 | Required next action and actor, still pending rather than completed |

## Rules

1. Build the table from [[result]], retaining the urgency and loss selected by [[choice]].
2. Pass only when all five slots meet the working-value constraints in [[core]] and follow the chosen action. Check actors, causality, event order, urgency, loss, and completed versus pending status against [[result]] and the drafting constraints from [[input]]. Filled cells alone are not a pass.
3. If a value is missing, unsupported, or disconnected, mark failure with the affected slot and send it to [[debug]].
4. Do not repair a weak value here. Fix the node that owns it before rebuilding the table.

## Leave

- The validated scene table, or the failing slot and reason
- Drafting constraints from [[input]]
