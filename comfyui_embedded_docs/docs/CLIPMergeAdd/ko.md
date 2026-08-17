# CLIP 병합 (더하기)

CLIPMergeAdd 노드는 두 CLIP 모델을 결합하여 첫 번째 모델에 두 번째 모델의 패치를 추가합니다. 첫 번째 CLIP 모델의 복사본을 생성하고, position ID 및 logit scale 매개변수를 제외한 두 번째 모델의 핵심 패치를 선택적으로 통합합니다. 이를 통해 기본 모델의 구조를 유지하면서 CLIP 모델 구성 요소를 병합할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `clip1` | 복제되어 병합의 기반으로 사용되는 기본 CLIP 모델입니다 | CLIP | 예 | - |
| `clip2` | 기본 모델에 추가할 핵심 패치를 제공하는 보조 CLIP 모델입니다 | CLIP | 예 | - |

참고: `clip2`의 핵심 패치는 강도 1.0으로 추가됩니다. `.position_ids` 또는 `.logit_scale`로 끝나는 키는 병합에서 제외됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `CLIP` | 기본 모델 구조에 보조 모델의 패치가 추가된 병합된 CLIP 모델입니다 | CLIP |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/ko.md)

---
**Source fingerprint (SHA-256):** `e6271ea9139598eb580f79ce63ff5d92307d7ed93f57cdc666c5e022b671a0dd`
