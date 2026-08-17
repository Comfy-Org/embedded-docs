# StableZero123 조건 설정

StableZero123_Conditioning 노드는 입력 이미지와 카메라 각도를 처리하여 3D 모델 생성을 위한 컨디셔닝 데이터와 잠재 표현을 생성합니다. CLIP 비전 모델을 사용하여 이미지 특징을 인코딩하고, 고도 및 방위각을 기반으로 한 카메라 임베딩 정보와 결합한 다음, 다운스트림 3D 생성 작업을 위해 포지티브 및 네거티브 컨디셔닝과 함께 잠재 표현을 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `clip_vision` | 이미지 특징을 인코딩하는 데 사용되는 CLIP 비전 모델 | CLIP_VISION | 예 | - |
| `init_image` | 처리 및 인코딩할 입력 이미지 | IMAGE | 예 | - |
| `vae` | 픽셀을 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델 | VAE | 예 | - |
| `width` | 잠재 표현의 출력 너비 (기본값: 256, 8로 나누어 떨어져야 함) | INT | 예 | 16 to MAX_RESOLUTION |
| `height` | 잠재 표현의 출력 높이 (기본값: 256, 8로 나누어 떨어져야 함) | INT | 예 | 16 to MAX_RESOLUTION |
| `batch_size` | 배치에서 생성할 샘플 수 (기본값: 1) | INT | 예 | 1 to 4096 |
| `elevation` | 카메라 고도 각도 (도 단위, 기본값: 0.0) | FLOAT | 예 | -180.0 to 180.0 |
| `azimuth` | 카메라 방위각 (도 단위, 기본값: 0.0) | FLOAT | 예 | -180.0 to 180.0 |

**참고:** `width` 및 `height` 매개변수는 8로 나누어 떨어져야 합니다. 노드가 잠재 표현 차원을 만들기 위해 자동으로 8로 나누기 때문입니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `positive` | 이미지 특징과 카메라 임베딩을 결합한 포지티브 컨디셔닝 데이터 | CONDITIONING |
| `negative` | 0으로 초기화된 특징을 가진 네거티브 컨디셔닝 데이터 | CONDITIONING |
| `latent` | [batch_size, 4, height//8, width//8] 차원의 잠재 표현 | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/ko.md)

---
**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`
