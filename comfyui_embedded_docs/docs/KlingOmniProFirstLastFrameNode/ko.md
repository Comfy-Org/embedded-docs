> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/ko.md)

이 노드는 Kling AI 모델을 사용하여 비디오를 생성합니다. 시작 이미지와 텍스트 프롬프트가 필요합니다. 선택적으로 종료 이미지 또는 최대 6개의 참조 이미지를 제공하여 비디오의 내용과 스타일을 안내할 수 있습니다. 이 노드는 이러한 입력을 처리하여 지정된 지속 시간과 해상도의 비디오를 생성합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | 예 | `"kling-video-o1"` | 비디오 생성에 사용할 특정 Kling AI 모델입니다. |
| `prompt` | STRING | 예 | - | 비디오 내용을 설명하는 텍스트 프롬프트입니다. 긍정적 및 부정적 설명을 모두 포함할 수 있습니다. |
| `duration` | INT | 예 | 3 ~ 10 | 생성할 비디오의 원하는 길이(초 단위)입니다 (기본값: 5). |
| `first_frame` | IMAGE | 예 | - | 비디오 시퀀스의 시작 이미지입니다. |
| `end_frame` | IMAGE | 아니요 | - | 비디오의 선택적 종료 프레임입니다. 이는 `reference_images`와 동시에 사용할 수 없습니다. |
| `reference_images` | IMAGE | 아니요 | - | 최대 6개의 추가 참조 이미지입니다. |
| `resolution` | COMBO | 아니요 | `"1080p"`<br>`"720p"` | 생성된 비디오의 출력 해상도입니다 (기본값: "1080p"). |

**중요 제약사항:**

* `end_frame` 입력은 `reference_images` 입력과 동시에 사용할 수 없습니다.
* `end_frame`이나 `reference_images`를 제공하지 않으면 `duration`은 5초 또는 10초로만 설정할 수 있습니다.
* 모든 입력 이미지(`first_frame`, `end_frame`, `reference_images`)는 너비와 높이 모두 최소 300픽셀의 크기를 가져야 합니다.
* 모든 입력 이미지의 종횡비는 1:2.5에서 2.5:1 사이여야 합니다.
* `reference_images` 입력을 통해 최대 6개의 이미지를 제공할 수 있습니다.
* `prompt` 텍스트는 길이가 1자에서 2500자 사이여야 합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 비디오 파일입니다. |
