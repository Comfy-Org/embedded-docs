> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsAudioIsolation/ko.md)

ElevenLabs Voice Isolation 노드는 오디오 파일에서 배경 소음을 제거하여 보컬이나 음성을 분리합니다. 오디오를 ElevenLabs API로 전송하여 처리하고 정제된 오디오를 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | 예 | | 배경 소음을 제거하기 위해 처리할 오디오입니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `audio` | AUDIO | 배경 소음이 제거된 처리된 오디오입니다. |
