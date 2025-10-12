> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/ko.md)

TripoTextureNode는 Tripo API를 사용하여 텍스처가 적용된 3D 모델을 생성합니다. 모델 작업 ID를 입력받아 PBR 재질, 텍스처 품질 설정, 정렬 방법 등 다양한 옵션을 포함한 텍스처 생성을 적용합니다. 이 노드는 Tripo API와 통신하여 텍스처 생성 요청을 처리하고 결과 모델 파일과 작업 ID를 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | 예 | - | 텍스처를 적용할 모델의 작업 ID |
| `texture` | BOOLEAN | 아니오 | - | 텍스처 생성 여부 (기본값: True) |
| `pbr` | BOOLEAN | 아니오 | - | PBR(물리 기반 렌더링) 재질 생성 여부 (기본값: True) |
| `texture_seed` | INT | 아니오 | - | 텍스처 생성을 위한 랜덤 시드 (기본값: 42) |
| `texture_quality` | COMBO | 아니오 | "standard"<br>"detailed" | 텍스처 생성 품질 수준 (기본값: "standard") |
| `texture_alignment` | COMBO | 아니오 | "original_image"<br>"geometry" | 텍스처 정렬 방법 (기본값: "original_image") |

*참고: 이 노드는 시스템에서 자동으로 처리되는 인증 토큰과 API 키가 필요합니다.*

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model_file` | STRING | 텍스처가 적용된 생성된 모델 파일 |
| `model task_id` | MODEL_TASK_ID | 텍스처 생성 과정을 추적하기 위한 작업 ID |