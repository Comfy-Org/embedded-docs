> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/ko.md)

# Kling Image to Video Camera Control Node

Kling Image to Video Camera Control Node는 정지 이미지를 영화 같은 동영상으로 변환하며 전문적인 카메라 움직임을 제공합니다. 이 특수한 이미지-동영상 변환 노드를 사용하면 원본 이미지에 초점을 유지하면서 줌, 회전, 팬, 틸트, 1인칭 시점 등 가상 카메라 동작을 제어할 수 있습니다. 현재 카메라 제어는 kling-v1-5 모델의 프로 모드에서 5초 길이로만 지원됩니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | 예 | - | 참조 이미지 - URL 또는 Base64 인코딩 문자열, 10MB를 초과할 수 없으며 해상도는 300*300px 이상, 화면비는 1:2.5 ~ 2.5:1 사이여야 합니다. Base64는 data:image 접두사를 포함하지 않아야 합니다. |
| `프롬프트` | STRING | 예 | - | 긍정적 텍스트 프롬프트 |
| `부정 프롬프트` | STRING | 예 | - | 부정적 텍스트 프롬프트 |
| `cfg 스케일` | FLOAT | 아니오 | 0.0-1.0 | 텍스트 지침의 강도를 제어합니다 (기본값: 0.75) |
| `종횡비` | COMBO | 아니오 | 여러 옵션 사용 가능 | 동영상 화면비 선택 (기본값: 16:9) |
| `카메라 제어` | CAMERA_CONTROL | 예 | - | Kling Camera Controls 노드를 사용하여 생성할 수 있습니다. 동영상 생성 중 카메라 이동과 모션을 제어합니다. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `비디오 ID` | VIDEO | 생성된 동영상 출력 |
| `길이` | STRING | 생성된 동영상의 고유 식별자 |
| `duration` | STRING | 생성된 동영상의 길이 |