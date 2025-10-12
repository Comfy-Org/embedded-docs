> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/ko.md)

PairConditioningCombine 노드는 두 쌍의 조건화 데이터(긍정적, 부정적)를 단일 쌍으로 결합합니다. 두 개의 별도 조건화 쌍을 입력으로 받아 ComfyUI의 내부 조건화 결합 로직을 사용하여 병합합니다. 이 노드는 실험적이며 주로 고급 조건화 조작 워크플로우에 사용됩니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `긍정 조건 A` | CONDITIONING | 예 | - | 첫 번째 긍정적 조건화 입력 |
| `부정 조건 A` | CONDITIONING | 예 | - | 첫 번째 부정적 조건화 입력 |
| `긍정 조건 B` | CONDITIONING | 예 | - | 두 번째 긍정적 조건화 입력 |
| `부정 조건 B` | CONDITIONING | 예 | - | 두 번째 부정적 조건화 입력 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `부정 조건` | CONDITIONING | 결합된 긍정적 조건화 출력 |
| `negative` | CONDITIONING | 결합된 부정적 조건화 출력 |