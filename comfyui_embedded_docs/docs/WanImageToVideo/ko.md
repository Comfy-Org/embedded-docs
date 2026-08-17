# WAN 비디오 생성 (이미지 → 비디오)

WanImageToVideo 노드는 비디오 생성 작업을 위한 컨디셔닝 및 잠재 표현을 준비합니다. 비디오 생성을 위한 빈 잠재 공간을 생성하고, 선택적으로 시작 이미지와 CLIP 비전 출력을 통합하여 비디오 생성 과정을 안내할 수 있습니다. 이 노드는 제공된 이미지 및 비전 데이터를 기반으로 긍정 및 부정 컨디셔닝 입력을 모두 수정합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 생성을 안내하는 긍정 컨디셔닝 입력 | CONDITIONING | 예 | - |
| `negative` | 생성을 안내하는 부정 컨디셔닝 입력 | CONDITIONING | 예 | - |
| `vae` | 이미지를 잠재 공간으로 인코딩하는 VAE 모델 | VAE | 예 | - |
| `width` | 출력 비디오의 너비 (기본값: 832, 스텝: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `height` | 출력 비디오의 높이 (기본값: 480, 스텝: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `length` | 비디오의 프레임 수 (기본값: 81, 스텝: 4) | INT | 예 | 1 to MAX_RESOLUTION |
| `batch_size` | 배치에서 생성할 비디오 수 (기본값: 1) | INT | 예 | 1 to 4096 |
| `clip_vision_output` | 추가 컨디셔닝을 위한 선택적 CLIP 비전 출력 | CLIP_VISION_OUTPUT | 아니요 | - |
| `start_image` | 비디오 생성을 초기화하는 선택적 시작 이미지. 제공되면 이미지가 지정된 너비와 높이에 맞게 크기가 조정되고, 비디오의 첫 프레임이 이 이미지로 초기화됩니다. 나머지 프레임은 중립 회색(0.5) 값으로 채워집니다. 이미지의 처음 `length` 프레임만 사용됩니다. | IMAGE | 아니요 | - |

**참고:** `start_image`가 제공되면 노드는 VAE를 사용하여 이미지 시퀀스를 인코딩하고 컨디셔닝 입력에 마스크를 적용합니다. 마스크는 시작 이미지로 초기화된 프레임을 제외한 모든 프레임을 덮어, 생성이 제공된 이미지를 기반으로 진행될 수 있게 합니다. `clip_vision_output` 매개변수가 제공되면 긍정 및 부정 입력 모두에 비전 기반 컨디셔닝을 추가합니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `positive` | 이미지 및 비전 데이터가 반영된 수정된 긍정 컨디셔닝 | CONDITIONING |
| `negative` | 이미지 및 비전 데이터가 반영된 수정된 부정 컨디셔닝 | CONDITIONING |
| `latent` | 비디오 생성에 사용할 수 있는 빈 잠재 공간 텐서, 형태: [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `46779f9f2f3da16826b7b547761a96597a3b6b43ce51a9c13367987642f3d5b7`
