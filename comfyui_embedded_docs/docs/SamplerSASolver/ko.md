# SamplerSASolver

SamplerSASolver 노드는 확산 모델용 사용자 정의 샘플링 알고리즘을 구현합니다. 예측-보정(predictor-corrector) 접근 방식과 구성 가능한 차수 설정, 확률적 미분 방정식(SDE) 매개변수를 사용하여 입력 모델에서 샘플을 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 샘플링에 사용할 확산 모델 | MODEL | 예 | - |
| `eta` | 단계 크기 조정 계수를 제어합니다 (기본값: 1.0) | FLOAT | 아니요 | 0.0 - 10.0 |
| `sde_start_percent` | SDE 샘플링이 시작되는 노이즈 제거 프로세스의 시작 백분율로, 모델의 샘플링 일정을 사용하여 시그마 값으로 변환됩니다 (기본값: 0.2) | FLOAT | 아니요 | 0.0 - 1.0 |
| `sde_end_percent` | SDE 샘플링이 중지되는 노이즈 제거 프로세스의 종료 백분율로, 모델의 샘플링 일정을 사용하여 시그마 값으로 변환됩니다 (기본값: 0.8) | FLOAT | 아니요 | 0.0 - 1.0 |
| `s_noise` | 샘플링 중 추가되는 노이즈의 양을 제어합니다 (기본값: 1.0) | FLOAT | 아니요 | 0.0 - 100.0 |
| `predictor_order` | 솔버에서 예측기 구성 요소의 차수 (기본값: 3) | INT | 아니요 | 1 - 6 |
| `corrector_order` | 솔버에서 보정기 구성 요소의 차수 (기본값: 4) | INT | 아니요 | 0 - 6 |
| `use_pece` | PECE(Predict-Evaluate-Correct-Evaluate) 방법을 활성화 또는 비활성화합니다 | BOOLEAN | 아니요 | - |
| `simple_order_2` | 단순화된 2차 계산을 활성화 또는 비활성화합니다 | BOOLEAN | 아니요 | - |

참고: `model`을 제외한 모든 입력은 고급 매개변수이며, 노드 인터페이스에서 기본적으로 숨겨져 있습니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
|-------------|-------------|-----------|
| `sampler` | 확산 모델과 함께 사용할 수 있는 구성된 샘플러 객체 | SAMPLER |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/ko.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
