# 모델 샘플링 (연속 V)

ModelSamplingContinuousV 노드는 연속 V-예측 샘플링 매개변수를 적용하여 모델의 샘플링 동작을 수정합니다. 입력 모델의 복제본을 생성하고 고급 샘플링 제어를 위한 사용자 정의 시그마 범위 설정으로 구성합니다. 이를 통해 사용자는 특정 최소 및 최대 시그마 값으로 샘플링 프로세스를 미세 조정할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 연속 V-예측 샘플링으로 수정할 입력 모델 | MODEL | 예 | - |
| `sampling` | 적용할 샘플링 방법. 현재는 V-예측만 지원됩니다. | COMBO | 예 | `"v_prediction"` |
| `sigma_max` | 샘플링에 사용할 최대 시그마 값 (기본값: 500.0) | FLOAT | 예 | 0.0 – 1000.0 (단계 0.001) |
| `sigma_min` | 샘플링에 사용할 최소 시그마 값 (기본값: 0.03) | FLOAT | 예 | 0.0 – 1000.0 (단계 0.001) |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | 연속 V-예측 샘플링이 적용된 수정된 모델 | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/ko.md)

---
**Source fingerprint (SHA-256):** `8549be9dd2375374c20da7c74a756a90285716db0e52fed8a1a2b753cd6d75fe`
