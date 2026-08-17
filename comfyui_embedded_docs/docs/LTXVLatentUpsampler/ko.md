# LTXVLatentUpsampler

LTXVLatentUpsampler 노드는 비디오 잠재 표현의 공간 해상도를 2배로 증가시킵니다. 이 노드는 전용 업스케일 모델을 사용하여 잠재 데이터를 처리하며, 해당 잠재 데이터는 먼저 비정규화된 후 제공된 VAE의 채널 통계를 사용하여 다시 정규화됩니다. 이 노드는 잠재 공간 내의 비디오 워크플로우를 위해 설계되었습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `samples` | 업스케일할 비디오의 입력 잠재 표현입니다. | LATENT | 예 |  |
| `upscale_model` | 잠재 데이터에 2배 업스케일링을 수행하는 데 사용되는 로드된 모델입니다. | LATENT_UPSCALE_MODEL | 예 |  |
| `vae` | 업스케일링 전에 입력 잠재를 비정규화하고 이후에 출력 잠재를 정규화하는 데 사용되는 VAE 모델입니다. | VAE | 예 |  |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `LATENT` | 입력과 비교하여 공간 차원이 2배로 증가된 업스케일된 잠재 표현입니다. 출력 잠재는 입력과 동일한 배치 크기, 채널 수 및 시간 길이를 가지며, 입력 잠재와 동일한 데이터 타입으로 다시 변환됩니다. 입력에 `noise_mask`가 포함된 경우 출력에서 제거됩니다. | LATENT |

참고: 이 노드는 실험 단계로 표시되어 있습니다.

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/ko.md)

---
**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`
