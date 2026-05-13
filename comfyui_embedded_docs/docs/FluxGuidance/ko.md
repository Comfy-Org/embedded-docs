> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxGuidance/ko.md)

## 입력

| 매개변수 | 데이터 타입 | 설명 |
|----------------|-----------|-------------|
| `조건` | CONDITIONING | 이전 인코딩 또는 처리 단계에서 얻은 입력 조건화 데이터입니다 |
| `지침` | FLOAT | 이미지 생성 시 텍스트 프롬프트의 영향을 제어하며, 0.0에서 100.0 사이로 조정 가능합니다 |

## 출력

| 매개변수 | 데이터 타입 | 설명 |
|----------------|-----------|-------------|
| CONDITIONING | CONDITIONING | 새로운 guidance 값을 포함하는 업데이트된 조건화 데이터입니다 |