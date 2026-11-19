# ⏰ 우리반타이머

교실 TV·전자칠판용 큰 숫자 타이머 프로그램입니다.

## 기능
- **⚙️ 소리 설정** – 알람 소리 4가지(삐삐삐·종소리·실로폰·부드러운 차임) 미리 듣기, 음량, 울림 자동 멈춤(30초·1분·3분·안 멈춤)
- **📱 휴대폰 알림 (apk)** – 앱을 내리거나 꺼도 알람·타이머가 휴대폰 알림으로 울림 (처음 실행 때 알림 허용 필요)
- **⧉ 작은 창 (PC)** – 화면 오른쪽 아래에 항상 위로 뜨는 작은 타이머. PPT 슬라이드쇼 위에도 보임. 창을 끌어 옮기거나 크기 조절 가능, ⤢ 버튼·M 키·더블클릭으로 원래 크기
- **🎨 테마** – 다크 글래스 / 화이트 글래스 전환 (오른쪽 위 ☀️·🌙 버튼)
- **🕐 시계** – 현재 날짜·시각 + 세계시각 8개 도시(서울, 도쿄, 베이징, 뉴델리, 런던, 파리, 뉴욕, 시드니), 낮/밤 표시
- **⏱ 스톱워치** – 시작/멈춤, 구간 기록, 초기화
- **⏳ 타이머** – 숫자를 눌러 숫자판으로 직접 입력(예: 7·3·0 → 7분 30초), 1분~40분 빠른 설정, −1분·−10초·+10초·+1분·+5분 조절(진행 중에도 바로 반영), 진행 막대, 마지막 1분 주황·10초 빨강, 끝나면 화면 깜빡임 + 소리
- **⏰ 알람** – 여러 개 저장(껐다 켜기, 삭제), 메모 표시

## 단축키
| 키 | 기능 |
|---|---|
| 1 / 2 / 3 / 4 | 시계 / 스톱워치 / 타이머 / 알람 탭 |
| Space | 시작·멈춤 |
| R | 초기화 |
| L | 스톱워치 기록 |
| Enter / E | 타이머 시간 직접 입력 |
| ↑ / ↓ | 타이머 1분 더하기 / 빼기 (진행 중에도 가능) |
| T | 다크 ↔ 화이트 테마 |
| M | 작은 창 ↔ 원래 크기 (PC) |
| Enter / E | 타이머 시간 직접 입력 |
| ↑ / ↓ | 타이머 1분 더하기 / 빼기 (진행 중에도 가능) |
| F11 | 전체화면 |
| 아무 키 / 화면 클릭 | 울리는 소리 멈춤 |

## 다운로드
**최신 버전: https://github.com/gimcheonbugogcho27-bot/Timer/releases/latest**
- `ClassTimer-Portable.exe` – 설치 없이 실행 (Windows)
- `ClassTimer-Setup.exe` – 설치형 (Windows)
- `ClassTimer.apk` – 안드로이드
- `ClassTimer-InstallGuide.zip` – 설치 가이드 (PC · 안드로이드 · 아이폰, A4 인쇄용 이미지)

**아이폰·설치 없이 쓰기: https://gimcheonbugogcho27-bot.github.io/Timer/**
사파리에서 열고 공유 → 홈 화면에 추가 (앱이 화면에 켜져 있을 때만 알람이 울려요)

## exe · apk 자동 빌드
이 저장소에 올리면 GitHub Actions가 자동으로 Windows exe와 Android apk를 만듭니다.

1. 저장소 위쪽 **Actions** 탭 → **Build EXE & APK** 클릭
2. 가장 최근 실행(초록 체크) 클릭 → 아래 **Artifacts**에서 다운로드
   - `우리반타이머-windows`: `ClassTimer-Portable.exe`, `ClassTimer-Setup.exe`
   - `우리반타이머-android`: `ClassTimer.apk` (휴대폰·태블릿에 설치, 실행 중 화면 꺼짐 방지)

> 수동 실행: Actions 탭 → Build EXE & APK → **Run workflow**
> 릴리스: main에 올릴 때마다 `package.json`의 version(예: 1.0.0)으로 릴리스가 자동으로 만들어지거나 갱신됩니다. 새 버전으로 따로 남기려면 version을 올리세요.
> apk 설치 시 "출처를 알 수 없는 앱" 설치를 허용해야 합니다.

※ 서명 없는 exe라 처음 실행할 때 Windows가 "PC 보호" 창을 띄우면 **추가 정보 → 실행**을 누르세요.

## 내 PC에서 직접 빌드
```bash
npm install
npm start      # 바로 실행
npm run dist   # dist 폴더에 exe 생성
```
`index.html`만 브라우저로 열어도 그대로 사용할 수 있습니다.

## 앱 아이콘
`icon.svg`가 원본입니다. 알림 소리는 `scripts/make_sounds.py`로 만듭니다(`android-res/raw`). 아이콘을 바꾸려면 `scripts/make_icons.py`의 그림을 고친 뒤 실행하면 exe용(`build/icon.png`)과 apk용(`android-res/`) 아이콘이 모두 다시 만들어집니다.
