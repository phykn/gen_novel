## Role

Organize the user's message and supplied files without changing their facts.

## Steps

1. Read the user's message and the supplied source files. Treat inline text as source input even when there are no files.
2. List each source's identity and contents in one line. Use `user message` for inline text and the supplied path for each file. If a requested file cannot be read, leave a failure reason; do not treat it as absent.
3. If no existing draft text or file is supplied, mark the input type as `new start`.
4. If draft text or a draft file is supplied for continuation, mark the input type as `existing draft`.
5. Decide the output language.
6. If a genre exists, write in one line what effect the scene should show.
7. If there are two or more source files, summarize each separately.
8. If one file mixes scenes, setting, notes, and draft text, summarize that file.
9. If summary files exist, write their locations in the input list table.
10. Keep source facts distinct from later proposed candidates. Summaries must not invent actions, results, changes, or next actions.

## Leave

- Input type: `new start` or `existing draft`
- Output language
- Input list table
- Source identity or path
- What each source contains
- Genre effect the scene should show
- Summary file location

## Working Values

Values used later must come from one of these:

- source input;
- a summary created from source input;
- a candidate created by [[seed]] or [[block]] and accepted by the next node.

Keep the source or accepted candidate for each working value identifiable.
[[result]] may derive consequences from these values without adding unsupported facts.
Do not send unchecked invented action, result, change, or next action to prose.

## Summary Files

When a summary is required and files can be written, create `work/summary/` during execution.
For each summarized source file, create `work/summary/<source-file-name>.md`.
If different sources have the same file name, add a numeric suffix so they cannot overwrite each other, and record each source-to-summary mapping in the input list.
Keep the original supplied path in each summary.
In a chat without file access, keep the same separate summaries in the run's context and mark their locations as `in chat`; do not claim to have created files.

## Limits

- Do not create work files inside the `graph` folder.
- Do not create work folders or work files before execution.
- Do not merge summaries from multiple source files into one file.

## Output Language

- If the user names an output language, use that language.
- If no output language is given and an existing draft exists, use the existing draft language.
- If there is no existing draft, use the user's input language.
- If input languages are mixed, use the main input language.
- If it is still unclear, leave a failure reason.
