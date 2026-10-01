## Role

Turn the 5-slot paragraph order table that passed [[check]] into draft prose.

## Rules

1. Do not let the prose become smarter than the table.
2. Turn slots 1 through 5 into prose in order.
3. Do not change the slot order.
4. Do not fill an empty slot with a new sentence.
5. If a sentence needs a fact, image, action, or result that is not in the table, do not write that sentence.
6. After prose drafting, check whether any slot is missing.
7. If the prose adds an unsupported value or loses a slot, leave a failure reason for [[debug]] before delivering it.

## Delivery

- Return the draft in the output language chosen by [[input]].
- If the user requested a file, save to that path and report it; keep generated files outside `graph/` and preserve the supplied draft unless the user asked to edit it.
- A scene-level table produces a scene draft. Do not invent extra scenes to claim a complete chapter.
- When the requested chapter ends with an unresolved problem, pass that problem to [[hook]] for the next run.

## Limits

- Do not add a new scene, setting, or character.
- Do not turn values that have not passed the check into prose.
