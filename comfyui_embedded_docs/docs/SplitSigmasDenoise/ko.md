# 시그마 배열 분할 (노이즈 제거양)

SplitSigmasDenoise 노드는 노이즈 제거 강도 매개변수를 기반으로 시그마 값 시퀀스를 두 부분으로 나눕니다. 입력 시그마를 높은 시그마 시퀀스와 낮은 시그마 시퀀스로 분할하며, 분할 지점은 총 단계 수에 denoise 계수를 곱하여 결정됩니다. 이를 통해 노이즈 스케줄을 서로 다른 강도 범위로 분리하여 특수 처리를 수행할 수 있습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
| --- | --- | --- | --- | --- |
| `sigmas` | 노이즈 스케줄을 나타내는 시그마 값의 입력 시퀀스 | SIGMAS | 예 | - |
| `denoise` | 시그마 시퀀스를 분할할 위치를 결정하는 노이즈 제거 강도 계수 (기본값: 1.0) | FLOAT | 예 | 0.0 - 1.0 |

참고: 총 단계 수는 시그마 값 수에서 1을 뺀 값입니다. 두 출력 시퀀스는 분할 지점에서 하나의 시그마 값을 공유합니다. `denoise` = 0.0일 때 `high_sigmas`는 비어 있으며, `denoise` = 1.0일 때 `high_sigmas`는 첫 번째 시그마 값만 포함하고 `low_sigmas`는 전체 시퀀스를 포함합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `high_sigmas` | 더 높은 시그마 값을 포함하는 시그마 시퀀스의 첫 번째 부분 | SIGMAS |
| `low_sigmas` | 더 낮은 시그마 값을 포함하는 시그마 시퀀스의 두 번째 부분 | SIGMAS |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/ko.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
