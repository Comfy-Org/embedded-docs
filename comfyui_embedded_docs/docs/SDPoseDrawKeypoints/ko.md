# SDPoseDrawKeypoints

SDPoseDrawKeypoints 노드는 포즈 추정 데이터(키포인트)를 가져와 빈 캔버스에 시각적 골격으로 그립니다. 이 노드를 사용하면 몸통, 머리, 손, 얼굴, 발 등 포즈의 여러 부분을 선택적으로 그릴 수 있으며, 선 너비와 점 크기를 사용자 지정할 수 있습니다. 결과 이미지는 시각화에 사용하거나 포즈 이미지가 필요한 다른 노드의 입력으로 사용할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `keypoints` | 그려질 포즈 키포인트 데이터입니다. 이 데이터는 일반적으로 포즈 감지 노드에서 생성됩니다. | POSE_KEYPOINT | 예 | - |
| `draw_body` | 주요 신체 골격을 그릴지 여부를 제어합니다 (기본값: True). | BOOLEAN | 아니요 | - |
| `draw_hands` | 손 키포인트를 그릴지 여부를 제어합니다 (기본값: True). | BOOLEAN | 아니요 | - |
| `draw_face` | 얼굴 키포인트를 그릴지 여부를 제어합니다 (기본값: True). | BOOLEAN | 아니요 | - |
| `draw_feet` | 발 키포인트를 그릴지 여부를 제어합니다 (기본값: False). | BOOLEAN | 아니요 | - |
| `stick_width` | 신체 골격을 그릴 때 사용되는 선의 너비입니다 (기본값: 4). | INT | 아니요 | 1 to 10 |
| `face_point_size` | 얼굴 키포인트를 그릴 때 사용되는 점의 크기입니다 (기본값: 3). | INT | 아니요 | 1 to 10 |
| `score_threshold` | 키포인트가 그려지기 위해 필요한 최소 신뢰 점수입니다. 이 값보다 낮은 점수의 키포인트는 무시됩니다 (기본값: 0.3). | FLOAT | 아니요 | 0.0 to 1.0 |
| `draw_head` | 머리 키포인트(코, 눈, 귀)와 머리 연결선을 그릴지 여부를 제어합니다 (기본값: True). | BOOLEAN | 아니요 | - |

**참고:** `keypoints` 입력이 비어 있거나 `None`인 경우, 노드는 빈 64x64 이미지를 출력합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `output` | 그려진 포즈 키포인트가 포함된 이미지입니다. 이미지 크기는 입력 키포인트 데이터에 지정된 `canvas_height` 및 `canvas_width`와 일치합니다. | IMAGE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/ko.md)

---
**Source fingerprint (SHA-256):** `2b2b9530b55c56e278666bd5d139bb6a1bb503b75b948a89266b9982b5a295e4`
