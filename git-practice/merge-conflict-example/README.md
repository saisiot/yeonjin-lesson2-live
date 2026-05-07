# 충돌 시나리오 — 일부러 부딪히고, 손으로 푼다

> **충돌은 정상이에요. 안 일어나는 게 이상한 거.**
>
> 두 갈래에서 **같은 파일의 같은 줄을 다르게** 고치고 본 줄기에 둘 다 합치려 하면 Git이 멈춥니다.
> "어느 쪽이 맞는지 사람이 정해주세요." — 이게 충돌의 신호.

---

## 시나리오

회사 소개 한 줄짜리 파일 `회사_소개.md` 를 main에 만들고,
- **feature-a** 갈래는 **친근한 톤**으로 같은 줄을 수정 ("안녕하세요! 저희는…")
- **feature-b** 갈래는 **전문적 톤**으로 같은 줄을 수정 ("당사는 …을 제공합니다")

main에서 둘을 차례로 merge하면 → 두 번째 merge에서 **CONFLICT**.
사람이 직접 편집해서 결정 → `git add` → `git commit` 으로 마무리.

라이브에서 강사가 먼저 시연하고, 그 자리에서 학생이 같이 따라 칩니다.

---

## 0. 준비 — 깨끗한 폴더에서 시작

```bash
mkdir conflict-demo
cd conflict-demo
git init
```

---

## 1. main에 회사_소개.md 만들기

VSCode에서 `회사_소개.md` 새 파일 만들고 **딱 한 줄**:

```
저희는 AI 교육 회사입니다.
```

저장 후:

```bash
git add 회사_소개.md
git commit -m "회사 소개 초안"
```

---

## 2. feature-a 갈래에서 친근한 톤으로 수정

```bash
git switch -c feature-a
```

`회사_소개.md` 를 다음 한 줄로 **고쳐 저장**:

```
안녕하세요! 저희는 AI 교육을 함께 만들어가는 따뜻한 회사예요.
```

(참고용 전체 내용: `feature-a-changes.md` 파일 보면 됨.)

```bash
git add 회사_소개.md
git commit -m "친근한 톤으로 수정 (feature-a)"
```

---

## 3. main으로 돌아가서 feature-b 갈래에서 전문적 톤으로 수정

```bash
git switch main
git switch -c feature-b
```

`회사_소개.md` 를 다음 한 줄로 **고쳐 저장** (이번엔 main 기준에서 시작했으니 원래 한 줄에서 출발):

```
당사는 데이터 기반의 AI 교육 솔루션을 제공하는 전문 기업입니다.
```

(참고용 전체 내용: `feature-b-changes.md` 파일 보면 됨.)

```bash
git add 회사_소개.md
git commit -m "전문적 톤으로 수정 (feature-b)"
```

---

## 4. main에서 feature-a 먼저 흡수 (잘 됨)

```bash
git switch main
git merge feature-a
```

**결과:** `Fast-forward` — 매끄럽게 합쳐짐. 지금 main의 `회사_소개.md`는 친근한 톤.

---

## 5. main에서 feature-b 흡수 시도 — 충돌!

```bash
git merge feature-b
```

**결과:**

```
Auto-merging 회사_소개.md
CONFLICT (content): Merge conflict in 회사_소개.md
Automatic merge failed; fix conflicts and then commit the result.
```

> Git이 멈춥니다. **두 갈래가 같은 줄을 서로 다르게 고쳤기 때문.** 어느 쪽 채택할지 사람만 알 수 있음.

`git status` 로 확인:

```bash
git status
# both modified: 회사_소개.md
```

---

## 6. 충돌 마커 모양 — VSCode에서 파일 열기

`회사_소개.md` 를 열면 다음과 같이 보여요:

```
<<<<<<< HEAD
안녕하세요! 저희는 AI 교육을 함께 만들어가는 따뜻한 회사예요.
=======
당사는 데이터 기반의 AI 교육 솔루션을 제공하는 전문 기업입니다.
>>>>>>> feature-b
```

