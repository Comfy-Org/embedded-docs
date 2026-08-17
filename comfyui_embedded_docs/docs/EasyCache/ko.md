# EasyCache

EasyCache 노드는 샘플링 중 이전에 계산된 단계를 재사용하여 성능을 개선하는 모델용 네이티브 캐싱 시스템을 구현합니다. 이 노드는 샘플링 타임라인에서 캐시 사용을 시작하고 중지할 시점을 구성할 수 있는 임계값을 사용하여 모델에 EasyCache 기능을 추가합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | EasyCache를 추가할 모델입니다. | MODEL | 예 | - |
| `reuse_threshold` | 캐시된 단계를 재사용하기 위한 임계값입니다(기본값: 0.2). | FLOAT | 예 | 0.0 - 3.0 |
| `start_percent` | EasyCache 사용을 시작할 상대적 샘플링 단계입니다(기본값: 0.15). | FLOAT | 예 | 0.0 - 1.0 |
| `end_percent` | EasyCache 사용을 종료할 상대적 샘플링 단계입니다(기본값: 0.95). | FLOAT | 예 | 0.0 - 1.0 |
| `verbose` | 상세 정보를 로그로 기록할지 여부입니다(기본값: False). | BOOLEAN | 예 | - |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `model` | EasyCache가 적용된 모델입니다. | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/ko.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
