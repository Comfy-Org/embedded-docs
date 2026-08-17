# AlignYourSteps 스케쥴러

AlignYourStepsScheduler 노드는 다양한 확산 모델 유형에 대해 노이즈 제거 과정에서 사용되는 시그마 값을 생성합니다. 선택된 모델에 대한 기본 노이즈 수준을 선택하고, `denoise` 설정에 따라 단계 수를 조정하며, 0으로 끝나는 시그마 값 텐서를 반환합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model_type` | 기본 노이즈 수준을 선택하는 데 사용되는 모델 유형입니다 (기본값: "SD1") | COMBO | 예 | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `steps` | 생성할 총 샘플링 단계 수입니다 (기본값: 10) | INT | 예 | 1 to 10000 |
| `denoise` | 샘플링 프로세스의 사용 정도를 제어합니다: 1.0은 모든 단계를 사용하고, 낮은 값은 더 적은 단계를 사용하며, 0.0은 빈 시그마 텐서를 반환합니다 (기본값: 1.0) | FLOAT | 예 | 0.0 to 1.0 |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `sigmas` | 노이즈 제거 과정에 대해 계산된 시그마 값입니다. `denoise`가 0.0이면 빈 텐서가 반환됩니다. | SIGMAS |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/ko.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`
