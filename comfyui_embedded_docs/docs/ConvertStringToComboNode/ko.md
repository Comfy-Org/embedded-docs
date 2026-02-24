> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConvertStringToComboNode/ko.md)

Convert String to Combo 노드는 텍스트 문자열을 입력으로 받아 Combo 데이터 타입으로 변환합니다. 이를 통해 Combo 입력이 필요한 다른 노드에서 텍스트 값을 선택 항목으로 사용할 수 있습니다. 이 노드는 문자열 값을 변경 없이 그대로 전달하지만, 데이터 타입만 변경합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `string` | STRING | 예 | 해당 없음 | Combo 타입으로 변환할 텍스트 문자열입니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | COMBO | 입력 문자열이 Combo 데이터 타입으로 포맷된 형태입니다. |
