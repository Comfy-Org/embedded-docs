# DecimateMesh

DecimateMesh는 활성 계산 장치에서 계산을 실행하면서 QEM(Quadric Error Metric) 단순화를 사용하여 3D 메시를 목표 면 수로 단순화합니다. `"midpoint"` 배치 모드는 머리카락과 같은 얇은 특징을 보존하면서 최상의 품질을 제공하는 cumesh에 충실한 사전 설정이며, `"qem"`은 선택적 라인 및 특징 가장자리 제어와 함께 QEM 최적 위치에 정점을 배치합니다. 출력 메시는 용접된 상태를 유지합니다.

## 입력

### 공통 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 단순화할 3D 메시입니다. | MESH | 예 | - |
| `target_face_count` | 최대 목표 면 수입니다. 0이면 비활성화됩니다. (기본값: 200000) | INT | 예 | 0 to 50000000 |
| `placement_mode` | midpoint: cumesh에 충실한 (권장). qem: QEM 최적 배치. (기본값: `"midpoint"`) | DYNAMIC_COMBO | 예 | `"midpoint"`<br>`"qem"` |

### Midpoint 입력

`"midpoint"` 배치 모드는 추가 하위 매개변수를 노출하지 않으며 기본 미드포인트 배치 사전 설정을 사용합니다.

### QEM 입력

다음 하위 매개변수는 `placement_mode`가 `"qem"`으로 설정된 경우에만 인터페이스에 나타납니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `line_quadric_weight` | 가장자리별 라인 쿼드릭 가중치입니다. 날카로운 능선/골짜기를 보존합니다. 0 = 비활성화. (기본값: 0.0) | FLOAT | 아니오 | 0.0 to 100.0 |
| `feature_edge_quadric_weight` | 이면각 특징 가장자리(주름)에 대한 추가 쿼드릭 가중치입니다. 0 = 비활성화. (기본값: 0.0) | FLOAT | 아니오 | 0.0 to 1000.0 |
| `feature_edge_min_dihedral_deg` | 가장자리를 특징 가장자리로 간주하기 위한 최소 이면각(도)입니다. (기본값: 30.0) | FLOAT | 아니오 | 0.0 to 180.0 |
| `clamp_v_to_edge` | QEM 최적 위치를 축약된 가장자리 세그먼트에 투영합니다. (기본값: true) | BOOLEAN | 아니오 | `true`<br>`false` |

참고: `target_face_count`가 0이거나 메시에 이미 대상보다 적은 면이 있는 경우 데시메이션은 건너뜁니다. 노드는 자체적으로 면 감소 요약을 표시합니다(예: `faces: 1.23M → 200K (-84%)`).

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `mesh` | 면 수가 줄어든 단순화된 메시입니다. 연결성은 용접된 상태로 유지됩니다. | MESH |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/ko.md)

---
**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`
