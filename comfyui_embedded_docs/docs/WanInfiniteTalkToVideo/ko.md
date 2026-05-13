> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/ko.md)

# WanInfiniteTalkToVideo 노드

WanInfiniteTalkToVideo 노드는 오디오 입력으로부터 비디오 시퀀스를 생성합니다. 이 노드는 하나 또는 두 명의 화자로부터 추출된 오디오 특징을 조건으로 하는 비디오 확산 모델을 사용하여 토킹 헤드 비디오의 잠재 표현을 생성합니다. 새로운 시퀀스를 생성하거나 이전 프레임을 모션 컨텍스트로 사용하여 기존 시퀀스를 확장할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `mode` | COMBO | 예 | `"single_speaker"`<br>`"two_speakers"` | 오디오 입력 모드입니다. `"single_speaker"`는 하나의 오디오 입력을 사용합니다. `"two_speakers"`는 두 번째 화자와 해당 마스크의 입력을 활성화합니다. |
| `model` | MODEL | 예 | - | 기본 비디오 확산 모델입니다. |
| `model_patch` | MODELPATCH | 예 | - | 오디오 투영 레이어를 포함하는 모델 패치입니다. |
| `positive` | CONDITIONING | 예 | - | 생성을 안내하는 긍정 조건입니다. |
| `negative` | CONDITIONING | 예 | - | 생성을 안내하는 부정 조건입니다. |
| `vae` | VAE | 예 | - | 이미지를 잠재 공간으로 인코딩하거나 잠재 공간에서 디코딩하는 데 사용되는 VAE입니다. |
| `width` | INT | 아니요 | 16 - MAX_RESOLUTION | 출력 비디오의 픽셀 단위 너비입니다. 16으로 나누어 떨어져야 합니다. (기본값: 832) |
| `height` | INT | 아니요 | 16 - MAX_RESOLUTION | 출력 비디오의 픽셀 단위 높이입니다. 16으로 나누어 떨어져야 합니다. (기본값: 480) |
| `length` | INT | 아니요 | 1 - MAX_RESOLUTION | 생성할 프레임 수입니다. (기본값: 81) |
| `clip_vision_output` | CLIPVISIONOUTPUT | 아니요 | - | 추가 조건을 위한 선택적 CLIP 비전 출력입니다. |
| `start_image` | IMAGE | 아니요 | - | 비디오 시퀀스를 초기화하는 선택적 시작 이미지입니다. |
| `audio_encoder_output_1` | AUDIOENCODEROUTPUT | 예 | - | 첫 번째 화자의 특징을 포함하는 기본 오디오 인코더 출력입니다. |
| `motion_frame_count` | INT | 아니요 | 1 - 33 | 시퀀스 확장 시 모션 컨텍스트로 사용할 이전 프레임 수입니다. (기본값: 9) |
| `audio_scale` | FLOAT | 아니요 | -10.0 - 10.0 | 오디오 조건에 적용되는 스케일링 계수입니다. (기본값: 1.0) |
| `previous_frames` | IMAGE | 아니요 | - | 확장할 이전 비디오 프레임입니다(선택 사항). |
| `audio_encoder_output_2` | AUDIOENCODEROUTPUT | 아니요 | - | 두 번째 오디오 인코더 출력입니다. `mode`가 `"two_speakers"`로 설정된 경우 필수입니다. |
| `mask_1` | MASK | 아니요 | - | 첫 번째 화자의 마스크입니다. 두 개의 오디오 입력을 사용하는 경우 필수입니다. |
| `mask_2` | MASK | 아니요 | - | 두 번째 화자의 마스크입니다. 두 개의 오디오 입력을 사용하는 경우 필수입니다. |

**매개변수 제약 조건:**

* `mode`가 `"two_speakers"`로 설정된 경우, `audio_encoder_output_2`, `mask_1`, `mask_2` 매개변수가 필수가 됩니다.
* `audio_encoder_output_2`가 제공되면 `mask_1`과 `mask_2`도 함께 제공되어야 합니다.
* `mask_1`과 `mask_2`가 제공되면 `audio_encoder_output_2`도 함께 제공되어야 합니다.
* `previous_frames`가 제공되면 `motion_frame_count`에 지정된 수만큼의 프레임 이상을 포함해야 합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | 오디오 조건이 적용된 패치된 모델입니다. |
| `positive` | CONDITIONING | 추가 컨텍스트(예: 시작 이미지, CLIP 비전)로 수정될 수 있는 긍정 조건입니다. |
| `negative` | CONDITIONING | 추가 컨텍스트로 수정될 수 있는 부정 조건입니다. |
| `latent` | LATENT | 잠재 공간에서 생성된 비디오 시퀀스입니다. |
| `trim_image` | INT | 시퀀스 확장 시 모션 컨텍스트 시작 부분에서 제거해야 하는 프레임 수입니다. |

---
**Source fingerprint (SHA-256):** `6bb976da5cac0b61edb7d4c9d206c7c7ea9ffc0e982034c23c7f2e891e972888`
