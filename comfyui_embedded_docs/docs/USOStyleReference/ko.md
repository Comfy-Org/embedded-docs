> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/ko.md)

USOStyleReference 노드는 CLIP 비전 출력에서 인코딩된 이미지 특징을 사용하여 모델에 스타일 참조 패치를 적용합니다. 시각적 입력에서 추출된 스타일 정보를 통합하여 입력 모델의 수정된 버전을 생성하며, 이를 통해 스타일 전이 또는 참조 기반 생성 기능을 가능하게 합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | 스타일 참조 패치를 적용할 기본 모델 |
| `model_patch` | MODEL_PATCH | 예 | - | 스타일 참조 정보를 포함하는 모델 패치 |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 예 | - | CLIP 비전 처리에서 추출된 인코딩된 시각적 특징 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | 적용된 스타일 참조 패치가 포함된 수정된 모델 |
