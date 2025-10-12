> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/ko.md)

Kling Lip Sync Text to Video 노드는 비디오 파일에서 입 모양을 텍스트 프롬프트에 맞춰 동기화합니다. 입력 비디오를 받아 제공된 텍스트에 맞춰 캐릭터의 입 모양이 정렬된 새로운 비디오를 생성합니다. 이 노드는 음성 합성을 사용하여 자연스러운 음성 동기화를 구현합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `비디오` | VIDEO | 예 | - | 입 모양 동기화를 위한 입력 비디오 파일 |
| `텍스트` | STRING | 예 | - | 입 모양 동기화 비디오 생성을 위한 텍스트 콘텐츠. mode가 text2video일 때 필수입니다. 최대 길이는 120자입니다. |
| `음성` | COMBO | 아니오 | "Melody"<br>"Bella"<br>"Aria"<br>"Ethan"<br>"Ryan"<br>"Dorothy"<br>"Nathan"<br>"Lily"<br>"Aaron"<br>"Emma"<br>"Grace"<br>"Henry"<br>"Isabella"<br>"James"<br>"Katherine"<br>"Liam"<br>"Mia"<br>"Noah"<br>"Olivia"<br>"Sophia" | 입 모양 동기화 오디오용 음성 선택 (기본값: "Melody") |
| `음성 속도` | FLOAT | 아니오 | 0.8-2.0 | 음성 속도. 유효 범위: 0.8~2.0, 소수점 첫째 자리까지 정확함. (기본값: 1) |

**비디오 요구사항:**
- 비디오 파일은 100MB를 초과하지 않아야 함
- 높이/너비는 720px에서 1920px 사이여야 함
- 지속 시간은 2초에서 10초 사이여야 함

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `비디오 ID` | VIDEO | 입 모양이 동기화된 오디오가 포함된 생성된 비디오 |
| `길이` | STRING | 생성된 비디오의 고유 식별자 |
| `duration` | STRING | 생성된 비디오의 지속 시간 정보 |