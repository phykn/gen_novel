## Role
Find the first node where the failure appeared.

## Rules
1. In the failed result, find the value that is empty or wrong.
2. Trace the value from its source using the owners below. If it was valid upstream, repair the first node that dropped or changed it; otherwise return to its owner. Choose one node, rather than rerunning the node that merely reported the failure.
3. Repair that value and rerun the downstream path in [[index]].
4. If it cannot be fixed inside the available source and accepted values, drop that candidate and try another.
5. If none can pass, return a short failure reason and one focused request for the earliest missing scene value. Do not draft around it or keep retrying the same failure. Unreadable or conflicting sources must be resolved in [[input]], not bypassed with another candidate.

## Owners

| Failed value | Return to |
| --- | --- |
| Unreadable or conflicting source, missing summary, input type, language, or drafting constraint | [[input]] |
| Visible starting point or existing problem | [[opening]]; use [[seed]] only when its new-start condition applies |
| Current physical action, urgency, or immediate loss | [[choice]]; use [[block]] if an existing loose idea needs an action candidate |
| Pre-action context, executed-action link, visible change, observer access, or pending consequence | [[result]] |
| Valid values put into the wrong table slots | [[check]] |
| Correct table expanded with unsupported prose, omitted values, wrong order, or changed viewpoint, tense, or action status | [[write]] |
| Unresolved chapter-end problem without a first-action candidate | [[hook]] |
| Passing hook candidates without a selected action or handoff | [[next]] |

An empty table slot is a missing value owned upstream, not a reason for [[check]] to invent one.

## Limits
- Do not first blame the failure on missing character, event, or setting.
- Choose only one node at a time.
- Do not loop the same candidate twice for the same reason.
