# HunyuanVideo15SuperResolution

HunyuanVideo15SuperResolution 노드는 비디오 초고해상도 프로세스를 위한 컨디셔닝 데이터를 준비합니다. 이 노드는 비디오의 잠재(latent) 표현과 선택적 시작 이미지를 받아서, 노이즈 증강 값 및 선택적 CLIP 비전 데이터와 함께 패키징하여 모델이 더 높은 해상도의 출력을 생성하는 데 사용할 수 있는 형식으로 만듭니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 연결된 잠재(latent) 및 노이즈 증강 데이터로 수정할 포지티브 컨디셔닝 입력입니다. | CONDITIONING | 예 | N/A |
| `negative` | 연결된 잠재(latent) 및 노이즈 증강 데이터로 수정할 네거티브 컨디셔닝 입력입니다. | CONDITIONING | 예 | N/A |
| `vae` | 선택적 `start_image`를 인코딩하는 데 사용되는 VAE입니다. `start_image`가 제공되는 경우 필수입니다. | VAE | 아니오 | N/A |
| `start_image` | 초고해상도 프로세스를 안내하는 선택적 시작 이미지입니다. 제공된 경우 업스케일링되고 `vae`로 인코딩된 후 컨디셔닝 잠재(latent)의 시작 부분에 배치됩니다. | IMAGE | 아니오 | N/A |
| `clip_vision_output` | 선택적 CLIP 비전 임베딩입니다. 제공된 경우 포지티브 및 네거티브 컨디셔닝 모두에 추가됩니다. | CLIP_VISION_OUTPUT | 아니오 | N/A |
| `latent` | 컨디셔닝에 통합할 잠재 비디오 표현입니다. | LATENT | 예 | N/A |
| `noise_augmentation` | 컨디셔닝에 적용할 노이즈 증강의 강도입니다(기본값: 0.70). 고급 매개변수입니다. | FLOAT | 예 | 0.0 - 1.0 (step 0.01) |

**참고:** `start_image`를 제공하는 경우 인코딩을 위해 `vae`도 연결해야 합니다. `start_image`는 입력 `latent`에 의해 암시된 치수에 맞게 자동으로 업스케일링되며, VAE는 첫 번째 세 개의 색상 채널(RGB)만 사용합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 연결된 잠재(latent), 노이즈 증강 및 선택적 CLIP 비전 데이터를 포함하는 수정된 포지티브 컨디셔닝입니다. | CONDITIONING |
| `negative` | 연결된 잠재(latent), 노이즈 증강 및 선택적 CLIP 비전 데이터를 포함하는 수정된 네거티브 컨디셔닝입니다. | CONDITIONING |
| `latent` | 변경 없이 그대로 전달되는 입력 잠재(latent)입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/ko.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
