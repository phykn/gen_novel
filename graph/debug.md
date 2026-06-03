## Role
Find the first node where the failure appeared.

## Rules
1. In the failed result, find the value that is empty or wrong.
2. If the source input is insufficient, return to [[input]].
3. If the opening-scene starting point is unclear, return to [[opening]].
4. If there is no action to take now, return to [[choice]].
5. If nothing changed after the action, return to [[result]].
6. If a slot in the paragraph order table is empty, return to [[check]].
7. If prose drafting broke the slot order, return to [[write]].
8. If an unresolved end-of-chapter problem does not make a first action for the next chapter, return to [[hook]].
9. If the first action for the next chapter is hard to choose, return to [[next]].
10. If prose looks good but the action, change, or immediate next action disappeared, return to the node that last owned that value.
11. If it cannot be fixed inside the existing values, drop that candidate.

## Limits
- Do not first blame the failure on missing character, event, or setting.
- Choose only one node at a time.
- Do not loop the same candidate twice for the same reason.
