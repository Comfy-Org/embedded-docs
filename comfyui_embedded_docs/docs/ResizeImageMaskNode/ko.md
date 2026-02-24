> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/ko.md)

Resize Image/Mask 노드는 입력 이미지나 마스크의 크기를 변경하는 여러 방법을 제공합니다. 배율에 따른 스케일링, 특정 크기 설정, 다른 입력의 크기에 맞추기, 픽셀 수를 기준으로 조정 등 다양한 방법을 사용하며, 품질을 위해 여러 보간 방법을 활용합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `input` | IMAGE 또는 MASK | 예 | 해당 없음 | 크기를 조정할 이미지 또는 마스크입니다. |
| `resize_type` | COMBO | 예 | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE` | 새로운 크기를 결정하는 데 사용할 방법입니다. 선택한 타입에 따라 필요한 매개변수가 변경됩니다. |
| `multiplier` | FLOAT | 아니요 | 0.01 ~ 8.0 | 스케일링 배율입니다. `resize_type`이 `SCALE_BY`일 때 필요합니다 (기본값: 1.00). |
| `width` | INT | 아니요 | 0 ~ 8192 | 목표 너비(픽셀)입니다. `resize_type`이 `SCALE_DIMENSIONS` 또는 `SCALE_WIDTH`일 때 필요합니다 (기본값: 512). |
| `height` | INT | 아니요 | 0 ~ 8192 | 목표 높이(픽셀)입니다. `resize_type`이 `SCALE_DIMENSIONS` 또는 `SCALE_HEIGHT`일 때 필요합니다 (기본값: 512). |
| `crop` | COMBO | 아니요 | `"disabled"`<br>`"center"` | 가로세로 비율이 일치하지 않을 때 적용할 자르기 방법입니다. `resize_type`이 `SCALE_DIMENSIONS` 또는 `MATCH_SIZE`일 때만 사용 가능합니다 (기본값: "center"). |
| `longer_size` | INT | 아니요 | 0 ~ 8192 | 이미지의 긴 변에 대한 목표 크기입니다. `resize_type`이 `SCALE_LONGER_DIMENSION`일 때 필요합니다 (기본값: 512). |
| `shorter_size` | INT | 아니요 | 0 ~ 8192 | 이미지의 짧은 변에 대한 목표 크기입니다. `resize_type`이 `SCALE_SHORTER_DIMENSION`일 때 필요합니다 (기본값: 512). |
| `megapixels` | FLOAT | 아니요 | 0.01 ~ 16.0 | 목표 총 메가픽셀 수입니다. `resize_type`이 `SCALE_TOTAL_PIXELS`일 때 필요합니다 (기본값: 1.0). |
| `match` | IMAGE 또는 MASK | 아니요 | 해당 없음 | 입력의 크기를 맞출 대상 이미지 또는 마스크입니다. `resize_type`이 `MATCH_SIZE`일 때 필요합니다. |
| `scale_method` | COMBO | 예 | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` | 스케일링에 사용할 보간 알고리즘입니다 (기본값: "area"). |

**참고:** `crop` 매개변수는 `resize_type`이 `SCALE_DIMENSIONS` 또는 `MATCH_SIZE`로 설정된 경우에만 사용 가능하며 관련이 있습니다. `SCALE_WIDTH` 또는 `SCALE_HEIGHT`를 사용할 때는 다른 차원이 원본 가로세로 비율을 유지하도록 자동으로 조정됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `resized` | IMAGE 또는 MASK | 크기가 조정된 이미지 또는 마스크로, 입력의 데이터 타입과 일치합니다. |
