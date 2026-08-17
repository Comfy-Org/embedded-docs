# And

And 노드는 여러 입력 값에 대해 논리 AND 연산을 수행합니다. 제공된 모든 값이 Python의 truthiness 규칙에 따라 참(true)으로 간주될 때만 `true`를 반환합니다. 이 노드는 여러 조건이 모두 충족되었는지 확인할 때 유용합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `values` | 평가할 확장 가능한 값 목록입니다. 노드에서 최소 하나의 값이 필요하며, 노드의 "+" 버튼을 클릭하여 슬롯을 더 추가할 수 있습니다. 각 슬롯은 모든 데이터 유형을 허용합니다. | ANY | 예 | 1개 이상 |

**참고:** 이 노드는 값이 `true`인지 `false`인지 판단할 때 Python의 truthiness 규칙을 사용합니다. 예를 들어, 빈 문자열, 숫자 0, 빈 목록, `None`은 모두 `false`로 간주됩니다. 다른 모든 값은 `true`로 간주됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `BOOLEAN` | 모든 입력 값이 참(true)이면 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다. | BOOLEAN |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/ko.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
