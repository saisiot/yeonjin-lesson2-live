# Git 설치 가이드

> **이걸 왜 깔까요?** 1회차 비유로 Git은 "이력 도구"입니다. 글을 쓰다가 망쳤을 때 어제로 되돌릴 수 있게 매듭을 묶어두는 장치예요. 2회차 세션 2 전체가 이 친구를 손으로 굴려보는 시간입니다 — 매듭 묶기, 갈래 만들기, 갈래 합치기, 다른 사람에게 검토받기.

---

## 1단계 — 다운로드

OS마다 받는 자리가 다릅니다.

### Mac

Mac은 Git 설치 방식이 두 가지예요. **첫 번째 방법이 가장 간단합니다.**

**방법 1 — 자동 안내 받기 (추천)**

1. Mac에서 **터미널** 앱을 엽니다 (`Cmd + Space` → `터미널` 검색).
2. 다음 한 줄을 칩니다.

   ```
   git --version
   ```

3. 만약 Git이 아직 안 깔려 있으면, **"명령어 줄 개발자 도구를 설치하시겠습니까?"** (Xcode Command Line Tools) 라는 창이 뜹니다.
4. **"설치"** 버튼을 누르고, 약관 동의 → 비밀번호 입력 → 기다리시면 됩니다 (5~10분 정도).
5. 설치가 끝나면 다시 `git --version` 쳤을 때 숫자가 보입니다.

> 이 방법이 Mac 공식 권장 방식이에요. Apple이 자동으로 띄워주는 안내를 그대로 따라가시면 됩니다.

**방법 2 — Homebrew 사용 (1번이 안 될 때만)**

이미 Homebrew를 쓰고 계시면 다음 한 줄로도 가능합니다.

```
brew install git
```

> Homebrew를 안 쓰셨다면 굳이 이걸 위해 새로 까실 필요는 없어요. 방법 1로 충분합니다.

### Windows

**공식 다운로드 페이지**: https://git-scm.com/download/win

페이지에 들어가면 OS를 자동 감지해서 적절한 설치 파일을 받게 해줍니다. **"64-bit Git for Windows Setup"**을 받으시면 됩니다 (요즘 노트북은 거의 다 64비트예요).

[스크린샷: Git 공식 다운로드 페이지의 Windows용 설치 파일 링크]

---

## 2단계 — 설치

### Mac

방법 1을 따라가셨으면 이미 끝났습니다. 3단계로 넘어가세요.

### Windows

다운로드 받은 `.exe` 파일을 더블클릭하면 설치 마법사가 뜹니다. 옵션이 많은데, **대부분 기본값 그대로** 두시면 됩니다. 다음 자리만 짚어드릴게요.

1. **Select Components** 화면 — 기본값 그대로 두면 **Git Bash**와 **Git GUI**가 같이 깔립니다. 둘 다 그대로 두세요.
2. **Choosing the default editor** 화면 — 기본값이 Vim일 텐데, 화살표 메뉴에서 **"Use Visual Studio Code as Git's default editor"**로 바꾸시면 라이브에서 편합니다 (VSCode가 이미 깔려 있어야 함).
3. **Adjusting the name of the initial branch** — **"Override the default branch name for new repositories"** 선택 후 `main`이라고 입력해두세요.
4. 그 외 화면들 — 전부 **Next** 눌러 진행하시면 됩니다.

설치가 끝나면 시작 메뉴에 **Git Bash**라는 앱이 새로 생깁니다.

[스크린샷: Windows Git 설치 마법사의 default editor 화면에서 VSCode를 선택한 모습]

> **PowerShell vs Git Bash 어디서 명령을 칠까?** Windows는 명령창이 두 종류 깔립니다.
> - **Git Bash** — Git 명령어가 가장 잘 동작합니다. **여기 쓰시는 걸 권합니다.**
> - **PowerShell** — Windows 기본 명령창. Git도 되긴 하지만 가끔 잔재 문제가 있어요.
>
> 라이브에선 **Git Bash**로 통일하겠습니다. 시작 메뉴에서 "Git Bash" 검색해서 여시면 됩니다.

---

## 3단계 — 확인

터미널(Mac) 또는 Git Bash(Windows)에서 다음 한 줄.

```
git --version
```

`git version 2.x.x` 같은 숫자가 보이면 성공입니다.

[스크린샷: 터미널/Git Bash에 git --version 결과가 출력된 모습]

---

## 4단계 — 초기 설정 (필수)

Git은 매듭을 묶을 때마다 "이걸 누가 묶었는지" 이름표를 붙입니다. 그러려면 본인 이름과 이메일을 한 번 등록해둬야 해요. 노트북에 한 번만 해두면 그 다음부터는 자동으로 붙습니다.

다음 세 줄을 차례로 칩니다 (이메일 자리에 본인 GitHub 가입 이메일 넣으세요 — 추후 GitHub 연동을 위해).

```
git config --global user.name "연진"
```

```
git config --global user.email "본인이메일@example.com"
```

```
git config --global init.defaultBranch main
```

> **세 번째 줄은 왜 치나요?** Git이 새 폴더를 만들 때 기본 갈래 이름을 `main`으로 쓰겠다는 약속이에요. 옛날엔 다른 이름을 썼는데 요즘은 `main`이 표준이라 미리 맞춰두면 라이브에서 헷갈릴 일이 줄어듭니다.

설정이 잘 됐는지 한 번 확인해보세요.

```
git config --list
```

화면에 본인 이름과 이메일이 보이면 통과입니다. 너무 길면 `q` 키로 빠져나오시면 됩니다.

[스크린샷: git config --list 출력 결과에 user.name과 user.email이 보이는 모습]

---

## 5단계 (옵션) — GitHub 계정과 연동

GitHub 계정이 만들어졌으면 거기까지로 충분합니다. **본인 노트북 Git이 GitHub에 코드를 올릴 수 있게 인증하는 일은 라이브에서 같이 합니다** — 토큰을 만들어 붙이거나 브라우저 인증 창을 통과하는 단계라 처음 하면 헷갈릴 수 있어서, 그날 같이 진행하는 게 안전합니다.

지금은 GitHub 가입(이메일 인증까지)만 끝내두시면 됩니다.

---

## 막힐 때 — 자주 보는 자리

- **Mac에서 `git --version` 쳤는데 아무 일도 안 일어남** → Xcode Command Line Tools 설치 창이 뒤에 가려져 있을 수 있어요. 다른 창들 다 정리하고 다시 쳐보세요.
- **Mac에서 Xcode 설치가 너무 오래 걸림** → 첫 설치는 5~10분 걸립니다. 인터넷 속도에 따라 더 걸릴 수도 있어요. 끊지 마시고 기다리세요.
- **Windows에서 PowerShell엔 잡히는데 Git Bash엔 안 잡힘** (또는 그 반대) → 보통 같이 잡힙니다. 한 쪽만 잡히면 노트북 재시작 한 번.
- **`git config --global user.name "연진"` 쳤는데 'fatal: $HOME not set' 에러** → 권한 문제일 수 있어요. 라이브 전에 알려주세요.
- **Windows에서 한글 이름이 깨짐** → user.name은 영문 또는 한글 둘 다 OK인데, 깨지면 영문으로 두셔도 됩니다 (예: `"yeonjin"`). 라이브에서 다시 봅니다.
- **`git config --list` 결과를 종료하고 싶음** → `q` 키 한 번 누르면 빠져나옵니다.
