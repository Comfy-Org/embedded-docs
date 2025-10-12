> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Regular/ko.md)

Rodin 3D Regular 노드는 Rodin API를 사용하여 3D 에셋을 생성합니다. 입력 이미지를 가져와 Rodin 서비스를 통해 처리하여 3D 모델을 생성합니다. 이 노드는 작업 생성부터 최종 3D 모델 파일 다운로드까지 전체 워크플로를 처리합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | 예 | - | 3D 모델 생성에 사용되는 입력 이미지 |
| `Seed` | INT | 예 | - | 재현 가능한 결과를 위한 랜덤 시드 값 |
| `Material_Type` | STRING | 예 | - | 3D 모델에 적용할 재질 유형 |
| `Polygon_count` | STRING | 예 | - | 생성될 3D 모델의 목표 폴리곤 수 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | 생성된 3D 모델의 파일 경로 |
