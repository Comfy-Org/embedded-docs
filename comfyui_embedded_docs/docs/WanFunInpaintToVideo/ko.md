# WAN 비디오 생성 (Fun Inpaint)

WanFunInpaintToVideo 노드는 시작 이미지와 종료 이미지 사이를 인페인팅하여 비디오 시퀀스를 생성합니다. 긍정 및 부정 컨디셔닝과 선택적 프레임 이미지를 입력받아 비디오 잠재 표현을 생성합니다. 이 노드는 구성 가능한 크기 및 길이 매개변수로 비디오 생성을 처리합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `positive` | 비디오 생성을 위한 긍정 컨디셔닝 프롬프트 | CONDITIONING | 예 | - |
| `negative` | 비디오 생성 시 피해야 할 부정 컨디셔닝 프롬프트 | CONDITIONING | 예 | - |
| `vae` | 인코딩/디코딩 작업을 위한 VAE 모델 | VAE | 예 | - |
| `width` | 출력 비디오 너비(픽셀) (기본값: 832, 단계: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `height` | 출력 비디오 높이(픽셀) (기본값: 480, 단계: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `length` | 비디오 시퀀스의 프레임 수 (기본값: 81, 단계: 4) | INT | 예 | 1 to MAX_RESOLUTION |
| `batch_size` | 배치에서 생성할 비디오 수 (기본값: 1) | INT | 예 | 1 to 4096 |
| `clip_vision_output` | 추가 컨디셔닝을 위한 선택적 CLIP 비전 출력 | CLIP_VISION_OUTPUT | 아니요 | - |
| `start_image` | 비디오 생성을 위한 선택적 시작 프레임 이미지 | IMAGE | 아니요 | - |
| `end_image` | 비디오 생성을 위한 선택적 종료 프레임 이미지 | IMAGE | 아니요 | - |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `positive` | 처리된 긍정 컨디셔닝 출력 | CONDITIONING |
| `negative` | 처리된 부정 컨디셔닝 출력 | CONDITIONING |
| `latent` | 생성된 비디오 잠재 표현 | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/ko.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
