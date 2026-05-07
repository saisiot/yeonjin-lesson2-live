# Python 설치 가이드

> **이걸 왜 깔까요?** 1회차 비유로 Python은 "실행 환경"입니다. VSCode에서 글을 써놔도 그 글을 실제로 돌려보려면 통역기가 노트북에 깔려 있어야 해요. 그게 Python입니다. 2회차 마지막에 변수·리스트·함수 한 줄씩 칠 때, 그걸 실제로 돌려서 결과 보여주는 게 이 친구예요.

---

## 1단계 — 다운로드

공식 사이트는 다음 한 곳입니다.

**공식 다운로드 페이지**: https://www.python.org/downloads/

페이지에 들어가면 본인 OS에 맞는 최신 버전이 큰 노란 버튼으로 보입니다. **Python 3.11 이상**이면 충분합니다 (3.12, 3.13도 OK).

- **Mac 사용자**: "Download Python 3.x.x" 버튼 → `.pkg` 파일이 다운로드됩니다.
- **Windows 사용자**: "Download Python 3.x.x" 버튼 → `.exe` 설치 파일이 다운로드됩니다.

[스크린샷: Python 공식 다운로드 페이지의 큰 노란 버튼]

> ⚠️ Windows 사용자가 "Microsoft Store에서 Python을 받을 수 있다"는 안내를 보실 수 있어요. **그건 쓰지 마세요**. 가짜 Python(설치 페이지로 보내는 미끼)이거나 권한 문제로 라이브 중 골치 아픈 자리가 자주 생깁니다. 무조건 위 공식 사이트에서 받으세요.

---

## 2단계 — 설치

### Mac

1. 다운로드 받은 `.pkg` 파일을 더블클릭합니다.
2. 마법사가 뜨면 **계속 → 계속 → 동의 → 설치** 순으로 진행합니다.
3. 중간에 Mac 비밀번호를 한 번 묻습니다 — 본인 노트북 로그인 비밀번호 치시면 됩니다.
4. 설치 완료 메시지가 뜨면 닫으세요.

> Mac은 시스템에 이미 옛날 Python(2.x 또는 3.x)이 깔려 있을 수 있어요. 위 설치는 그것과 별개로 새 버전을 추가하는 거라 충돌 걱정 안 하셔도 됩니다.

### Windows — 매우 중요

1. 다운로드 받은 `.exe` 파일을 더블클릭합니다.
2. **설치 마법사 첫 화면 아래쪽에 체크박스 두 개가 있습니다**.
   - ✅ **"Add python.exe to PATH"** ← **이 체크박스를 반드시 켜세요**.
   - ✅ "Use admin privileges when installing py.exe" (있으면 같이 체크)
3. **"Install Now"** 클릭.
4. 설치 끝나면 "Disable path length limit"라는 추가 옵션이 보일 수 있어요 — 보이면 그것도 한 번 클릭해두세요.

[스크린샷: Windows Python 설치 마법사 첫 화면, 'Add python.exe to PATH' 체크박스가 강조된 모습]

> **왜 PATH 체크박스가 중요한가**: 이걸 안 켜면 터미널에서 `python` 이라고 쳤을 때 노트북이 "그게 어디 있는 명령인지 모르겠다"고 답합니다. 그러면 다시 깔거나 따로 설정을 해야 해요. 처음에 한 번 켜두면 깔끔하게 끝납니다.

---

## 3단계 — 확인

설치가 잘 됐는지 봅니다. VSCode를 켜고, **터미널 → 새 터미널**로 터미널을 여세요. 또는 Mac은 "터미널" 앱, Windows는 "PowerShell" 또는 "Git Bash"를 그냥 열어도 됩니다.

다음 한 줄을 칩니다.

```
python --version
```

`Python 3.11.x` 같은 숫자가 보이면 성공입니다.

