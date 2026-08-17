# 모델 샘플링 (FLUX)

ModelSamplingFlux 노드는 이미지 크기를 기반으로 시프트 매개변수를 계산하여 주어진 모델에 Flux 모델 샘플링을 적용합니다. 지정된 너비, 높이 및 시프트 매개변수에 따라 모델의 동작을 조정하는 특수 샘플링 구성을 생성한 다음, 새 샘플링 설정이 적용된 수정된 모델을 반환합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | Flux 샘플링을 적용할 모델 | MODEL | 예 | - |
| `max_shift` | 샘플링 계산을 위한 최대 시프트 값 (기본값: 1.15) | FLOAT | 예 | 0.0 - 100.0 |
| `base_shift` | 샘플링 계산을 위한 기본 시프트 값 (기본값: 0.5) | FLOAT | 예 | 0.0 - 100.0 |
| `width` | 대상 이미지의 픽셀 단위 너비 (기본값: 1024) | INT | 예 | 16 - MAX_RESOLUTION |
| `height` | 대상 이미지의 픽셀 단위 높이 (기본값: 1024) | INT | 예 | 16 - MAX_RESOLUTION |

유효 시프트 값은 `width`와 `height`에서 파생된 잠재 크기를 기반으로 `base_shift`와 `max_shift` 사이에서 보간됩니다. `step` 값은 `max_shift`와 `base_shift`의 경우 0.01이며, `width`와 `height`의 경우 8입니다. `max_shift`와 `base_shift` 매개변수는 사용자 인터페이스에서 고급 옵션으로 표시됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | Flux 샘플링 구성이 적용된 수정된 모델 | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/ko.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`
