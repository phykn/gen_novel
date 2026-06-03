## Role

Leave the source input file list and summary file locations.

## Steps

1. Check the list of source input files.
2. For each file, write its file name and what it contains in one line.
3. If there is no existing draft file, mark the input type as `new start`.
4. If there is an existing draft file, mark the input type as `existing draft`.
5. Decide the output language.
6. If a genre exists, write in one line what effect the scene should show.
7. If there are two or more source files, make one summary file per source file.
8. If one file mixes scenes, setting, notes, and draft text, make a summary file for that file.
9. If summary files exist, write their locations in the input list table.
10. Check that no action, result, change, or next action was invented outside the source.

## Leave

- Input type: `new start` or `existing draft`
- Output language
- Input list table
- Source file name
- What the file contains
- Genre effect the scene should show
- Summary file location

## Working Values

Values used later must come from one of these:

- source input;
- a summary created from source input;
- a candidate created by [[seed]] or [[block]] and accepted by the next node.

Do not send unchecked invented action, result, change, or next action to prose.

## Summary Files

If there are two or more source files, create `work/summary/` during execution.
If one file mixes scenes, setting, notes, and draft text, create `work/summary/` during execution.
For each summarized source file, create `work/summary/<source-file-name>.md`.

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
