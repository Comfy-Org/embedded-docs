# 완카메라이미지투비디오

WanCameraImageToVideo는 이미지에서 비디오 생성을 위한 컨디셔닝 및 잠재(latent) 데이터를 준비합니다. 이 노드는 긍정 및 부정 컨디셔닝 프롬프트와 함께 선택적 시작 이미지 및 카메라 컨트롤을 입력받아, 수정된 컨디셔닝과 비디오 모델이 채울 수 있는 빈 잠재 텐서를 출력합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 비디오 생성을 위한 긍정 컨디셔닝 프롬프트 | CONDITIONING | 예 | - |
| `negative` | 비디오 생성에서 피해야 할 부정 컨디셔닝 프롬프트 | CONDITIONING | 예 | - |
| `vae` | 이미지를 잠재 공간으로 인코딩하기 위한 VAE 모델 | VAE | 예 | - |
| `width` | 출력 비디오 너비(픽셀 단위) (기본값: 832, 간격: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `height` | 출력 비디오 높이(픽셀 단위) (기본값: 480, 간격: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `length` | 비디오 시퀀스의 프레임 수 (기본값: 81, 간격: 4) | INT | 예 | 1 to MAX_RESOLUTION |
| `batch_size` | 동시에 생성할 비디오 수 (기본값: 1) | INT | 예 | 1 to 4096 |
| `clip_vision_output` | 추가 컨디셔닝을 위한 선택적 CLIP 비전 출력 | CLIP_VISION_OUTPUT | 아니요 | - |
| `start_image` | 선택적 시작 이미지로, 비디오 시퀀스를 초기화합니다. 제공된 경우 비디오의 첫 번째 프레임은 이 이미지를 기반으로 하며, 시작 프레임과 생성된 콘텐츠를 혼합하기 위해 마스크가 적용됩니다. 이미지는 지정된 너비와 높이에 맞게 크기가 조정됩니다. | IMAGE | 아니요 | - |
| `camera_conditions` | 비디오 생성을 위한 선택적 카메라 임베딩 조건입니다. 제공된 경우 이 조건은 긍정 및 부정 컨디셔닝 모두에 적용됩니다. | WAN_CAMERA_EMBEDDING | 아니요 | - |

**참고:** `start_image`가 제공되면 노드는 이를 사용하여 비디오 시퀀스를 초기화하고 시작 프레임과 생성된 콘텐츠를 혼합하기 위해 마스킹을 적용합니다. `camera_conditions` 및 `clip_vision_output` 매개변수는 선택 사항이지만 제공되면 긍정 및 부정 프롬프트 모두에 대한 컨디셔닝을 수정합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 카메라 조건, CLIP 비전 출력 및/또는 시작 이미지 데이터가 적용된 수정된 긍정 컨디셔닝 | CONDITIONING |
| `negative` | 카메라 조건, CLIP 비전 출력 및/또는 시작 이미지 데이터가 적용된 수정된 부정 컨디셔닝 | CONDITIONING |
| `latent` | 비디오 모델과 함께 사용하기 위해 생성된 빈 비디오 잠재 표현입니다. 잠재 텐서의 차원은 [batch_size, 16, frames, height/8, width/8]이며, 여기서 frames는 ((length - 1) // 4) + 1로 계산됩니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
