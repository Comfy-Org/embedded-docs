# RemeshMesh

Remesh Mesh는 원본 표면 주변의 좁은 밴드 거리 필드를 샘플링하고 Dual Contouring으로 추출하여 깨끗하고 균일한 테셀레이션으로 메시를 재구성합니다. 이는 지저분하거나 비매니폴드 또는 자기 교차하는 토폴로지를 정규화하며, 정확한 면 개수를 얻기 위해 Decimate Mesh 이전에 실행하도록 설계되었습니다. 처리는 활성 컴퓨트 장치에서 실행되며 출력 메시는 용접된 상태로 유지됩니다.

## 입력

### 공통 입력

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 리메시할 입력 메시입니다. | MESH | 예 | — |
| `resolution` | 복셀 그리드 해상도(출력 밀도)입니다. 256이면 약 10만 개, 512이면 약 100만 개의 면이 생성됩니다. 정확한 면 개수가 필요한 경우 Decimate Mesh를 이어서 실행하세요. (기본값: 512) | INT | 예 | 32 - 2048 |
| `sign_mode` | 표면 추출에 사용되는 부호 거리 모드입니다. "udf"는 지저분하거나 비매니폴드 입력에 강건합니다. "sdf"는 QEF(이차 오차 함수) 날카로운 특징 복원으로 깨끗한 단일 표면을 생성하지만 일관된 와인딩이 필요합니다. 모드를 선택하면 해당 모드의 세부 하위 옵션이 표시됩니다. (기본값: "udf") | DYNAMIC_COMBO | 예 | "udf"<br>"sdf" |
| `band` | 복셀 단위의 좁은 밴드 폭입니다. UDF 모드에서는 표면을 오프셋하기도 합니다. (고급, 기본값: 1.0) | FLOAT | 예 | 0.5 - 4.0 |
| `project_back` | 정점을 원본 표면 쪽으로 선형 보간합니다 (0 = 순수 DC, 1 = 스냅됨). (고급, 기본값: 0.0) | FLOAT | 예 | 0.0 - 1.0 |
| `fix_poles` | 발란스 3 정점 쌍을 붕괴시킵니다(DC T-접합 아티팩트). (고급, 기본값: false) | BOOLEAN | 예 | true / false |
| `smooth_iters` | Taubin 평활화 반복 횟수입니다 (0 = 끄기). 2-3회면 DC 계단형 아티팩트를 정리하지만, 더 높은 값은 QEF 모서리를 과도하게 평활화합니다. (기본값: 0) | INT | 예 | 0 - 20 |
| `drop_small_components` | 가장 큰 구성 요소의 면 수 대비 이 비율 미만의 구성 요소를 제거합니다. 0이면 비활성화됩니다. (고급, 기본값: 0.01) | FLOAT | 예 | 0.0 - 0.5 |
| `precluster_max_verts` | 필드 쿼리 전에 입력 정점 수를 제한합니다. 이 값을 초과하는 입력은 먼저 클러스터 감소되어 이 값으로 줄어듭니다. 거대한 메시에서 OOM(메모리 부족)을 방지합니다. (고급, 기본값: 20,000,000) | INT | 예 | 0 - 100,000,000 |

### "udf" 모드 입력

이 매개변수들은 `sign_mode`가 `"udf"`로 설정된 경우 표시됩니다.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `qef` | 더 선명한 모서리를 위한 QEF(이차 오차 함수) 이중 정점 배치입니다. (기본값: false) | BOOLEAN | 아니요 | true / false |
| `drop_inverted_components` | 안쪽 법선(음수 부피) 폐쇄 구성 요소, 즉 UDF 내부 셸을 제거합니다. (기본값: false) | BOOLEAN | 아니요 | true / false |
| `drop_enclosed_components` | 가장 큰 구성 요소의 경계 상자 내부에 있으면서 메시 내부 점 판정(레이캐스트)을 통과하지 못하는 구성 요소를 제거합니다. 정당한 중첩 부품이 있는 경우 비활성화하세요. (기본값: false) | BOOLEAN | 아니요 | true / false |

### "sdf" 모드 입력

이 매개변수들은 `sign_mode`가 `"sdf"`로 설정된 경우 표시됩니다.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `qef` | QEF(이차 오차 함수) 이중 정점 배치(날카로운 특징 복원)와 모서리 교차 중심점 사이를 선택합니다. (기본값: true) | BOOLEAN | 아니요 | true / false |
| `manifold` | 매니폴드 Dual Contouring: 다중 시트 경우에 대해 복셀당 1-4개의 이중 정점을 생성합니다. 더 느립니다. (기본값: false) | BOOLEAN | 아니요 | true / false |

참고: `qef` 옵션은 선택된 모드에 따라 기본값이 다릅니다. "udf" 모드에서는 false이고 "sdf" 모드에서는 true입니다. `precluster_max_verts`가 0보다 크고 입력 메시의 정점 수가 이 값을 초과하면 필드 쿼리 전에 메시가 해당 목표 값으로 클러스터 감소됩니다. 처리 후 노드는 입력 대비 출력 면 수 변화를 노드에 표시합니다(예: "faces: 1.23M → 200K (-84%)").

## 출력

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `mesh` | 균일한 테셀레이션과 용접된 토폴로지를 가진 리메시된 메시입니다. 입력에 정점 색상이 있는 경우 보존되며, UV, 법선, 탄젠트는 전달되지 않습니다. | MESH |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/ko.md)

---
**Source fingerprint (SHA-256):** `33b9603aad2aa8f4122dab75aa9d60caa0ab7ed81300461f3b773bb997251d99`
