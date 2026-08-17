# TripoSplat 컨디셔닝

이 노드는 DINOv3 비전 인코더와 Flux2 VAE를 사용하여 입력 이미지를 인코딩하고, TripoSplat 모델을 위한 positive 및 negative 컨디셔닝 데이터를 생성합니다. 또한 KSampler의 시작점으로 사용되는 고정 크기 노이즈 대상(잠재(latent) 시퀀스 및 카메라 토큰)을 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | DINOv3 ViT-H/16+ 이미지 인코더 | CLIP_VISION | 예 | - |
| `vae` | Flux2 VAE | VAE | 예 | - |
| `image` | 인코딩할 입력 이미지 | IMAGE | 예 | - |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `positive` | DINOv3 이미지 특징과 입력 이미지의 Flux2 VAE 잠재(latent)를 포함하는 positive 컨디셔닝 데이터 | CONDITIONING |
| `negative` | 0으로 채워진 DINOv3 특징과 0으로 채워진 Flux2 VAE 잠재(latent)를 포함하는 negative 컨디셔닝 데이터 | CONDITIONING |
| `latent` | KSampler용 고정 크기 노이즈 대상(잠재(latent) + 카메라) | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/ko.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
