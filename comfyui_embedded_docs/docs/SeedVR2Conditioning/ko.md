# SeedVR2 컨디셔닝 적용

이 노드는 SeedVR2 모델과 함께 사용하기 위해 VAE 잠재 변수에서 positive 및 negative 컨디셔닝을 구성합니다. 잠재 변수에 마스크 채널을 추가한 다음, 모델에 내장된 positive 및 negative 컨디셔닝 임베딩과 결합하여 샘플링에 필요한 컨디셔닝 값을 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | SeedVR2 모델입니다. | MODEL | 예 | - |
| `vae_conditioning` | 컨디셔닝을 구성할 VAE 잠재 변수입니다. 표시 이름: `latent`. | LATENT | 예 | - |

`vae_conditioning` 잠재 변수는 SeedVR2 VAE가 기대하는 채널 수를 가진 Comfy 채널 우선 레이아웃(B, C, T, H, W)의 5차원 텐서여야 합니다. 채널-마지막 레이아웃의 잠재 변수는 오류와 함께 거부됩니다. `model` 입력은 예상되는 내부 구조를 가진 유효한 SeedVR2 모델이어야 합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `positive` | 샘플링을 위한 positive 컨디셔닝입니다. | CONDITIONING |
| `negative` | 샘플링을 위한 negative 컨디셔닝입니다. | CONDITIONING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/ko.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
