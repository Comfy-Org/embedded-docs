> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/ko.md)

EmptyCosmosLatentVideo 노드는 지정된 크기의 빈 잠재 비디오 텐서를 생성합니다. 이 노드는 너비, 높이, 길이, 배치 크기 매개변수를 설정할 수 있으며, 비디오 생성 워크플로의 시작점으로 사용할 수 있는 0으로 채워진 잠재 표현을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | 예 | 16 ~ MAX_RESOLUTION | 잠재 비디오의 너비(픽셀 단위) (기본값: 1280, 16으로 나누어져야 함) |
| `height` | INT | 예 | 16 ~ MAX_RESOLUTION | 잠재 비디오의 높이(픽셀 단위) (기본값: 704, 16으로 나누어져야 함) |
| `length` | INT | 예 | 1 ~ MAX_RESOLUTION | 잠재 비디오의 프레임 수 (기본값: 121) |
| `batch_size` | INT | 아니오 | 1 ~ 4096 | 배치로 생성할 잠재 비디오의 수 (기본값: 1) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `samples` | LATENT | 0 값으로 생성된 빈 잠재 비디오 텐서 |