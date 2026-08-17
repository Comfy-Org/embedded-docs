# Flux2Scheduler

Flux2Scheduler 노드는 Flux2 모델에 특별히 맞춤화된 디노이징(노이즈 제거) 과정을 위한 일련의 노이즈 레벨(sigmas)을 생성합니다. 이 노드는 디노이징 단계 수와 대상 이미지의 크기에 따라 스케줄을 계산하며, 이 스케줄은 이미지 생성 중 노이즈 제거 진행 과정에 영향을 미칩니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `steps` | 수행할 디노이징 단계 수입니다. 값이 높을수록 일반적으로 더 상세한 결과를 얻을 수 있지만 처리 시간이 더 오래 걸립니다(기본값: 20). | INT | 예 | 1 to 4096 |
| `width` | 생성할 이미지의 너비(픽셀 단위)입니다. 이 값은 노이즈 스케줄 계산에 영향을 미칩니다(기본값: 1024). | INT | 예 | 16 to 16384 (MAX_RESOLUTION) |
| `height` | 생성할 이미지의 높이(픽셀 단위)입니다. 이 값은 노이즈 스케줄 계산에 영향을 미칩니다(기본값: 1024). | INT | 예 | 16 to 16384 (MAX_RESOLUTION) |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `sigmas` | 샘플러의 디노이징 스케줄을 정의하는 일련의 노이즈 레벨 값(sigmas)입니다. 출력에는 단계 수보다 하나 더 많은 값(`steps + 1`)이 포함됩니다. | SIGMAS |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/ko.md)

---
**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`
