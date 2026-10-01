## Role

Choose the next page for the current task and locate each page's responsibility.
This folder contains drafting rules; source material and runtime output stay outside it.

## Route

Read [[core]] before drafting.

### Draft a scene

New input may be a genre and rough idea; continuation input may be only the previous draft.
Do not require a character sheet, world sheet, chapter plan, or style guide.

| When | Read | Next |
| --- | --- | --- |
| Start a run | [[input]] | [[opening]] after organizing the input |
| A new start has only genre or idea and lacks a visible scene value | [[seed]] | [[opening]] to accept or reject one proposed value |
| Input is organized | [[opening]] | [[choice]] after accepting an opening candidate |
| A loose idea does not yet constrain an action | [[block]] | [[choice]] for a current action, or [[hook]] for an existing chapter-end problem |
| Opening candidates exist | [[choice]] | [[result]] after choosing one current action |
| The current action is chosen | [[result]] | [[check]] after deriving its visible consequences |
| Scene values exist | [[check]] | [[write]] only when all five slots pass |
| The paragraph order table passes | [[write]] | Deliver the prose; use [[hook]] if a chapter ends with an unresolved problem |
| A chapter-end problem remains | [[hook]] | [[next]] when at least one first-action candidate exists |
| One or more hook candidates exist | [[next]] | Use its handoff as input to the next run |

### Recover or maintain

- A node fails or prose loses a scene value: [[debug]] locates the earliest owner to repair. Resume there and rerun the downstream nodes.
- No candidate can pass using available values: return the failure reason and request only the missing scene value. Do not fill prose with invented facts or request a complete setting sheet.
- Review or change this graph: [[review]].
- An earlier prompt starts at `graph/route.md`: [[route]] leads here.

## Pages

- [[core]]: scene values and preservation constraints.
- [[input]]: source identities, summaries, language, and input type.
- [[seed]]: one proposed scene value for a sparse new start.
- [[opening]]: visible opening candidates and their existing problems.
- [[block]]: blocked and required actions derived from a loose idea.
- [[choice]]: the current action, urgency, and immediate loss.
- [[result]]: visible change, observer, and immediate consequence of that action.
- [[check]]: validation and ordering of the five scene values.
- [[write]]: prose from the accepted table and delivery.
- [[hook]]: first-action candidates from unresolved chapter-end problems.
- [[next]]: selection and handoff of the next chapter's first action.
- [[debug]]: failure ownership and bounded recovery.
- [[review]]: maintenance checks and use trials.
- [[route]]: the published starting command kept for existing prompts.
