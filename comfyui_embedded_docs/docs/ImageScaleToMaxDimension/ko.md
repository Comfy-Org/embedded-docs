> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/ko.md)

ImageScaleToMaxDimension 노드는 이미지를 원본 종횡비를 유지하면서 지정된 최대 크기 내에 맞도록 크기를 조정합니다. 이미지가 세로 방향인지 가로 방향인지 계산한 후, 더 큰 치수를 목표 크기에 맞추고 더 작은 치수는 비례적으로 조정합니다. 이 노드는 다양한 품질 및 성능 요구 사항에 맞게 여러 가지 업스케일링 방법을 지원합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | 크기를 조정할 입력 이미지 |
| `upscale_method` | STRING | 예 | "area"<br>"lanczos"<br>"bilinear"<br>"nearest-exact"<br>"bicubic" | 이미지 크기 조정에 사용되는 보간 방법 |
| `largest_size` | INT | 예 | 0 ~ 16384 | 크기 조정된 이미지의 최대 치수 (기본값: 512) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `image` | IMAGE | 가장 큰 치수가 지정된 크기와 일치하도록 조정된 이미지 |