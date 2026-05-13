> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/ko.md)

# Kling 립싱크 텍스트-투-비디오 노드

Kling 립 싱크 텍스트-투-비디오 노드는 비디오 파일의 입 움직임을 텍스트 프롬프트와 동기화합니다. 입력 비디오를 받아 캐릭터의 입술 움직임이 제공된 텍스트와 일치하는 새로운 비디오를 생성합니다. 이 노드는 음성 합성을 사용하여 자연스러운 발화 동기화를 구현합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | 예 | - | 립싱크를 위한 입력 비디오 파일 |
| `text` | STRING | 예 | - | 립싱크 비디오 생성을 위한 텍스트 내용. 모드가 text2video일 때 필수입니다. 최대 길이는 120자입니다. |
| `voice` | COMBO | 아니요 | "Melody"<br>"Bella"<br>"Aria"<br>"Ethan"<br>"Ryan"<br>"Dorothy"<br>"Nathan"<br>"Lily"<br>"Aaron"<br>"Emma"<br>"Grace"<br>"Henry"<br>"Isabella"<br>"James"<br>"Katherine"<br>"Liam"<br>"Mia"<br>"Noah"<br>"Olivia"<br>"Sophia" | 립싱크 오디오를 위한 음성 선택 (기본값: "Melody") |
| `voice_speed` | FLOAT | 아니요 | 0.8-2.0 | 말하기 속도. 유효 범위: 0.8~2.0, 소수점 첫째 자리까지 정확합니다. (기본값: 1) |

**비디오 요구 사항:**

- 비디오 파일은 100MB를 초과할 수 없습니다
- 높이/너비는 720px에서 1920px 사이여야 합니다
- 길이는 2초에서 10초 사이여야 합니다

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 립싱크 오디오가 적용된 생성된 비디오 |
| `video_id` | STRING | 생성된 비디오의 고유 식별자 |
| `duration` | STRING | 생성된 비디오의 길이 정보 |

---
**Source fingerprint (SHA-256):** `f16200d52ba05acfedebc027dde91e2c91bdbb80086888d947c9f56a4e92856d`
