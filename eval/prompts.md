# Prompt Boundary Trials

Start at the README command and follow the graph. Treat each request as a separate run.
Save the actual user-facing response separately from any trial notes; notes are evidence, not a substitute for doing the task.
Use isolated output files and preserve all supplied sources. These trials check instruction following under their inputs, not every model's behavior.

## Stakes, Status, And Prose Form

Request:

> 한국어 초고만 두 문단으로 써 줘. 3인칭 과거형을 유지해 줘. 주인공 윤은 녹슨 수문 손잡이를 붙잡고 있다. 종이 울리기 전에 수문을 열지 않으면 지하에 갇힌 민의 숨이 끊긴다. 윤이 손잡이를 돌리면 수문이 열리고 물이 빠져 젖은 사다리가 드러난다. 민은 그 변화를 보고 사다리를 올라야 한다. 이번 초고는 민이 올라야 한다는 지점에서 끝내 줘.

Expect two paragraphs of Korean prose, third person and past tense, without a working table or graph explanation. Preserve the deadline and threatened loss, all five values in order, and Min's climb as pending. Sentence variation must not add actions, reactions, or details absent from the accepted values.

## Continuation Voice And Language

Request:

> 다음 기존 초고에서 이어 써 줘. 앞부분을 다시 쓰지 말고 초고만 보여 줘.
>
> 기존 초고:
> I turn the wheel. The gate opens and the water drains. I see Min hanging from the exposed ladder. He needs the loose rope beside my foot before the bell; without it he cannot climb.
>
> 이어쓰기 참고: 나는 발 옆의 느슨한 밧줄을 민에게 던진다. 민이 밧줄을 받아 쥐고, 나는 밧줄 끝이 민의 손에 있는 것을 본다. 민은 사다리를 오르기 위해 그 밧줄을 허리에 묶어야 한다. 이번에는 묶어야 한다는 지점에서 끝낸다.

Expect only new English prose in first-person present tense. The Korean request does not override the existing draft's language. Preserve the current state, rope deadline and loss, supplied catch and visible result; end with tying the rope still required. Do not reopen the gate, repeat the old draft, switch narrator, narrate Min's private thoughts, or complete the tying/climb.

## Unknown Action Result

Request:

> 다음 초고를 이어 써 줘. 새로운 장치 설정을 만들지 마.
>
> 정은 지하실의 빨간 버튼에 손을 댔다. 10초 안에 버튼을 누르지 않으면 잠긴 방의 산소가 끊긴다. 버튼을 누르면 실제로 무엇이 일어나는지는 아직 알 수 없다.

Expect a focused request for the effect of pressing the button and no continuation prose. An action's urgency and loss do not prove its success or a device's mechanism; do not open a door, supply oxygen, or invent a signal as its result.

## Conflicting Sources And Input-Only Work

Request:

> 아래 두 출처의 입력 정리만 해 줘. 소설 초고는 아직 쓰지 마.
>
> 기존 초고: 윤은 홀로 수문 앞에 있었다. 손잡이는 부러져 떨어져 있었다.
> 메모: 같은 순간 윤은 민과 함께 수문 앞에 있다. 온전한 손잡이를 쥐고 있다.

Expect `existing draft` input, separate source identities, and both conflicts: who is present, and the handle's state. The input type describes the source; it does not authorize continuation. Ask which version applies without silently selecting one or drafting. No artificial files are required for inline sources.

Repeat with an explicit correction: “메모가 이 장면의 수정본이야. 기존 초고 파일은 수정하지 말고 입력 정리만 다시 해 줘.” Expect the memo's facts to be selected and the source draft to remain unchanged; do not ask the already answered question again.

## A Dropped Value And An Incorrect Actor

Use the stakes request above. Supply a table whose slot 1 contains only the handle image; the deadline and loss were valid in choice but omitted by result. Ask for validation and recovery before prose.

Expect the drop to be repaired in result, then the table rebuilt and the requested prose delivered. Do not approve the incomplete table or ask the user to repeat values already in the source. Contrast this with a loss absent from the source, which belongs to choice.

Separately use the supplied-opening request from [scene trials](scenes.md), where **Min reveals the ladder**, with a table that instead says the water alone exposes it. Expect the altered actor/causality to be rejected and the supplied action restored before prose. Do not “fix” the original input to match the table.

## A Resolved Deadline And A Handoff

Request:

> 다음 장 첫 행동 전달문만 만들어 줘. 한국어, 3인칭 과거형을 유지해 줘. 이전 초고: 윤은 종이 울리기 전에 수문을 열었다. 수문을 열지 않으면 민의 숨이 끊길 상황이었지만, 이제 물은 모두 빠졌다. 민은 드러난 사다리를 보고 있었다. 지하를 벗어나려면 사다리를 올라야 했다.

Expect a handoff whose first line names Min's pending climb, followed by the unresolved exit problem, prior draft, language, and tense. The gate deadline and its drowning risk have been resolved; do not attach them to the climb. Mark urgency or immediate loss for climbing as unspecified. Do not draft a next scene or treat the handoff as permission to skip choice and result.

## Viewpoint And File Delivery

Repeat the stakes request with the added constraints: “윤의 1인칭 과거형으로 써 줘. 윤은 민이 사다리를 보는 모습을 볼 수 있다.” Expect first-person narration to preserve the observable event without adding Min's private understanding or a shift into Min's viewpoint.

In an isolated writable directory, request a draft at a new output path and confirm that the saved file matches the delivered prose. Keep an existing source draft unchanged. Also perform a run in which file-writing access is explicitly unavailable: expect the prose in the response and an accurate statement that no file was saved.

## A Different Acting Character

Request:

> 주인공 윤의 1인칭 현재형 초고를 이어 써 줘. 기존 초고: 나는 밧줄을 민에게 건넨다. 민은 사다리에 매달린 채 밧줄을 쥐고 있다. 민의 손은 곧 미끄러질 참이고, 지금 몸을 묶지 않으면 아래로 떨어진다.
>
> 다음 장면의 값: 민이 자기 허리에 밧줄을 묶는다. 매듭이 몸을 받쳐 민이 손 하나를 사다리에서 뗄 수 있게 된다. 나는 그 손이 자유로워진 것을 본다. 민은 그 손으로 위쪽 가로대를 잡아야 한다. 여기서 끝내 줘.

Expect Yun to remain the first-person narrator and protagonist while Min performs the supported current action. Keep the loss, knot and freed hand, Yun's observation, and the required grip in order. Do not invent an action for Yun just to make the protagonist act, switch narrator to Min, or complete the next grip.
