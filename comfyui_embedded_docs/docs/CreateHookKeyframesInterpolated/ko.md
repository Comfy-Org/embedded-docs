> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/ko.md)

시작점과 끝점 사이에 보간된 강도 값을 가진 훅 키프레임 시퀀스를 생성합니다. 이 노드는 생성 과정의 지정된 백분율 범위에서 강도 매개변수를 부드럽게 전환하는 여러 키프레임을 생성하며, 다양한 보간 방법을 사용하여 전환 곡선을 제어합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `strength_start` | FLOAT | 예 | 0.0 - 10.0 | 보간 시퀀스의 시작 강도 값 (기본값: 1.0) |
| `strength_end` | FLOAT | 예 | 0.0 - 10.0 | 보간 시퀀스의 끝 강도 값 (기본값: 1.0) |
| `interpolation` | COMBO | 예 | 여러 옵션 사용 가능 | 강도 값 사이를 전환하는 데 사용되는 보간 방법 |
| `start_percent` | FLOAT | 예 | 0.0 - 1.0 | 생성 과정에서의 시작 백분율 위치 (기본값: 0.0) |
| `end_percent` | FLOAT | 예 | 0.0 - 1.0 | 생성 과정에서의 끝 백분율 위치 (기본값: 1.0) |
| `keyframes_count` | INT | 예 | 2 - 100 | 보간 시퀀스에서 생성할 키프레임 수 (기본값: 5) |
| `print_keyframes` | BOOLEAN | 예 | True/False | 생성된 키프레임 정보를 로그에 출력할지 여부 (기본값: False) |
| `prev_hook_kf` | HOOK_KEYFRAMES | 아니오 | - | 추가할 선택적 이전 훅 키프레임 그룹 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | 보간된 시퀀스를 포함하는 생성된 훅 키프레임 그룹 |