# TypeSafe Jev (Yes/No)

TypeSafe Jev (예/아니오) 노드는 연결된 텍스트, 이미지 또는 둘 다에 대해 예/아니오 질문을 하고 답변을 불리언으로 반환합니다. `result`를 If/Else Switch 노드에 연결하여 워크플로를 분기하거나, `probability`를 읽어 모델이 얼마나 확신하는지에 따라 동작할 수 있습니다. 이 노드는 API 노드입니다. Comfy 서버에서 실행되며 크레딧이 있는 Comfy.org 계정이 필요합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 사용할 Jev 모델입니다. 현재 사용 가능한 모델은 `jev-1.14.0` 하나뿐입니다. | COMBO | 예 | `"jev-1.14.0"` |
| `question` | 연결된 텍스트와 이미지가 답할 예/아니오 질문입니다. '예'일 때 실행하려는 상황이 되도록 질문하세요. 이미지 소켓이 여러 개인 경우 해당 이름을 사용하세요. 예: `Does image_2 show the same person as image_1?` (기본값: `Is there a person in the image?`). | STRING | 예 | 1~1000자 |
| `threshold` | 예일 확률이 이 값 이상이면 답은 '예'입니다 (기본값: 0.5). | FLOAT | 예 | 0.01 ~ 0.99 (단계: 0.01) |
| `images` | 질문의 대상이 되는 이미지입니다. 총 최대 32개 이미지까지 가능하며, 배치 입력은 이미지당 한 번씩 계산됩니다. 모든 이미지의 긴 변은 총 이미지 수에 따라 제한됩니다. 최대 4개 이미지의 경우 1568px, 최대 8개는 1024px, 최대 16개는 768px, 최대 32개는 512px이므로, 배치가 클수록 각 이미지의 세부 묘사가 줄어듭니다. | AUTOGROW | 아니오 | 0~32개 이미지 |
| `text` | 질문의 대상이 되는 텍스트입니다. 프롬프트나 LLM 응답 등이 해당합니다. | STRING | 아니오 | 0~3000자 |

**참고:**

- 텍스트 또는 이미지를 하나 이상 연결하세요. 둘 다 비어 있으면 노드에서 오류가 발생합니다.
- `probability`가 `threshold` 이상이면 `result`는 true이고, `answer`는 동일한 판정을 `yes` 또는 `no`로 반환합니다.
- 과금은 토큰 기반입니다. 노드의 가격 배지는 100만 토큰당 대략적인 요금을 보여줍니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `result` | 불리언 형태의 답변입니다. 예일 확률이 `threshold` 이상이면 true입니다. | BOOLEAN |
| `answer` | `yes` 또는 `no` 텍스트 형태의 답변입니다. | STRING |
| `probability` | 예일 확률로, 0(확실히 아니오)에서 1(확실히 예)까지입니다. | FLOAT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/ko.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
