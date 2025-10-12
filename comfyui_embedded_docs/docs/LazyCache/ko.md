> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/ko.md)

LazyCache는 EasyCache의 자체 제작 버전으로, 더욱 간편한 구현을 제공합니다. ComfyUI의 모든 모델과 호환되며 샘플링 중 계산량을 줄이기 위한 캐싱 기능을 추가합니다. 일반적으로 EasyCache보다 성능이 낮지만, 일부 드문 경우에 더 효과적일 수 있으며 보편적인 호환성을 제공합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | LazyCache를 추가할 모델입니다. |
| `reuse_threshold` | FLOAT | 아니오 | 0.0 - 3.0 | 캐시된 단계를 재사용하기 위한 임계값 (기본값: 0.2). |
| `start_percent` | FLOAT | 아니오 | 0.0 - 1.0 | LazyCache 사용을 시작할 상대적 샘플링 단계 (기본값: 0.15). |
| `end_percent` | FLOAT | 아니오 | 0.0 - 1.0 | LazyCache 사용을 종료할 상대적 샘플링 단계 (기본값: 0.95). |
| `verbose` | BOOLEAN | 아니오 | - | 상세 정보를 기록할지 여부 (기본값: False). |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | LazyCache 기능이 추가된 모델입니다. |