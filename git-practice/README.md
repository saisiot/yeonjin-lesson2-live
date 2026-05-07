# Git 실습 — 손으로 굴려보는 한 페이지

> 이 한 페이지를 라이브에서 위에서 아래로 따라갑니다.
> 명령어 외우기 X. **"이게 ___의 진화"** 한 줄 비유로 흐름만 잡으세요.
>
> 줄기: **"변경을 한 매듭으로 묶고, 매듭들을 본 줄기에 합친다."**

---

## 0. 라이브 시작 전 30초 체크

- [ ] VSCode 열림
- [ ] 터미널 열림 (Mac은 zsh / Windows는 **Git Bash** 권장. PowerShell도 동작은 함)
- [ ] `git --version` / `python --version` 둘 다 한 줄 출력됨
- [ ] GitHub 계정 로그인 됨

> **Mac vs Windows 셸 한 줄**
> 이 문서의 모든 명령은 셸 종류와 거의 무관해요. 다만 **Windows에서는 Git Bash**를 쓰면 Mac/Linux와 똑같이 동작합니다. PowerShell도 됩니다 (경로 표기만 살짝 다름).

---

## 1. 내 이름표 붙이기 — `git config`

> **이게 "이 컴퓨터에서 매듭 만드는 사람이 누구인가" 라벨의 진화.**
> 모든 commit에 "누가 만들었는지" 이름·이메일이 같이 박힙니다. 한 번만 등록하면 평생 따라옴.

```bash
git config --global user.name "Yeonjin Kim"
git config --global user.email "kokp0205@naver.com"
```

확인:

```bash
git config --global --list
```

**결과 화면 (한 줄):** `user.name=...`, `user.email=...` 두 줄이 보이면 OK.

**막힐 때:** "name 옆에 따옴표 닫는 거 잊지 말기. 따옴표 안엔 공백 있어도 됨."

---

## 2. 작업 폴더 만들기 + `git init`

> **이게 "이 폴더에 이력 기능 켜기"의 진화.**
> 그냥 폴더는 변경이 사라지면 끝. `git init` 하면 그 폴더 안에 `.git` 이라는 작은 창고가 생기고, 이때부터 변경이 매듭으로 쌓여요.

```bash
# 어디서든 작업하기 좋은 자리에서
mkdir my-first-repo
cd my-first-repo
git init
```

**결과 화면 (한 줄):** `Initialized empty Git repository in .../my-first-repo/.git/`

**막힐 때 (Windows):** `mkdir`은 그대로 동작. `cd` 도 그대로. 폴더 못 찾겠으면 VSCode → "폴더 열기"로 GUI에서.

---

## 3. 첫 파일 만들기 + `git status`

> **`git status`는 "지금 카운터에 뭐 올라가 있나"의 진화.**
> 작업 폴더에서 뭘 고쳤는지, 그중 매듭에 들어갈 후보로 올려둔 게 뭔지 한눈에 보여줘요.

`sample/` 폴더의 `일기.md`를 작업 폴더로 가져옵니다 (또는 같은 내용으로 새로 만듭니다).

```bash
# sample 폴더에서 가져오기 (또는 직접 작성)
cp /path/to/git-practice/sample/일기.md ./
git status
```

**결과 화면 (한 줄):** `Untracked files: 일기.md` 가 빨갛게 뜸. "이건 아직 카운터에 안 올렸어요" 신호.

---

## 4. 카운터에 올리고 매듭 묶기 — `git add` + `git commit`

> **`git add`는 "이 변경을 카운터에 올려놓기"의 진화.**
> **`git commit`은 "카운터의 것들을 한 매듭으로 묶어 보관"의 진화.**

```bash
git add 일기.md
git status        # 초록색으로 바뀜 — "카운터에 올라옴"
git commit -m "첫 일기 추가"
```

**결과 화면 (한 줄):** `[main (root-commit) abc1234] 첫 일기 추가` — 매듭 하나 생김.

**막힐 때:** 커밋 메시지는 한 줄로 명확히. 컨벤션 외우지 마세요. "내일의 내가 봐도 알 수 있게" 한 줄.

---

## 5. 지난 매듭들 보기 — `git log`

> **이게 "지난 매듭들의 일기장"의 진화.**

```bash
git log
git log --oneline    # 한 줄씩 압축해서
```

