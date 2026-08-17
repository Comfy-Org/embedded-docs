# VOIDSampler

## 개요

VOIDSampler 노드는 VOID 인페인팅 모델을 위해 특별히 설계된 전문화된 DDIM 샘플링 방법을 제공합니다. 이 노드는 표준 KSampler가 적용하는 노이즈 스케일링 없이 VOID 모델 훈련 중에 사용된 것과 동일한 노이즈 제거 프로세스를 구현합니다. 이 노드는 SamplerCustom 또는 SamplerCustomAdvanced 노드와 함께 사용하도록 설계되었으며, RandomNoise 또는 VOIDWarpedNoiseSource와 함께 사용해야 합니다.

## 입력

이 노드는 구성 가능한 입력 매개변수가 없습니다. 고정된 DDIM 샘플링 알고리즘을 적용하는 독립형 샘플러입니다.

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| *입력 없음* | 이 노드는 입력 매개변수를 허용하지 않습니다. | - | - | - |

참고: VOID 모델은 입력 표준 편차가 약 1인 알파 공간에서 작동하는 diffusers CogVideoXDDIMScheduler로 훈련되었습니다. 표준 KSampler는 약 4500배를 곱하는 노이즈 스케일링을 적용하므로 이 훈련과 호환되지 않습니다. VOIDSampler는 해당 스케일링을 건너뛰고 시그마-알파 변환을 사용하여 DDIM 업데이트 규칙을 직접 구현합니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `SAMPLER` | VOID DDIM 알고리즘을 구현하는 샘플러 객체로, SamplerCustom 또는 SamplerCustomAdvanced 노드에 연결할 준비가 되었습니다. | SAMPLER |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/ko.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
