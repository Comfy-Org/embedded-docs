# TypeSafe Jev (Choice)

TypeSafe Jev (Choice) 노드는 연결된 텍스트, 이미지 또는 둘 다에 대해 사용자 지정 옵션 중 하나를 선택합니다. `choice`를 옵션 이름이 입력으로 전달되는 Branch 노드에 연결하거나, `option_index`를 사용하여 선택된 옵션의 위치를 기준으로 전환할 수 있습니다. 이 노드는 API 노드이며 Comfy.org 계정과 API 키가 필요합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 사용할 Jev 모델입니다. 현재 사용 가능한 모델은 `jev-1.14.0` 하나뿐입니다. | COMBO | 예 | `"jev-1.14.0"` |
| `question` | 옵션들이 답하는 질문입니다. 이미지 소켓이 여러 개인 경우 해당 이름을 사용하십시오. 예: `Which season is shown in image_1?` (기본값: `What style is the image?`). | STRING | 예 | 1~1000자 |
| `options` | 선택할 옵션으로, 한 줄에 하나씩 입력합니다. 어느 옵션에도 해당하지 않는 입력을 위해 `other`와 같은 옵션을 추가하십시오(기본값: `photo`, `illustration`, `3d render`, `anime`, `sketch` 및 `other`, 한 줄에 하나씩). | STRING | 예 | 2~50개 옵션, 각 최대 40자 |
| `images` | 질문의 대상이 되는 이미지입니다. 총 최대 32개 이미지까지 지원하며, 배치된 입력은 이미지마다 한 번씩 카운트되고, 4개를 초과하는 이미지는 더 작은 크기로 전송됩니다. | AUTOGROW | 아니요 | 0~32개 이미지 |
| `text` | 질문의 대상이 되는 텍스트로, 프롬프트나 LLM 응답 등이 있습니다. | STRING | 아니요 | 0~3000자 |

**참고:**

- 텍스트 또는 최소 하나의 이미지를 연결하십시오. 둘 다 비어 있으면 노드에서 오류가 발생합니다.
- 옵션이 2개 미만이거나 50개를 초과하는 경우, 옵션이 40자를 초과하는 경우, 또는 두 옵션이 대소문자만 다른 경우 노드에서 오류가 발생합니다.
- `option_index`는 0부터 계산하므로 목록의 첫 번째 옵션은 인덱스 0을 갖습니다.
- 요금은 토큰 기반으로 청구됩니다. 노드의 가격 배지는 1M 토큰당 대략적인 요율을 표시합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `choice` | 선택된 옵션으로, `options`에 표시된 것과 정확히 동일하게 기록됩니다. | STRING |
| `option_index` | 옵션 목록에서 선택된 옵션의 위치이며, 0부터 시작합니다. | INT |
| `confidence` | Jev가 얼마나 확신하는지를 나타내며, 0(명확한 선택 없음)부터 1(확실함)까지입니다. | FLOAT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/ko.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`
