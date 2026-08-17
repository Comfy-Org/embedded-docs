# Wan22FunControlToVideo

Wan22FunControlToVideo 노드는 Wan 비디오 모델 아키텍처를 사용하여 비디오 생성을 위한 컨디셔닝 및 잠재 표현을 준비합니다. 이 노드는 긍정 및 부정 컨디셔닝 입력과 선택적 참조 이미지 및 제어 비디오를 처리하여 비디오 합성에 필요한 잠재 공간 표현을 생성합니다. 노드는 공간적 스케일링과 시간적 차원을 처리하여 비디오 모델에 적합한 컨디셔닝 데이터를 생성합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 비디오 생성을 안내하는 긍정 컨디셔닝 입력 | CONDITIONING | 예 | - |
| `negative` | 비디오 생성을 안내하는 부정 컨디셔닝 입력 | CONDITIONING | 예 | - |
| `vae` | 이미지를 잠재 공간으로 인코딩하는 데 사용되는 VAE 모델 | VAE | 예 | - |
| `width` | 출력 비디오 너비(픽셀 단위) (기본값: 832, 스텝: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `height` | 출력 비디오 높이(픽셀 단위) (기본값: 480, 스텝: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `length` | 비디오 시퀀스의 프레임 수 (기본값: 81, 스텝: 4) | INT | 예 | 1 to MAX_RESOLUTION |
| `batch_size` | 생성할 비디오 시퀀스 수 (기본값: 1) | INT | 예 | 1 to 4096 |
| `ref_image` | 시각적 안내를 제공하는 선택적 참조 이미지 | IMAGE | 아니요 | - |
| `control_video` | 생성 과정을 안내하는 선택적 제어 비디오 | IMAGE | 아니요 | - |

**참고:** `length` 매개변수는 4프레임 단위로 처리되며, 노드는 잠재 공간에 대한 시간적 스케일링을 자동으로 처리합니다. `ref_image`가 제공되면 참조 잠재를 통해 컨디셔닝에 영향을 줍니다. `control_video`가 제공되면 컨디셔닝에 사용되는 concat 잠재 표현에 직접 영향을 줍니다. `start_image` 매개변수는 이 노드의 스키마에서 입력으로 노출되지 않지만 실행 로직에서 참조됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | concat 잠재, 마스크 및 선택적 참조 잠재를 포함한 비디오 특정 잠재 데이터가 포함된 수정된 긍정 컨디셔닝 | CONDITIONING |
| `negative` | concat 잠재, 마스크 및 선택적 참조 잠재를 포함한 비디오 특정 잠재 데이터가 포함된 수정된 부정 컨디셔닝 | CONDITIONING |
| `latent` | 배치 크기, 잠재 채널 및 공간/시간적 스케일링에 따라 비디오 생성에 적합한 차원을 가진 빈 잠재 텐서 | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
