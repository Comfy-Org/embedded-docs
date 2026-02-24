> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/ko.md)

Empty Qwen Image Layered Latent 노드는 Qwen 이미지 모델과 함께 사용하기 위해 빈 다중 레이어 잠재 표현을 생성합니다. 이 노드는 지정된 레이어 수, 배치 크기 및 공간 차원으로 구조화된 0으로 채워진 텐서를 생성합니다. 이 빈 잠재 표현은 후속 이미지 생성 또는 조작 워크플로우의 시작점 역할을 합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | 예 | 16 ~ MAX_RESOLUTION | 생성할 잠재 이미지의 너비입니다. 값은 16으로 나누어 떨어져야 합니다. (기본값: 640) |
| `height` | INT | 예 | 16 ~ MAX_RESOLUTION | 생성할 잠재 이미지의 높이입니다. 값은 16으로 나누어 떨어져야 합니다. (기본값: 640) |
| `layers` | INT | 예 | 0 ~ MAX_RESOLUTION | 잠재 구조에 추가할 추가 레이어의 수입니다. 이는 잠재 표현의 깊이를 정의합니다. (기본값: 3) |
| `batch_size` | INT | 아니오 | 1 ~ 4096 | 배치로 생성할 잠재 샘플의 수입니다. (기본값: 1) |

**참고:** `width` 및 `height` 매개변수는 내부적으로 8로 나누어져 출력 잠재 텐서의 공간 차원을 결정합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `samples` | LATENT | 0으로 채워진 잠재 텐서입니다. 형태는 `[batch_size, 16, layers + 1, height // 8, width // 8]`입니다. |
