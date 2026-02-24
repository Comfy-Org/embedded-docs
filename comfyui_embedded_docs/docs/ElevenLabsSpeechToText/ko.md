> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToText/ko.md)

ElevenLabs Speech to Text 노드는 오디오 파일을 텍스트로 전사합니다. ElevenLabs의 API를 사용하여 음성을 문자 기록으로 변환하며, 자동 언어 감지, 다른 화자 식별, 음악이나 웃음과 같은 비언어적 소리 태그 지정과 같은 기능을 지원합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | 예 | - | 전사할 오디오입니다. |
| `model` | COMBO | 예 | `"scribe_v2"` | 전사에 사용할 모델입니다. 이 모델을 선택하면 추가 매개변수가 표시됩니다. |
| `tag_audio_events` | BOOLEAN | 아니요 | - | 전사본에 (웃음), (음악) 등의 소리를 주석으로 추가합니다. 이 매개변수는 `"scribe_v2"` 모델이 선택되었을 때 표시됩니다. (기본값: False) |
| `diarize` | BOOLEAN | 아니요 | - | 어떤 화자가 말하는지 주석을 추가합니다. 이 매개변수는 `"scribe_v2"` 모델이 선택되었을 때 표시됩니다. (기본값: False) |
| `diarization_threshold` | FLOAT | 아니요 | 0.1 - 0.4 | 화자 분리 민감도입니다. 값이 낮을수록 화자 변경에 더 민감합니다. 이 매개변수는 `"scribe_v2"` 모델이 선택되고 `diarize`가 활성화되었을 때 표시됩니다. (기본값: 0.22) |
| `temperature` | FLOAT | 아니요 | 0.0 - 2.0 | 무작위성 제어입니다. 0.0은 모델 기본값을 사용합니다. 값이 높을수록 무작위성이 증가합니다. 이 매개변수는 `"scribe_v2"` 모델이 선택되었을 때 표시됩니다. (기본값: 0.0) |
| `timestamps_granularity` | COMBO | 아니요 | `"word"`<br>`"character"`<br>`"none"` | 전사된 단어의 타이밍 정밀도입니다. 이 매개변수는 `"scribe_v2"` 모델이 선택되었을 때 표시됩니다. (기본값: "word") |
| `language_code` | STRING | 아니요 | - | ISO-639-1 또는 ISO-639-3 언어 코드입니다 (예: 'en', 'es', 'fra'). 자동 감지를 위해서는 비워 두세요. (기본값: "") |
| `num_speakers` | INT | 아니요 | 0 - 32 | 예측할 최대 화자 수입니다. 자동 감지를 위해서는 0으로 설정하세요. (기본값: 0) |
| `seed` | INT | 아니요 | 0 - 2147483647 | 재현성을 위한 시드입니다 (결정론적 보장은 없음). (기본값: 1) |

**참고:** `diarize` 옵션이 활성화된 상태에서는 `num_speakers` 매개변수를 0보다 큰 값으로 설정할 수 없습니다. `diarize`를 비활성화하거나 `num_speakers`를 0으로 설정해야 합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `text` | STRING | 오디오에서 전사된 텍스트입니다. |
| `language_code` | STRING | 오디오에서 감지된 언어 코드입니다. |
| `words_json` | STRING | 타임스탬프 및 활성화된 경우 화자 레이블을 포함한 상세한 단어 수준 정보가 담긴 JSON 형식의 문자열입니다. |
