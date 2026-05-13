> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/ko.md)

# WanSoundImageToVideoExtend 노드

WanSoundImageToVideoExtend 노드는 기존 비디오 잠재 표현에 추가 프레임을 생성하여 비디오를 확장합니다. 선택적으로 오디오, 참조 이미지 및 제어 비디오의 안내를 받을 수 있습니다. 시작 비디오 잠재 표현을 입력받아 제공된 조건화 및 오디오 신호를 활용하여 더 긴 비디오 시퀀스를 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 비디오에 포함되어야 할 내용을 안내하는 긍정 조건화 프롬프트 |
| `negative` | CONDITIONING | 예 | - | 비디오에서 제외되어야 할 내용을 지정하는 부정 조건화 프롬프트 |
| `vae` | VAE | 예 | - | 비디오 프레임의 인코딩 및 디코딩에 사용되는 변분 오토인코더 |
| `length` | INT | 예 | 1 ~ MAX_RESOLUTION | 비디오 시퀀스에 생성할 총 프레임 수 (기본값: 77, 단계: 4) |
| `video_latent` | LATENT | 예 | - | 확장의 시작점이 되는 초기 비디오 잠재 표현 |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | 아니요 | - | 사운드 특성에 기반하여 비디오 생성에 영향을 줄 수 있는 선택적 오디오 임베딩 |
| `ref_image` | IMAGE | 아니요 | - | 비디오 생성을 위한 시각적 안내를 제공하는 선택적 참조 이미지 |
| `control_video` | IMAGE | 아니요 | - | 생성된 비디오의 움직임과 스타일을 안내할 수 있는 선택적 제어 비디오 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 비디오 컨텍스트가 적용된 처리된 긍정 조건화 |
| `negative` | CONDITIONING | 비디오 컨텍스트가 적용된 처리된 부정 조건화 |
| `latent` | LATENT | 확장된 비디오 시퀀스를 포함하는 생성된 비디오 잠재 표현 |

---
**Source fingerprint (SHA-256):** `fc9aee5d51e96b864da7d75f592f07691be8b970346998b209b3ad8a72308ecb`
