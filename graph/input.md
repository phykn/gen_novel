## Role

Organize the user's message and supplied files without changing their facts.

## Steps

1. Identify the requested output: input organization, a new scene, continuation, or a next-action handoff. Read the user's message and supplied files; inline text needs no file.
2. List each source's identity and contents in one line. Use `user message` for inline text and the supplied path for each file. If a requested source cannot be read, stop and identify it; request an accessible path or its contents rather than treating it as absent.
3. If the sources include draft text or a draft file, mark the input type as `existing draft`; otherwise mark it as `new start`. This describes the source, not permission to continue it: the requested output controls which task runs.
4. Resolve material conflicts before choosing scene values. Use an explicit user correction where given; otherwise identify the conflicting sources and ask which fact applies. Do not silently blend versions or let a summary override its source.
5. Record the output language and drafting constraints below.
6. If a genre exists, write in one line what effect the scene should show.
7. Summarize each source file separately when there are two or more files, or when a single file mixes scenes, setting, notes, and draft text.
8. Record the summary locations in the input list. Keep facts, actors, event order, uncertainty, deadlines, and pending actions intact; summaries must not invent scene values.
9. For input organization alone, return the organized sources and any unresolved conflict, then stop. Otherwise follow [[index]].

## Leave

- Input type: `new start` or `existing draft`
- Requested output
- Output language
- Drafting constraints and requested output path, if any
- Genre effect the scene should show
- Input list table: source identity or supplied path, one-line contents, and summary location (when required)

## Summary Files

When a summary is required and files can be written, create `work/summary/` during execution.
For each summarized source file, create `work/summary/<source-stem>.md` (for example, `notes.md` becomes `work/summary/notes.md`).
If that path already exists, is a supplied source path, or was chosen for another source in this run, add a numeric suffix and keep checking until the path is unused. Apply this on every run; preserve supplied files and never overwrite an earlier summary.
Record each source-to-summary mapping in the input list.
Keep the original supplied path in each summary.
When a summary leaves a required detail unclear, reread that part of the original source before asking the user. [[core]] owns the allowed sources of working values.
In a chat without file access, keep the same separate summaries in the run's context and mark their locations as `in chat`; do not claim to have created files.

## Limits

- Do not create work files inside the `graph` folder.
- Do not create work folders or work files before execution.
- Do not merge summaries from multiple source files into one file.

## Drafting Constraints

Record supplied protagonist, viewpoint, tense, tone, length or paragraph count, and forbidden additions without requesting a style sheet.
For continuation, retain the draft's viewpoint and tense unless the user requests a change. Keep completed actions in the past of the scene; continue from its current state.
Narration may report only what its viewpoint can know or perceive. A character being present does not by itself establish that they saw a change.
Carry these constraints with the scene values through [[check]], [[write]], and any [[next]] handoff.

## Output Language

- If the user names an output language, use that language.
- If no output language is given and an existing draft exists, use the existing draft language.
- If there is no existing draft, use the user's input language.
- If input languages are mixed, use the main input language.
- If it is still unclear, leave a failure reason.
