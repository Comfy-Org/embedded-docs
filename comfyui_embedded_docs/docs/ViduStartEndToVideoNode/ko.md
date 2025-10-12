> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/ko.md)

Vidu Start End To Video Generation 노드는 시작 프레임과 종료 프레임 사이의 프레임을 생성하여 비디오를 생성합니다. 텍스트 프롬프트를 사용하여 비디오 생성 과정을 안내하며, 다양한 해상도와 움직임 설정을 가진 여러 비디오 모델을 지원합니다. 이 노드는 처리를 시작하기 전에 시작 프레임과 종료 프레임의 종횡비가 호환되는지 검증합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 예 | `"vidu_q1"`<br>[VideoModelName enum의 다른 모델 값들] | 모델 이름 (기본값: "vidu_q1") |
| `first_frame` | IMAGE | 예 | - | 시작 프레임 |
| `end_frame` | IMAGE | 예 | - | 종료 프레임 |
| `prompt` | STRING | 아니오 | - | 비디오 생성을 위한 텍스트 설명 |
| `duration` | INT | 아니오 | 5-5 | 출력 비디오의 길이(초 단위) (기본값: 5, 5초로 고정됨) |
| `seed` | INT | 아니오 | 0-2147483647 | 비디오 생성을 위한 시드 (0인 경우 랜덤) (기본값: 0) |
| `resolution` | COMBO | 아니오 | `"1080p"`<br>[Resolution enum의 다른 해상도 값들] | 지원되는 값은 모델 및 지속 시간에 따라 다를 수 있음 (기본값: "1080p") |
| `movement_amplitude` | COMBO | 아니오 | `"auto"`<br>[MovementAmplitude enum의 다른 움직임 진폭 값들] | 프레임 내 객체들의 움직임 진폭 (기본값: "auto") |

**참고:** 시작 프레임과 종료 프레임은 호환되는 종횡비를 가져야 합니다 (min_rel=0.8, max_rel=1.25 비율 허용 오차로 검증됨).

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | VIDEO | 생성된 비디오 파일 |