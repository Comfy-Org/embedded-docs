> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/ko.md)

RegexExtract 노드는 정규 표현식을 사용하여 텍스트에서 패턴을 검색합니다. 첫 번째 일치 항목, 모든 일치 항목, 일치 항목의 특정 그룹, 또는 여러 일치 항목에 걸친 모든 그룹을 찾을 수 있습니다. 이 노드는 대소문자 구분, 다중 행 매칭, dotall 동작을 위한 다양한 정규 표현식 플래그를 지원합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | 예 | - | 패턴을 검색할 입력 텍스트 |
| `regex_pattern` | STRING | 예 | - | 검색할 정규 표현식 패턴 |
| `mode` | COMBO | 예 | "First Match"<br>"All Matches"<br>"First Group"<br>"All Groups" | 추출 모드는 일치 항목의 어떤 부분이 반환되는지 결정합니다 |
| `case_insensitive` | BOOLEAN | 아니오 | - | 매칭 시 대소문자를 무시할지 여부 (기본값: True) |
| `multiline` | BOOLEAN | 아니오 | - | 문자열을 여러 줄로 처리할지 여부 (기본값: False) |
| `dotall` | BOOLEAN | 아니오 | - | 점(.)이 줄바꿈 문자와 일치할지 여부 (기본값: False) |
| `group_index` | INT | 아니오 | 0-100 | 그룹 모드를 사용할 때 추출할 캡처 그룹 인덱스 (기본값: 1) |

**참고:** "First Group" 또는 "All Groups" 모드를 사용할 때, `group_index` 매개변수는 추출할 캡처 그룹을 지정합니다. 그룹 0은 전체 일치 항목을 나타내며, 그룹 1+는 정규 표현식 패턴의 번호가 매겨진 캡처 그룹을 나타냅니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | STRING | 선택한 모드와 매개변수에 기반하여 추출된 텍스트 |
