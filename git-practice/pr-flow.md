# Pull Request 흐름 — GitHub UI 단계별

> **PR은 "변경을 본 줄기에 넣기 전 검토받는 자리"의 진화.**
> 혼자 작업하는 지금은 셀프 머지지만, 실제 협업·AI 외주 시 이 자리가 핵심.

---

## 흐름 요약

```
[로컬] 새 갈래 만들기 + 변경 + commit + push
   ↓
[GitHub] Compare & pull request 클릭
   ↓
[GitHub] PR 제목·설명 작성 → Create pull request
   ↓
[GitHub] Files changed 탭에서 변경 검토
   ↓
[GitHub] Merge pull request → Confirm merge
   ↓
[로컬] main으로 돌아와서 git pull
   ↓
(옵션) [정리] 다 쓴 갈래 삭제
```

---

## 1단계 — 로컬에서 새 갈래 + 변경 + push (CLI)

> 이게 "내 시도를 본 줄기 건드리지 않고 클라우드까지 올려두기"의 진화.

```bash
# 본 줄기에서 시작
git switch main
git pull                              # 최신 상태 맞추기

# 새 갈래 만들기 + 갈아타기 한 번에
git switch -c feature-readme-update

# README.md 수정 (VSCode에서)
# 예: "이 저장소는 연진의 첫 Git 연습장입니다." 한 줄 추가

git add README.md
git commit -m "README 소개 한 줄 추가"
git push -u origin feature-readme-update
```

**`-u` 의미 한 줄**: "이 로컬 갈래가 클라우드 어떤 갈래에 묶이는지 한 번 등록." 다음부터는 `git push` 한 단어로 끝.

**Mac vs Windows**: 명령어 동일. Windows는 Git Bash 권장.

---

## 2단계 — GitHub 저장소 페이지 방문

브라우저에서 본인 저장소 URL로 접속:
`https://github.com/<your-username>/my-first-repo`

방금 push한 직후라면 **노란 배너**가 떠 있어요:

> **`feature-readme-update` had recent pushes ... [Compare & pull request]**

**[Compare & pull request]** 버튼 클릭.

[스크린샷 자리: 저장소 메인 페이지 상단 노란 배너 — "Compare & pull request" 버튼 강조]

**막힐 때:**
- 노란 배너 안 보이면 → 상단 탭 **"Pull requests"** → **"New pull request"** → base: `main`, compare: `feature-readme-update` 선택.

---

## 3단계 — PR 작성 화면

다음 항목 확인·작성:

### 3-1. base / compare 갈래 확인

화면 위쪽:

> **base: main ← compare: feature-readme-update**

- **base**: 합쳐질 본 줄기 (main)
- **compare**: 들고 가는 갈래 (feature-readme-update)

**틀리면 머지 방향이 거꾸로 됨. 꼭 확인.**

[스크린샷 자리: PR 생성 화면 상단 base/compare 드롭다운 두 개 강조]

### 3-2. 제목

기본값: 마지막 commit 메시지 ("README 소개 한 줄 추가").

> **제목은 한 줄로 명확하게.** 컨벤션 외우지 마세요. "내일의 내가 봐도 알 수 있게."

### 3-3. 설명 (description)

빈 칸이지만, 다음 정도 박아두면 본인이 나중에 봐도 좋음:

```
## 무엇을 바꿨나
README에 저장소 한 줄 소개 추가.

## 왜
처음 들어오는 사람이 이 저장소가 뭔지 한 줄로 알게 하려고.
```

[스크린샷 자리: PR 작성 화면 — 제목 입력란 + 설명(description) Markdown 에디터]

### 3-4. 생성

오른쪽 아래 초록색 버튼 **[Create pull request]** 클릭.

---

## 4단계 — PR 페이지에서 변경 리뷰

PR이 생성되면 PR 상세 페이지로 이동. 여기 탭이 4개 있음:

| 탭 | 역할 |
|---|---|
| **Conversation** | 토론·코멘트 자리. 혼자 작업 시엔 거의 비어있음. |
| **Commits** | 이 PR에 들어간 매듭들 목록. |
| **Checks** | 자동 검사 (GitHub Actions). 오늘은 없음. |
| **Files changed** | 실제 코드 차이 (diff) — **여기가 검토 자리**. |

**[Files changed]** 탭 클릭 → 빨강(삭제)·초록(추가) 줄로 정확히 뭐 바뀌었는지 보임.

[스크린샷 자리: Files changed 탭 — 빨강·초록 줄 diff 보이는 화면]

> **여기서 본인이 뭘 바꿨는지 한 번 더 확인.** "어, 의도 안 한 줄도 들어갔네" → 로컬에서 추가 commit + push 하면 PR에 자동 반영.

---

## 5단계 — 머지 (혼자 작업이니 셀프 머지)

**Conversation** 탭으로 돌아옴. 페이지 아래쪽에 초록 버튼:

> **[Merge pull request]**

클릭 → 메시지 자동 채워짐 → **[Confirm merge]** 클릭.

[스크린샷 자리: Merge pull request 초록 버튼 강조]

머지 완료 화면:

> **Pull request successfully merged and closed.**

옆에 **[Delete branch]** 버튼이 뜸. 클라우드의 다 쓴 갈래 정리하려면 클릭. (안 눌러도 됨.)

[스크린샷 자리: 머지 완료 후 보라색 "Merged" 배지 + Delete branch 버튼]

> **머지 방식 한 줄:** GitHub 기본은 "Merge commit". 다른 옵션(Squash, Rebase)은 무시. 오늘은 기본만.

---

## 6단계 — 로컬에서 main으로 돌아와서 받기

PR이 머지된 건 **클라우드**에서 일어난 일. 내 로컬 main은 아직 모름.

```bash
git switch main
git pull
git log --oneline    # 머지된 매듭이 main에 들어와 있음
```

**Mac vs Windows**: 동일.

---

## 7단계 (옵션) — 다 쓴 갈래 정리

```bash
# 로컬 갈래 삭제
git branch -d feature-readme-update

# 클라우드 갈래는 GitHub UI의 [Delete branch] 버튼으로 (5단계에서 했으면 스킵)
# 또는:
git push origin --delete feature-readme-update
```

> **갈래 삭제 안 무서워요.** 매듭은 main에 이미 들어가 있고, 갈래는 라벨일 뿐. 라벨만 떼는 거.

---

## 막힐 때 백업

- **"Compare & pull request" 배너가 안 보임** → Pull requests 탭 → New pull request에서 직접 갈래 선택.
- **"This branch has no conflicts"** 표시 안 됨 → 충돌 있는 거. 로컬에서 `git pull origin main` → 충돌 풀기 → push.
- **"Merge pull request" 버튼이 회색** → 충돌 있거나 권한 문제. 메시지 그대로 읽으면 답이 있음.
- **PR을 잘못 만들었음** → 페이지 아래 "Close pull request"로 닫기. 매듭은 안 사라짐.

---

## 한 줄 요약

> **PR = "이 변경, 본 줄기에 넣어도 돼요?" 라고 묻는 자리.** 혼자 작업이면 본인이 묻고 본인이 답함. 협업이면 동료·AI가 답함. 흐름은 똑같음.
