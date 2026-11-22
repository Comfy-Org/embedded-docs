# TypeSafe Jev (Pick Image)

TypeSafe Jev (Pick Image) 노드는 배치에서 이미지 하나를 선택합니다. `index`를 Get Image from Batch에 연결하여 선택된 이미지를 유지하거나, `confidence`를 읽어 선택이 충분히 좋은지 판단할 수 있습니다. 이 노드는 API 노드이며 Comfy.org 계정과 API 키가 필요합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 사용할 Jev 모델입니다. 현재 사용 가능한 모델은 하나뿐입니다: `jev-1.14.0`. | COMBO | 예 | `"jev-1.14.0"` |
| `question` | 선택할 이미지를 지정합니다. 프롬프트를 `text`에 연결하면 해당 프롬프트와 가장 잘 일치하는 이미지를 선택합니다(기본값: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | 예 | 1~1000자 |
| `images` | 선택할 이미지입니다. 배치 입력은 이미지마다 한 번씩 계산되므로 배치의 모든 이미지가 후보가 됩니다. | IMAGE | 예 | 2~32개 이미지 |
| `text` | 질문의 대상이 되는 텍스트입니다. 예를 들어 이미지를 생성할 때 사용한 프롬프트입니다. | STRING | 아니요 | 0~3000자 |

**참고:**

- 이미지가 2개 미만이거나 32개 초과로 연결되면 노드에서 오류가 발생합니다.
- `index`는 0부터 시작하며, 이는 Get Image from Batch가 기대하는 위치입니다.
- 과금은 토큰 기반입니다. 노드의 가격 배지는 1M 토큰당 대략적인 요율을 표시합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `index` | 배치에서 선택된 이미지의 위치이며 0부터 시작합니다. | INT |
| `confidence` | Jev가 얼마나 확신하는지를 나타내며, 0(명확한 선택 없음)부터 1(확실함)까지입니다. | FLOAT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/ko.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
