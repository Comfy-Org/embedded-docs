> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/ko.md)

# PairConditioningSetPropertiesAndCombine 노드

PairConditioningSetPropertiesAndCombine 노드는 기존의 긍정 및 부정 조건화 입력에 새로운 조건화 데이터를 적용하여 조건화 쌍을 수정하고 결합합니다. 적용되는 조건화의 강도를 조정하고 조건화 영역이 설정되는 방식을 제어할 수 있습니다. 이 노드는 여러 조건화 소스를 함께 혼합해야 하는 고급 조건화 조작 워크플로우에서 특히 유용합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 예 | - | 원본 긍정 조건화 입력 |
| `negative` | CONDITIONING | 예 | - | 원본 부정 조건화 입력 |
| `positive_NEW` | CONDITIONING | 예 | - | 적용할 새로운 긍정 조건화 |
| `negative_NEW` | CONDITIONING | 예 | - | 적용할 새로운 부정 조건화 |
| `strength` | FLOAT | 예 | 0.0 ~ 10.0 | 새로운 조건화를 적용하기 위한 강도 계수 (기본값: 1.0) |
| `set_cond_area` | STRING | 예 | "default"<br>"mask bounds" | 조건화 영역이 적용되는 방식을 제어 (기본값: "default") |
| `mask` | MASK | 아니요 | - | 조건화 적용 영역을 제한하는 선택적 마스크 |
| `hooks` | HOOKS | 아니요 | - | 고급 제어를 위한 선택적 후크 그룹 |
| `timesteps` | TIMESTEPS_RANGE | 아니요 | - | 선택적 타임스텝 범위 지정 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 결합된 긍정 조건화 출력 |
| `negative` | CONDITIONING | 결합된 부정 조건화 출력 |

---
**Source fingerprint (SHA-256):** `d434fdc1ccbe3ddee6293a6300cc55d30cb5bf357025b26777791746f51e755e`
