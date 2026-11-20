# Google Gemini Decision (Score)

연결한 텍스트, 이미지, 오디오 또는 비디오를 1부터 10까지 평가하고, 점수와 함께 설정한 임계값에서 참/거짓이 바뀌는 불리언 값을 받습니다. 출력을 필터링하거나 정렬하는 데 사용할 수 있습니다. 예를 들어 점수가 7 이상인 이미지만 유지하고, `result`를 If/Else Switch 노드에 연결해 그 결과에 따라 동작하게 할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 사용할 모델입니다(기본값: `"gemini-decision-1"`). | COMBO | 예 | `"gemini-decision-1"` |
| `question` | 평가할 대상과 1과 10이 무엇을 의미하는지 설명합니다(기본값: "Rate the technical quality of the image from 1 (worst) to 10 (best)."). | STRING | 예 | 1~5000자 |
| `threshold` | `result`는 점수가 이 값 이상일 때 true가 됩니다. 깨끗하고 선명한 이미지는 약 7~8점, 심하게 손상된 이미지는 약 3~5점을 받습니다(기본값: 6.0). | FLOAT | 예 | 1.0 ~ 10.0 (단계: 0.1) |
| `images` | 평가할 이미지입니다. 확장 가능한 슬롯(`image_1` ... `image_16`)을 통해 최대 16개까지 지정할 수 있습니다. 배치된 이미지는 이미지당 한 번씩 집계됩니다. | IMAGE | 아니요 | 최대 16개 이미지 |
| `audio` | 평가할 오디오 클립입니다. | AUDIO | 아니요 | - |
| `video` | 평가할 비디오 클립입니다. | VIDEO | 아니요 | - |
| `text` | 질문의 대상이 되는 텍스트입니다. 예를 들어 프롬프트나 LLM 응답 등이며, 최대 20000자까지 가능합니다. | STRING | 아니요 | 최대 20000자 |

`text`, `images`, `audio`, `video` 중 최소 하나를 연결하세요. 평가할 대상이 없으면 노드에서 오류가 발생합니다. 이미지가 여러 개인 경우 질문 안에서 `image_1`, `image_2` 등으로 이름을 지정하세요.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `result` | 점수가 `threshold` 이상이면 true, 그렇지 않으면 false입니다. | BOOLEAN |
| `score` | 1부터 10까지의 평가 점수입니다. | FLOAT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionScore/ko.md)

---
**Source fingerprint (SHA-256):** `9b0a68cc7f29b1d4d23e23e051a008f34932aac6d1fe1a16e45a0e70b4df412f`
