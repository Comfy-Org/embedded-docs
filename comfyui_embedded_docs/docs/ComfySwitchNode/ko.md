> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/ko.md)

Switch 노드는 불리언 조건에 따라 두 가지 가능한 입력 중 하나를 선택합니다. `switch`가 활성화되면 `on_true` 입력을 출력하고, `switch`가 비활성화되면 `on_false` 입력을 출력합니다. 이를 통해 워크플로우에서 조건부 논리를 생성하고 다양한 데이터 경로를 선택할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `switch` | BOOLEAN | 예 | | 출력할 입력을 결정하는 불리언 조건입니다. 활성화(true)되면 `on_true` 입력이 선택됩니다. 비활성화(false)되면 `on_false` 입력이 선택됩니다. |
| `on_false` | MATCH_TYPE | 아니요 | | `switch`가 비활성화(false)되었을 때 출력으로 전달될 데이터입니다. 이 입력은 `switch`가 false일 때만 필요합니다. |
| `on_true` | MATCH_TYPE | 아니요 | | `switch`가 활성화(true)되었을 때 출력으로 전달될 데이터입니다. 이 입력은 `switch`가 true일 때만 필요합니다. |

**입력 요구사항 참고:** `on_false` 및 `on_true` 입력은 조건부로 필수입니다. 노드는 `switch`가 true일 때만 `on_true` 입력을 요청하고, `switch`가 false일 때만 `on_false` 입력을 요청합니다. 두 입력은 모두 동일한 데이터 타입이어야 합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | 선택된 데이터입니다. `switch`가 true이면 `on_true` 입력의 값이, `switch`가 false이면 `on_false` 입력의 값이 출력됩니다. |
