> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/ko.md)

ElevenLabs Instant Voice Clone 노드는 한 사람의 목소리 녹음 파일 1개에서 8개를 분석하여 새로운 고유 음성 모델을 생성합니다. 이 노드는 샘플을 ElevenLabs API로 전송하며, API는 이를 처리하여 텍스트 음성 합성에 사용할 수 있는 음성 복제본을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `audio_*` | AUDIO | 예 | 1개 ~ 8개 파일 | 음성 복제에 사용할 오디오 녹음 파일입니다. 1개에서 8개 사이의 오디오 파일을 제공해야 합니다. |
| `remove_background_noise` | BOOLEAN | 아니요 | True / False | 오디오 분리 기술을 사용하여 음성 샘플의 배경 잡음을 제거합니다. (기본값: False) |

**참고:** 최소한 하나의 오디오 파일을 제공해야 하며, 최대 여덟 개까지 제공할 수 있습니다. 노드는 추가한 오디오 파일에 대해 입력 슬롯을 자동으로 생성합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `voice` | ELEVENLABS_VOICE | 새로 생성된 복제 음성 모델의 고유 식별자입니다. 이 출력은 다른 ElevenLabs 텍스트 음성 합성 노드에 연결할 수 있습니다. |
