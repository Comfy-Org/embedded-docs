> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/ko.md)

# WanMoveTrackToVideo 노드

WanMoveTrackToVideo 노드는 비디오 생성을 위한 컨디셔닝 및 잠재 공간 데이터를 준비하며, 선택적으로 모션 트래킹 정보를 통합합니다. 시작 이미지 시퀀스를 잠재 표현으로 인코딩하고, 객체 트랙의 위치 데이터를 혼합하여 생성된 비디오의 움직임을 안내할 수 있습니다. 이 노드는 수정된 포지티브 및 네거티브 컨디셔닝과 함께 비디오 모델에 사용할 준비가 된 빈 잠재 텐서를 출력합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 수정할 포지티브 컨디셔닝 입력입니다. |
| `negative` | CONDITIONING | 예 | - | 수정할 네거티브 컨디셔닝 입력입니다. |
| `vae` | VAE | 예 | - | 시작 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델입니다. |
| `tracks` | TRACKS | 아니요 | - | 객체 경로가 포함된 선택적 모션 트래킹 데이터입니다. |
| `strength` | FLOAT | 아니요 | 0.0 - 100.0 | 트랙 컨디셔닝의 강도입니다. (기본값: 1.0) |
| `width` | INT | 아니요 | 16 - MAX_RESOLUTION | 출력 비디오의 너비입니다. 16으로 나누어 떨어져야 합니다. (기본값: 832) |
| `height` | INT | 아니요 | 16 - MAX_RESOLUTION | 출력 비디오의 높이입니다. 16으로 나누어 떨어져야 합니다. (기본값: 480) |
| `length` | INT | 아니요 | 1 - MAX_RESOLUTION | 비디오 시퀀스의 프레임 수입니다. (기본값: 81) |
| `batch_size` | INT | 아니요 | 1 - 4096 | 잠재 출력의 배치 크기입니다. (기본값: 1) |
| `start_image` | IMAGE | 예 | - | 인코딩할 시작 이미지 또는 이미지 시퀀스입니다. |
| `clip_vision_output` | CLIPVISIONOUTPUT | 아니요 | - | 컨디셔닝에 추가할 선택적 CLIP 비전 모델 출력입니다. |

**참고:** `strength` 매개변수는 `tracks`가 제공된 경우에만 효과가 있습니다. `tracks`가 제공되지 않거나 `strength`가 0.0인 경우 트랙 컨디셔닝이 적용되지 않습니다. `start_image`는 컨디셔닝을 위한 잠재 이미지와 마스크를 생성하는 데 사용됩니다. 제공되지 않으면 노드는 컨디셔닝을 그대로 전달하고 빈 잠재 텐서를 출력합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 수정된 포지티브 컨디셔닝으로, `concat_latent_image`, `concat_mask` 및 `clip_vision_output`을 포함할 수 있습니다. |
| `negative` | CONDITIONING | 수정된 네거티브 컨디셔닝으로, `concat_latent_image`, `concat_mask` 및 `clip_vision_output`을 포함할 수 있습니다. |
| `latent` | LATENT | `batch_size`, `length`, `height` 및 `width` 입력에 의해 차원이 결정된 빈 잠재 텐서입니다. |

---
**Source fingerprint (SHA-256):** `9677addf5b94b42efd3015f51380c1fa9b16d4a5105cc7f24de0be34c0042bbc`
