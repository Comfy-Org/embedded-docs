# MoGe 포인트 맵 → 메시

이 노드는 MoGe 포인트 맵을 3D 메시로 변환합니다. MoGe 깊이 추정 노드가 생성한 지오메트리 데이터를 입력으로 받아, 그중 한 이미지를 UV 좌표와 선택적 텍스처가 포함된 메시로 삼각분할합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `moge_geometry` | 포인트 맵, 깊이, 그리고 선택적으로 원본 이미지를 포함하는 MoGe 지오메트리 데이터입니다. | MOGE_GEOMETRY | 예 | N/A |
| `batch_index` | 배치된 MoGe 지오메트리 중 메시로 변환할 이미지를 지정합니다. 이미지별 정점 수가 다르므로 배치를 단일 MESH로 결합할 수 없습니다(기본값: 0). | INT | 예 | 0 to 4096 |
| `decimation` | 정점 스트라이드입니다. 1 = 전체 해상도(기본값: 1). | INT | 예 | 1 to 8 |
| `discontinuity_threshold` | 3x3 깊이 범위가 이 비율을 초과하는 픽셀을 제거합니다. 0 = 비활성화(기본값: 0.04). | FLOAT | 예 | 0.0 to 1.0 |
| `texture` | 원본 이미지를 baseColor 텍스처로 전달합니다(기본값: True). | BOOLEAN | 예 | True/False |

참고: `batch_index`는 제공된 `moge_geometry`의 배치 크기보다 작아야 합니다. 입력 지오메트리에는 포인트 데이터가 포함되어야 하며, 생성된 메시가 비어 있으면 노드는 `discontinuity_threshold = 0`을 제안하는 오류를 반환합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `MESH` | 정점, 면, UV 좌표, 그리고 원본 이미지에서 가져온 선택적 텍스처를 포함한 3D 메시입니다. | MESH |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/ko.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
