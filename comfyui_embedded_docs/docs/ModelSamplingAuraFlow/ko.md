# 모델 샘플링 (AuraFlow)

ModelSamplingAuraFlow 노드는 AuraFlow 모델 아키텍처를 위해 특별히 설계된 샘플링 구성을 확산 모델에 적용합니다. `shift` 매개변수를 적용하여 샘플링 분포를 조정함으로써 모델의 샘플링 동작을 수정합니다. 이 노드는 SD3 모델 샘플링 프레임워크에서 상속되며 샘플링 과정을 세밀하게 제어할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | AuraFlow 샘플링 구성을 적용할 확산 모델입니다. | MODEL | 예 | - |
| `shift` | 샘플링 분포에 적용할 시프트 값입니다. 기본값: 1.73. 단계: 0.01. | FLOAT | 예 | 0.0 - 100.0 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `model` | AuraFlow 샘플링 구성이 적용된 수정된 모델입니다. | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/ko.md)

---
**Source fingerprint (SHA-256):** `7ca35632ae73517c78aa31a528492427c9af37862322ff7335f895c597ee1709`
