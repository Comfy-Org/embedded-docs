> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/ko.md)

Vidu Image To Video Generation 노드는 시작 이미지와 선택적인 텍스트 설명을 사용하여 비디오를 생성합니다. AI 모델을 활용하여 제공된 이미지 프레임에서 확장되는 비디오 콘텐츠를 생성합니다. 이 노드는 이미지와 매개변수를 외부 서비스로 전송하고 생성된 비디오를 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 예 | `vidu_q1`<br>*기타 VideoModelName 옵션* | 모델 이름 (기본값: vidu_q1) |
| `image` | IMAGE | 예 | - | 생성된 비디오의 시작 프레임으로 사용될 이미지 |
| `prompt` | STRING | 아니오 | - | 비디오 생성을 위한 텍스트 설명 (기본값: 빈 값) |
| `duration` | INT | 아니오 | 5-5 | 출력 비디오의 지속 시간(초) (기본값: 5, 5초로 고정) |
| `seed` | INT | 아니오 | 0-2147483647 | 비디오 생성을 위한 시드 값 (0인 경우 무작위) (기본값: 0) |
| `resolution` | COMBO | 아니오 | `r_1080p`<br>*기타 Resolution 옵션* | 지원되는 값은 모델 및 지속 시간에 따라 다를 수 있음 (기본값: r_1080p) |
| `movement_amplitude` | COMBO | 아니오 | `auto`<br>*기타 MovementAmplitude 옵션* | 프레임 내 객체의 움직임 진폭 (기본값: auto) |

**제약 조건:**

- 하나의 입력 이미지만 허용됨 (여러 이미지 처리 불가)
- 입력 이미지는 1:4에서 4:1 사이의 종횡비를 가져야 함

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 비디오 출력 |
