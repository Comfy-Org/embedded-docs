# WanMoveTrackToVideo

The WanMoveTrackToVideo 노드는 비디오 생성을 위한 컨디셔닝 및 잠재 데이터를 준비합니다. VAE를 사용하여 시작 이미지 시퀀스를 잠재 공간으로 인코딩하고, 선택적으로 모션 트래킹 정보를 통합하여 생성된 비디오에서 객체의 움직임을 안내할 수 있습니다. 이 노드는 수정된 포지티브 및 네거티브 컨디셔닝과 함께 비디오 생성 모델에 적합한 빈 잠재 텐서를 출력합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 수정할 포지티브 컨디셔닝 입력입니다. | CONDITIONING | 예 | - |
| `negative` | 수정할 네거티브 컨디셔닝 입력입니다. | CONDITIONING | 예 | - |
| `vae` | 시작 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델입니다. | VAE | 예 | - |
| `tracks` | 객체 경로를 포함하는 선택적 모션 트래킹 데이터입니다. | TRACKS | 아니오 | - |
| `strength` | 트랙 컨디셔닝의 강도입니다. `tracks`가 제공되고 값이 0.0보다 클 때만 효과가 있습니다. (기본값: 1.0) | FLOAT | 예 | 0.0 - 100.0 |
| `width` | 출력 비디오의 너비입니다. 16 단위로 설정합니다. (기본값: 832) | INT | 예 | 16 - MAX_RESOLUTION |
| `height` | 출력 비디오의 높이입니다. 16 단위로 설정합니다. (기본값: 480) | INT | 예 | 16 - MAX_RESOLUTION |
| `length` | 비디오 시퀀스의 프레임 수입니다. 4 단위로 설정합니다. (기본값: 81) | INT | 예 | 1 - MAX_RESOLUTION |
| `batch_size` | 잠재 출력의 배치 크기입니다. (기본값: 1) | INT | 예 | 1 - 4096 |
| `start_image` | VAE로 인코딩할 시작 이미지 또는 이미지 시퀀스입니다. | IMAGE | 예 | - |
| `clip_vision_output` | 컨디셔닝에 추가할 선택적 CLIP 비전 모델 출력입니다. | CLIP_VISION_OUTPUT | 아니오 | - |

참고: 트랙 기반 모션은 `tracks`가 제공되고 `strength`가 0.0보다 클 때만 적용됩니다. 그렇지 않으면 컨디셔닝은 수정되지 않은 인코딩된 시작 이미지를 받습니다. `start_image`는 컨디셔닝을 위한 잠재 이미지와 마스크를 생성하는 데 사용됩니다. 사용할 수 없으면 노드는 컨디셔닝만 통과시키고 빈 잠재 텐서를 출력합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 수정된 포지티브 컨디셔닝으로, `concat_latent_image`, `concat_mask`, `clip_vision_output`을 포함할 수 있습니다. | CONDITIONING |
| `negative` | 수정된 네거티브 컨디셔닝으로, `concat_latent_image`, `concat_mask`, `clip_vision_output`을 포함할 수 있습니다. | CONDITIONING |
| `latent` | `batch_size`, `length`, `height`, `width` 입력에 따라 크기가 결정되는 빈 잠재 텐서입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
