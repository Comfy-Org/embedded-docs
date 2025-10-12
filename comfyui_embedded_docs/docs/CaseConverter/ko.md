> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CaseConverter/ko.md)

Case Converter 노드는 텍스트 문자열을 다양한 글자 케이스 형식으로 변환합니다. 입력 문자열을 받아 선택된 모드에 따라 변환을 수행하며, 지정된 케이스 형식이 적용된 출력 문자열을 생성합니다. 이 노드는 텍스트의 대소문자를 변경하기 위한 네 가지 다른 케이스 변환 옵션을 지원합니다.

## 입력

| 매개변수 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|-----------|-----------|------------|---------|-------|-------------|
| `string` | STRING | String | - | - | 다른 케이스 형식으로 변환할 텍스트 문자열 |
| `mode` | STRING | Combo | - | ["UPPERCASE", "lowercase", "Capitalize", "Title Case"] | 적용할 케이스 변환 모드: UPPERCASE는 모든 글자를 대문자로 변환, lowercase는 모든 글자를 소문자로 변환, Capitalize는 첫 글자만 대문자로 변환, Title Case는 각 단어의 첫 글자를 대문자로 변환 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | STRING | 지정된 케이스 형식으로 변환된 입력 문자열 |