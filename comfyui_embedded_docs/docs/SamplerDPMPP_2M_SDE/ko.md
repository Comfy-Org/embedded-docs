# DPMPP_2M_SDE 샘플러

SamplerDPMPP_2M_SDE 노드는 확산 모델을 위한 DPM++ 2M SDE 샘플러를 생성합니다. 이 샘플러는 2차 다단계 솔버와 확률적 미분 방정식(SDE) 노이즈를 결합하여 샘플을 생성합니다. 또한 샘플링 과정을 제어할 수 있는 다양한 솔버 유형과 노이즈 처리 옵션을 제공합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `solver_type` | 샘플링 시 사용할 미분 방정식 솔버의 유형: "midpoint" 또는 "heun" (기본값: "midpoint") | COMBO | 예 | "midpoint"<br>"heun" |
| `eta` | 샘플링 과정에서 확률성(무작위성)의 양을 제어합니다 (기본값: 1.0) | FLOAT | 예 | 0.0 - 100.0 |
| `s_noise` | 샘플링 중 추가되는 노이즈의 양을 제어합니다 (기본값: 1.0) | FLOAT | 예 | 0.0 - 100.0 |
| `noise_device` | 노이즈 계산에 사용되는 장치입니다. "gpu"는 GPU에서 노이즈 생성을 수행하여 잠재적으로 더 빠른 성능을 제공하고, "cpu"는 CPU를 사용합니다 (기본값: "gpu") | COMBO | 예 | "gpu"<br>"cpu" |

참고: `noise_device`가 "cpu"로 설정되면 노드는 `dpmpp_2m_sde` 샘플러를 생성합니다. "gpu"로 설정되면 GPU에서 노이즈 관련 계산을 수행하는 `dpmpp_2m_sde_gpu` 변형을 생성합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `sampler` | 샘플링 파이프라인에서 사용할 준비가 된 구성된 샘플러 객체 | SAMPLER |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/ko.md)

---
**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`
