> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/ko.md)

# SDPoseFaceBBoxes

SDPoseFaceBBoxes 노드는 포즈 키포인트 데이터를 처리하여 사람 얼굴 주변의 경계 상자를 감지하고 생성합니다. 프레임 내 각 사람의 2D 얼굴 키포인트를 분석하고, 해당 포인트를 기반으로 경계 상자를 계산하며, 상자의 크기와 모양을 조정할 수 있습니다. 생성된 경계 상자는 SDPoseKeypointExtractor와 같은 SDPose 워크플로우의 다른 노드와 호환되는 형식으로 제공됩니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `keypoints` | POSE_KEYPOINT | 예 | - | 프레임별로 감지된 사람과 그들의 신체/얼굴 랜드마크에 대한 정보를 포함하는 포즈 키포인트 데이터입니다. |
| `scale` | FLOAT | 아니요 | 1.0 - 10.0 | 감지된 각 얼굴 주변 경계 상자 영역의 배율입니다. 값이 클수록 더 큰 상자가 생성됩니다. (기본값: 1.5) |
| `force_square` | BOOLEAN | 아니요 | - | 더 짧은 경계 상자 축을 확장하여 자르기 영역이 항상 정사각형이 되도록 합니다. (기본값: True) |

**참고:** `keypoints` 입력은 SDPoseKeypointExtractor와 같은 노드에서 생성된 특정 형식이어야 하며, 각 사람에 대한 `canvas_height`, `canvas_width`, `people` 데이터와 `face_keypoints_2d`를 포함해야 합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `bboxes` | BOUNDINGBOX | 각 프레임에 대한 얼굴 경계 상자 목록입니다. 각 경계 상자는 왼쪽 상단 좌표(`x`, `y`), `width` 및 `height`로 정의됩니다. 이 출력은 SDPoseKeypointExtractor 노드의 `bboxes` 입력과 호환됩니다. |