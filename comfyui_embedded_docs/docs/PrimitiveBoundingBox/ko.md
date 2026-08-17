# 바운딩 박스

PrimitiveBoundingBox 노드는 위치와 크기로 정의되는 단순한 사각형 영역을 생성합니다. 이 노드는 왼쪽 위 모서리의 X 및 Y 좌표와 함께 너비 및 높이 값을 입력받아 워크플로우의 다른 노드에서 사용할 수 있는 경계 상자 데이터 구조를 출력합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `x` | 경계 상자의 왼쪽 위 모서리 X 좌표입니다 (기본값: 0). | INT | 예 | 0 to 8192 |
| `y` | 경계 상자의 왼쪽 위 모서리 Y 좌표입니다 (기본값: 0). | INT | 예 | 0 to 8192 |
| `width` | 경계 상자의 너비입니다 (기본값: 512). | INT | 예 | 1 to 8192 |
| `height` | 경계 상자의 높이입니다 (기본값: 512). | INT | 예 | 1 to 8192 |

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `bounding_box` | 정의된 사각형의 `x`, `y`, `width`, `height` 속성을 포함하는 데이터 구조입니다. | BOUNDING_BOX |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/ko.md)

---
**Source fingerprint (SHA-256):** `dc50286b09b8aaf7ff21eb699b9a04317f099b3deedb6cb7d4a1ec7668edeb97`
