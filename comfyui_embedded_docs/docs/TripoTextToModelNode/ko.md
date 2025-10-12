> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/ko.md)

Tripo의 API를 사용하여 텍스트 프롬프트를 기반으로 3D 모델을 동기적으로 생성합니다. 이 노드는 텍스트 설명을 받아 선택적 텍스처 및 재질 속성을 가진 3D 모델을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 예 | - | 3D 모델 생성을 위한 텍스트 설명 (다중 행 입력) |
| `negative_prompt` | STRING | 아니오 | - | 생성된 모델에서 피해야 할 내용에 대한 텍스트 설명 (다중 행 입력) |
| `model_version` | COMBO | 아니오 | 여러 옵션 사용 가능 | 생성을 위해 사용할 Tripo 모델의 버전 |
| `style` | COMBO | 아니오 | 여러 옵션 사용 가능 | 생성된 모델에 대한 스타일 설정 (기본값: "None") |
| `texture` | BOOLEAN | 아니오 | - | 모델에 대한 텍스처를 생성할지 여부 (기본값: True) |
| `pbr` | BOOLEAN | 아니오 | - | PBR(물리 기반 렌더링) 재질을 생성할지 여부 (기본값: True) |
| `image_seed` | INT | 아니오 | - | 이미지 생성을 위한 랜덤 시드 (기본값: 42) |
| `model_seed` | INT | 아니오 | - | 모델 생성을 위한 랜덤 시드 (기본값: 42) |
| `texture_seed` | INT | 아니오 | - | 텍스처 생성을 위한 랜덤 시드 (기본값: 42) |
| `texture_quality` | COMBO | 아니오 | "standard"<br>"detailed" | 텍스처 생성 품질 수준 (기본값: "standard") |
| `face_limit` | INT | 아니오 | -1 ~ 500000 | 생성된 모델의 최대 면 수, -1은 제한 없음 (기본값: -1) |
| `quad` | BOOLEAN | 아니오 | - | 삼각형 대신 사각형 기반 지오메트리를 생성할지 여부 (기본값: False) |

**참고:** `prompt` 매개변수는 필수이며 비워둘 수 없습니다. 프롬프트가 제공되지 않으면 노드에서 오류가 발생합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model_file` | STRING | 생성된 3D 모델 파일 |
| `model task_id` | MODEL_TASK_ID | 모델 생성 프로세스에 대한 고유 작업 식별자 |
