> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/ko.md)

HunyuanVideo15ImageToVideo 노드는 HunyuanVideo 1.5 모델 기반의 비디오 생성을 위해 조건화 및 잠재 공간 데이터를 준비합니다. 비디오 시퀀스에 대한 초기 잠재 표현을 생성하며, 선택적으로 시작 이미지나 CLIP 비전 출력을 통합하여 생성 과정을 안내할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 비디오에 포함되어야 할 내용을 설명하는 긍정적 조건화 프롬프트입니다. |
| `negative` | CONDITIONING | 예 | - | 비디오에서 피해야 할 내용을 설명하는 부정적 조건화 프롬프트입니다. |
| `vae` | VAE | 예 | - | 시작 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE(변분 자동인코더) 모델입니다. |
| `width` | INT | 아니요 | 16 ~ MAX_RESOLUTION | 출력 비디오 프레임의 너비(픽셀)입니다. 16으로 나누어 떨어져야 합니다. (기본값: 848) |
| `height` | INT | 아니요 | 16 ~ MAX_RESOLUTION | 출력 비디오 프레임의 높이(픽셀)입니다. 16으로 나누어 떨어져야 합니다. (기본값: 480) |
| `length` | INT | 아니요 | 1 ~ MAX_RESOLUTION | 비디오 시퀀스의 총 프레임 수입니다. (기본값: 33) |
| `batch_size` | INT | 아니요 | 1 ~ 4096 | 단일 배치에서 생성할 비디오 시퀀스의 수입니다. (기본값: 1) |
| `start_image` | IMAGE | 아니요 | - | 비디오 생성을 초기화하기 위한 선택적 시작 이미지입니다. 제공되면 인코딩되어 첫 번째 프레임을 조건화하는 데 사용됩니다. |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 아니요 | - | 생성에 추가적인 시각적 조건화를 제공하기 위한 선택적 CLIP 비전 임베딩입니다. |

**참고:** `start_image`가 제공되면, 쌍선형 보간법을 사용하여 지정된 `width`와 `height`에 맞게 자동으로 크기가 조정됩니다. 이미지 배치의 첫 `length` 프레임이 사용됩니다. 인코딩된 이미지는 해당 `concat_mask`와 함께 `concat_latent_image`로 `positive` 및 `negative` 조건화에 추가됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 인코딩된 시작 이미지나 CLIP 비전 출력이 포함될 수 있는 수정된 긍정적 조건화입니다. |
| `negative` | CONDITIONING | 인코딩된 시작 이미지나 CLIP 비전 출력이 포함될 수 있는 수정된 부정적 조건화입니다. |
| `latent` | LATENT | 지정된 배치 크기, 비디오 길이, 너비 및 높이에 맞게 구성된 차원을 가진 빈 잠재 텐서입니다. |
