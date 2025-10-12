> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/ko.md)

EasyCache 노드는 샘플링 과정에서 이전에 계산된 단계를 재사용하여 성능을 향상시키기 위한 모델용 기본 캐싱 시스템을 구현합니다. 샘플링 타임라인 동안 캐시 사용을 시작하고 중지할 시점에 대한 구성 가능한 임계값을 통해 모델에 EasyCache 기능을 추가합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | EasyCache를 추가할 모델입니다. |
| `reuse_threshold` | FLOAT | 아니오 | 0.0 - 3.0 | 캐시된 단계를 재사용하기 위한 임계값 (기본값: 0.2). |
| `start_percent` | FLOAT | 아니오 | 0.0 - 1.0 | EasyCache 사용을 시작할 상대적 샘플링 단계 (기본값: 0.15). |
| `end_percent` | FLOAT | 아니오 | 0.0 - 1.0 | EasyCache 사용을 종료할 상대적 샘플링 단계 (기본값: 0.95). |
| `verbose` | BOOLEAN | 아니오 | - | 상세 정보를 로깅할지 여부 (기본값: False). |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | EasyCache 기능이 추가된 모델입니다. |