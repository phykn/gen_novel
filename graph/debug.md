## Role
Find the first node where the failure appeared.

## Rules
1. In the failed result, find the value that is empty or wrong.
2. Find the earliest missing or wrong value using the owners below. Choose one node, rather than rerunning the node that merely reported the failure.
3. Repair that value and rerun the downstream path in [[index]].
4. If it cannot be fixed inside the available source and accepted values, drop that candidate and try another.
5. If none can pass, return the failure reason and the one missing scene value needed to continue. Do not keep retrying the same failure.

## Owners

| Failed value | Return to |
| --- | --- |
| Unreadable source, missing summary, input type, or output language | [[input]] |
| Visible starting point or existing problem | [[opening]]; use [[seed]] only when its new-start condition applies |
| Current physical action, urgency, or immediate loss | [[choice]]; use [[block]] if an existing loose idea needs an action candidate |
| Pre-action image, executed-action link, visible change, observer, or immediate consequence | [[result]] |
| Valid values put into the wrong table slots | [[check]] |
| Correct table expanded with unsupported prose, omitted values, or wrong prose order | [[write]] |
| Unresolved chapter-end problem without a first-action candidate | [[hook]] |
| Passing hook candidates without a selected action or handoff | [[next]] |

An empty table slot is a missing value owned upstream, not a reason for [[check]] to invent one.

## Limits
- Do not first blame the failure on missing character, event, or setting.
- Choose only one node at a time.
- Do not loop the same candidate twice for the same reason.
