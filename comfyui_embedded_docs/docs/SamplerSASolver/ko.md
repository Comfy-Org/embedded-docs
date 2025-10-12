> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/ko.md)

SamplerSASolver 노드는 확산 모델을 위한 사용자 정의 샘플링 알고리즘을 구현합니다. 예측자-수정자 접근법과 구성 가능한 차수 설정 및 확률적 미분방정식(SDE) 매개변수를 사용하여 입력 모델로부터 샘플을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | 샘플링에 사용할 확산 모델 |
| `eta` | FLOAT | 예 | 0.0 - 10.0 | 스텝 크기 스케일링 인자를 제어합니다 (기본값: 1.0) |
| `sde_start_percent` | FLOAT | 예 | 0.0 - 1.0 | SDE 샘플링의 시작 백분율 (기본값: 0.2) |
| `sde_end_percent` | FLOAT | 예 | 0.0 - 1.0 | SDE 샘플링의 종료 백분율 (기본값: 0.8) |
| `s_noise` | FLOAT | 예 | 0.0 - 100.0 | 샘플링 중 추가되는 노이즈의 양을 제어합니다 (기본값: 1.0) |
| `predictor_order` | INT | 예 | 1 - 6 | 솔버에서 예측자 구성 요소의 차수 (기본값: 3) |
| `corrector_order` | INT | 예 | 0 - 6 | 솔버에서 수정자 구성 요소의 차수 (기본값: 4) |
| `use_pece` | BOOLEAN | 예 | - | PECE (Predict-Evaluate-Correct-Evaluate) 방법을 활성화 또는 비활성화합니다 |
| `simple_order_2` | BOOLEAN | 예 | - | 단순화된 2차 계산을 활성화 또는 비활성화합니다 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 확산 모델과 함께 사용할 수 있는 구성된 샘플러 객체 |