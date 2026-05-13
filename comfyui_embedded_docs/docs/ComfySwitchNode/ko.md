> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/ko.md)

Switch 노드는 불리언 조건에 따라 두 개의 입력 중 하나를 선택합니다. `switch`가 활성화된 경우 `on_true` 입력을 출력하고, `switch`가 비활성화된 경우 `on_false` 입력을 출력합니다. 이를 통해 워크플로우에서 조건부 로직을 생성하고 서로 다른 데이터 경로를 선택할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `switch` | BOOLEAN | 예 | | 통과시킬 입력을 결정하는 불리언 조건입니다. 활성화된 경우(true) `on_true` 입력이 선택됩니다. 비활성화된 경우(false) `on_false` 입력이 선택됩니다. |
| `on_false` | MATCH_TYPE | 아니요 | | `switch`가 비활성화된 경우(false) 출력으로 전달될 데이터입니다. 이 입력은 `switch`가 false일 때만 필요합니다. |
| `on_true` | MATCH_TYPE | 아니요 | | `switch`가 활성화된 경우(true) 출력으로 전달될 데이터입니다. 이 입력은 `switch`가 true일 때만 필요합니다. |

**입력 요구 사항 참고:** `on_false` 및 `on_true` 입력은 조건부로 필요합니다. 노드는 `switch`가 true일 때만 `on_true` 입력을 요청하고, `switch`가 false일 때만 `on_false` 입력을 요청합니다. 두 입력은 동일한 데이터 타입이어야 합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | MATCH_TYPE | 선택된 데이터입니다. `switch`가 true이면 `on_true` 입력의 값이고, `switch`가 false이면 `on_false` 입력의 값입니다. |

---
**Source fingerprint (SHA-256):** `9f3cf58c1a04116fa0cbe8007fe3ed90e93c4de2e65f6778761d03fb21a63af3`
