# AutogrowPrefixTestNode

AutogrowPrefixTestNode는 autogrow 입력 기능을 테스트하기 위해 설계된 논리 노드입니다. 동적 개수의 float 입력을 받아 해당 값들을 쉼표로 구분된 문자열로 결합한 뒤, 그 문자열을 출력합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `autogrow` | float 값을 허용하는 동적 입력 그룹입니다. 그룹은 1~10개의 float 입력을 보유할 수 있으며, 노드는 제공된 모든 값을 처리합니다. | FLOAT | 예 | 1~10개 입력 |

**참고:** `autogrow` 입력은 최대 10개까지 float 입력을 추가로 늘릴 수 있는 특수한 동적 입력입니다. 최소 입력 수는 1개입니다. 이 노드의 `min` 및 `max` 값은 각 개별 float의 값 범위가 아니라 그룹에 허용되는 입력 수를 정의합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `output` | 모든 입력 float 값을 쉼표로 구분하여 포함하는 단일 문자열입니다. | STRING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/ko.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
