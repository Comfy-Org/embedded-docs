# ComfySoftSwitchNode

Soft Switch 노드는 부울(boolean) 조건에 따라 두 개의 입력 값 중 하나를 선택합니다. `switch`가 true이면 `on_true` 입력의 값을 출력하고, `switch`가 false이면 `on_false` 입력의 값을 출력합니다. 이 노드는 지연(lazy) 평가 방식으로 설계되었으며, 즉 `switch` 상태에 따라 필요한 입력만 평가합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `switch` | 통과시킬 입력을 결정하는 부울 조건입니다. true이면 `on_true` 입력이 선택되고, false이면 `on_false` 입력이 선택됩니다. | BOOLEAN | 예 | true<br>false |
| `on_false` | `switch` 조건이 false일 때 출력할 값입니다. 이 입력은 선택 사항이지만, `on_false` 또는 `on_true` 중 하나 이상은 연결되어 있어야 합니다. | MATCH_TYPE | 아니요 |  |
| `on_true` | `switch` 조건이 true일 때 출력할 값입니다. 이 입력은 선택 사항이지만, `on_false` 또는 `on_true` 중 하나 이상은 연결되어 있어야 합니다. | MATCH_TYPE | 아니요 |  |

**참고:** `on_false` 및 `on_true` 입력은 노드의 내부 템플릿에 정의된 대로 동일한 데이터 타입이어야 합니다. 노드가 작동하려면 이 두 입력 중 하나 이상이 연결되어 있어야 합니다. 하나의 입력만 연결된 경우, `switch` 상태와 관계없이 해당 값이 출력으로 전달됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `output` | 선택된 값입니다. 연결된 `on_false` 또는 `on_true` 입력의 데이터 타입과 일치합니다. | MATCH_TYPE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/ko.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
