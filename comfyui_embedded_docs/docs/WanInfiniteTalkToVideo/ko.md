# WanInfiniteTalkToVideo

WanInfiniteTalkToVideo 노드는 오디오에서 토킹헤드 비디오 클립을 생성합니다. 하나 또는 두 명의 화자로부터 얻은 오디오 특징을 비디오 확산 모델에 조건화하며, 선택적으로 시작 이미지나 이전 프레임을 컨텍스트로 사용할 수 있습니다. 그런 다음 패치된 모델, 컨디셔닝, 샘플링을 위한 잠재 비디오를 반환합니다.

## 입력

### 공통 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `mode` | 오디오 모드입니다. `"single_speaker"`를 선택하면 하나의 오디오 입력을 사용합니다. `"two_speakers"`를 선택하면 아래 나열된 두 번째 화자 입력이 추가됩니다. | DYNAMIC_COMBO | 예 | `"single_speaker"`<br>`"two_speakers"` |
| `model` | 패치할 기본 비디오 확산 모델입니다. | MODEL | 예 | - |
| `model_patch` | 오디오 프로젝션 레이어를 포함하는 모델 패치입니다. | MODELPATCH | 예 | - |
| `positive` | 비디오 생성을 안내하는 데 사용되는 긍정적 컨디셔닝입니다. | CONDITIONING | 예 | - |
| `negative` | 비디오 생성을 안내하는 데 사용되는 부정적 컨디셔닝입니다. | CONDITIONING | 예 | - |
| `vae` | 이미지와 이전 프레임을 잠재 공간으로 인코딩하는 데 사용되는 VAE입니다. | VAE | 예 | - |
| `width` | 생성된 비디오의 너비(픽셀 단위)로, 16 단위로 지정합니다. (기본값: 832) | INT | 예 | 16 - MAX_RESOLUTION (step 16) |
| `height` | 생성된 비디오의 높이(픽셀 단위)로, 16 단위로 지정합니다. (기본값: 480) | INT | 예 | 16 - MAX_RESOLUTION (step 16) |
| `length` | 생성할 프레임 수입니다. (기본값: 81) | INT | 예 | 1 - MAX_RESOLUTION (step 4) |
| `audio_encoder_output_1` | 첫 번째 화자의 오디오 인코더 출력으로, 컨디셔닝에 사용되는 오디오 특징을 포함합니다. | AUDIOENCODEROUTPUT | 예 | - |
| `start_image` | 비디오의 시작 부분을 초기화하는 데 사용되는 선택적 시작 이미지입니다. `width` 및 `height`로 크기가 조정됩니다. | IMAGE | 아니요 | - |
| `clip_vision_output` | 긍정 및 부정 컨디셔닝에 모두 추가되는 선택적 CLIP 비전 출력입니다. | CLIPVISIONOUTPUT | 아니요 | - |
| `motion_frame_count` | 모션 컨텍스트로 사용할 이전 프레임 수입니다. (기본값: 9) | INT | 예 | 1 - 33 (step 1) |
| `audio_scale` | 오디오 컨디셔닝에 적용되는 스케일링 계수입니다. (기본값: 1.0) | FLOAT | 예 | -10.0 - 10.0 (step 0.01) |
| `previous_frames` | 기존 시퀀스를 확장하는 데 사용되는 선택적 이전 비디오 프레임입니다. 노드는 마지막 `motion_frame_count` 프레임을 모션 컨텍스트로 사용합니다. | IMAGE | 아니요 | - |

### 단일 화자 입력

`single_speaker`를 선택하면 추가 입력이 추가되지 않습니다.

### 두 화자 입력

이 입력들은 `mode`가 `"two_speakers"`일 때 사용할 수 있습니다.

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | 두 번째 화자의 오디오 인코더 출력입니다. 제공되는 경우 `mask_1`과 `mask_2`도 함께 제공해야 합니다. | AUDIOENCODEROUTPUT | 아니요 | - |
| `mask_1` | 첫 번째 화자의 마스크입니다. 두 개의 오디오 입력을 사용할 때 필요합니다. | MASK | 아니요 | - |
| `mask_2` | 두 번째 화자의 마스크입니다. 두 개의 오디오 입력을 사용할 때 필요합니다. | MASK | 아니요 | - |

**매개변수 제약 조건:**

- `audio_encoder_output_2`가 제공되면 `mask_1`과 `mask_2`도 모두 제공해야 합니다.
- `mask_1`과 `mask_2`가 모두 제공되면 `audio_encoder_output_2`도 제공해야 합니다.
- `previous_frames`가 제공되면 `motion_frame_count`에 지정된 수 이상의 프레임을 포함해야 합니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `model` | 오디오 컨디셔닝과 샘플링 래퍼가 적용된 패치된 모델입니다. | MODEL |
| `positive` | 시작 이미지 또는 CLIP 비전 컨텍스트로 수정될 수 있는 긍정적 컨디셔닝입니다. | CONDITIONING |
| `negative` | 시작 이미지 또는 CLIP 비전 컨텍스트로 수정될 수 있는 부정적 컨디셔닝입니다. | CONDITIONING |
| `latent` | 생성할 비디오를 나타내는 0으로 초기화된 잠재 텐서입니다. | LATENT |
| `trim_image` | 이전 프레임에서 확장할 때 시작 부분에서 잘라낼 프레임 수입니다. 새 시퀀스를 시작할 때는 0입니다. | INT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
