> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/ko.md)

EasyCache 노드는 모델을 위한 네이티브 캐싱 시스템을 구현하여 샘플링 과정에서 이전에 계산된 단계를 재사용함으로써 성능을 향상시킵니다. 샘플링 타임라인에서 캐시 사용을 시작하고 중지할 시점에 대한 구성 가능한 임계값을 사용하여 모델에 EasyCache 기능을 추가합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | EasyCache를 추가할 모델입니다. |
| `reuse_threshold` | FLOAT | 아니요 | 0.0 - 3.0 | 캐시된 단계를 재사용하기 위한 임계값입니다(기본값: 0.2). |
| `start_percent` | FLOAT | 아니요 | 0.0 - 1.0 | EasyCache 사용을 시작할 상대적 샘플링 단계입니다(기본값: 0.15). |
| `end_percent` | FLOAT | 아니요 | 0.0 - 1.0 | EasyCache 사용을 종료할 상대적 샘플링 단계입니다(기본값: 0.95). |
| `verbose` | BOOLEAN | 아니요 | - | 상세 정보를 로그로 출력할지 여부입니다(기본값: False). |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | EasyCache 기능이 추가된 모델입니다. |

---
**Source fingerprint (SHA-256):** `e9d9bf5ecae8034b562f1a27acf528d1f3241d7d28621beba149d3e9bd66a247`
