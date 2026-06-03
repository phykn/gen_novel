# gen_novel

`gen_novel` is a small starting point for writing a novel draft.

Writing a novel often gets stuck before the draft begins.
You may have a genre, a character, or one scene in mind, but not a full setting sheet, cast list, or chapter plan.
You may also have an existing draft and want the AI to continue from it without explaining the whole process again.

This project reduces that starting friction.
You give the AI the material you already have: genre, idea, protagonist, opening scene, or an existing draft file.
The AI then starts writing from that input.
It does not ask for a complete setting sheet before drafting.
The graph protects the smallest scene values that make prose possible: what is visible now, what the protagonist must do now, what is lost if that action does not happen, what changes after the action, and what must happen next.

Use it when you want to turn an idea into draft pages without rebuilding the instruction every time.
It can start a new draft from a short premise, or continue from an existing draft file.

## How To Start

Copy the block below into an AI chat.
Fill in the lines you need with whatever you already know.
Leave unused lines blank or delete them.
If you have an existing draft, write its file name on the last line.
If not, delete the last line.

```text
Read `graph/route.md`.

Genre and idea:
Protagonist:
Opening scene:
Existing draft file: (file name, if any)
```
