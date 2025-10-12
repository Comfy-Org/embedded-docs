> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/ko.md)

ConditioningSetPropertiesAndCombine 노드는 새로운 조건화 입력의 속성을 기존 조건화 입력에 적용하여 조건화 데이터를 수정합니다. 두 조건화 세트를 결합하면서 새로운 조건화의 강도를 제어하고 조건화 영역이 적용되는 방식을 지정합니다.

## 입력

| 매개변수 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|-----------|-----------|------------|---------|-------|-------------|
| `cond` | CONDITIONING | 필수 | - | - | 수정될 원본 조건화 데이터 |
| `cond_NEW` | CONDITIONING | 필수 | - | - | 적용할 속성을 제공하는 새로운 조건화 데이터 |
| `strength` | FLOAT | 필수 | 1.0 | 0.0 - 10.0 | 새로운 조건화 속성의 강도를 제어합니다 |
| `set_cond_area` | STRING | 필수 | default | ["default", "mask bounds"] | 조건화 영역이 적용되는 방식을 결정합니다 |
| `mask` | MASK | 선택사항 | - | - | 조건화를 적용할 특정 영역을 정의하는 선택적 마스크 |
| `hooks` | HOOKS | 선택사항 | - | - | 사용자 정의 처리를 위한 선택적 훅 함수 |
| `timesteps` | TIMESTEPS_RANGE | 선택사항 | - | - | 조건화가 적용되는 시점을 제어하는 선택적 타임스텝 범위 |

**참고:** `mask`가 제공될 때, `set_cond_area` 매개변수는 "mask bounds"를 사용하여 조건화 적용을 마스크된 영역으로 제한할 수 있습니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 수정된 속성을 가진 결합된 조건화 데이터 |