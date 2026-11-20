# Google Gemini Decision (Yes/No)

연결한 텍스트, 이미지, 오디오 또는 비디오에 대해 예/아니오 질문을 던지고, 라우팅에 사용할 불리언 값을 받습니다. `result`를 If/Else Switch 노드에 연결하면 실행을 두 경로 중 하나로 보낼 수 있으며, 모델이 그렇게 답한 이유를 확인하고 싶을 때는 `answer`와 `probability`를 읽으면 됩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 사용할 모델입니다(기본값: `"gemini-decision-1"`). | COMBO | 예 | `"gemini-decision-1"` |
| `question` | 연결된 대상에 대한 예/아니오 질문으로, 최대 5000자까지 입력할 수 있습니다. "예"가 곧 처리하려는 상황이 되도록 질문을 작성하십시오(기본값: "Is there a person in the image?"). | STRING | 예 | 1~5000자 |
| `threshold` | `result`가 true가 되는 "예"의 확률입니다. 명확한 예 답변은 약 0.85~0.92의 점수를 받으므로, 0.9 이상으로 설정하면 그러한 답변 상당수가 거부됩니다(기본값: 0.5). | FLOAT | 예 | 0.01 ~ 0.99 (단계: 0.01) |
| `images` | 질문할 이미지로, 확장 가능한 슬롯(`image_1` ... `image_16`)에 걸쳐 최대 16개까지 지정할 수 있습니다. 배치된 이미지는 이미지마다 한 번씩 계산됩니다. | IMAGE | 아니요 | 최대 16개 이미지 |
| `audio` | 질문할 오디오 클립입니다. | AUDIO | 아니요 | - |
| `video` | 질문할 비디오 클립입니다. | VIDEO | 아니요 | - |
| `text` | 질문의 대상이 되는 텍스트로, 프롬프트나 LLM 응답 등이 해당되며 최대 20000자까지 입력할 수 있습니다. | STRING | 아니요 | 최대 20000자 |

`text`, `images`, `audio`, `video` 중 최소 하나를 연결해야 하며, 살펴볼 대상이 없으면 노드에서 오류가 발생합니다. 이미지가 여러 개인 경우 질문 안에서 각 이미지를 `image_1`, `image_2` 등으로 지칭하십시오.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `result` | 불리언으로 표현된 답변으로, "예"이면 true, "아니오"이면 false입니다. | BOOLEAN |
| `answer` | 문자열 `"yes"` 또는 `"no"`로 표현된 답변입니다. | STRING |
| `probability` | 0과 1 사이의 "예"일 확률입니다. | FLOAT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionYesNo/ko.md)

---
**Source fingerprint (SHA-256):** `0339031baf5648609b82526bed97ce8744986878bcbb706dcd3aa79a7370d83f`
