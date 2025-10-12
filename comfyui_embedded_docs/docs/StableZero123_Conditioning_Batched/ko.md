> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/ko.md)

StableZero123_Conditioning_Batched 노드는 입력 이미지를 처리하여 3D 모델 생성을 위한 조건화 데이터를 생성합니다. CLIP 비전 및 VAE 모델을 사용하여 이미지를 인코딩한 후, 고도 및 방위각을 기반으로 카메라 임베딩을 생성하여 배치 처리를 위한 긍정 및 부정 조건화와 잠재 표현을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | 예 | - | 입력 이미지를 인코딩하는 데 사용되는 CLIP 비전 모델 |
| `init_image` | IMAGE | 예 | - | 처리 및 인코딩될 초기 입력 이미지 |
| `vae` | VAE | 예 | - | 이미지 픽셀을 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델 |
| `width` | INT | 아니오 | 16부터 MAX_RESOLUTION | 처리된 이미지의 출력 너비 (기본값: 256, 8로 나누어져야 함) |
| `height` | INT | 아니오 | 16부터 MAX_RESOLUTION | 처리된 이미지의 출력 높이 (기본값: 256, 8로 나누어져야 함) |
| `batch_size` | INT | 아니오 | 1부터 4096 | 배치에서 생성할 조건화 샘플의 수 (기본값: 1) |
| `elevation` | FLOAT | 아니오 | -180.0부터 180.0 | 초기 카메라 고도 각도 (도 단위, 기본값: 0.0) |
| `azimuth` | FLOAT | 아니오 | -180.0부터 180.0 | 초기 카메라 방위각 (도 단위, 기본값: 0.0) |
| `elevation_batch_increment` | FLOAT | 아니오 | -180.0부터 180.0 | 각 배치 항목에 대해 고도를 증가시킬 양 (기본값: 0.0) |
| `azimuth_batch_increment` | FLOAT | 아니오 | -180.0부터 180.0 | 각 배치 항목에 대해 방위각을 증가시킬 양 (기본값: 0.0) |

**참고:** `width` 및 `height` 매개변수는 8로 나누어져야 합니다. 노드는 내부적으로 이러한 차원을 8로 나누어 잠재 공간 생성을 수행하기 때문입니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 이미지 임베딩과 카메라 매개변수를 포함하는 긍정 조건화 데이터 |
| `negative` | CONDITIONING | 0으로 초기화된 임베딩을 가진 부정 조건화 데이터 |
| `latent` | LATENT | 배치 인덱싱 정보와 함께 처리된 이미지의 잠재 표현 |