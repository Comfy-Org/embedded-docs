> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/ko.md)

PairConditioningSetDefaultAndCombine 노드는 기본 조건화 값을 설정하고 입력 조건화 데이터와 결합합니다. 긍정적 및 부정적 조건화 입력과 해당 기본값을 받아 ComfyUI의 훅 시스템을 통해 처리하여 기본값이 포함된 최종 조건화 출력을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 처리할 기본 긍정적 조건화 입력 |
| `negative` | CONDITIONING | 예 | - | 처리할 기본 부정적 조건화 입력 |
| `positive_DEFAULT` | CONDITIONING | 예 | - | 폴백으로 사용될 기본 긍정적 조건화 값 |
| `negative_DEFAULT` | CONDITIONING | 예 | - | 폴백으로 사용될 기본 부정적 조건화 값 |
| `hooks` | HOOKS | 아니오 | - | 사용자 정의 처리 로직을 위한 선택적 훅 그룹 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 기본값이 포함된 처리된 긍정적 조건화 |
| `negative` | CONDITIONING | 기본값이 포함된 처리된 부정적 조건화 |
