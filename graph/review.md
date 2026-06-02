## Role

Check whether the draft-generation path can be followed from beginning to end.

## Check

- [[route]]
- Role of each node
- Failure search path

## Pass

- A first-time reader can find the execution path immediately from [[route]].
- New start input and existing draft input are both handled by [[input]] and [[opening]].
- Each node states only one job.
- Opening-scene starting point, current action, result link, check, output, hook, and next action do not do each other's jobs.
- Genre-specific devices are used only as effects from the input, not as required slots.
- The premise remains that settings not present in the input are not added.
- [[write]] only turns the 5-slot paragraph order table from [[check]] into prose.

## Fail

- Long explanation makes the next node unclear.
- The same judgment repeats across multiple nodes.
- One node handles the opening-scene starting point, current action, result link, and hook choice together.
- An output node turns unchecked values into prose.

## Failure Handling

- If the failure location is unknown, go to [[debug]].
- If the path itself is unclear, fix [[route]] first.
