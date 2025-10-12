> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/ko.md)

WanSoundImageToVideo 노드는 이미지에서 비디오 콘텐츠를 생성하며, 선택적으로 오디오 조건을 적용할 수 있습니다. 긍정적 및 부정적 조건 프롬프트와 VAE 모델을 사용하여 비디오 잠재 표현을 생성하며, 참조 이미지, 오디오 인코딩, 제어 비디오 및 모션 참조를 통합하여 비디오 생성 과정을 안내할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 생성된 비디오에 나타나야 할 콘텐츠를 안내하는 긍정적 조건 프롬프트 |
| `negative` | CONDITIONING | 예 | - | 생성된 비디오에서 피해야 할 콘텐츠를 지정하는 부정적 조건 프롬프트 |
| `vae` | VAE | 예 | - | 비디오 잠재 표현을 인코딩 및 디코딩하는 데 사용되는 VAE 모델 |
| `width` | INT | 예 | 16 ~ MAX_RESOLUTION | 출력 비디오의 너비(픽셀 단위) (기본값: 832, 16으로 나누어져야 함) |
| `height` | INT | 예 | 16 ~ MAX_RESOLUTION | 출력 비디오의 높이(픽셀 단위) (기본값: 480, 16으로 나누어져야 함) |
| `length` | INT | 예 | 1 ~ MAX_RESOLUTION | 생성된 비디오의 프레임 수 (기본값: 77, 4로 나누어져야 함) |
| `batch_size` | INT | 예 | 1 ~ 4096 | 동시에 생성할 비디오의 수 (기본값: 1) |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | 아니오 | - | 사운드 특성을 기반으로 비디오 생성에 영향을 줄 수 있는 선택적 오디오 인코딩 |
| `ref_image` | IMAGE | 아니오 | - | 비디오 콘텐츠에 대한 시각적 안내를 제공하는 선택적 참조 이미지 |
| `control_video` | IMAGE | 아니오 | - | 생성된 비디오의 모션과 구조를 안내하는 선택적 제어 비디오 |
| `ref_motion` | IMAGE | 아니오 | - | 비디오의 움직임 패턴에 대한 안내를 제공하는 선택적 모션 참조 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 비디오 생성을 위해 수정된 처리된 긍정적 조건 |
| `negative` | CONDITIONING | 비디오 생성을 위해 수정된 처리된 부정적 조건 |
| `latent` | LATENT | 최종 비디오 프레임으로 디코딩할 수 있는 잠재 공간 내 생성된 비디오 표현 |