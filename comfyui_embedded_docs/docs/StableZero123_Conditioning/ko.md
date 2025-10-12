> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/ko.md)

StableZero123_Conditioning 노드는 입력 이미지와 카메라 각도를 처리하여 3D 모델 생성을 위한 조건화 데이터와 잠재 표현을 생성합니다. CLIP 비전 모델을 사용하여 이미지 특징을 인코딩하고, 고도와 방위각을 기반으로 한 카메라 임베딩 정보와 결합하여 하류 3D 생성 작업을 위한 양수 및 음수 조건화와 잠재 표현을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | 예 | - | 이미지 특징을 인코딩하는 데 사용되는 CLIP 비전 모델 |
| `init_image` | IMAGE | 예 | - | 처리 및 인코딩될 입력 이미지 |
| `vae` | VAE | 예 | - | 픽셀을 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델 |
| `width` | INT | 아니오 | 16 ~ MAX_RESOLUTION | 잠재 표현의 출력 너비 (기본값: 256, 8로 나누어져야 함) |
| `height` | INT | 아니오 | 16 ~ MAX_RESOLUTION | 잠재 표현의 출력 높이 (기본값: 256, 8로 나누어져야 함) |
| `batch_size` | INT | 아니오 | 1 ~ 4096 | 배치에서 생성할 샘플 수 (기본값: 1) |
| `elevation` | FLOAT | 아니오 | -180.0 ~ 180.0 | 카메라 고도 각도 (단위: 도, 기본값: 0.0) |
| `azimuth` | FLOAT | 아니오 | -180.0 ~ 180.0 | 카메라 방위각 (단위: 도, 기본값: 0.0) |

**참고:** `width` 및 `height` 매개변수는 8로 나누어져야 합니다. 노드는 이 값을 자동으로 8로 나누어 잠재 표현 차원을 생성합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 이미지 특징과 카메라 임베딩을 결합한 양수 조건화 데이터 |
| `negative` | CONDITIONING | 0으로 초기화된 특징을 가진 음수 조건화 데이터 |
| `latent` | LATENT | [batch_size, 4, height//8, width//8] 차원을 가진 잠재 표현 |