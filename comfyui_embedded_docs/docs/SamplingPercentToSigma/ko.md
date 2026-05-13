> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/ko.md)

# SamplingPercentToSigma (샘플링 백분율-시그마 변환)

SamplingPercentToSigma 노드는 샘플링 백분율 값을 모델의 샘플링 매개변수를 사용하여 해당 시그마 값으로 변환합니다. 0.0에서 1.0 사이의 백분율 값을 입력받아 모델의 노이즈 스케줄에서 적절한 시그마 값으로 매핑하며, 경계값에서 계산된 시그마 또는 실제 최대/최소 시그마 값을 반환하는 옵션을 제공합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | 변환에 사용되는 샘플링 매개변수를 포함한 모델 |
| `sampling_percent` | FLOAT | 예 | 0.0 ~ 1.0 | 시그마로 변환할 샘플링 백분율 (기본값: 0.0) |
| `return_actual_sigma` | BOOLEAN | 예 | - | 구간 확인에 사용되는 값 대신 실제 시그마 값을 반환합니다. 이는 0.0 및 1.0에서의 결과에만 영향을 미칩니다. (기본값: False) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `sigma_value` | FLOAT | 입력 샘플링 백분율에 해당하는 변환된 시그마 값 |

---
**Source fingerprint (SHA-256):** `88ecea0528dfeff75248a8dfee8381e1f73d1a2d9ee3e7f8e37fef0f2b2499ec`
