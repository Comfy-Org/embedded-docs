> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/ko.md)

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `name` | STRING | 예 | model_patches 폴더에서 사용 가능한 모든 모델 패치 파일 | model_patches 디렉토리에서 로드할 모델 패치의 파일 이름 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `MODEL_PATCH` | MODEL_PATCH | 워크플로우에서 사용하기 위해 ModelPatcher로 래핑된 로드된 모델 패치 |
