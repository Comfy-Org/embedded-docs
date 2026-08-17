# Not

Not 노드는 모든 입력 값에 대해 논리 NOT 연산을 수행합니다. 입력 값이 falsy(예: 0, 빈 문자열, None 또는 False)로 간주되면 True를 반환하고, 입력 값이 truthy이면 False를 반환합니다. Python의 표준 진리값 판정 규칙을 사용합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `value` | 반전할 입력 값입니다. 모든 데이터 유형이 허용되며 Python의 진리값 규칙을 사용하여 평가됩니다. | ANY | 예 | Any value |

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
|-------------|-------------|-----------|
| `output` | 입력 값의 논리적 반전입니다. 입력이 falsy이면 True를 반환하고, 입력이 truthy이면 False를 반환합니다. | BOOLEAN |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNotNode/ko.md)

---
**Source fingerprint (SHA-256):** `24bbe667a0800b187d991b24894794e2ce710256200a2667ff391c1e644963a5`
