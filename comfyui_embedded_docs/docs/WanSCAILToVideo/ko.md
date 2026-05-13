> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/ko.md)

WanSCAILToVideo 노드는 비디오 생성을 위한 컨디셔닝과 빈 잠재 공간을 준비합니다. 참조 이미지, 포즈 비디오, CLIP 비전 출력과 같은 선택적 입력을 처리하여 비디오 모델의 포지티브 및 네거티브 컨디셔닝에 임베딩합니다. 이 노드는 수정된 컨디셔닝과 지정된 비디오 크기의 빈 잠재 텐서를 출력합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 포지티브 컨디셔닝 입력입니다. |
| `negative` | CONDITIONING | 예 | - | 네거티브 컨디셔닝 입력입니다. |
| `vae` | VAE | 예 | - | 이미지와 비디오 프레임 인코딩에 사용되는 VAE 모델입니다. |
| `width` | INT | 예 | 32 ~ MAX_RESOLUTION | 출력 비디오의 픽셀 단위 너비입니다(기본값: 512). 8로 나누어 떨어져야 합니다. |
| `height` | INT | 예 | 32 ~ MAX_RESOLUTION | 출력 비디오의 픽셀 단위 높이입니다(기본값: 896). 8로 나누어 떨어져야 합니다. |
| `length` | INT | 예 | 1 ~ MAX_RESOLUTION | 비디오의 프레임 수입니다(기본값: 81). 4로 나누어 떨어져야 합니다. |
| `batch_size` | INT | 예 | 1 ~ 4096 | 한 배치에서 생성할 비디오 수입니다(기본값: 1). |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 아니요 | - | 컨디셔닝을 위한 선택적 CLIP 비전 출력입니다. |
| `reference_image` | IMAGE | 아니요 | - | 컨디셔닝을 위한 선택적 참조 이미지입니다. |
| `pose_video` | IMAGE | 아니요 | - | 포즈 컨디셔닝에 사용되는 비디오입니다. 주 비디오 해상도의 절반으로 축소됩니다. |
| `pose_strength` | FLOAT | 예 | 0.0 ~ 10.0 | 포즈 잠재의 강도입니다(기본값: 1.0). |
| `pose_start` | FLOAT | 예 | 0.0 ~ 1.0 | 포즈 컨디셔닝을 사용할 시작 단계입니다(기본값: 0.0). |
| `pose_end` | FLOAT | 예 | 0.0 ~ 1.0 | 포즈 컨디셔닝을 사용할 종료 단계입니다(기본값: 1.0). |

**참고:** `pose_video` 입력은 처음 `length` 프레임에 대해서만 처리됩니다. `reference_image`는 배치의 첫 번째 이미지에 대해서만 처리됩니다. `reference_image`가 제공되면 동일한 크기의 0으로 채워진 잠재가 네거티브 컨디셔닝에 사용됩니다. `clip_vision_output`이 제공되면 포지티브 및 네거티브 컨디셔닝 모두에 적용됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 수정된 포지티브 컨디셔닝으로, 참조 이미지 잠재, CLIP 비전 출력 또는 포즈 비디오 잠재가 포함될 수 있습니다. |
| `negative` | CONDITIONING | 수정된 네거티브 컨디셔닝으로, 참조 이미지 잠재, CLIP 비전 출력 또는 포즈 비디오 잠재가 포함될 수 있습니다. |
| `latent` | LATENT | `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` 형태의 빈 잠재 텐서입니다. |

---
**Source fingerprint (SHA-256):** `63de4b6fe41fc23ea81c21965a2dbfc82120bb1bad6785b2130af824e015fbcb`
