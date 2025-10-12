> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/ko.md)

WanTrackToVideo 노드는 모션 트래킹 데이터를 비디오 시퀀스로 변환합니다. 트랙 포인트를 처리하고 해당 비디오 프레임을 생성하여 동작 좌표를 입력으로 받아 비디오 생성에 사용할 수 있는 비디오 조건화 및 잠재 표현을 출력합니다. 트랙이 제공되지 않을 경우 표준 이미지-비디오 변환으로 폴백(fallback)합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 비디오 생성을 위한 긍정적 조건화 |
| `negative` | CONDITIONING | 예 | - | 비디오 생성을 위한 부정적 조건화 |
| `vae` | VAE | 예 | - | 인코딩 및 디코딩을 위한 VAE 모델 |
| `tracks` | STRING | 예 | - | 여러 줄 문자열 형태의 JSON 형식 트래킹 데이터 (기본값: "[]") |
| `width` | INT | 예 | 16 ~ MAX_RESOLUTION | 출력 비디오 너비 (픽셀 단위) (기본값: 832, 단계: 16) |
| `height` | INT | 예 | 16 ~ MAX_RESOLUTION | 출력 비디오 높이 (픽셀 단위) (기본값: 480, 단계: 16) |
| `length` | INT | 예 | 1 ~ MAX_RESOLUTION | 출력 비디오의 프레임 수 (기본값: 81, 단계: 4) |
| `batch_size` | INT | 예 | 1 ~ 4096 | 동시에 생성할 비디오 수 (기본값: 1) |
| `temperature` | FLOAT | 예 | 1.0 ~ 1000.0 | 모션 패칭(Motion Patching)을 위한 온도 매개변수 (기본값: 220.0, 단계: 0.1) |
| `topk` | INT | 예 | 1 ~ 10 | 모션 패칭을 위한 Top-k 값 (기본값: 2) |
| `start_image` | IMAGE | 아니오 | - | 비디오 생성을 위한 시작 이미지 |
| `clip_vision_output` | CLIPVISIONOUTPUT | 아니오 | - | 추가 조건화를 위한 CLIP 비전 출력 |

**참고:** `tracks`에 유효한 트래킹 데이터가 포함되어 있으면, 노드는 모션 트랙을 처리하여 비디오를 생성합니다. `tracks`가 비어 있으면 표준 이미지-비디오 모드로 전환됩니다. `start_image`가 제공되면 비디오 시퀀스의 첫 번째 프레임을 초기화합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 모션 트랙 정보가 적용된 긍정적 조건화 |
| `negative` | CONDITIONING | 모션 트랙 정보가 적용된 부정적 조건화 |
| `latent` | LATENT | 생성된 비디오의 잠재 표현 |
