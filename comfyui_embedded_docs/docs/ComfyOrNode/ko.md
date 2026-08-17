# Or

ComfyOrNode는 여러 입력 값에 대해 논리적 OR 연산을 수행합니다. 제공된 값 중 하나라도 Python의 표준 진리값 규칙에 따라 truthy로 간주되면 `true`를 반환합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `value` | 진리값을 평가할 값입니다. 입력을 더 추가하여 여러 값을 제공할 수 있습니다. 이 값들 중 하나라도 truthy이면 노드는 `true`를 반환합니다. | ANY | 예 | 최소 1개 값; 여러 값 허용 |

**참고:** 이 노드는 최소 1개의 입력 값을 허용합니다. 자동 확장(autogrow) 기능을 사용하여 필요에 따라 입력을 더 추가할 수 있습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `BOOLEAN` | 입력 값 중 하나라도 truthy이면 `true`를 반환하고, 모든 입력 값이 falsy이면 `false`를 반환합니다. | BOOLEAN |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/ko.md)

---
**Source fingerprint (SHA-256):** `f673aa2b0d754f55c51ba9c9ceea7d9de9a21d2e7308bd1281b4d4461243e4ad`
