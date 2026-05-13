> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/ko.md)

**PairConditioningSetDefaultAndCombine** 노드는 기본 컨디셔닝 값을 설정하고 이를 입력 컨디셔닝 데이터와 결합합니다. 양성 및 음성 컨디셔닝 입력과 해당 기본값을 받아 ComfyUI의 후크 시스템을 통해 처리하여 기본값이 통합된 최종 컨디셔닝 출력을 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 처리할 기본 양성 컨디셔닝 입력입니다. |
| `negative` | CONDITIONING | 예 | - | 처리할 기본 음성 컨디셔닝 입력입니다. |
| `positive_DEFAULT` | CONDITIONING | 예 | - | 대체값으로 사용할 기본 양성 컨디셔닝 값입니다. |
| `negative_DEFAULT` | CONDITIONING | 예 | - | 대체값으로 사용할 기본 음성 컨디셔닝 값입니다. |
| `hooks` | HOOKS | 아니요 | - | 사용자 정의 처리 로직을 위한 선택적 후크 그룹입니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 기본값이 통합되어 처리된 양성 컨디셔닝입니다. |
| `negative` | CONDITIONING | 기본값이 통합되어 처리된 음성 컨디셔닝입니다. |

---
**Source fingerprint (SHA-256):** `dfa47d0fe02e81db8b68d20ae9b765c2518773f4f7fc8caf774cb870267dbb21`
