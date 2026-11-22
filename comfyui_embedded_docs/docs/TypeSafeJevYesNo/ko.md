# TypeSafe Jev (Yes/No)

The TypeSafe Jev (Yes/No) 노드는 연결된 텍스트, 이미지 또는 둘 모두에 대해 예/아니요 질문을 하고 답변을 불리언으로 반환합니다. `result`를 If/Else Switch 노드에 연결하여 워크플로를 라우팅하거나, `probability`를 읽어 모델이 얼마나 확신하는지에 따라 작업할 수 있습니다. 이 노드는 API 노드이며 Comfy.org 계정과 API 키가 필요합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 사용할 Jev 모델입니다. 현재 사용 가능한 모델은 하나뿐입니다: `jev-1.14.0`. | COMBO | 예 | `"jev-1.14.0"` |
| `question` | 연결된 텍스트와 이미지가 답할 예/아니요 질문입니다. '예'가 작업을 수행할 경우가 되도록 질문하세요. 여러 이미지 소켓이 있는 경우 해당 이름을 사용하세요. 예: `Does image_2 show the same person as image_1?` (기본값: `Is there a person in the image?`). | STRING | 예 | 1~1000자 |
| `threshold` | 예일 확률이 이 값 이상이면 답은 예가 됩니다 (기본값: 0.5). | FLOAT | 예 | 0.01 ~ 0.99 (단계: 0.01) |
| `images` | 질문의 대상이 되는 이미지입니다. 총 최대 32개 이미지까지 지원하며, 배치 입력은 이미지당 한 번으로 집계되고, 4개를 초과하는 이미지는 더 작은 크기로 전송됩니다. | AUTOGROW | 아니요 | 0~32개 이미지 |
| `text` | 질문의 대상이 되는 텍스트입니다. 예를 들어 프롬프트나 LLM 응답입니다. | STRING | 아니요 | 0~3000자 |

**참고:**

- 텍스트 또는 하나 이상의 이미지를 연결하세요. 둘 다 비어 있으면 노드에서 오류가 발생합니다.
- `result`는 `probability`가 `threshold` 이상일 때 true이며, `answer`는 동일한 판정을 `yes` 또는 `no`로 반환합니다.
- 과금은 토큰 기반이며, 노드의 가격 배지는 100만 토큰당 대략적인 요금을 표시합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `result` | 불리언 형태의 답변입니다. 예일 확률이 `threshold` 이상일 때 true입니다. | BOOLEAN |
| `answer` | `yes` 또는 `no` 텍스트 형태의 답변입니다. | STRING |
| `probability` | 예일 확률로, 0(확실히 아니요)부터 1(확실히 예)까지입니다. | FLOAT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/ko.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
