# HunyuanVideo15ImageToVideo

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 비디오에 포함되어야 할 내용을 설명하는 긍정 컨디셔닝 프롬프트입니다. | CONDITIONING | 예 | - |
| `negative` | 비디오에서 제외되어야 할 내용을 설명하는 부정 컨디셔닝 프롬프트입니다. | CONDITIONING | 예 | - |
| `vae` | 시작 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE(Variational Autoencoder) 모델입니다. | VAE | 예 | - |
| `width` | 출력 비디오 프레임의 너비(픽셀)입니다. 16으로 나누어 떨어져야 합니다. (기본값: 848) | INT | 예 | 16 to MAX_RESOLUTION, step: 16 |
| `height` | 출력 비디오 프레임의 높이(픽셀)입니다. 16으로 나누어 떨어져야 합니다. (기본값: 480) | INT | 예 | 16 to MAX_RESOLUTION, step: 16 |
| `length` | 비디오 시퀀스의 총 프레임 수입니다. 값은 4씩 증가합니다. (기본값: 33) | INT | 예 | 1 to MAX_RESOLUTION, step: 4 |
| `batch_size` | 단일 배치에서 생성할 비디오 시퀀스 수입니다. (기본값: 1) | INT | 예 | 1 to 4096 |
| `start_image` | 비디오 생성을 초기화하는 선택적 시작 이미지입니다. 제공되면 인코딩되어 첫 번째 프레임을 컨디셔닝하는 데 사용됩니다. 이미지의 첫 `length` 프레임만 사용됩니다. | IMAGE | 아니요 | - |
| `clip_vision_output` | 생성에 추가적인 시각적 컨디셔닝을 제공하는 선택적 CLIP 비전 임베딩입니다. | CLIP_VISION_OUTPUT | 아니요 | - |

**참고:** `start_image`가 제공되면 지정된 `width` 및 `height`에 맞게 양선형 보간을 사용하여 자동으로 크기가 조정되며, RGB 채널만 사용됩니다. 이미지 배치의 첫 `length` 프레임이 사용됩니다. 인코딩된 이미지는 `concat_latent_image` 및 해당 `concat_mask`로 `positive` 및 `negative` 컨디셔닝에 모두 추가됩니다. 마스크는 시작 이미지가 덮는 프레임에 대해서는 0.0으로 설정되고 나머지 프레임에 대해서는 1.0으로 설정됩니다. `clip_vision_output`이 제공되면 이것도 `positive` 및 `negative` 컨디셔닝에 모두 추가됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 인코딩된 시작 이미지나 CLIP 비전 출력을 포함할 수 있는 수정된 긍정 컨디셔닝입니다. | CONDITIONING |
| `negative` | 인코딩된 시작 이미지나 CLIP 비전 출력을 포함할 수 있는 수정된 부정 컨디셔닝입니다. | CONDITIONING |
| `latent` | 지정된 배치 크기, 비디오 길이, 너비 및 높이에 맞게 차원이 구성된 빈 잠재 텐서입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `dbedf7f378ae9613c8f47fe9876a4576c815055b4cdb6bf687b7575fcd7ea80a`