**마커 해석 한 줄씩:**
- `<<<<<<< HEAD` — "여기부터는 **현재 갈래(main)** 의 내용"
- `=======` — "구분선 — 위는 main, 아래는 들고 온 갈래"
- `>>>>>>> feature-b` — "여기까지가 **feature-b** 의 내용"

VSCode는 친절하게 위에 4개 버튼을 띄워줍니다:
- **Accept Current Change** (HEAD 쪽만 살림)
- **Accept Incoming Change** (feature-b 쪽만 살림)
- **Accept Both Changes** (둘 다 남김)
- **Compare Changes** (옆에 비교 띄움)

---

## 7. 해결 — 사람이 결정

선택지 셋 중 하나:

### 선택 A — 친근한 톤만 살리기

파일 내용을 다음 한 줄로 **싹 바꿔 저장** (마커 세 줄 다 지움):

```
안녕하세요! 저희는 AI 교육을 함께 만들어가는 따뜻한 회사예요.
```

### 선택 B — 전문적 톤만 살리기

```
당사는 데이터 기반의 AI 교육 솔루션을 제공하는 전문 기업입니다.
```

### 선택 C — 둘을 합쳐 새로 쓰기 (실전에서 가장 흔함)

```
저희는 데이터 기반 AI 교육을 따뜻하게 만들어가는 회사입니다.
```

> **공통 원칙:** `<<<<<<<`, `=======`, `>>>>>>>` **세 마커는 무조건 다 지운다.** 한 글자라도 남으면 또 충돌처럼 깨짐.

---

## 8. 해결 마무리 — add + commit

```bash
git add 회사_소개.md
git status        # "All conflicts fixed but you are still merging." 확인
git commit        # 메시지 자동 채워짐 — 그대로 저장하고 빠져나오면 끝
```

> **편집기가 떠서 당황할 수 있어요.** 보통 Vim이 뜨는데:
> - `i` 눌러서 편집 모드 (안 건드려도 됨)
> - `Esc` → `:wq` → Enter (저장하고 빠져나오기)
>
> 또는 메시지 안 건드리고 그냥 `:wq` 만 쳐도 충분.
> Mac 기본 `nano`가 뜨면: `Ctrl+X` → `Y` → Enter.

```bash
git log --oneline
# 머지 매듭 + feature-a, feature-b 매듭 모두 보임
```

---

## 9. 정리 (옵션)

```bash
git branch -d feature-a
git branch -d feature-b
```

---

## 충돌이 무섭지 않은 이유 — 한 문장씩

- 충돌은 **에러가 아니에요.** "사람이 결정해줘" 신호일 뿐.
- 마커는 **친절한 표시**. "여기부터 여기까지가 누구 거" 알려줌.
- VSCode 4개 버튼은 **흔한 선택을 한 클릭으로** 만들어줌.
- 잘못 풀어도 **commit 안 했으면 되돌릴 수 있음** — 다시 편집하면 됨.

---

## Mac vs Windows

- 모든 명령어 동일.
- 편집기 종료가 다를 수 있음:
  - Mac/Linux: 보통 Vim (`:wq`) 또는 nano (`Ctrl+X` → `Y`)
  - Windows Git Bash: 보통 Vim (`:wq`)
  - 처음 한 번 `git config --global core.editor "code --wait"` 해두면 VSCode가 뜨고 그냥 닫으면 됨 (선택).

---

## 라이브 강사 메모 (학생에게 안 보여줘도 됨)

- 충돌 만들기 전 학생에게 한 번 짚기: **"지금부터 일부러 충돌 만들 거예요."**
- 충돌 떴을 때 학생 표정 살피고: **"멈췄죠? 정상이에요. 안 멈추는 게 이상한 거."**
- 마커 해석은 **천천히 한 줄씩**. VSCode 4버튼은 처음에 **안 누르고 손으로** 한 번 풀어보기 (마커 의미가 손에 박힘).
- 해결 후 `git log --oneline` 으로 **두 갈래가 다 들어와 있다** 보여주는 게 줄기 회수.
