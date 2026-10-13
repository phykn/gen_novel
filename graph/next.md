## Role
Choose one first action for the next chapter from one or more hook candidates.

## Rules

1. Start with the first candidate left by [[hook]].
2. If there is no unresolved problem, move to the next candidate.
3. If there is no first required action and actor, or that action has already been completed, move to the next candidate.
4. Choose the action from the first candidate that passes.
5. Take the action name only from words inside the candidate.
6. Leave the required action and actor as the first line of the next chapter input, followed by the unresolved problem, its supported urgency and loss (or the fact that they are missing), and the previous draft's location or text. Keep the output language and drafting constraints from [[input]].
7. If no candidate passes, leave a failure reason for [[debug]].

## Leave

- Unresolved problem
- Next chapter's first action
- Supported urgency and loss, or what is still missing
- Previous draft location or text, output language, and drafting constraints for [[input]]

## Limits

The handoff selects a pending action, not a completed event or a guaranteed result.
The next run still follows [[input]], [[opening]], [[choice]], [[result]], and [[check]] before drafting. A selected hook does not bypass their requirements.
