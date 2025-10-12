> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/ko.md)

WanVaceToVideo 노드는 비디오 생성 모델을 위한 비디오 조건 데이터를 처리합니다. 긍정적 및 부정적 조건 입력과 비디오 제어 데이터를 받아 비디오 생성을 위한 잠재 표현을 준비합니다. 이 노드는 비디오 업스케일링, 마스킹 및 VAE 인코딩을 처리하여 비디오 모델에 적합한 조건 구조를 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 생성을 안내하는 긍정적 조건 입력 |
| `negative` | CONDITIONING | 예 | - | 생성을 안내하는 부정적 조건 입력 |
| `vae` | VAE | 예 | - | 이미지와 비디오 프레임을 인코딩하는 데 사용되는 VAE 모델 |
| `width` | INT | 예 | 16부터 MAX_RESOLUTION까지 | 출력 비디오 너비 (픽셀) (기본값: 832, 단계: 16) |
| `height` | INT | 예 | 16부터 MAX_RESOLUTION까지 | 출력 비디오 높이 (픽셀) (기본값: 480, 단계: 16) |
| `length` | INT | 예 | 1부터 MAX_RESOLUTION까지 | 비디오의 프레임 수 (기본값: 81, 단계: 4) |
| `batch_size` | INT | 예 | 1부터 4096까지 | 동시에 생성할 비디오 수 (기본값: 1) |
| `strength` | FLOAT | 예 | 0.0부터 1000.0까지 | 비디오 조건을 위한 제어 강도 (기본값: 1.0, 단계: 0.01) |
| `control_video` | IMAGE | 아니오 | - | 제어 조건을 위한 선택적 입력 비디오 |
| `control_masks` | MASK | 아니오 | - | 비디오의 어떤 부분을 수정할지 제어하기 위한 선택적 마스크 |
| `reference_image` | IMAGE | 아니오 | - | 추가 조건을 위한 선택적 참조 이미지 |

**참고:** `control_video`가 제공되면 지정된 너비와 높이에 맞게 업스케일링됩니다. `control_masks`가 제공되면 제어 비디오의 차원과 일치해야 합니다. `reference_image`가 제공되면 VAE를 통해 인코딩되고 잠재 시퀀스 앞에 추가됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 비디오 제어 데이터가 적용된 긍정적 조건 |
| `negative` | CONDITIONING | 비디오 제어 데이터가 적용된 부정적 조건 |
| `latent` | LATENT | 비디오 생성을 위해 준비된 빈 잠재 텐서 |
| `trim_latent` | INT | 참조 이미지가 사용될 때 잘라낼 잠재 프레임 수 |