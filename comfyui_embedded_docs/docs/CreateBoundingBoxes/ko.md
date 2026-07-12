# 바운딩 박스 생성

캔버스에 바운딩 박스를 그립니다. Ideogram 프롬프트 요소, 픽셀 공간 바운딩 박스, 미리보기 이미지를 출력합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `배경` | 캔버스와 미리보기에서 배경으로 사용되는 선택적 이미지입니다. | IMAGE | No | - |
| `bboxes` | Bounding boxes, elements, or a JSON string to initialize the canvas. A new upstream value initializes the canvas; edits made on the canvas take priority and are kept until the upstream value changes again. | BOUNDING_BOX, ARRAY, STRING | No | - |
| `너비` | 캔버스 및 바운딩 박스의 픽셀 그리드 너비입니다. | INT | Yes | 64 to 16384 (step: 16) |
| `높이` | 캔버스 및 바운딩 박스의 픽셀 그리드 높이입니다. | INT | Yes | 64 to 16384 (step: 16) |
| `에디터 상태` | 바운딩 박스를 그리고 각 박스의 유형, 텍스트, 설명, 컬러 팔레트를 설정하세요. 배경 요소부터 시작하고 전경은 마지막에 추가하세요. | BOUNDING_BOXES | Yes | - |
| `last_incoming` | Internal state managed by the canvas: the upstream bboxes value that last initialized it. Leave empty to re-initialize the canvas from the bboxes input on the next run. | BOUNDING_BOXES | No | - |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `preview` | An RGB image showing the canvas with all bounding boxes rendered, including labels, color palette swatches, and descriptive text. | IMAGE |
| `bboxes` | A list of bounding boxes in pixel coordinates, with each box containing x, y, width, and height values. | BOUNDING_BOX |
| `elements` | A structured array of element objects, each containing type, bounding box coordinates (normalized 0-1000), text (for text type), description, and color palette. | ARRAY |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/ko.md)

---
**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`
