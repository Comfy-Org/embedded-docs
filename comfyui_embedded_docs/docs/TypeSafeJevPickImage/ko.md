# TypeSafe Jev (Pick Image)

TypeSafe Jev (Pick Image) 노드는 배치에서 이미지 하나를 선택합니다. 동일한 이미지 배치를 `index`와 함께 Get Image from Batch에 연결하여 선택된 이미지를 유지하거나, `confidence`를 읽어 선택이 충분히 좋은지 판단할 수 있습니다. 이 노드는 API 노드입니다. Comfy 서버에서 실행되며 크레딧이 있는 Comfy.org 계정이 필요합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 사용할 Jev 모델입니다. 현재 사용 가능한 모델은 `jev-1.14.0` 하나뿐입니다. | COMBO | 예 | `"jev-1.14.0"` |
| `question` | 선택할 이미지를 지정합니다. 프롬프트를 `text`에 연결하면 가장 잘 일치하는 이미지를 선택합니다(기본값: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | 예 | 1~1000자 |
| `images` | 선택 대상 이미지입니다. 배치 입력은 이미지마다 한 번씩 계산되므로 배치의 모든 이미지가 후보가 됩니다. 업로드 전 모든 이미지의 긴 변은 배치 크기에 따라 제한됩니다. 최대 4개 이미지는 1568px, 최대 8개는 1024px, 최대 16개는 768px, 최대 32개는 512px이므로, 배치가 클수록 모든 이미지의 세부 묘사가 줄어들 수 있습니다. | IMAGE | 예 | 2~32개 이미지 |
| `text` | 질문의 대상이 되는 텍스트입니다. 예를 들어 이미지를 생성할 때 사용한 프롬프트입니다. | STRING | 아니요 | 0~3000자 |

**참고:**

- 이미지가 2개 미만이거나 32개 초과로 연결되면 노드에서 오류가 발생합니다.
- `index`는 0부터 계산되며, 이는 Get Image from Batch가 기대하는 위치입니다.
- 요금은 토큰 기반으로 청구되며, 노드의 가격 배지에는 100만 토큰당 대략적인 요율이 표시됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `index` | 선택된 이미지의 배치 내 위치이며 0부터 시작합니다. | INT |
| `confidence` | Jev가 얼마나 확신하는지를 나타내며, 0(명확한 최선의 선택 없음)에서 1(확실함)까지입니다. | FLOAT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/ko.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
