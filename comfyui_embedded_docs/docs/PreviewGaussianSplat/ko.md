# 스플랫 미리보기

PreviewGaussianSplat 노드를 사용하면 3D 가우시안 스플랫 파일을 출력 디렉토리에 저장하지 않고 ComfyUI 인터페이스에서 직접 미리 볼 수 있습니다. 이 노드는 파일을 임시 폴더에 임시로 저장하고, 3D 미리보기 창에 표시하며, 모델 데이터, 카메라 정보 및 미리보기 크기를 다른 노드로 전달합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 가우시안 스플랫 3D 파일입니다. | FILE3D | 예 | splat, ply, spz, ksplat |
| `model_3d_info` | 3D 모델에 대한 선택적 메타데이터 정보입니다. | LOAD3DMODELINFO | 아니요 | - |
| `viewport_state` | 카메라 및 모델 정보를 포함한 3D 뷰포트의 현재 상태입니다. | LOAD3D | 예 | - |
| `camera_info` | 미리보기에 대한 선택적 카메라 정보입니다. | LOAD3DCAMERA | 아니요 | - |
| `width` | 미리보기 렌더링의 너비(픽셀)입니다 (기본값: 1024). | INT | 예 | 1 to 4096 |
| `height` | 미리보기 렌더링의 높이(픽셀)입니다 (기본값: 1024). | INT | 예 | 1 to 4096 |

참고: `camera_info` 또는 `model_3d_info`가 제공되지 않으면 노드는 `viewport_state`의 해당 값을 대신 사용합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `model_3d` | 입력된 3D 가우시안 스플랫 파일이 변경 없이 전달됩니다. | FILE3D |
| `model_3d_info` | 입력 또는 뷰포트 상태에서 가져온 3D 모델의 메타데이터 정보입니다. | LOAD3DMODELINFO |
| `camera_info` | 입력 또는 뷰포트 상태에서 가져온 미리보기용 카메라 정보입니다. | LOAD3DCAMERA |
| `width` | 미리보기 렌더링의 너비입니다. | INT |
| `height` | 미리보기 렌더링의 높이입니다. | INT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/ko.md)

---
**Source fingerprint (SHA-256):** `7157a0b34d7bda3e7ec86cb2ac09e0e10ff96ea7037bb6c9d6ad2c879fdedbb2`
