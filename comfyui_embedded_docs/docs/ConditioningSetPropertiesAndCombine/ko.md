> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/ko.md)

ConditioningSetPropertiesAndCombine 노드는 기존 컨디셔닝 입력에 새 컨디셔닝 입력의 속성을 적용하여 컨디셔닝 데이터를 수정합니다. 이 노드는 두 컨디셔닝 세트를 결합하면서 새 컨디셔닝의 강도를 제어하고 컨디셔닝 영역이 적용되는 방식을 지정합니다.

## 입력

| 매개변수 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|-----------|-----------|------------|---------|-------|-------------|
| `cond` | CONDITIONING | 필수 | - | - | 수정할 원본 컨디셔닝 데이터 |
| `cond_NEW` | CONDITIONING | 필수 | - | - | 적용할 속성을 제공하는 새 컨디셔닝 데이터 |
| `strength` | FLOAT | 필수 | 1.0 | 0.0 - 10.0 | 새 컨디셔닝 속성의 강도를 제어합니다 |
| `set_cond_area` | STRING | 필수 | default | ["default", "mask bounds"] | 컨디셔닝 영역이 적용되는 방식을 결정합니다 |
| `mask` | MASK | 선택 사항 | - | - | 컨디셔닝을 위한 특정 영역을 정의하는 선택적 마스크 |
| `hooks` | HOOKS | 선택 사항 | - | - | 사용자 지정 처리를 위한 선택적 후크 함수 |
| `timesteps` | TIMESTEPS_RANGE | 선택 사항 | - | - | 컨디셔닝 적용 시점을 제어하는 선택적 타임스텝 범위 |

**참고:** `mask`가 제공되면 `set_cond_area` 매개변수에서 "mask bounds"를 사용하여 컨디셔닝 적용을 마스크 영역으로 제한할 수 있습니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 수정된 속성이 적용된 결합 컨디셔닝 데이터 |

---
**Source fingerprint (SHA-256):** `da57eeae428a103cbad77af063419ed0e85aeaa0b8805c8c197df27613477fa8`
