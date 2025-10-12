> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/ko.md)

PrimitiveFloat 노드는 워크플로우에서 사용할 수 있는 부동 소수점 숫자 값을 생성합니다. 단일 숫자 입력을 받아 동일한 값을 출력하며, ComfyUI 파이프라인 내에서 다양한 노드 간에 부동 소수점 값을 정의하고 전달할 수 있도록 합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `value` | FLOAT | 예 | -sys.maxsize ~ sys.maxsize | 출력할 부동 소수점 숫자 값 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | FLOAT | 입력된 부동 소수점 숫자 값 |