# CLIP 병합 (빼기)

CLIPMergeSubtract 노드는 한 모델의 가중치를 다른 모델에서 빼서 두 CLIP 모델을 병합합니다. 첫 번째 모델을 복제한 다음 두 번째 모델의 키 패치를 빼서 새 CLIP 모델을 생성하며, 감산 강도를 제어하기 위해 조정 가능한 승수를 사용합니다. 이를 통해 기본 모델에서 특정 특성을 제거하여 세밀하게 모델을 혼합할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `clip1` | 복제 및 수정될 기본 CLIP 모델입니다. | CLIP | 예 | - |
| `clip2` | 기본 모델에서 뺄 키 패치를 가진 CLIP 모델입니다. | CLIP | 예 | - |
| `multiplier` | 감산 연산의 강도를 제어합니다. (기본값: 1.0) | FLOAT | 예 | -10.0 to 10.0 (step: 0.01) |

**참고:** 이 노드는 승수 값과 관계없이 `.position_ids` 및 `.logit_scale` 매개변수를 감산 연산에서 제외합니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `clip` | 첫 번째 모델에서 두 번째 모델의 가중치를 뺀 결과인 CLIP 모델입니다. | CLIP |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/ko.md)

---
**Source fingerprint (SHA-256):** `62a8cf719c34d9e2b7321f6eeb03c881f0767fd36b80e25e74feff4c0a29045e`
