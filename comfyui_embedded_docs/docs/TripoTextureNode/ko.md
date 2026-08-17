# Tripo: 텍스처 모델

TripoTextureNode는 Tripo API를 사용하여 텍스처가 적용된 3D 모델을 생성합니다. 이 노드는 모델 작업 ID를 입력받아 PBR 재질, 텍스처 품질 설정, 정렬 방법, 선택적 텍스트 안내 등 다양한 옵션으로 텍스처 생성을 적용합니다. 노드는 Tripo API와 통신하여 텍스처 생성 요청을 처리하고 결과 모델 파일과 작업 ID를 반환합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | 텍스처를 적용할 모델의 작업 ID입니다. | MODEL_TASK_ID | 예 | - |
| `texture` | 텍스처 생성 여부입니다. (기본값: True) | BOOLEAN | 아니요 | - |
| `pbr` | PBR(물리 기반 렌더링) 재질 생성 여부입니다. (기본값: True) | BOOLEAN | 아니요 | - |
| `texture_seed` | 텍스처 생성용 난수 시드입니다. (기본값: 42) | INT | 아니요 | - |
| `texture_quality` | 텍스처 생성 품질 수준입니다. (기본값: "standard"). "detailed" 옵션은 미화 0.20달러, "standard"는 미화 0.10달러입니다. | COMBO | 아니요 | "standard"<br>"detailed" |
| `texture_alignment` | 텍스처 정렬 방법입니다. (기본값: "original_image"). "original_image"는 원본 입력 이미지에 텍스처를 정렬하고, "geometry"는 3D 지오메트리에 정렬합니다. | COMBO | 아니요 | "original_image"<br>"geometry" |
| `texture_prompt` | 텍스처 생성을 위한 선택적 텍스트 안내입니다. 가져온 모델(Tripo: Import Model)의 경우 색상을 추론할 소스 이미지가 없으므로 실제로는 필수입니다. (여러 줄 텍스트 상자, 기본값: 빈 문자열) | STRING | 아니요 | - |

*참고: 이 노드에는 인증 토큰과 API 키가 필요하며, 시스템에서 자동으로 처리됩니다.*

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
|-------------|-------------|-----------|
| `model_file` | 텍스처가 적용된 생성 모델 파일입니다. (하위 호환용으로만 사용) | STRING |
| `model task_id` | 텍스처 생성 과정을 추적하기 위한 작업 ID입니다. | MODEL_TASK_ID |
| `GLB` | 텍스처가 적용된 GLB 형식의 생성된 3D 모델입니다. | FILE3DGLB |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/ko.md)

---
**Source fingerprint (SHA-256):** `a0157b7fa2bb94d174ea5893d7389885180876794032a510642586e310ba30d4`
