# LTXV 스케줄러

LTXVScheduler 노드는 사용자 정의 샘플링 프로세스를 위한 시그마 값을 생성합니다. 입력 잠재(latent)의 토큰 수를 기반으로 노이즈 일정 매개변수를 계산하고 시그모이드 변환을 적용하여 샘플링 일정을 생성합니다. 이 노드는 선택적으로 결과 시그마를 지정된 종료 값에 맞게 늘릴 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `steps` | 샘플링 단계 수 (기본값: 20) | INT | 예 | 1-10000 |
| `max_shift` | 시그마 계산을 위한 최대 이동 값 (기본값: 2.05) | FLOAT | 예 | 0.0-100.0 |
| `base_shift` | 시그마 계산을 위한 기본 이동 값 (기본값: 0.95) | FLOAT | 예 | 0.0-100.0 |
| `stretch` | 시그마를 [terminal, 1] 범위로 늘립니다 (기본값: True) | BOOLEAN | 예 | True/False |
| `terminal` | 늘린 후 시그마의 종료 값 (기본값: 0.1) | FLOAT | 예 | 0.0-0.99 |
| `latent` | 시그마 조정을 위한 토큰 수를 계산하는 데 사용되는 선택적 잠재 입력 | LATENT | 아니요 | - |

**참고:** `latent` 매개변수는 선택 사항입니다. 제공되지 않으면 노드는 계산에 기본 토큰 수 4096을 사용합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `sigmas` | 샘플링 프로세스를 위해 생성된 시그마 값 | SIGMAS |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/ko.md)

---
**Source fingerprint (SHA-256):** `5b4907e905e27a951c332c400e24023ef089df7a5f4a17b1fc8ba42a41302399`
