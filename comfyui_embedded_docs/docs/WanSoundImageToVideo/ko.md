# WanSoundImageToVideo

WanSoundImageToVideo 노드는 선택적 오디오 컨디셔닝을 사용하여 이미지에서 비디오 생성을 준비합니다. 긍정 및 부정 컨디셔닝 프롬프트와 VAE 모델을 입력받아 컨디셔닝 입력과 빈 잠재 텐서를 구성하며, 참조 이미지, 오디오 인코딩, 컨트롤 비디오, 모션 참조를 통합하여 비디오 생성 과정을 안내할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 생성될 비디오에 나타나야 할 내용을 안내하는 긍정 컨디셔닝 프롬프트입니다. | CONDITIONING | 예 | - |
| `negative` | 생성될 비디오에서 피해야 할 내용을 지정하는 부정 컨디셔닝 프롬프트입니다. | CONDITIONING | 예 | - |
| `vae` | 비디오 잠재 표현을 인코딩 및 디코딩하는 데 사용되는 VAE 모델입니다. | VAE | 예 | - |
| `width` | 출력 비디오의 픽셀 단위 너비입니다 (기본값: 832, 16으로 나누어져야 함). | INT | 예 | 16 to MAX_RESOLUTION (step: 16) |
| `height` | 출력 비디오의 픽셀 단위 높이입니다 (기본값: 480, 16으로 나누어져야 함). | INT | 예 | 16 to MAX_RESOLUTION (step: 16) |
| `length` | 생성된 비디오의 프레임 수입니다 (기본값: 77, 4로 나누어져야 함). | INT | 예 | 1 to MAX_RESOLUTION (step: 4) |
| `batch_size` | 동시에 생성할 비디오 수입니다 (기본값: 1). | INT | 예 | 1 to 4096 |
| `audio_encoder_output` | 사운드 특성에 따라 비디오 생성에 영향을 줄 수 있는 선택적 오디오 인코딩입니다. 제공되면 오디오 특징이 보간되어 비디오 생성 컨디셔닝에 사용됩니다. | AUDIOENCODEROUTPUT | 아니요 | - |
| `ref_image` | 비디오 콘텐츠에 시각적 안내를 제공하는 선택적 참조 이미지입니다. 이미지는 지정된 너비와 높이에 맞게 업스케일된 후 잠재 표현으로 인코딩됩니다. 입력 배치의 첫 번째 이미지만 사용됩니다. | IMAGE | 아니요 | - |
| `control_video` | 생성된 비디오의 움직임과 구조를 안내하는 선택적 컨트롤 비디오입니다. 비디오는 업스케일 및 인코딩된 후 출력 조건화에 사용됩니다. 처음 `length` 프레임만 사용됩니다. | IMAGE | 아니요 | - |
| `ref_motion` | 비디오의 움직임 패턴에 대한 안내를 제공하는 선택적 모션 참조입니다. 입력에 73개 이상의 프레임이 있으면 마지막 73개만 사용됩니다. 73개 미만이면 중립 프레임으로 시퀀스가 채워집니다. | IMAGE | 아니요 | - |

**참고:** 선택적 입력(`audio_encoder_output`, `ref_image`, `control_video`, `ref_motion`)은 독립적으로 또는 함께 사용할 수 있습니다. 컨트롤 비디오 컨디셔닝은 항상 적용되며, `control_video`가 제공되지 않으면 빈(제로) 컨트롤 비디오가 사용됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 비디오 생성을 위해 수정된 처리된 긍정 컨디셔닝입니다. 해당 선택적 입력이 제공되면 오디오 임베딩, 참조 잠재 표현, 모션 참조 및 컨트롤 비디오 컨디셔닝이 포함됩니다. | CONDITIONING |
| `negative` | 비디오 생성을 위해 수정된 처리된 부정 컨디셔닝입니다. 해당 선택적 입력이 제공되면 오디오 임베딩(0으로 설정), 참조 잠재 표현, 모션 참조 및 컨트롤 비디오 컨디셔닝이 포함됩니다. | CONDITIONING |
| `latent` | 비디오 생성을 위한 시작점 역할을 하는 빈 잠재 텐서입니다. 잠재 텐서의 형태는 [batch_size, 16, latent_t, height/8, width/8]이며, 여기서 latent_t = ((length - 1) // 4) + 1입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
