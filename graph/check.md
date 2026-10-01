## Role
Validate the values from [[result]] and put them in a 5-slot paragraph order table.

## Rules

1. Put the pre-action image from [[result]] in slot 1.
2. Put the executed action in slot 2.
3. Put what changed after the action in slot 3.
4. Put who sees or hears the change in slot 4.
5. Put the action that must happen immediately in slot 5.
6. Pass only when all five slots are present, follow the chosen action, and use source facts, accepted candidates, or their supported consequences from [[result]].
7. If a value is missing, unsupported, or disconnected, mark failure with the affected slot and send it to [[debug]].
8. Do not repair a weak value here. Fix the node that owns it before rebuilding the table.

## Leave

- Slot 1: pre-action image
- Slot 2: executed action
- Slot 3: change after the action
- Slot 4: who sees or hears the change
- Slot 5: immediate next action
- Failure reason
