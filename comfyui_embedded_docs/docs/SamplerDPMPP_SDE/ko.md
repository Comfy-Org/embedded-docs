# DPMPP_SDE 샘플러

SamplerDPMPP_SDE 노드는 샘플링 프로세스에서 사용할 DPM++ SDE(확률 미분 방정식) 샘플러를 생성합니다. 이 샘플러는 구성 가능한 노이즈 매개변수와 장치 선택 기능을 갖춘 확률적 샘플링 방법을 제공합니다. 샘플링 파이프라인에서 사용할 수 있는 샘플러 객체를 반환합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `eta` | 샘플링 프로세스의 확률적 특성을 제어합니다 (기본값: 1.0) | FLOAT | 예 | 0.0 - 100.0 |
| `s_noise` | 샘플링 중에 추가되는 노이즈의 양을 제어합니다 (기본값: 1.0) | FLOAT | 예 | 0.0 - 100.0 |
| `r` | 샘플링 동작에 영향을 주는 매개변수입니다 (기본값: 0.5) | FLOAT | 예 | 0.0 - 100.0 |
| `noise_device` | 노이즈 계산이 수행되는 장치를 선택합니다 (기본값: "gpu"). "cpu"로 설정하면 표준 `dpmpp_sde` 샘플러가 사용되고, "gpu"로 설정하면 `dpmpp_sde_gpu` 샘플러가 사용됩니다. | COMBO | 예 | "gpu"<br>"cpu" |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `sampler` | 샘플링 파이프라인에서 사용할 수 있도록 구성된 DPM++ SDE 샘플러 객체를 반환합니다 | SAMPLER |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/ko.md)

---
**Source fingerprint (SHA-256):** `56949712f245abfcc48c09d7d14a1a7778e80ba58535e538484c382d7e0d02c6`
