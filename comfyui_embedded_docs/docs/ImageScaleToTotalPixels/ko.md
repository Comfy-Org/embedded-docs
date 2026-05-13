> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToTotalPixels/ko.md)

**ImageScaleToTotalPixels** 노드는 이미지의 가로세로 비율을 유지하면서 지정된 총 픽셀 수로 크기를 조정하도록 설계되었습니다. 원하는 픽셀 수를 달성하기 위해 이미지를 업스케일링하는 다양한 방법을 제공합니다.

## 입력

| 매개변수 | 데이터 타입 | 설명 |
|---|---|---|
| `image` | `IMAGE` | 지정된 총 픽셀 수로 업스케일링할 입력 이미지입니다. |
| `upscale_method` | COMBO[STRING] | 이미지 업스케일링에 사용되는 방법입니다. 업스케일링된 이미지의 품질과 특성에 영향을 미칩니다. |
| `megapixels` | `FLOAT` | 메가픽셀 단위의 대상 이미지 크기입니다. 업스케일링된 이미지의 총 픽셀 수를 결정합니다. |

## 출력

| 매개변수 | 데이터 타입 | 설명 |
|---|---|---|
| `image` | `IMAGE` | 원본 가로세로 비율을 유지하면서 지정된 총 픽셀 수로 업스케일링된 이미지입니다. |