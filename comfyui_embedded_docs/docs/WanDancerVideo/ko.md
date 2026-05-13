> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/ko.md)

WanDancerVideo 노드는 WanDancer 모델을 사용한 비디오 생성에 필요한 조건화 데이터와 빈 잠재 텐서를 준비합니다. 시작 이미지, 마스크, CLIP 비전 임베딩 및 오디오 특징과 같은 선택적 입력과 함께 긍정 및 부정 조건화를 결합하여 생성된 비디오를 제어합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | | 비디오 생성을 안내하는 긍정 조건화입니다. |
| `negative` | CONDITIONING | 예 | | 비디오 생성을 안내하는 부정 조건화입니다. |
| `vae` | VAE | 예 | | 시작 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE입니다. |
| `width` | INT | 예 | 16 ~ MAX_RESOLUTION (단위: 16) | 생성된 비디오의 픽셀 단위 너비입니다 (기본값: 480). |
| `height` | INT | 예 | 16 ~ MAX_RESOLUTION (단위: 16) | 생성된 비디오의 픽셀 단위 높이입니다 (기본값: 832). |
| `length` | INT | 예 | 1 ~ MAX_RESOLUTION (단위: 4) | 생성된 비디오의 프레임 수입니다. WanDancer의 경우 149로 유지해야 합니다 (기본값: 149). |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 아니요 | | 첫 번째 프레임에 대한 CLIP 비전 임베딩입니다. |
| `clip_vision_output_ref` | CLIP_VISION_OUTPUT | 아니요 | | 참조 이미지에 대한 CLIP 비전 임베딩입니다. |
| `start_image` | IMAGE | 아니요 | | 인코딩할 초기 이미지입니다. 지정된 `length`까지 여러 프레임이 될 수 있습니다. |
| `mask` | MASK | 아니요 | | 시작 이미지에 대한 이미지 조건화 마스크입니다. 흰색 영역은 유지되고 검은색 영역은 생성됩니다. 로컬 생성에 사용됩니다. |
| `audio_encoder_output` | AUDIO_ENCODER_OUTPUT | 아니요 | | 오디오 인코더의 출력으로, 오디오 조건화 생성을 위한 오디오 특징, fps 및 주입 비율을 제공합니다. |

**매개변수 제약 조건 참고:**
- `start_image` 및 `mask` 입력은 선택 사항이지만 함께 사용할 수 있습니다. `start_image`가 제공되면 인코딩되어 잠재 텐서와 연결됩니다. `mask`도 제공되면 시작 이미지 중 유지할 부분(흰색)과 재생성할 부분(검은색)을 제어합니다. `mask`가 제공되지 않으면 전체 시작 이미지 영역이 조건화 안내로 사용됩니다.
- `clip_vision_output` 및 `clip_vision_output_ref` 입력은 선택 사항이며, 첫 번째 프레임과 참조 이미지에 대한 시각적 컨텍스트를 제공하기 위해 함께 사용할 수 있습니다.
- `audio_encoder_output` 입력은 선택 사항이며, 오디오 조건화 생성을 위한 오디오 특징을 제공합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 추가 데이터(연결된 잠재 텐서, CLIP 비전, 오디오)가 첨부된 긍정 조건화입니다. |
| `negative` | CONDITIONING | 추가 데이터(연결된 잠재 텐서, CLIP 비전, 오디오)가 첨부된 부정 조건화입니다. |
| `latent` | LATENT | 지정된 비디오 길이, 높이 및 너비와 일치하는 차원의 빈 잠재 텐서입니다. |

---
**Source fingerprint (SHA-256):** `7ab1b4662eb8d780295ea3a3e3139c64d81e03a979a293a481f82deaf1fc2f7e`
