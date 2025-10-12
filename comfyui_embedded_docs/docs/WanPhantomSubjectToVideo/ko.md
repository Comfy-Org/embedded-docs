> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/ko.md)

WanPhantomSubjectToVideo 노드는 조건 입력과 선택적 참조 이미지를 처리하여 비디오 콘텐츠를 생성합니다. 비디오 생성을 위한 잠재 표현을 생성하며, 입력 이미지가 제공될 경우 시각적 지침을 통합할 수 있습니다. 이 노드는 비디오 모델을 위해 시간 차원 연결을 사용하여 조건 데이터를 준비하고, 수정된 조건과 생성된 잠재 비디오 데이터를 출력합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 비디오 생성을 안내하는 긍정적 조건 입력 |
| `negative` | CONDITIONING | 예 | - | 특정 특성을 피하기 위한 부정적 조건 입력 |
| `vae` | VAE | 예 | - | 이미지가 제공될 때 인코딩을 위한 VAE 모델 |
| `width` | INT | 아니오 | 16부터 MAX_RESOLUTION | 출력 비디오 너비 (픽셀 단위, 기본값: 832, 16으로 나누어져야 함) |
| `height` | INT | 아니오 | 16부터 MAX_RESOLUTION | 출력 비디오 높이 (픽셀 단위, 기본값: 480, 16으로 나누어져야 함) |
| `length` | INT | 아니오 | 1부터 MAX_RESOLUTION | 생성된 비디오의 프레임 수 (기본값: 81, 4로 나누어져야 함) |
| `batch_size` | INT | 아니오 | 1부터 4096 | 동시에 생성할 비디오 수 (기본값: 1) |
| `images` | IMAGE | 아니오 | - | 시간 차원 조건을 위한 선택적 참조 이미지 |

**참고:** `images`가 제공될 경우, 지정된 `width`와 `height`에 맞게 자동으로 업스케일되며, 처리에는 처음 `length` 프레임만 사용됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 이미지가 제공될 때 시간 차원 연결이 적용된 수정된 긍정적 조건 |
| `negative_text` | CONDITIONING | 이미지가 제공될 때 시간 차원 연결이 적용된 수정된 부정적 조건 |
| `negative_img_text` | CONDITIONING | 이미지가 제공될 때 시간 차원 연결이 제로화된 부정적 조건 |
| `latent` | LATENT | 지정된 크기와 길이를 가진 생성된 잠재 비디오 표현 |
