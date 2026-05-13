> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/ko.md)

# Tripo 이미지-3D 모델 노드

Tripo의 API를 사용하여 단일 이미지를 기반으로 3D 모델을 동기식으로 생성합니다. 이 노드는 입력 이미지를 받아 텍스처, 품질 및 모델 속성에 대한 다양한 사용자 지정 옵션과 함께 3D 모델로 변환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | 3D 모델을 생성하는 데 사용되는 입력 이미지 |
| `model_version` | COMBO | 아니요 | 여러 옵션 사용 가능 | 생성에 사용할 Tripo 모델 버전 |
| `style` | COMBO | 아니요 | 여러 옵션 사용 가능 | 생성된 모델의 스타일 설정 (기본값: "None") |
| `texture` | BOOLEAN | 아니요 | - | 모델에 텍스처를 생성할지 여부 (기본값: True) |
| `pbr` | BOOLEAN | 아니요 | - | 물리 기반 렌더링 사용 여부 (기본값: True) |
| `model_seed` | INT | 아니요 | - | 모델 생성을 위한 난수 시드 (기본값: 42) |
| `orientation` | COMBO | 아니요 | 여러 옵션 사용 가능 | 생성된 모델의 방향 설정 |
| `texture_seed` | INT | 아니요 | - | 텍스처 생성을 위한 난수 시드 (기본값: 42) |
| `texture_quality` | COMBO | 아니요 | "standard"<br>"detailed" | 텍스처 생성 품질 수준 (기본값: "standard") |
| `texture_alignment` | COMBO | 아니요 | "original_image"<br>"geometry" | 텍스처 매핑 정렬 방법 (기본값: "original_image") |
| `face_limit` | INT | 아니요 | -1 ~ 500000 | 생성된 모델의 최대 면 수, -1은 제한 없음 (기본값: -1) |
| `quad` | BOOLEAN | 아니요 | - | 삼각형 대신 사각형 면 사용 여부 (기본값: False) |
| `geometry_quality` | COMBO | 아니요 | "standard"<br>"detailed" | 지오메트리 생성 품질 수준 (기본값: "standard") |

**참고:** `image` 매개변수는 필수이며 노드가 작동하려면 반드시 제공되어야 합니다. 이미지가 제공되지 않으면 노드에서 RuntimeError가 발생합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model_file` | STRING | 생성된 3D 모델 파일 (하위 호환성 전용) |
| `model task_id` | MODEL_TASK_ID | 모델 생성 과정 추적을 위한 작업 ID |
| `GLB` | FILE3DGLB | GLB 형식으로 생성된 3D 모델 |

---
**Source fingerprint (SHA-256):** `1342de2f9788fac504fa0cfa248d011c04a8874307bb26dac86a7ced43a2809e`
