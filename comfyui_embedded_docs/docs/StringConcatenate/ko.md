> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringConcatenate/ko.md)

StringConcatenate 노드는 두 개의 텍스트 문자열을 지정된 구분자로 결합하여 하나의 문자열로 만듭니다. 두 개의 입력 문자열과 구분자 문자 또는 문자열을 받아서, 두 입력 사이에 구분자를 삽입하여 연결된 단일 문자열을 출력합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `string_a` | STRING | 예 | - | 연결할 첫 번째 텍스트 문자열 |
| `string_b` | STRING | 예 | - | 연결할 두 번째 텍스트 문자열 |
| `delimiter` | STRING | 아니오 | - | 두 입력 문자열 사이에 삽입할 문자 또는 문자열 (기본값: 빈 문자열) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | STRING | string_a와 string_b 사이에 구분자가 삽입된 결합된 문자열 |
