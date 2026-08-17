# WanMoveTracksFromCoords

WanMoveTracksFromCoords 노드는 JSON 형식의 좌표 문자열에서 모션 트랙을 생성합니다. 좌표 데이터를 다른 비디오 처리 노드에서 사용할 수 있는 텐서 형식으로 변환하며, 선택적으로 마스크를 적용하여 시간에 따른 트랙의 가시성을 제어할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `track_coords` | 트랙의 좌표 데이터를 포함하는 JSON 형식 문자열입니다. 기본값은 빈 목록(`"[]"`)입니다. | STRING | 아니요 | N/A |
| `track_mask` | 선택적 마스크입니다. 제공되면 노드는 이를 사용하여 프레임별로 각 트랙의 가시성을 결정합니다. 제공되지 않으면 모든 트랙이 모든 프레임에서 표시되는 것으로 간주됩니다. | MASK | 아니요 | N/A |

**참고:** `track_coords` 입력은 특정 JSON 구조를 기대합니다. 트랙 목록이어야 하며, 각 트랙은 프레임 목록이고, 각 프레임은 `x` 및 `y` 좌표를 포함하는 객체입니다. 프레임 수는 모든 트랙에서 일관되어야 합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `tracks` | 생성된 트랙 데이터로, 각 트랙의 경로 좌표와 가시성 정보를 포함합니다. | TRACKS |
| `track_length` | 생성된 트랙의 총 프레임 수입니다. | INT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/ko.md)

---
**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`
