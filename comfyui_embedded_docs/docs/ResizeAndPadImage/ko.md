> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeAndPadImage/ko.md)

ResizeAndPadImage 노드는 이미지의 원래 종횡비를 유지하면서 지정된 크기 안에 맞도록 이미지의 크기를 조정합니다. 이미지를 대상 너비와 높이 안에 맞도록 비율에 맞게 축소한 다음, 남은 공간을 채우기 위해 가장자리에 패딩을 추가합니다. 패딩 색상과 보간 방법을 사용자 정의하여 패딩 영역의 모양과 크기 조정 품질을 제어할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | 크기를 조정하고 패딩을 추가할 입력 이미지 |
| `target_width` | INT | 예 | 1 ~ MAX_RESOLUTION | 출력 이미지의 원하는 너비 (기본값: 512) |
| `target_height` | INT | 예 | 1 ~ MAX_RESOLUTION | 출력 이미지의 원하는 높이 (기본값: 512) |
| `padding_color` | COMBO | 예 | "white"<br>"black" | 크기가 조정된 이미지 주변의 패딩 영역에 사용할 색상 |
| `interpolation` | COMBO | 예 | "area"<br>"bicubic"<br>"nearest-exact"<br>"bilinear"<br>"lanczos" | 이미지 크기 조정에 사용되는 보간 방법 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `image` | IMAGE | 크기가 조정되고 패딩이 추가된 출력 이미지 |
