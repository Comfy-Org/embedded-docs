# SV3D 조건 설정

SV3D_Conditioning 노드는 SV3D 모델을 사용하여 3D 비디오 생성을 위한 conditioning 데이터를 준비합니다. 초기 이미지를 받아 CLIP vision 및 VAE 인코더를 통해 처리하여 positive 및 negative conditioning과 함께 잠재 표현(latent representation)을 생성합니다. 이 노드는 지정된 비디오 프레임 수에 따라 다중 프레임 비디오 생성을 위한 카메라 고도(elevation) 및 방위각(azimuth) 시퀀스를 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | 입력 이미지를 인코딩하는 데 사용되는 CLIP 비전 모델입니다. | CLIP_VISION | 예 | - |
| `init_image` | 3D 비디오 생성의 시작점이 되는 초기 이미지입니다. | IMAGE | 예 | - |
| `vae` | 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델입니다. | VAE | 예 | - |
| `width` | 생성되는 비디오 프레임의 출력 너비입니다(기본값: 576, 8로 나누어 떨어져야 합니다). | INT | 예 | 16 ~ MAX_RESOLUTION (8씩 증가) |
| `height` | 생성되는 비디오 프레임의 출력 높이입니다(기본값: 576, 8로 나누어 떨어져야 합니다). | INT | 예 | 16 ~ MAX_RESOLUTION (8씩 증가) |
| `video_frames` | 비디오 시퀀스에 생성할 프레임 수입니다(기본값: 21). | INT | 예 | 1 ~ 4096 |
| `elevation` | 3D 뷰를 위한 카메라 고도 각도(도 단위)로, 모든 프레임에 적용됩니다(기본값: 0.0). | FLOAT | 예 | -90.0 ~ 90.0 (0.1씩 증가) |

참고: 카메라 방위각은 0도에서 시작하여 프레임당 360 / (video_frames - 1)도씩 증가하므로, 카메라는 시퀀스 전체에 걸쳐 객체 주위를 완전히 한 바퀴 공전합니다. 동일한 `elevation` 값이 모든 프레임에 적용됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `positive` | 생성에 사용되는 이미지 임베딩과 카메라 매개변수를 포함하는 positive conditioning 데이터입니다. | CONDITIONING |
| `negative` | 대비 생성을 위해 임베딩이 0으로 설정된 negative conditioning 데이터입니다. | CONDITIONING |
| `latent` | 지정된 비디오 프레임 수와 해상도에 맞는 차원을 가진 빈 latent 텐서입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/ko.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`
