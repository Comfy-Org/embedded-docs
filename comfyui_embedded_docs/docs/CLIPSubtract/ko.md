CLIPSubtract 노드는 두 개의 CLIP 모델 간의 뺄셈 연산을 수행합니다. 첫 번째 CLIP 모델을 기준으로 삼아 두 번째 CLIP 모델의 주요 패치를 차감하며, 선택적 승수를 통해 뺄셈 강도를 조절할 수 있습니다. 이를 통해 한 모델의 특정 특성을 다른 모델을 사용하여 제거함으로써 미세 조정된 모델 혼합이 가능합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 입력 형태 | 기본값 | 범위 |
| --- | --- | --- | --- | --- | --- |
| `clip1` | 수정될 기준 CLIP 모델입니다 | CLIP | 필수 | - | - |
| `clip2` | 기준 모델에서 주요 패치가 차감될 CLIP 모델입니다 | CLIP | 필수 | - | - |
| `multiplier` | 뺄셈 연산의 강도를 제어합니다. 양수 값은 clip2의 특성을 차감하고, 음수 값은 특성을 추가합니다. | FLOAT | 필수 | 1.0 | -10.0 ~ 10.0, 간격 0.01 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `CLIP` | 뺄셈 연산 후 생성된 결과 CLIP 모델입니다 | CLIP |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSubtract/ko.md)

---
**Source fingerprint (SHA-256):** `ea7b6f838d6eb083d2d9bc07891b6ef2f3e625861ab1de9279df351e58f2a2a8`
