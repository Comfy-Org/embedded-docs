# ElevenLabs 음성 변환

ElevenLabs Speech to Speech 노드는 입력 오디오 파일을 한 목소리에서 다른 목소리로 변환합니다. ElevenLabs API를 사용하여 오디오의 원래 내용과 감정적 어조를 유지하면서 음성을 변환합니다.

## 입력

### 공통 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 음성 간 변환에 사용할 모델입니다. 각 모델 옵션은 일치하는 음성 설정 세트(similarity_boost, style, use_speaker_boost, speed)를 제공합니다. | DYNAMIC_COMBO | 아니오 | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `voice` | 변환 대상 목소리입니다. Voice Selector 또는 Instant Voice Clone에서 연결하십시오. | CUSTOM | 예 | - |
| `audio` | 변환할 소스 오디오입니다. | AUDIO | 예 | - |
| `stability` | 음성 안정성입니다. 값이 낮을수록 더 넓은 감정 범위를 제공하고, 값이 높을수록 더 일관되지만 잠재적으로 단조로운 음성을 생성합니다(기본값: 0.5). | FLOAT | 아니오 | 0.0 - 1.0 |
| `output_format` | 오디오 출력 형식입니다(기본값: "mp3_44100_192"). | COMBO | 아니오 | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `seed` | 재현성을 위한 시드입니다(기본값: 0). | INT | 아니오 | 0 - 4294967295 |
| `remove_background_noise` | 오디오 분리를 사용하여 입력 오디오에서 배경 소음을 제거합니다(기본값: False). | BOOLEAN | 아니오 | - |

### 음성 설정(`eleven_multilingual_sts_v2` 및 `eleven_english_sts_v2` 공유)

모델을 선택하면 이러한 음성 설정을 변환에 사용할 수 있습니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `speed` | 음성 속도입니다. 1.0은 보통 속도이며, <1.0은 더 느리게, >1.0은 더 빠르게 재생됩니다(기본값: 1.0). | FLOAT | 아니오 | 0.7 - 1.3 |
| `similarity_boost` | 유사도 부스트입니다. 값이 높을수록 목소리가 원본에 더 가까워집니다(기본값: 0.75). | FLOAT | 아니오 | 0.0 - 1.0 |
| `use_speaker_boost` | 원본 화자 음성과의 유사도를 높입니다(기본값: False). | BOOLEAN | 아니오 | - |
| `style` | 스타일 과장 정도입니다. 값이 높을수록 스타일 표현이 증가하지만 안정성이 감소할 수 있습니다(기본값: 0.0). | FLOAT | 아니오 | 0.0 - 0.2 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `audio` | 지정된 출력 형식의 변환된 오디오 파일입니다. | AUDIO |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/ko.md)

---
**Source fingerprint (SHA-256):** `a3cd602181d134b9ab517bfac092ea30b62ef5a9942a905c0c3e6959b34370ca`
