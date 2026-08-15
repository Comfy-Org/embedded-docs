# ElevenLabs 텍스트 음성 변환

ElevenLabs Text to Speech 노드는 ElevenLabs API를 사용하여 작성된 텍스트를 음성 오디오로 변환합니다. 음성을 선택하고 안정성, 속도, 스타일과 같은 음성 특성을 조정하여 맞춤형 오디오 출력을 생성할 수 있습니다.

## 입력

### 공통 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 텍스트 음성 변환에 사용할 모델입니다. 모델을 선택하면 해당 모델의 특정 매개변수가 표시됩니다. | DYNAMIC_COMBO | 예 | "eleven_multilingual_v2"<br>"eleven_v3" |
| `voice` | 음성 합성에 사용할 음성입니다. Voice Selector 또는 Instant Voice Clone에서 연결하세요. | ELEVENLABS_VOICE | 예 | N/A |
| `text` | 음성으로 변환할 텍스트입니다. 최소 한 글자 이상이어야 합니다. | STRING | 예 | N/A |
| `stability` | 음성 안정성입니다. 값이 낮을수록 더 넓은 감정 표현이 가능하고, 값이 높을수록 더 일관되지만 잠재적으로 단조로운 음성이 생성됩니다 (기본값: 0.5). | FLOAT | 예 | 0.0 - 1.0 |
| `apply_text_normalization` | 텍스트 정규화 모드입니다. 'auto'는 시스템이 결정하고, 'on'은 항상 정규화를 적용하며, 'off'는 정규화를 건너뜁니다. | COMBO | 예 | "auto"<br>"on"<br>"off" |
| `language_code` | ISO-639-1 또는 ISO-639-3 언어 코드입니다 (예: 'en', 'es', 'fra'). 자동 감지를 위해 비워 두세요 (기본값: ""). | STRING | 예 | N/A |
| `seed` | 재현을 위한 시드입니다 (결정적 결과는 보장되지 않음) (기본값: 1). | INT | 예 | 0 - 2147483647 |
| `output_format` | 오디오 출력 형식입니다. | COMBO | 예 | "mp3_44100_192"<br>"opus_48000_192" |

### eleven_multilingual_v2 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `speed` | 음성 속도입니다. 1.0은 보통 속도이며, <1.0은 느리게, >1.0은 빠르게 재생됩니다 (기본값: 1.0). | FLOAT | 예 | 0.7 - 1.3 |
| `similarity_boost` | 유사도 부스트입니다. 값이 높을수록 원본 음성과 더 유사해집니다 (기본값: 0.75). | FLOAT | 예 | 0.0 - 1.0 |
| `use_speaker_boost` | 원본 화자 음성과의 유사도를 향상시킵니다 (기본값: False). | BOOLEAN | 예 | True<br>False |
| `style` | 스타일 과장 정도입니다. 값이 높을수록 스타일 표현이 증가하지만 안정성이 감소할 수 있습니다 (기본값: 0.0). | FLOAT | 예 | 0.0 - 0.2 |

### eleven_v3 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `speed` | 음성 속도입니다. 1.0은 보통 속도이며, <1.0은 느리게, >1.0은 빠르게 재생됩니다 (기본값: 1.0). | FLOAT | 예 | 0.7 - 1.3 |
| `similarity_boost` | 유사도 부스트입니다. 값이 높을수록 원본 음성과 더 유사해집니다 (기본값: 0.75). | FLOAT | 예 | 0.0 - 1.0 |

**참고:** `text` 입력에는 최소 한 글자 이상이 포함되어야 합니다. `language_code`를 비워 두면 언어가 자동으로 감지됩니다. `use_speaker_boost` 및 `style` 매개변수는 `eleven_multilingual_v2` 모델에서만 사용할 수 있습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `audio` | 텍스트 음성 변환으로 생성된 오디오입니다. | AUDIO |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSpeech/ko.md)

---
**Source fingerprint (SHA-256):** `78ed1c6af2d0b1cc0293d725492a8b104b6d0c6bc18d9971b75047db946cdd33`
