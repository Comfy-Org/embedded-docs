# StableCascade 초고해상도 컨트롤넷

StableCascade_SuperResolutionControlnet 노드는 Stable Cascade 초고해상도 처리를 위한 입력을 준비합니다. 입력 이미지를 받아 VAE로 인코딩하여 controlnet 입력을 생성하고, 동시에 Stable Cascade 파이프라인의 스테이지 C와 스테이지 B를 위한 플레이스홀더 잠재 표현을 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `image` | 초고해상도 처리를 위해 사용될 입력 이미지입니다. | IMAGE | 예 | - |
| `vae` | 입력 이미지를 인코딩하는 데 사용되는 VAE 모델입니다. | VAE | 예 | - |

참고: VAE로 인코딩할 때 입력 이미지의 처음 세 개의 색상 채널만 사용됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `controlnet_input` | controlnet 입력에 적합한 인코딩된 이미지 표현입니다. | IMAGE |
| `stage_c` | Stable Cascade 처리의 스테이지 C를 위한 플레이스홀더 잠재 표현이며, 입력 이미지 크기를 16으로 나눈 차원을 갖습니다. | LATENT |
| `stage_b` | Stable Cascade 처리의 스테이지 B를 위한 플레이스홀더 잠재 표현이며, 입력 이미지 크기를 2로 나눈 차원을 갖습니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/ko.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