**결과 화면 (한 줄):** 매듭 하나당 한 줄, 해시(영문 7자리) + 메시지.

**막힐 때:** 페이지가 안 빠져나오면 `q` 키 한 번. (Vim이 아니에요. less라는 페이저예요.)

---

## 6. 추적 안 하기 — `.gitignore`

> **이게 "이 종류는 추적 안 함" 라벨의 진화.**
> 임시 메모, OS가 멋대로 만든 파일(`.DS_Store`), 빌드 결과물 — 매듭에 들어갈 필요 없는 것들을 미리 빼둡니다.

`sample/.gitignore`와 `sample/notes.md`를 작업 폴더에 가져옵니다.

```bash
git status
# notes.md 가 untracked 로 뜸
# .gitignore 도 뜸 — .gitignore 자체는 추적해야 함

git add .gitignore
git commit -m ".gitignore 추가"
git status
# 이제 notes.md 가 사라짐 — "추적 안 함" 라벨이 작동
```

**결과 화면 (한 줄):** `nothing to commit, working tree clean` — notes.md는 무시됨.

**막힐 때:** `.gitignore`는 **commit하기 전에** 추가해야 효과 있음. 이미 추적 중인 파일은 별도 명령(`git rm --cached`) 필요 — 오늘은 안 함.

---

## 7. 갈래 만들기 — `git branch` + `git switch`

> **`git branch`는 "갈래 표시"의 진화.**
> **`git switch`는 "갈래 갈아타기"의 진화.**
> 본 줄기(main)는 그대로 두고, 옆에서 다른 시도를 안전하게.

```bash
git branch feature-todo        # 갈래 생성
git switch feature-todo        # 갈래로 갈아타기
git branch                     # 현재 어디 있는지 * 표시로 확인
```

**결과 화면 (한 줄):** `* feature-todo` 가 별표 붙음.

> **단축형:** `git switch -c feature-todo` 하면 생성+갈아타기 한 번에.

---

## 8. 갈래에서 작업 + commit

`sample/todo.md`를 작업 폴더에 가져와서 commit.

```bash
# todo.md 추가
git add todo.md
git commit -m "todo 목록 추가"

# todo.md 안의 항목 한 개 체크 — VSCode에서 직접 편집
git add todo.md
git commit -m "오늘 할 일 1개 완료 표시"
```

**결과 화면 (한 줄):** `feature-todo` 갈래에 매듭 2개. `git log --oneline` 으로 확인.

---

## 9. 본 줄기에 합치기 — `git merge`

> **이게 "갈래를 본 줄기에 흡수"의 진화.**

```bash
git switch main          # 본 줄기로 돌아오기
git merge feature-todo   # feature-todo 갈래를 흡수
git log --oneline        # main에도 그 매듭들이 보임
```

**결과 화면 (한 줄):** `Fast-forward` 또는 매듭이 깔끔히 합쳐진 메시지.

**막힐 때:** 합쳐진 갈래는 정리해도 됨 — `git branch -d feature-todo` (옵션).

---

## 10. 충돌 만들고 풀기 — 라이브 핵심 데모

> **충돌은 "두 갈래가 같은 자리를 다르게 고쳤을 때 — 사람이 결정해줘야 함"의 신호.**
> **충돌은 정상이에요. 안 일어나는 게 이상한 거.**

자세한 단계는 `merge-conflict-example/README.md` 참고. 핵심 흐름만:

```bash
# 1) main에 회사_소개.md 만들고 commit
# 2) feature-a 갈래 만들어서 회사_소개.md 친근한 톤으로 수정 + commit
# 3) main으로 돌아와서 feature-b 갈래 만들어서 같은 파일 같은 줄을 전문적 톤으로 수정 + commit
# 4) main에서 feature-a를 merge — 잘 됨
# 5) main에서 feature-b를 merge — 충돌!
git merge feature-b
# CONFLICT (content): Merge conflict in 회사_소개.md
```

VSCode가 충돌 마커를 보여줍니다:

```
<<<<<<< HEAD
(현재 main에 있는 내용 — feature-a가 합쳐진 친근한 톤)
=======
(feature-b의 전문적 톤)
>>>>>>> feature-b
```

