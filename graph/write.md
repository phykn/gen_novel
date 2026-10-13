## Role

Turn the 5-slot scene table that passed [[check]] into fluent draft prose.

## Rules

1. Use the passed table and the drafting constraints carried from [[input]]. Do not supply missing scene values while writing.
2. Render slots 1 through 5 in order. They are ordered scene values, not a requirement for five sentences or five paragraphs. Combine or split sentences and paragraphs to meet the requested form.
3. Preserve the actors, causal links, urgency, immediate loss, viewpoint, and tense. Use natural wording and rhythm without adding story facts or unsupported perceptions.
4. Keep slot 5 pending. End at what must happen next; do not perform that action or invent its outcome within this table.
5. If a sentence needs a fact, image, action, or result outside the table, leave it out. Do not pad a length request by repeating values or adding another scene.
6. Compare the draft with all five slots and the drafting constraints. If it changes a value, loses one, or violates a constraint, return that failure to [[debug]] before delivery.

## Delivery

- Return the draft in the output language chosen by [[input]]. Keep working tables and validation notes out of the response unless requested.
- For continuation, return only the new prose unless the user requests a combined draft.
- If the user requested a file, save to that path and report it; keep generated files outside `graph/` and preserve the supplied draft unless the user asked to edit it. If the path conflicts with that preservation requirement, resolve the path before saving. Without file-writing access, return the text and state that it was not saved.
- A scene-level table produces a scene draft. Do not invent extra scenes to claim a complete chapter.
- When the requested chapter ends with an unresolved problem, pass that problem to [[hook]] for the next run.

## Limits

- Do not add a new scene, setting, or character.
- Do not turn values that have not passed the check into prose.
