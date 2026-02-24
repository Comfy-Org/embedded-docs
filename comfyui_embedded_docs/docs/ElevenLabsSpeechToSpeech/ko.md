> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/ko.md)

ElevenLabs Speech to Speech 노드는 입력 오디오 파일의 음성을 다른 음성으로 변환합니다. ElevenLabs API를 사용하여 오디오의 원본 내용과 감정적 톤을 유지하면서 음성을 변환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `voice` | CUSTOM | 예 | - | 변환할 대상 음성입니다. Voice Selector 또는 Instant Voice Clone 노드에서 연결하세요. |
| `audio` | AUDIO | 예 | - | 변환할 원본 오디오입니다. |
| `stability` | FLOAT | 아니요 | 0.0 - 1.0 | 음성 안정성입니다. 값이 낮을수록 감정 표현 범위가 넓어지고, 값이 높을수록 더 일관되지만 단조로울 수 있는 음성을 생성합니다 (기본값: 0.5). |
| `model` | DYNAMICCOMBO | 아니요 | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` | 음성 대 음성 변환에 사용할 모델입니다. 각 옵션은 음성 설정(유사성 부스트, 스타일, 화자 부스트 사용, 속도)의 특정 세트를 제공합니다. |
| `output_format` | COMBO | 아니요 | `"mp3_44100_192"`<br>`"opus_48000_192"` | 오디오 출력 형식입니다 (기본값: "mp3_44100_192"). |
| `seed` | INT | 아니요 | 0 - 4294967295 | 재현성을 위한 시드 값입니다 (기본값: 0). |
| `remove_background_noise` | BOOLEAN | 아니요 | - | 오디오 분리를 사용하여 입력 오디오의 배경 잡음을 제거합니다 (기본값: False). |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `audio` | AUDIO | 지정된 출력 형식으로 변환된 오디오 파일입니다. |