**해결:**
1. 마커(`<<<<<<<`, `=======`, `>>>>>>>`) **세 줄을 다 지우고** 둘 중 하나만 남기거나, 둘을 합치거나, 새로 작성
2. 저장
3. `git add 회사_소개.md`
4. `git commit` — 메시지는 자동 채워짐. 그대로 저장하고 빠져나오면 끝

---

## 11. GitHub 저장소 연결 — `git remote add`

> **이게 "내 폴더와 클라우드 폴더 연결선"의 진화.**

GitHub 웹에서 빈 저장소 새로 만들기 (README·gitignore 다 체크 해제. 정말 빈 채로).

```bash
git remote add origin https://github.com/yeonjin-kim/my-first-repo.git
git remote -v   # 연결 확인
```

**결과 화면 (한 줄):** `origin  https://...  (fetch)` / `(push)` 두 줄.

---

## 12. 내 매듭들 → 클라우드 — `git push`

> **이게 "내 폴더의 매듭들을 클라우드에 올리기"의 진화.**

```bash
git push -u origin main
```

**결과 화면 (한 줄):** 진행률 바 + `branch 'main' set up to track 'origin/main'`.

**막힐 때:** 처음엔 GitHub 인증 창이 떠요. Mac은 키체인, Windows는 Git Credential Manager가 자동으로 뜸. 토큰·비번은 한 번만 넣으면 다음엔 자동.

---

## 13. 클라우드 → 내 폴더 — `git pull`

> **이게 "클라우드 매듭을 내 폴더로 받기"의 진화.**
> 시연: GitHub 웹에서 직접 README 같은 파일 한 줄 추가하고 commit → 로컬에서 pull.

```bash
git pull
git log --oneline   # 새 매듭이 받아져 있음
```

**결과 화면 (한 줄):** `Updating .../...`, `Fast-forward`, 변경된 파일 목록.

---

## 14. Pull Request 흐름 — 검토받고 합치기

> **PR은 "변경을 본 줄기에 넣기 전 검토받는 자리"의 진화.**

자세한 GitHub UI 단계는 `pr-flow.md` 참고. 명령어만 요약:

```bash
git switch -c feature-readme-update         # 갈래 만들기
# README.md 한 줄 수정 (VSCode에서)
git add README.md
git commit -m "README 소개 한 줄 추가"
git push -u origin feature-readme-update    # GitHub에 갈래 올리기
```

이후 GitHub 웹에서:
1. 노란 배너 "Compare & pull request" 클릭
2. 제목·설명 작성 후 "Create pull request"
3. "Files changed" 탭에서 변경 확인
4. "Merge pull request" → "Confirm merge"

마지막으로 로컬 동기화:

```bash
git switch main
git pull              # 머지된 매듭 받기
git branch -d feature-readme-update   # 다 쓴 갈래 정리 (옵션)
```

---

## 15. 한 장 요약 (눈에 박는 흐름)

```
[설정] git config
   ↓
[로컬 시작] git init → status → add → commit → log
   ↓
[무시] .gitignore
   ↓
[갈래] branch / switch → 작업 → commit → merge
   ↓
[충돌] 마커 보고 사람이 결정 → add → commit
   ↓
[클라우드] remote add → push → pull
   ↓
[검토] 새 갈래 → push → PR → merge → pull
```

---

## 16. 막힐 때 백업 멘트

- "지금 화면 같이 봐드릴까요? 강사 화면 따라가셔도 돼요."
- "명령어 다 외우려 하지 마세요. 흐름이 보이면 됨. 검색하면 다 나와요."
- "충돌 떴어도 당황 X. 원래 있는 일이에요."
- "잘못 commit 했어요?" → 일단 진행. `git commit --amend` 같은 건 4회차나 검색으로.

---

## 17. 여기까지 왔으면

여기까지 왔으면 **깃 큰 그림 끝**입니다.

- 변경을 매듭으로 묶는 손 → 됨
- 갈래에서 안전하게 시도하고 합치는 손 → 됨
- 클라우드와 주고받는 손 → 됨
- 검토받고 합치는 손(PR) → 됨

더 깊이 (rebase, stash, 협업 워크플로, GitHub Actions 등)는 **4회차 또는 본인 사업 워크플로 잡힐 때** 다시 만납니다.

오늘은 여기까지. 손에 한 번이라도 굴려본 게 의미 있는 거.
