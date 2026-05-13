> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/ko.md)

StableCascade_SuperResolutionControlnet 노드는 Stable Cascade 초고해상도 처리를 위한 입력값을 준비합니다. 입력 이미지를 받아 VAE를 사용하여 인코딩함으로써 컨트롤넷 입력을 생성하고, 동시에 Stable Cascade 파이프라인의 스테이지 C와 스테이지 B를 위한 플레이스홀더 잠재 표현을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | 초고해상도 처리를 위한 입력 이미지 |
| `vae` | VAE | 예 | - | 입력 이미지를 인코딩하는 데 사용되는 VAE 모델 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `controlnet_input` | IMAGE | 컨트롤넷 입력에 적합하도록 인코딩된 이미지 표현 |
| `stage_c` | LATENT | Stable Cascade 처리의 스테이지 C를 위한 플레이스홀더 잠재 표현 |
| `stage_b` | LATENT | Stable Cascade 처리의 스테이지 B를 위한 플레이스홀더 잠재 표현 |

---
**Source fingerprint (SHA-256):** `78b6e5a02c48ac37a205ef9d8532a3aca19134de4ec7be98b2ee55969dab7b53`
