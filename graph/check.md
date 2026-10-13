## Role
Validate the scene values and own their order in a 5-slot paragraph table.

## Table

| Slot | Required value |
| --- | --- |
| 1 | Pre-action image, including why the chosen action must happen now and what is immediately lost without it |
| 2 | Executed current action |
| 3 | Visible change caused by that action |
| 4 | Who sees or hears that change |
| 5 | Immediate next action that is still required, not completed |

## Rules

1. Build the table from [[result]], retaining the urgency and loss selected by [[choice]].
2. Pass only when all five values are present, follow the chosen action, and meet the working-value constraints in [[core]].
3. If a value is missing, unsupported, or disconnected, mark failure with the affected slot and send it to [[debug]].
4. Do not repair a weak value here. Fix the node that owns it before rebuilding the table.

## Leave

- The validated paragraph order table, or the failing slot and reason
