> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/ko.md)

VideoTriangleCFGGuidance 노드는 비디오 모델에 삼각형 형태의 classifier-free guidance(CFG) 스케일링 패턴을 적용합니다. 이 노드는 최소 CFG 값과 원래 조건부 스케일 사이를 진동하는 삼각파 함수를 사용하여 시간에 따른 조건부 스케일을 수정합니다. 이를 통해 비디오 생성의 일관성과 품질 향상에 도움이 되는 동적 guidance 패턴이 생성됩니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `모델` | MODEL | 예 | - | 삼각형 CFG guidance를 적용할 비디오 모델 |
| `최소 cfg` | FLOAT | 예 | 0.0 - 100.0 | 삼각형 패턴의 최소 CFG 스케일 값 (기본값: 1.0) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `모델` | MODEL | 삼각형 CFG guidance가 적용된 수정된 모델 |