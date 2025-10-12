> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/ko.md)

Vidu Text To Video Generation 노드는 텍스트 설명으로부터 비디오를 생성합니다. 다양한 비디오 생성 모델을 사용하여 텍스트 프롬프트를 비디오 콘텐츠로 변환하며, 지속 시간, 화면 비율 및 시각적 스타일에 대한 사용자 정의 설정을 제공합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 예 | `vidu_q1`<br>*기타 VideoModelName 옵션* | 모델 이름 (기본값: vidu_q1) |
| `prompt` | STRING | 예 | - | 비디오 생성을 위한 텍스트 설명 |
| `duration` | INT | 아니오 | 5-5 | 출력 비디오의 지속 시간(초) (기본값: 5) |
| `seed` | INT | 아니오 | 0-2147483647 | 비디오 생성을 위한 시드 값 (0인 경우 무작위) (기본값: 0) |
| `aspect_ratio` | COMBO | 아니오 | `r_16_9`<br>*기타 AspectRatio 옵션* | 출력 비디오의 화면 비율 (기본값: r_16_9) |
| `resolution` | COMBO | 아니오 | `r_1080p`<br>*기타 Resolution 옵션* | 지원되는 값은 모델 및 지속 시간에 따라 다를 수 있음 (기본값: r_1080p) |
| `movement_amplitude` | COMBO | 아니오 | `auto`<br>*기타 MovementAmplitude 옵션* | 프레임 내 객체의 움직임 진폭 (기본값: auto) |

**참고:** `prompt` 필드는 필수이며 비워둘 수 없습니다. `duration` 매개변수는 현재 5초로 고정되어 있습니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 텍스트 프롬프트를 기반으로 생성된 비디오 |
