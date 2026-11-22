# TypeSafe Jev (Score)

The TypeSafe Jev (Score) 노드는 연결된 텍스트, 이미지 또는 둘 다를 1에서 10까지 평가하고 그 평가 점수를 임계값과 비교합니다. `result`를 If/Else Switch 노드에 연결하여 점수에 따라 동작하게 하거나, `score`를 읽어 원시 평가 점수를 사용할 수 있습니다. 이 노드는 API 노드이며 Comfy.org 계정과 API 키가 필요합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 사용할 Jev 모델입니다. 현재 사용 가능한 모델은 `jev-1.14.0` 하나뿐입니다. | COMBO | 예 | `"jev-1.14.0"` |
| `question` | 1에서 10까지의 척도로 평가할 내용입니다. 기본값처럼 1과 10이 무엇을 의미하는지 명시하세요(기본값: `Rate the technical quality of the image from 1 (worst) to 10 (best).`). | STRING | 예 | 1~1000자 |
| `threshold` | `result`는 점수가 이 값 이상일 때 true입니다(기본값: 5.0). | FLOAT | 예 | 1.0 ~ 10.0 (단계: 0.1) |
| `images` | 질문의 대상이 되는 이미지입니다. 총 최대 32개 이미지까지 지원하며, 배치 입력은 이미지마다 한 번씩 계산되고, 4개를 초과하는 이미지는 더 작은 크기로 전송됩니다. | AUTOGROW | 아니요 | 0~32개 이미지 |
| `text` | 질문의 대상이 되는 텍스트입니다. 예를 들어 프롬프트나 LLM 응답 등이 있습니다. | STRING | 아니요 | 0~3000자 |

**참고:**

- 텍스트 또는 최소 하나의 이미지를 연결해야 하며, 둘 다 비어 있으면 노드에서 오류가 발생합니다.
- 점수는 1에서 10까지 보고되며, 점수가 `threshold` 이상이면 `result`가 true입니다.
- 청구는 토큰 기반이며, 노드의 가격 배지는 100만 토큰당 대략적인 요율을 표시합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `result` | `score`가 `threshold` 이상일 때 true입니다. | BOOLEAN |
| `score` | 1(최악)에서 10(최고)까지의 평가 점수입니다. | FLOAT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevScore/ko.md)

---
**Source fingerprint (SHA-256):** `7e1970e903d2099ab3d7481a758c5291e87614b9eaf116d0ced6a1bcd36dc126`
