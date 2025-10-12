> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/ko.md)

WanCameraEmbedding 노드는 카메라 모션 매개변수를 기반으로 Plücker 임베딩을 사용하여 카메라 궤적 임베딩을 생성합니다. 다양한 카메라 움직임을 시뮬레이션하는 일련의 카메라 포즈를 생성하고 비디오 생성 파이프라인에 적합한 임베딩 텐서로 변환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `camera_pose` | COMBO | 예 | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" | 시뮬레이션할 카메라 움직임 유형 (기본값: "Static") |
| `width` | INT | 예 | 16 to MAX_RESOLUTION | 출력의 너비 (픽셀 단위) (기본값: 832, 단계: 16) |
| `height` | INT | 예 | 16 to MAX_RESOLUTION | 출력의 높이 (픽셀 단위) (기본값: 480, 단계: 16) |
| `length` | INT | 예 | 1 to MAX_RESOLUTION | 카메라 궤적 시퀀스의 길이 (기본값: 81, 단계: 4) |
| `speed` | FLOAT | 아니오 | 0.0 to 10.0 | 카메라 움직임의 속도 (기본값: 1.0, 단계: 0.1) |
| `fx` | FLOAT | 아니오 | 0.0 to 1.0 | 초점 거리 x 매개변수 (기본값: 0.5, 단계: 0.000000001) |
| `fy` | FLOAT | 아니오 | 0.0 to 1.0 | 초점 거리 y 매개변수 (기본값: 0.5, 단계: 0.000000001) |
| `cx` | FLOAT | 아니오 | 0.0 to 1.0 | 주점 x 좌표 (기본값: 0.5, 단계: 0.01) |
| `cy` | FLOAT | 아니오 | 0.0 to 1.0 | 주점 y 좌표 (기본값: 0.5, 단계: 0.01) |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `camera_embedding` | TENSOR | 생성된 카메라 임베딩 텐서 (궤적 시퀀스를 포함) |
| `width` | INT | 처리에 사용된 너비 값 |
| `height` | INT | 처리에 사용된 높이 값 |
| `length` | INT | 처리에 사용된 길이 값 |
