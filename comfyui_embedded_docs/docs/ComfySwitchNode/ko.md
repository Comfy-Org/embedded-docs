# 스위치

Switch 노드는 부울 조건에 따라 두 개의 가능한 입력 중 하나를 선택합니다. `switch`가 활성화되면 `on_true` 입력을 출력하고, `switch`가 비활성화되면 `on_false` 입력을 출력하여 워크플로우에서 조건부 로직을 생성하고 서로 다른 데이터 경로를 선택할 수 있게 합니다. 이 노드는 현재 실험적(experimental) 상태로 표시되어 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `switch` | 통과시킬 입력을 결정하는 부울 조건입니다. 활성화(참)되면 `on_true` 입력이 선택되고, 비활성화(거짓)되면 `on_false` 입력이 선택됩니다. | BOOLEAN | 예 |  |
| `on_false` | `switch`가 비활성화(거짓)되었을 때 출력으로 전달되는 데이터입니다. 이 입력은 `switch`가 거짓일 때만 필요합니다. | MATCH_TYPE | 아니오 |  |
| `on_true` | `switch`가 활성화(참)되었을 때 출력으로 전달되는 데이터입니다. 이 입력은 `switch`가 참일 때만 필요합니다. | MATCH_TYPE | 아니오 |  |

**입력 요구 사항 참고:** `on_false` 및 `on_true` 입력은 조건부로 필요합니다. 노드는 `switch`가 참일 때만 `on_true` 입력을 요청하고, `switch`가 거짓일 때만 `on_false` 입력을 요청합니다. 두 입력은 동일한 데이터 유형이어야 합니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `output` | 선택된 데이터입니다. `switch`가 참이면 `on_true` 입력의 값이고, `switch`가 거짓이면 `on_false` 입력의 값입니다. | MATCH_TYPE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/ko.md)

---
**Source fingerprint (SHA-256):** `d0adda02e7f997f27182cb26e11e934660ae5bd80f3091bed2fed7c981632ce5`
