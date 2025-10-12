> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/ko.md)

EmptyHunyuanImageLatent 노드는 Hunyuan 이미지 생성 모델과 함께 사용하기 위해 특정 차원의 빈 잠재 텐서를 생성합니다. 이 노드는 워크플로우의 후속 노드에서 처리될 수 있는 빈 시작점을 생성합니다. 노드를 사용하면 잠재 공간의 너비, 높이 및 배치 크기를 지정할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | 예 | 64 ~ MAX_RESOLUTION | 생성될 잠재 이미지의 너비(픽셀 단위) (기본값: 2048, 단계: 32) |
| `height` | INT | 예 | 64 ~ MAX_RESOLUTION | 생성될 잠재 이미지의 높이(픽셀 단위) (기본값: 2048, 단계: 32) |
| `batch_size` | INT | 예 | 1 ~ 4096 | 배치로 생성할 잠재 샘플의 수 (기본값: 1) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Hunyuan 이미지 처리용으로 지정된 차원을 가진 빈 잠재 텐서 |