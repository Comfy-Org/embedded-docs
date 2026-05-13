> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningCombine/ko.md)

PairConditioningCombine 노드는 두 개의 개별 컨디셔닝 쌍(각각 양성 및 음성 컨디셔닝으로 구성)을 하나의 결합된 쌍으로 병합합니다. 서로 다른 두 소스에서 양성 및 음성 컨디셔닝을 가져와 ComfyUI의 내부 로직을 사용하여 결합한 후, 최종적으로 하나의 양성 컨디셔닝과 하나의 음성 컨디셔닝을 출력합니다. 이 노드는 실험적이며 고급 컨디셔닝 조작 워크플로우를 위해 설계되었습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `긍정 조건 A` | CONDITIONING | 예 | - | 첫 번째 양성 컨디셔닝 입력 |
| `부정 조건 A` | CONDITIONING | 예 | - | 첫 번째 음성 컨디셔닝 입력 |
| `긍정 조건 B` | CONDITIONING | 예 | - | 두 번째 양성 컨디셔닝 입력 |
| `부정 조건 B` | CONDITIONING | 예 | - | 두 번째 음성 컨디셔닝 입력 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `부정 조건` | CONDITIONING | 결합된 양성 컨디셔닝 출력 |
| `negative` | CONDITIONING | 결합된 음성 컨디셔닝 출력 |

---
**Source fingerprint (SHA-256):** `34c14207930ba31fea054b2e641e9666e738ed786aa117449c4a27667bde41b1`
