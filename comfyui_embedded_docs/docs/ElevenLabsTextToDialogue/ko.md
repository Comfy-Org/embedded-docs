# ElevenLabs 텍스트 → 대화

The ElevenLabs Text to Dialogue 노드는 텍스트에서 다중 화자 오디오 대화를 생성합니다. 이 노드를 사용하면 각 참가자에 대해 서로 다른 텍스트 줄과 개별 음성을 지정하여 대화를 만들 수 있습니다. 노드는 대화 요청을 ElevenLabs API로 전송하고 생성된 오디오를 반환합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `stability` | 음성 안정성. 값이 낮을수록 더 넓은 감정 표현 범위를 제공하고, 값이 높을수록 더 일관되지만 지루해질 수 있는 음성을 생성합니다. (기본값: 0.5) | FLOAT | 예 | 0.0 - 1.0 |
| `apply_text_normalization` | 텍스트 정규화 모드. 'auto'는 시스템이 결정하고, 'on'은 항상 정규화를 적용하며, 'off'는 건너뜁니다. | COMBO | 예 | `"auto"`<br>`"on"`<br>`"off"` |
| `model` | 대화 생성에 사용할 모델. | COMBO | 예 | `"eleven_v3"` |
| `inputs` | 대화 항목 수. 숫자를 선택하면 해당 개수의 텍스트 및 음성 입력 필드가 생성됩니다. | DYNAMIC_COMBO | 예 | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `language_code` | ISO-639-1 또는 ISO-639-3 언어 코드(예: 'en', 'es', 'fra'). 자동 감지를 위해 비워 두세요. (기본값: 비어 있음) | STRING | 예 | - |
| `seed` | 재현성을 위한 시드. (기본값: 1) | INT | 예 | 0 - 4294967295 |
| `output_format` | 오디오 출력 형식. | COMBO | 예 | `"mp3_44100_192"`<br>`"opus_48000_192"` |

**참고:** `inputs` 매개변수는 동적입니다. 숫자(예: "3")를 선택하면 노드에 해당하는 세 개의 `text` 및 `voice` 입력 필드(예: `text1`, `voice1`, `text2`, `voice2`, `text3`, `voice3`)가 표시됩니다. 각 `text` 필드에는 최소한 한 글자 이상이 포함되어야 합니다. 각 `voice` 필드는 Voice Selector 또는 Instant Voice Clone 노드에서 연결된 음성을 허용합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `audio` | 선택한 출력 형식으로 생성된 다중 화자 대화 오디오. | AUDIO |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/ko.md)

---
**Source fingerprint (SHA-256):** `95b16143391a2282c58ebc66561b85338a8ce1f87e0ec769405225599d2c76ae`
