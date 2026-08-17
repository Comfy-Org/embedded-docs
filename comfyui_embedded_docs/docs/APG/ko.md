# 적응형 투사 가이던스

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model` | 적응형 투영 가이던스를 적용할 확산 모델 | MODEL | 예 | - |
| `eta` | 평행 가이던스 벡터의 크기를 제어합니다. 설정값 1에서 기본 CFG 동작을 나타냅니다 (기본값: 1.0). | FLOAT | 예 | -10.0 ~ 10.0 |
| `norm_threshold` | 가이던스 벡터를 이 값으로 정규화합니다. 설정값 0에서는 정규화가 비활성화됩니다 (기본값: 5.0). | FLOAT | 예 | 0.0 ~ 50.0 |
| `momentum` | 확산 중 가이던스의 이동 평균을 제어합니다. 설정값 0에서는 비활성화됩니다 (기본값: 0.0). | FLOAT | 예 | -5.0 ~ 1.0 |

## Outputs

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | 적응형 투영 가이던스가 샘플링 프로세스에 적용된 수정된 모델을 반환합니다 | MODEL |

APG(Adaptive Projected Guidance) 노드는 확산 과정에서 가이던스가 적용되는 방식을 조정하여 샘플링 프로세스를 수정합니다. 이 노드는 가이던스 벡터를 조건부 출력에 대해 평행 및 직교 구성 요소로 분리하여 보다 통제된 이미지 생성을 가능하게 합니다. 또한 가이던스 크기 조정, 크기 정규화, 모멘텀 적용을 위한 매개변수를 제공하여 확산 단계 간 전환을 더 부드럽게 만듭니다.

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/APG/ko.md)

---
**Source fingerprint (SHA-256):** `df0c76aee28479d49c4e471e54d1d32082adc6921a6a50b506675144a79e018a`
