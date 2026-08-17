# 엡실론 스케일링

이 노드는 연구 논문 "Elucidating the Exposure Bias in Diffusion Models" (arxiv.org/abs/2308.15321v6)의 엡실론 스케일링(Epsilon Scaling) 방법을 구현합니다. 이 방법은 샘플링 과정에서 예측된 노이즈를 스케일링하여 노출 편향(exposure bias)을 줄이는 데 도움을 주며, 이를 통해 생성된 이미지의 품질이 향상될 수 있습니다. 이 구현은 실용성과 효율성 때문에 논문에서 권장하는 "균일 스케줄(uniform schedule)"을 사용합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 엡실론 스케일링 패치가 적용될 모델입니다. | MODEL | 예 | - |
| `scaling_factor` | 예측된 노이즈가 스케일링되는 계수입니다. 1.0보다 큰 값은 예측된 노이즈를 줄이고, 1.0보다 작은 값은 노이즈를 증가시킵니다 (기본값: 1.005). | FLOAT | 예 | 0.5 - 1.5 (step: 0.001) |

참고: `scaling_factor`는 0으로 나누는 것을 방지하기 위해 값이 0이 되지 않도록 보호됩니다. UI는 최소값을 0.5로 강제하므로 정상적인 사용에서는 이 문제가 발생할 수 없습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | 입력 모델의 샘플링 과정에 엡실론 스케일링 함수가 적용된 패치된 복사본입니다. 원본 모델은 수정되지 않습니다. | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/ko.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`
