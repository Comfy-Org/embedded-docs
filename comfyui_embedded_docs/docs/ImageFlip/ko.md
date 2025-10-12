> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/ko.md)

ImageFlip 노드는 이미지를 다양한 축을 따라 뒤집습니다. 이미지를 x축을 따라 수직으로 또는 y축을 따라 수평으로 뒤집을 수 있습니다. 이 노드는 선택된 방법에 따라 torch.flip 연산을 사용하여 뒤집기 작업을 수행합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | 뒤집을 입력 이미지 |
| `flip_method` | STRING | 예 | "x-axis: vertically"<br>"y-axis: horizontally" | 적용할 뒤집기 방향 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `image` | IMAGE | 뒤집힌 출력 이미지 |
