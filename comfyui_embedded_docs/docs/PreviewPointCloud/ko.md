# 포인트 클라우드 미리보기

Preview Point Cloud 노드를 사용하면 3D 포인트 클라우드 파일(예: .ply 파일)을 출력 디렉토리에 저장하지 않고 ComfyUI 인터페이스에서 직접 볼 수 있습니다. 이 노드는 포인트 클라우드를 임시 파일에 저장하고 3D 미리보기 창에 표시하며, 모델 데이터, 모델 정보, 카메라 정보, 너비 및 높이를 후속 처리를 위해 그대로 전달합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 포인트 클라우드 파일(.ply) | FILE3D | 예 | - |
| `model_3d_info` | 3D 모델에 대한 정보입니다. 고급 입력입니다. 연결되지 않은 경우 `viewport_state`에 저장된 값이 사용됩니다. | LOAD3DMODELINFO | 아니요 | - |
| `viewport_state` | 현재 뷰포트 상태로, 미리보기에 사용되는 카메라 정보와 모델 정보를 포함할 수 있습니다. | LOAD3D | 예 | - |
| `camera_info` | 3D 뷰에 대한 카메라 정보입니다. 고급 입력입니다. 연결되지 않은 경우 `viewport_state`에 저장된 값이 사용됩니다. | LOAD3DCAMERA | 아니요 | - |
| `width` | 미리보기 창의 너비(픽셀 단위)입니다. 기본값은 1024입니다. | INT | 예 | 1~4096 |
| `height` | 미리보기 창의 높이(픽셀 단위)입니다. 기본값은 1024입니다. | INT | 예 | 1~4096 |

참고: `camera_info` 또는 `model_3d_info`가 연결되지 않은 경우, 노드는 `viewport_state`에 저장된 값을 사용합니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
|-------------|-------------|-----------|
| `model_3d` | 변경 없이 그대로 전달되는 포인트 클라우드 모델 데이터입니다. | FILE3D |
| `model_3d_info` | 미리보기에 사용되는 3D 모델 정보입니다. | LOAD3DMODELINFO |
| `camera_info` | 3D 뷰에 사용되는 카메라 정보입니다. | LOAD3DCAMERA |
| `width` | 미리보기 창의 너비입니다. | INT |
| `height` | 미리보기 창의 높이입니다. | INT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/ko.md)

---
**Source fingerprint (SHA-256):** `a192096df29c4d7029f6e7f4f32e0a2f48de5b3d0cd437bd5b03d79e15eb0987`
