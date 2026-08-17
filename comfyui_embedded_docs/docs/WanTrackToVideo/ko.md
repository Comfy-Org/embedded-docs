# WanTrackToVideo

WanTrackToVideo 노드는 모션 추적 데이터(포인트 궤적)를 사용하여 비디오 생성을 안내합니다. 이 노드는 트랙을 처리하고 선택적으로 시작 이미지와 결합하여, Wan 비디오 모델을 위한 컨디셔닝된 positive 및 negative 출력과 latent 텐서를 생성합니다. 유효한 트랙이 제공되지 않으면 표준 이미지-투-비디오 변환으로 대체됩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 비디오 생성을 위한 긍정 컨디셔닝 | CONDITIONING | 예 | - |
| `negative` | 비디오 생성을 위한 부정 컨디셔닝 | CONDITIONING | 예 | - |
| `vae` | 비디오 프레임 인코딩에 사용되는 VAE 모델 | VAE | 예 | - |
| `tracks` | JSON 형식의 추적 데이터를 담은 멀티라인 문자열 (기본값: "[]") | STRING | 예 | - |
| `width` | 출력 비디오의 픽셀 너비 (기본값: 832, 스텝: 16) | INT | 예 | 16 ~ MAX_RESOLUTION |
| `height` | 출력 비디오의 픽셀 높이 (기본값: 480, 스텝: 16) | INT | 예 | 16 ~ MAX_RESOLUTION |
| `length` | 출력 비디오의 프레임 수 (기본값: 81, 스텝: 4) | INT | 예 | 1 ~ MAX_RESOLUTION |
| `batch_size` | 동시에 생성할 비디오 수 (기본값: 1) | INT | 예 | 1 ~ 4096 |
| `temperature` | 모션 패칭을 위한 고급 온도 매개변수 (기본값: 220.0, 스텝: 0.1) | FLOAT | 예 | 1.0 ~ 1000.0 |
| `topk` | 모션 패칭을 위한 고급 top-k 값 (기본값: 2) | INT | 예 | 1 ~ 10 |
| `start_image` | 비디오 생성의 첫 프레임으로 사용되는 시작 이미지 | IMAGE | 예 | - |
| `clip_vision_output` | 추가 컨디셔닝을 위한 CLIP 비전 출력 | CLIP_VISION_OUTPUT | 아니요 | - |

**참고:**
- `tracks` 입력은 포인트 추적 데이터가 포함된 JSON 문자열 또는 JSON 문자열 목록을 기대합니다. `tracks`가 비어 있거나 구문 분석할 수 없으면 노드는 WanImageToVideo 동작으로 대체됩니다.
- `start_image`가 제공되면 `width` 및 `height`에 맞게 크기가 조정된 후 비디오 시퀀스의 첫 프레임으로 사용됩니다.
- `clip_vision_output`이 제공되면 positive 및 negative 컨디셔닝에 모두 추가됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 모션 트랙 및 선택적 이미지 정보가 적용된 긍정 컨디셔닝 | CONDITIONING |
| `negative` | 모션 트랙 및 선택적 이미지 정보가 적용된 부정 컨디셔닝 | CONDITIONING |
| `latent` | 요청된 비디오 크기, 길이 및 배치 크기에 맞는 0으로 채워진 latent 텐서 | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`
