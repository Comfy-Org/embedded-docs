> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/ko.md)

WanSoundImageToVideoExtend 노드는 오디오 조건화와 참조 이미지를 통합하여 이미지-비디오 생성을 확장합니다. 긍정적 및 부정적 조건화와 함께 비디오 잠재 데이터 및 선택적 오디오 임베딩을 입력받아 확장된 비디오 시퀀스를 생성합니다. 이 노드는 이러한 입력들을 처리하여 오디오 큐와 동기화될 수 있는 일관된 비디오 출력을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 비디오에 포함되어야 할 내용을 안내하는 긍정적 조건화 프롬프트 |
| `negative` | CONDITIONING | 예 | - | 비디오가 피해야 할 내용을 지정하는 부정적 조건화 프롬프트 |
| `vae` | VAE | 예 | - | 비디오 프레임 인코딩 및 디코딩에 사용되는 변분 자동인코더 |
| `length` | INT | 예 | 1 ~ MAX_RESOLUTION | 비디오 시퀀스에 대해 생성할 프레임 수 (기본값: 77, 단계: 4) |
| `video_latent` | LATENT | 예 | - | 확장을 위한 시작점 역할을 하는 초기 비디오 잠재 표현 |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | 아니오 | - | 사운드 특성을 기반으로 비디오 생성에 영향을 줄 수 있는 선택적 오디오 임베딩 |
| `ref_image` | IMAGE | 아니오 | - | 비디오 생성에 시각적 지침을 제공하는 선택적 참조 이미지 |
| `control_video` | IMAGE | 아니오 | - | 생성된 비디오의 모션과 스타일을 안내할 수 있는 선택적 제어 비디오 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 비디오 컨텍스트가 적용된 처리된 긍정적 조건화 |
| `negative` | CONDITIONING | 비디오 컨텍스트가 적용된 처리된 부정적 조건화 |
| `latent` | LATENT | 확장된 비디오 시퀀스를 포함하는 생성된 비디오 잠재 표현 |
