# ElevenLabs 음성 → 텍스트

ElevenLabs Speech to Text 노드는 ElevenLabs의 음성-텍스트 API를 사용하여 오디오를 텍스트로 전사합니다. 자동 언어 감지, 현재 말하는 화자 식별, 대본에서 (웃음) 또는 (음악) 같은 비음성 사운드 태그 지정을 지원합니다.

## 입력

### 공통 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 전사에 사용할 모델입니다. 모델을 선택하면 해당 모델의 특정 매개변수가 표시됩니다. | DYNAMIC_COMBO | 예 | `"scribe_v2"` |
| `audio` | 전사할 오디오입니다. | AUDIO | 예 | - |
| `language_code` | ISO-639-1 또는 ISO-639-3 언어 코드입니다(예: 'en', 'es', 'fra'). 자동 감지하려면 비워 두세요. (기본값: "") | STRING | 아니요 | - |
| `num_speakers` | 예측할 최대 화자 수입니다. 자동 감지하려면 0으로 설정하세요. (기본값: 0) | INT | 아니요 | 0 - 32 |
| `seed` | 재현을 위한 시드입니다(결정성은 보장되지 않음). (기본값: 1) | INT | 아니요 | 0 - 2147483647 |

### Scribe v2 입력

이 매개변수들은 `"scribe_v2"` 모델이 선택되었을 때 나타납니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `tag_audio_events` | 대본에서 (웃음), (음악) 등의 소리를 주석으로 표시합니다. (기본값: False) | BOOLEAN | 아니요 | - |
| `diarize` | 현재 말하는 화자를 주석으로 표시합니다. (기본값: False) | BOOLEAN | 아니요 | - |
| `diarization_threshold` | 화자 분리 민감도입니다. 값이 낮을수록 화자 변경에 더 민감하게 반응합니다. `diarize`가 활성화된 경우에만 사용됩니다. (기본값: 0.22) | FLOAT | 아니요 | 0.1 - 0.4 |
| `temperature` | 무작위성 제어입니다. 0.0은 모델 기본값을 사용합니다. 값이 높을수록 무작위성이 증가합니다. (기본값: 0.0) | FLOAT | 아니요 | 0.0 - 2.0 |
| `timestamps_granularity` | 전사 단어의 시간 정밀도입니다. (기본값: "word") | COMBO | 아니요 | `"word"`<br>`"character"`<br>`"none"` |

**참고:** `diarize`가 활성화된 경우 `num_speakers`를 0보다 큰 값으로 설정할 수 없습니다. `diarize`를 비활성화하거나 `num_speakers`를 0으로 설정하세요. 그렇지 않으면 오류가 발생합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `text` | 오디오에서 전사된 텍스트입니다. | STRING |
| `language_code` | 오디오에서 감지된 언어 코드입니다. | STRING |
| `words_json` | 타임스탬프와 활성화된 경우 화자 레이블을 포함한 상세한 단어 수준 정보가 담긴 JSON 형식 문자열입니다. | STRING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/ko.md)

---
**Source fingerprint (SHA-256):** `7eb5d72615aa8a9e4a8014e45b39cf83dc8d8432d7ce0dccba20489be80a5830`
