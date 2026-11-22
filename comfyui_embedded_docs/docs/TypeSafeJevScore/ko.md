# TypeSafe Jev (Score)

TypeSafe Jev (Score) 노드는 연결된 텍스트, 이미지 또는 둘 모두를 1~10점으로 평가하고 그 점수를 임계값과 비교합니다. 점수에 따라 동작하도록 `result`를 If/Else Switch 노드에 연결하거나, 원래 평가 점수를 사용하려면 `score`를 읽으세요. 이 노드는 API 노드입니다. Comfy 서버에서 실행되며 크레딧이 있는 Comfy.org 계정이 필요합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 사용할 Jev 모델입니다. 현재 사용 가능한 모델은 `jev-1.14.0` 하나뿐입니다. | COMBO | 예 | `"jev-1.14.0"` |
| `question` | 평가할 내용을 1~10 척도로 작성합니다. 기본값(기본값: `Rate the technical quality of the image from 1 (worst) to 10 (best).`)처럼 1과 10이 의미하는 바를 명시하세요. | STRING | 예 | 1~1000자 |
| `threshold` | 점수가 이 값 이상이면 `result`가 true가 됩니다(기본값: 5.0). | FLOAT | 예 | 1.0 ~ 10.0 (단계: 0.1) |
| `images` | 질문의 대상이 되는 이미지입니다. 총 최대 32개 이미지이며, 배치 입력은 이미지당 한 번으로 계산됩니다. 모든 이미지의 긴 변은 전체 이미지 수에 따라 제한됩니다. 최대 4개 이미지의 경우 1568픽셀, 최대 8개는 1024픽셀, 최대 16개는 768픽셀, 최대 32개는 512픽셀입니다. 따라서 배치가 클수록 각 이미지의 세부 묘사가 줄어듭니다. | AUTOGROW | 아니요 | 0~32개 이미지 |
| `text` | 질문의 대상이 되는 텍스트입니다. 예: 프롬프트 또는 LLM 응답. | STRING | 아니요 | 0~3000자 |

**참고:**

- 텍스트 또는 이미지 중 하나 이상을 연결하세요. 둘 다 비어 있으면 노드에서 오류가 발생합니다.
- 점수는 1에서 10까지로 보고되며, 점수가 `threshold` 이상이면 `result`가 true가 됩니다.
- 요금은 토큰 기반으로 청구되며, 노드의 가격 배지에는 100만 토큰당 대략적인 요금이 표시됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `result` | `score`가 `threshold` 이상일 때 true입니다. | BOOLEAN |
| `score` | 1(최악)에서 10(최고)까지의 평가 점수입니다. | FLOAT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevScore/ko.md)

---
**Source fingerprint (SHA-256):** `7e1970e903d2099ab3d7481a758c5291e87614b9eaf116d0ced6a1bcd36dc126`
