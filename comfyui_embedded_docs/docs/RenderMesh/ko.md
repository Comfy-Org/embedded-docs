# RenderMesh

이 노드는 단일 뷰를 레이캐스팅하여 3D 메시를 2D 이미지로 렌더링합니다. 텍스처가 적용된 메시, 정점 색상, 단색 음영 표면, 표면 법선 또는 깊이를 출력할 수 있습니다. 카메라와 선택적 모델 변환은 Load3D / Preview3D 뷰어에서 가져올 수 있습니다. 카메라가 연결되지 않은 경우 기본 정면 뷰가 자동으로 프레임됩니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 렌더링할 3D 메시입니다. | MESH | 예 | — |
| `mode` | 렌더링할 내용을 지정합니다. auto: 텍스처가 있으면 텍스처, 없으면 정점 색상, 그것도 없으면 단색 음영으로 렌더링합니다. (기본값: "auto") | COMBO | 예 | `"auto"`<br>`"texture"`<br>`"vertex colors"`<br>`"solid"`<br>`"normal"`<br>`"depth"` |
| `width` | 렌더링되는 이미지의 가로 크기(픽셀)입니다. (기본값: 1024) | INT | 예 | 64 to 4096 (step 8) |
| `height` | 렌더링되는 이미지의 세로 크기(픽셀)입니다. (기본값: 1024) | INT | 예 | 64 to 4096 (step 8) |
| `background` | 메시가 덮지 않는 픽셀에 사용되는 배경 색상입니다. (기본값: "#000000") | COLOR | 예 | — |
| `model_3d_info` | 동일한 Load3D / Preview3D 뷰어에서 가져온 모델 변환입니다. 뷰어 프레이밍과 일치시키려면 camera_info와 함께 연결하세요. | LOAD3D_MODEL_INFO | 아니요 | — |
| `camera_info` | Load3D / Preview3D 뷰어 또는 Create Camera Info 노드에서 가져온 카메라입니다. 아무것도 연결되지 않으면 기본 정면 뷰가 자동으로 프레임됩니다. | LOAD3D_CAMERA | 아니요 | — |

참고: 배치된 메시의 첫 번째 항목만 렌더링됩니다. 메시 배치에 항목이 두 개 이상 포함된 경우 노드는 경고를 기록하고 첫 번째 항목을 사용합니다. `texture` 모드에는 메시에 텍스처와 UV가 모두 있어야 하며, `vertex colors` 모드에는 정점 색상이 필요합니다. 선택한 모드에 필요한 데이터가 없으면 노드는 단색 음영 렌더링으로 대체합니다. `model_3d_info`와 `camera_info`는 동일한 Load3D / Preview3D 뷰어에서 함께 연결하여 렌더링이 뷰어 프레이밍과 일치하도록 하는 용도입니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
|-------------|-------------|-----------|
| `image` | 메시의 렌더링된 이미지입니다. | IMAGE |
| `mask` | 메시가 렌더링된 곳은 1.0이고 그 외는 0.0인 마스크입니다. | MASK |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/ko.md)

---
**Source fingerprint (SHA-256):** `d23e85a904520eb2dfed899eb3e6a9cf45c980df00c034503687ac4eccc66ac4`
