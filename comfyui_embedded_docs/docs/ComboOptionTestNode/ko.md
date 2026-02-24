> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/ko.md)

ComboOptionTestNode는 콤보 박스 선택을 테스트하고 통과시키기 위한 논리 노드입니다. 두 개의 콤보 박스 입력을 받으며, 각각 미리 정의된 옵션 세트를 가지고 있습니다. 선택된 값은 수정 없이 직접 출력됩니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `combo` | COMBO | 예 | `"option1"`<br>`"option2"`<br>`"option3"` | 세 가지 테스트 옵션 세트 중 첫 번째 선택입니다. |
| `combo2` | COMBO | 예 | `"option4"`<br>`"option5"`<br>`"option6"` | 다른 세 가지 테스트 옵션 세트 중 두 번째 선택입니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output_1` | COMBO | 첫 번째 콤보 박스(`combo`)에서 선택된 값을 출력합니다. |
| `output_2` | COMBO | 두 번째 콤보 박스(`combo2`)에서 선택된 값을 출력합니다. |