> **Mac에서 막힐 때**: 위 명령으로 `command not found`가 뜨거나 `Python 2.x`가 뜨면 다음을 시도하세요.
> ```
> python3 --version
> ```
> Mac에선 새로 깐 Python이 `python3`라는 이름으로 잡히는 게 일반적이에요. 라이브에서도 `python3`로 부르면 됩니다.

> **Windows에서 막힐 때**: `command not found` 또는 Microsoft Store가 열리면 PATH가 안 잡힌 겁니다. 2단계로 돌아가서 다시 설치하시되, "Add python.exe to PATH" 체크박스를 반드시 켜세요. 또는 설치 마법사를 다시 띄워서 "Modify"로 들어가 PATH 옵션을 다시 켤 수도 있습니다.

[스크린샷: 터미널에 'python --version' 결과로 'Python 3.11.x'가 출력된 모습]

---

## 4단계 — VSCode에서 Python 인터프리터 선택

VSCode가 "내가 쓸 Python이 어디 있는 그 친구야"를 알려줘야 합니다.

1. VSCode를 켭니다.
2. 단축키
   - **Mac**: `Cmd` + `Shift` + `P`
   - **Windows**: `Ctrl` + `Shift` + `P`
3. 위쪽에 입력창이 뜹니다. `Python: Select Interpreter` 라고 치고 엔터.
4. 방금 깐 Python 3.11+ 버전을 골라서 클릭합니다.

[스크린샷: VSCode Command Palette에서 'Python: Select Interpreter' 검색 결과와 Python 3.11+ 옵션]

---

## 5단계 — 첫 실행

직접 한 줄을 돌려봅니다. 이게 끝나면 라이브 전 자가 점검 끝입니다.

1. VSCode에서 **파일 → 새 텍스트 파일** (또는 `Cmd/Ctrl + N`).
2. 다음 한 줄을 칩니다.

   ```python
   print("안녕")
   ```

3. **파일 → 다른 이름으로 저장** (또는 `Cmd/Ctrl + S`)으로 저장하세요.
   - 파일 이름: `안녕.py`
   - 저장 위치: 본인이 찾기 쉬운 자리 (바탕화면 또는 문서 폴더)
4. 저장하면 VSCode가 "이건 파이썬 파일이구나" 알아보고 색깔이 입혀집니다.
5. **오른쪽 위 ▶ (재생) 버튼**을 클릭하거나, 파일 아무 곳에서 우클릭 → **"Run Python File in Terminal"** 선택.
6. 화면 아래 터미널에 `안녕`이라는 글자가 뜨면 성공입니다.

[스크린샷: VSCode에 안녕.py 파일이 열려 있고 터미널 아래쪽에 '안녕' 출력 결과가 보이는 모습]

> 이게 1회차에 들으셨던 "글 쓰는 종이 + 실행 환경"이 같이 동작한 첫 순간이에요. 종이(VSCode)에 글을 쓰고, 실행 환경(Python)이 그걸 통역해서 결과를 보여준 겁니다.

---

## 막힐 때 — 자주 보는 자리

- **`python --version` 했는데 'command not found' (Mac)** → `python3 --version` 시도. Mac은 보통 `python3`로 잡힙니다.
- **`python --version` 했는데 'command not found' (Windows)** → 설치할 때 "Add python.exe to PATH" 체크 안 한 거예요. 2단계 재설치.
- **`python` 쳤는데 Microsoft Store가 열림 (Windows)** → 가짜 Python이 잡힌 거예요. 공식 사이트에서 다시 설치하시고, 설정 → 앱 실행 별칭에서 "App Installer python.exe"를 끄세요.
- **VSCode ▶ 버튼이 안 보임** → 4단계 인터프리터 선택을 안 한 거예요. `Cmd/Ctrl + Shift + P` → `Python: Select Interpreter` 다시.
- **터미널에서 한글 깨짐 (Windows)** → 일단 무시하셔도 됩니다. 라이브에서 같이 봅니다.
