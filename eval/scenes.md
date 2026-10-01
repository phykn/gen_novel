# Scene Trials

Start from the README command, using only the graph and the supplied inputs.
Actually produce the prose, handoff, summaries, or failure response; a review opinion is not a completed trial.
Keep trial artifacts outside the rule graph. Treat each request as a separate run.
An agent trial demonstrates behavior under that trial's conditions, not all model or human behavior.

## Sparse New Start

Request:

> 장르와 아이디어: 비 오는 밤의 우체국을 배경으로 한 미스터리. 한국어로 짧은 초고를 써 줘.

Check that the message is accepted without files. Any generated scene values must be proposed one at a time by seed and accepted by opening; any generated action candidate must pass choice. The prose must follow all five checked slots, without a culprit, revelation, or new twist added during writing. If no supported candidate can pass, identify the missing scene value and stop without requesting a complete setting sheet.

## Supplied Opening

Request:

> 한국어로 짧은 첫 장면을 써 줘. 수문 기사 윤이 녹슨 수문 손잡이를 붙잡고 있다. 종이 울리기 전에 수문을 열지 않으면 지하에 갇힌 동료 민의 숨이 끊긴다. 윤이 손잡이를 돌리면 수문이 열려 물이 빠지고, 민이 젖은 사다리를 드러낸다. 민이 그 변화를 보고 사다리를 올라야 한다.

Expect Korean prose in this order: visible handle and deadline, Yun turning it, gate opening and water draining to expose the ladder, Min observing the change, Min's required climb. One supported opening is sufficient. Do not add the result of climbing or another rescue event.

## Existing Draft With A Missing Consequence

Request: continue from this supplied draft text.

> 윤이 손잡이를 돌리자 수문이 열렸다. 빠져나가는 물 아래로 사다리가 드러났다. 민은 사다리 맨 아래에 매달려 있었다. 종이 다시 울리기 전에 민은 위로 올라와야 했다.

Treat this as an existing draft in Korean. Preserve it. A first action can be selected from its unresolved climb, but do not invent a landing, rescue action, or new danger to fill the next consequence. If a full continuation table cannot pass, return the missing value and a focused request instead of drafting around it.

## Recovery And A Single Hook

Use the supplied-opening request with a table whose slot 5 is empty. Locate the value's owner, recover it from the same input, rebuild the table, and produce the same ordered scene. Do not repair the value inside check or write.

Then use the supplied scene's ending with exactly one hook candidate: Min must climb the revealed ladder before the bell. Follow hook and next. Expect a next-run input whose first line is the climb, followed by the unresolved problem, previous draft text or path, and Korean output language. No second hook candidate is required.

## Source Files And Summary Identity

In an isolated writable directory, supply two files named `notes.md` in different directories. Put a distinct source fact in each and request input organization. Execute the summary-writing steps. Expect two different summary files in `work/summary/`, each retaining its supplied path and facts, and two correct source-to-summary mappings. Neither file may be overwritten or merged into the other.

Repeat input organization with an explicitly requested draft path that does not exist. Expect a failure identifying that source; do not silently start a new draft.

## Maintainer Navigation

Starting from the README, identify the owner of paragraph slot order and the owner of a missing current action, with file references. Distinguish a missing current action from a missing immediate action after the result. Follow ordinary links without a private explanation of the graph.
