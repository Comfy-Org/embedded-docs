# ByteDance Seedream 5.0 Pro 레이어 분리

ByteDance Seedream 5.0 Pro 레이어 분리 기능은 이미지를 배경 플레이트와 최대 16개의 투명 레이어로 분해하며, 각 레이어에는 고유한 스태킹 순서, 경계 상자, 이름 및 설명이 포함됩니다. 배경, 레이어별 이미지와 마스크, 배치 상자, 그리고 편집 준비가 완료된 레이어 스택을 반환합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `image` | 분리할 이미지입니다. 정확히 하나의 이미지여야 하며, 최소 512x512픽셀, 종횡비 1:16~16:1이어야 합니다. 약 4MP보다 큰 입력은 업로드 전에 축소됩니다. | IMAGE | 예 | 단일 이미지 |
| `prompt` | 이미지를 분리하는 방법입니다. 비워 두면 주요 요소를 자동 감지하여 분리합니다. 자연어로 요소를 설명하여 분리를 제어하거나, `<bbox>left top right bottom</bbox>` 태그(0-1000 밀리좌표)로 정확한 영역을 지정할 수 있습니다. 기본값: 빈 문자열. | STRING | 예 | 여러 줄 텍스트 |
| `size` | 출력 해상도 수준입니다. "auto"는 입력 이미지 크기를 따릅니다(1K~2K 범위로 제한). 기본값: "auto". | COMBO | 예 | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | 생성에 사용할 시드입니다. 기본값: 0. | INT | 예 | 0 ~ 2147483647 |
| `prompt_optimization` | 프롬프트 최적화 모드입니다. "standard"는 더 높은 품질을, "fast"는 더 짧은 생성 시간을 제공합니다. 기본값: "standard". | COMBO | 아니요 | "standard"<br>"fast" |
| `watermark` | 이미지에 "AI 생성" 워터마크를 추가할지 여부입니다. 기본값: false. | BOOLEAN | 아니요 | false<br>true |
| `crop_layers` | 레이어/마스크 배치 출력의 지오메트리입니다(layer_stack은 영향을 받지 않으며 항상 타이트하게 유지됩니다). 전체 캔버스: 각 레이어가 경계 상자 위치의 기본 크기 캔버스에 배치됩니다. ImageCompositeMasked로 직접 재구성할 수 있습니다. 최소 크기: 각 레이어가 경계 상자로 잘립니다(배칭을 위해 가장 큰 레이어로 패딩됨). 텐서가 훨씬 작아집니다. bboxes 출력과 함께 Layers From Bounding Boxes를 사용하여 배치를 재구성합니다. 기본값: false(전체 캔버스). | BOOLEAN | 아니요 | false (전체 캔버스)<br>true (최소 크기) |

참고: 입력 이미지는 단일 이미지여야 하며 배치는 지원되지 않습니다. 이미지는 최소 512x512픽셀이고 종횡비가 1:16~16:1이어야 합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `base_image` | 레이어가 쌓이는 기본 이미지(배경 플레이트)입니다. | IMAGE |
| `base_mask` | 기본 이미지의 투명도입니다(1 = 투명, LoadImage 규칙). 현재는 항상 완전히 불투명합니다. | MASK |
| `layers` | 아래에서 위로 정렬된 투명 레이어입니다. 전체 캔버스 모드: 경계 상자 위치의 검은색 기본 크기 캔버스에 배치됩니다. 최소 크기 모드: 경계 상자로 잘리고 왼쪽 위를 기준으로 정렬되며 가장 큰 레이어에 맞춰 패딩됩니다. | IMAGE |
| `masks` | 레이어별 투명도로, layers 배치와 인덱스가 정렬됩니다(1 = 투명, LoadImage 규칙). ImageCompositeMasked 스타일 합성을 위해서는 먼저 InvertMask를 추가하세요. | MASK |
| `bboxes` | 레이어별 배치 상자 하나로, layers 배치와 인덱스가 정렬됩니다(둘 모두와 마스크를 Layers From Bounding Boxes에 입력하여 레이어별 배치를 재구성하세요): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]`는 레이어 자체 프레임 내의 콘텐츠 영역이며, 해당 오프셋을 더한 상자 위치에서 캔버스에 배치됩니다. | BOUNDING_BOX |
| `layer_stack` | Create Layered Image용 편집 준비가 된 레이어 문서입니다. 기본 플레이트와 각 요소가 고유한 이름의 타이트 크롭 레이어로 실제 위치 및 스태킹 순서에 따라 포함됩니다. 직접 연결하거나 Add Layer로 확장할 수 있습니다. | LAYERS |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/ko.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`
