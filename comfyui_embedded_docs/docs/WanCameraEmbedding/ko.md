# 완카메라임베딩

WanCameraEmbedding 노드는 카메라 모션 매개변수를 기반으로 Plücker 임베딩을 사용하여 카메라 궤적 임베딩을 생성합니다. 다양한 카메라 움직임을 시뮬레이션하는 카메라 포즈 시퀀스를 생성하고, 이를 비디오 생성 파이프라인에 적합한 임베딩 텐서로 변환합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `camera_pose` | 시뮬레이션할 카메라 움직임의 유형 (기본값: "Static") | COMBO | 예 | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" |
| `width` | 출력의 픽셀 단위 너비 (기본값: 832, 증가 단계: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `height` | 출력의 픽셀 단위 높이 (기본값: 480, 증가 단계: 16) | INT | 예 | 16 to MAX_RESOLUTION |
| `length` | 카메라 궤적 시퀀스의 길이 (기본값: 81, 증가 단계: 4) | INT | 예 | 1 to MAX_RESOLUTION |
| `speed` | 카메라 움직임의 속도 (기본값: 1.0, 증가 단계: 0.1) | FLOAT | 아니오 | 0.0 to 10.0 |
| `fx` | 초점 거리 x 매개변수 (기본값: 0.5, 증가 단계: 0.000000001) | FLOAT | 아니오 | 0.0 to 1.0 |
| `fy` | 초점 거리 y 매개변수 (기본값: 0.5, 증가 단계: 0.000000001) | FLOAT | 아니오 | 0.0 to 1.0 |
| `cx` | 주점 x 좌표 (기본값: 0.5, 증가 단계: 0.01) | FLOAT | 아니오 | 0.0 to 1.0 |
| `cy` | 주점 y 좌표 (기본값: 0.5, 증가 단계: 0.01) | FLOAT | 아니오 | 0.0 to 1.0 |

참고: `fx`, `fy`, `cx`, `cy`는 고급 매개변수입니다. `length` 매개변수는 첫 번째 카메라 프레임이 내부적으로 반복되므로 증가 단계가 4이며, 실제 처리되는 시퀀스 길이는 `length + 3`이 됩니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `camera_embedding` | 궤적 시퀀스를 포함하는 생성된 카메라 임베딩 텐서 | TENSOR |
| `width` | 처리에 사용된 너비 값 | INT |
| `height` | 처리에 사용된 높이 값 | INT |
| `length` | 처리에 사용된 길이 값 | INT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/ko.md)

---
**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`
