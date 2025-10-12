> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/ko.md)

PairConditioningSetProperties 노드는 양수와 음수 조건화 쌍의 속성을 동시에 수정할 수 있게 해줍니다. 강도 조정, 조건화 영역 설정, 그리고 선택적 마스킹 또는 타이밍 제어를 두 조건화 입력에 모두 적용하여 수정된 양수 및 음수 조건화 데이터를 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive_NEW` | CONDITIONING | 예 | - | 수정할 양수 조건화 입력 |
| `negative_NEW` | CONDITIONING | 예 | - | 수정할 음수 조건화 입력 |
| `strength` | FLOAT | 예 | 0.0 ~ 10.0 | 조건화에 적용되는 강도 배수 (기본값: 1.0) |
| `set_cond_area` | STRING | 예 | "default"<br>"mask bounds" | 조건화 영역 계산 방식을 결정합니다 |
| `mask` | MASK | 아니오 | - | 조건화 영역을 제한하는 선택적 마스크 |
| `hooks` | HOOKS | 아니오 | - | 고급 조건화 수정을 위한 선택적 후크 그룹 |
| `timesteps` | TIMESTEPS_RANGE | 아니오 | - | 조건화가 적용되는 시점을 제한하는 선택적 타임스텝 범위 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 적용된 속성을 가진 수정된 양수 조건화 |
| `negative` | CONDITIONING | 적용된 속성을 가진 수정된 음수 조건화 |