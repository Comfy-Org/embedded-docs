# MoGeGeometryToFOV

이 노드는 MoGe 지오메트리 객체에 저장된 카메라 내부 파라미터(intrinsics)로부터 화각(FOV)과 초점 거리를 도출합니다. 세로, 가로 또는 대각선 화각을 도(degrees) 또는 라디안(radians) 단위로 반환할 수 있습니다. 세로 화각 출력은 예를 들어 SAM3DBody_Predict 노드에 입력으로 사용할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `moge_geometry` | MoGe 지오메트리 객체입니다. 초점 거리 변환에 사용할 픽셀 높이를 읽기 위해 내부 파라미터 행렬(intrinsics matrix)과 이미지, 포인트, 또는 깊이 데이터 중 하나 이상을 포함해야 합니다. | MOGE_GEOMETRY | 예 | — |
| `axis` | 화각이 계산되는 축입니다: "vertical"(fov_y), "horizontal"(fov_x), 또는 "diagonal"(기본값: "vertical"). | COMBO | 예 | "vertical"<br>"horizontal"<br>"diagonal" |
| `unit` | 화각의 출력 단위(기본값: "degrees"). | COMBO | 예 | "degrees"<br>"radians" |

참고: `moge_geometry`에 내부 파라미터가 없거나(파노라마 지오메트리에는 내부 파라미터가 없음) 이미지, 포인트, 깊이 데이터 중 어느 것도 포함되지 않은 경우 이 노드는 오류를 발생시킵니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `fov` | 선택한 축을 따라 측정한 화각으로, 선택한 단위(도 또는 라디안)로 표시됩니다. | FLOAT |
| `focal_pixels` | 세로 내부 파라미터와 픽셀 높이에서 도출된 렌즈 초점 거리(픽셀 단위)입니다. | FLOAT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeGeometryToFOV/ko.md)

---
**Source fingerprint (SHA-256):** `983dc984847f93a8e002c73982571ecb38b7bae9c3dc4c201d9be17f785dcaed`
