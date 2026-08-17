# SamplerLCM

SamplerLCM 노드는 단계별 노이즈 설정을 조정할 수 있는 LCM(Latent Consistency Model) 샘플러를 제공합니다. `s_noise` 매개변수는 모델의 학습 노이즈 스케일에 대한 승수 역할을 하며, 각 샘플링 단계에서 적용되는 노이즈를 세밀하게 제어할 수 있게 합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `s_noise` | 첫 번째 단계에서의 단계별 노이즈 승수(1.0 = 학습과 일치). 기본값: 1.0. | FLOAT | 예 | 0.0 to 64.0 (step: 0.01) |
| `s_noise_end` | 마지막 단계에서의 단계별 노이즈 승수. 일정한 스케줄을 위해 `s_noise`와 동일하게 설정합니다. 기본값: 1.0. | FLOAT | 예 | 0.0 to 64.0 (step: 0.01) |
| `noise_clip_std` | 단계별 노이즈를 +/- N*std 범위로 제한합니다. 0이면 비활성화됩니다. 기본값: 0.0. | FLOAT | 예 | 0.0 to 10.0 (step: 0.01) |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `SAMPLER` | 샘플링 워크플로우에서 바로 사용할 수 있도록 구성된 LCM 샘플러 객체입니다. | SAMPLER |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/ko.md)

---
**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`
