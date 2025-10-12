> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/ko.md)

이 노드는 객체의 다양한 시점을 보여주는 최대 네 개의 이미지를 처리하여 Tripo의 API를 사용해 동기적으로 3D 모델을 생성합니다. 객체의 정면 이미지와 최소 하나 이상의 추가 시점(좌측, 후면, 또는 우측)이 필요하며, 텍스처 및 재질 옵션을 갖춘 완전한 3D 모델을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | 객체의 정면 뷰 이미지 (필수) |
| `image_left` | IMAGE | 아니오 | - | 객체의 좌측 뷰 이미지 |
| `image_back` | IMAGE | 아니오 | - | 객체의 후면 뷰 이미지 |
| `image_right` | IMAGE | 아니오 | - | 객체의 우측 뷰 이미지 |
| `model_version` | COMBO | 아니오 | 사용 가능한 여러 옵션 | 생성을 위해 사용할 Tripo 모델 버전 |
| `orientation` | COMBO | 아니오 | 사용 가능한 여러 옵션 | 3D 모델에 대한 방향 설정 |
| `texture` | BOOLEAN | 아니오 | - | 모델에 대한 텍스처 생성 여부 (기본값: True) |
| `pbr` | BOOLEAN | 아니오 | - | PBR(물리 기반 렌더링) 재질 생성 여부 (기본값: True) |
| `model_seed` | INT | 아니오 | - | 모델 생성을 위한 랜덤 시드 (기본값: 42) |
| `texture_seed` | INT | 아니오 | - | 텍스처 생성을 위한 랜덤 시드 (기본값: 42) |
| `texture_quality` | COMBO | 아니오 | "standard"<br>"detailed" | 텍스처 생성 품질 수준 (기본값: "standard") |
| `texture_alignment` | COMBO | 아니오 | "original_image"<br>"geometry" | 모델에 텍스처를 정렬하는 방법 (기본값: "original_image") |
| `face_limit` | INT | 아니오 | -1 ~ 500000 | 생성된 모델의 최대 면 수, -1은 제한 없음 (기본값: -1) |
| `quad` | BOOLEAN | 아니오 | - | 삼각형 대신 쿼드 기반 지오메트리 생성 여부 (기본값: False) |

**참고:** 정면 이미지(`image`)는 항상 필수입니다. 멀티뷰 처리를 위해 최소 하나 이상의 추가 시점 이미지(`image_left`, `image_back`, 또는 `image_right`)가 제공되어야 합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model_file` | STRING | 생성된 3D 모델의 파일 경로 또는 식별자 |
| `model task_id` | MODEL_TASK_ID | 모델 생성 과정을 추적하기 위한 작업 식별자 |
