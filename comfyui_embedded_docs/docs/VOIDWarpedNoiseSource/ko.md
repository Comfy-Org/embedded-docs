# VOIDWarpedNoiseSource

## 개요

이 노드는 LATENT(예: VOIDWarpedNoise 노드의 출력)를 NOISE 소스로 변환합니다. 이를 통해 왜곡된 노이즈를 SamplerCustomAdvanced 노드와 함께 사용하여 보다 정밀하게 제어된 이미지를 생성할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `warped_noise` | VOIDWarpedNoise의 왜곡된 노이즈 잠재 | LATENT | 예 | N/A |

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `NOISE` | SamplerCustomAdvanced와 함께 사용할 수 있는 노이즈 소스 | NOISE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/ko.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
