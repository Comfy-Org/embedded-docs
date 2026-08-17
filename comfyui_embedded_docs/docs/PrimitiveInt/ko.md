# 정수

PrimitiveInt 노드는 워크플로우에서 정수 값을 간단하게 처리할 수 있는 방법을 제공합니다. 정수 입력값을 받아 동일한 값을 출력하므로, 노드 간에 정수 매개변수를 전달하거나 다른 작업을 위한 특정 숫자 값을 설정하는 데 유용합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `value` | 출력할 정수 값 (기본값: 0) | INT | 예 | -9223372036854775807 ~ 9223372036854775807 |

참고: `value` 매개변수는 생성 후 고정 제어(control-after-generate) 동작으로 설정되어 있으므로, 각 생성 후 값이 자동으로 변경되지 않습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `output` | 변경 없이 그대로 전달된 입력 정수 값 | INT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveInt/ko.md)

---
**Source fingerprint (SHA-256):** `b928ec40c781043c1c8652de3aebedc755d9b63be9e2c773e3fb26ce4d594bba`
