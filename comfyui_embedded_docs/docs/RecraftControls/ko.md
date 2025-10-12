> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftControls/ko.md)

Recraft 생성을 사용자 정의하기 위한 Recraft Controls를 생성합니다. 이 노드를 사용하면 Recraft 이미지 생성 과정에서 사용될 색상 설정을 구성할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `colors` | COLOR | 아니요 | - | 주요 요소에 대한 색상 설정 |
| `background_color` | COLOR | 아니요 | - | 배경 색상 설정 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `recraft_controls` | CONTROLS | 색상 설정을 포함한 구성된 Recraft 컨트롤 |