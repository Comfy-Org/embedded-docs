# WanDancerVideo

WanDancerVideo는 WanDancer 모델을 사용한 비디오 생성을 위해 컨디셔닝 데이터와 빈 잠재 텐서를 준비합니다. 포지티브 및 네거티브 컨디셔닝을 입력받아, 시작 이미지, 마스크, CLIP 비전 임베딩, 오디오 특징과 선택적으로 결합하여 생성되는 비디오를 제어합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 비디오 생성을 안내하는 포지티브 컨디셔닝입니다. | CONDITIONING | 예 |  |
| `negative` | 비디오 생성을 안내하는 네거티브 컨디셔닝입니다. | CONDITIONING | 예 |  |
| `vae` | 시작 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE입니다. | VAE | 예 |  |
| `width` | 생성되는 비디오의 너비(픽셀)입니다 (기본값: 480). | INT | 예 | 16 to MAX_RESOLUTION (step: 16) |
| `height` | 생성되는 비디오의 높이(픽셀)입니다 (기본값: 832). | INT | 예 | 16 to MAX_RESOLUTION (step: 16) |
| `length` | 생성되는 비디오의 프레임 수입니다. WanDancer의 경우 149로 유지해야 합니다 (기본값: 149). | INT | 예 | 1 to MAX_RESOLUTION (step: 4) |
| `clip_vision_output` | 첫 번째 프레임에 대한 CLIP 비전 임베딩입니다. | CLIP_VISION_OUTPUT | 아니요 |  |
| `clip_vision_output_ref` | 참조 이미지에 대한 CLIP 비전 임베딩입니다. | CLIP_VISION_OUTPUT | 아니요 |  |
| `start_image` | 인코딩할 초기 이미지입니다. 프레임 수는 제한이 없습니다. | IMAGE | 아니요 |  |
| `mask` | 시작 이미지에 대한 이미지 컨디셔닝 마스크입니다. 흰색은 유지되고, 검은색은 생성됩니다. 로컬 생성에 사용됩니다. | MASK | 아니요 |  |
| `audio_encoder_output` | 오디오 인코더의 출력입니다. 오디오 조건 생성에 필요한 오디오 특징, FPS 및 오디오 주입 스케일을 제공합니다. | AUDIO_ENCODER_OUTPUT | 아니요 |  |

**매개변수 제약 사항 참고:**
- `start_image`가 제공되면 `width` × `height`로 크기가 조정되고, `length` 프레임 수로 제한된 다음, concat 마스크와 함께 두 컨디셔닝 모두에 첨부되는 잠재 텐서로 인코딩됩니다.
- `mask`는 `start_image`도 제공된 경우에만 적용됩니다. 마스크의 흰색 영역은 유지되고 검은색 영역은 생성됩니다. `mask`가 제공되지 않으면 시작 이미지 영역이 컨디셔닝 가이드로 사용되고 나머지 프레임이 생성됩니다.
- `clip_vision_output_ref`는 `clip_vision_output`이 제공된 경우에만 적용됩니다.
- `audio_encoder_output`은 오디오 특징, FPS 및 오디오 주입 스케일(기본값 1.0)을 두 컨디셔닝 모두에 첨부합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 추가 데이터(concat 잠재 텐서, CLIP 비전, 오디오)가 첨부된 포지티브 컨디셔닝입니다. | CONDITIONING |
| `negative` | 추가 데이터(concat 잠재 텐서, CLIP 비전, 오디오)가 첨부된 네거티브 컨디셔닝입니다. | CONDITIONING |
| `latent` | 지정된 비디오 길이, 높이 및 너비에 해당하는 차원을 가진 빈 잠재 텐서입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/ko.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
