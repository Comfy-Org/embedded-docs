> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/ko.md)

RegexMatch 노드는 텍스트 문자열에 지정된 정규 표현식 패턴과 일치하는 항목이 있는지 확인합니다. 입력 문자열을 검색하여 패턴이 텍스트 내에서 발견되었는지 여부를 예/아니오 결과로 반환합니다. 대소문자 구분 없음 일치 또는 여러 줄 모드와 같은 옵션을 활성화하여 검색 방식을 조정할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | 예 | - | 일치 항목을 검색할 텍스트 문자열 |
| `regex_pattern` | STRING | 예 | - | 문자열과 일치시킬 정규 표현식 패턴 |
| `case_insensitive` | BOOLEAN | 아니요 | - | 일치 시 대소문자를 무시할지 여부 (기본값: True) |
| `multiline` | BOOLEAN | 아니요 | - | 정규 표현식 일치에 여러 줄 모드를 활성화할지 여부 (기본값: False) |
| `dotall` | BOOLEAN | 아니요 | - | 정규 표현식 일치에 dotall 모드를 활성화할지 여부 (기본값: False) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `matches` | BOOLEAN | 정규 표현식 패턴이 입력 문자열의 일부와 일치하면 True를 반환하고, 그렇지 않으면 False를 반환합니다 |

---
**Source fingerprint (SHA-256):** `b0ee05277edd8600d880051aa33a940c01abc170553515ab02960f25b1aec2be`
