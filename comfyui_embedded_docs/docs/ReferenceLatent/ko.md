# 참조 잠재

이 노드는 편집 모델의 가이드 잠재 변수를 설정합니다. 컨디셔닝 데이터와 선택적 잠재 입력을 받아 참조 잠재 정보를 포함하도록 컨디셔닝을 수정합니다. 모델이 지원하는 경우 여러 ReferenceLatent 노드를 연결하여 여러 참조 이미지를 설정할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `conditioning` | 참조 잠재 정보로 수정될 컨디셔닝 데이터입니다. | CONDITIONING | 예 | - |
| `latent` | 편집 모델의 참조로 사용할 선택적 잠재 데이터입니다. | LATENT | 아니요 | - |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `output` | 참조 잠재 정보를 포함하는 수정된 컨디셔닝 데이터입니다. | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/ko.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
