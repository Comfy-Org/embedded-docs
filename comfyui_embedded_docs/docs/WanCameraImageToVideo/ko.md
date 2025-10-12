> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/ko.md)

WanCameraImageToVideo 노드는 이미지를 비디오 시퀀스로 변환하며, 비디오 생성을 위한 잠재 표현을 생성합니다. 이 노드는 조건 입력과 선택적 시작 이미지를 처리하여 비디오 모델과 함께 사용할 수 있는 비디오 잠재 표현을 생성합니다. 향상된 비디오 생성 제어를 위해 카메라 조건과 CLIP 비전 출력을 지원합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 비디오 생성을 위한 긍정적 조건 프롬프트 |
| `negative` | CONDITIONING | 예 | - | 비디오 생성에서 피할 부정적 조건 프롬프트 |
| `vae` | VAE | 예 | - | 이미지를 잠재 공간으로 인코딩하기 위한 VAE 모델 |
| `width` | INT | 예 | 16 ~ MAX_RESOLUTION | 출력 비디오 너비 (픽셀 단위, 기본값: 832, 단계: 16) |
| `height` | INT | 예 | 16 ~ MAX_RESOLUTION | 출력 비디오 높이 (픽셀 단위, 기본값: 480, 단계: 16) |
| `length` | INT | 예 | 1 ~ MAX_RESOLUTION | 비디오 시퀀스의 프레임 수 (기본값: 81, 단계: 4) |
| `batch_size` | INT | 예 | 1 ~ 4096 | 동시에 생성할 비디오 수 (기본값: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 아니오 | - | 추가 조건을 위한 선택적 CLIP 비전 출력 |
| `start_image` | IMAGE | 아니오 | - | 비디오 시퀀스를 초기화하기 위한 선택적 시작 이미지 |
| `camera_conditions` | WAN_CAMERA_EMBEDDING | 아니오 | - | 비디오 생성을 위한 선택적 카메라 임베딩 조건 |

**참고:** `start_image`가 제공되면, 노드는 이를 사용하여 비디오 시퀀스를 초기화하고 시작 프레임을 생성된 콘텐츠와 혼합하기 위해 마스킹을 적용합니다. `camera_conditions`와 `clip_vision_output` 매개변수는 선택 사항이지만, 제공될 경우 긍정적 및 부정적 프롬프트 모두에 대한 조건을 수정합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 카메라 조건과 CLIP 비전 출력이 적용된 수정된 긍정적 조건 |
| `negative` | CONDITIONING | 카메라 조건과 CLIP 비전 출력이 적용된 수정된 부정적 조건 |
| `latent` | LATENT | 비디오 모델에서 사용하기 위해 생성된 비디오 잠재 표현 |
