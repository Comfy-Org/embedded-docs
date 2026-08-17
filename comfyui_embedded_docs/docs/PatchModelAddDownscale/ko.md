# 다운스케일 추가 모델 패치 (Kohya Deep Shrink)

PatchModelAddDownscale 노드는 모델의 특정 블록에 다운스케일링 및 업스케일링 작업을 적용하여 Kohya Deep Shrink 기능을 구현합니다. 처리 중에 중간 특징의 해상도를 줄인 다음 원래 크기로 복원하므로 품질을 유지하면서 성능을 향상시킬 수 있습니다. 이 노드는 모델 실행 중 이러한 스케일링 작업이 발생하는 시기와 방법을 정밀하게 제어할 수 있게 합니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 다운스케일 패치를 적용할 모델 | MODEL | 예 | - |
| `block_number` | 다운스케일링이 적용될 특정 블록 번호 (기본값: 3) | INT | 아니요 | 1-32 |
| `downscale_factor` | 특징을 다운스케일링할 배율 (기본값: 2.0) | FLOAT | 아니요 | 0.1-9.0 |
| `start_percent` | 다운스케일링이 시작되는 노이즈 제거 과정의 시작 지점 (기본값: 0.0) | FLOAT | 아니요 | 0.0-1.0 |
| `end_percent` | 다운스케일링이 중지되는 노이즈 제거 과정의 종료 지점 (기본값: 0.35) | FLOAT | 아니요 | 0.0-1.0 |
| `downscale_after_skip` | 스킵 연결 후 다운스케일링을 적용할지 여부 (기본값: True) | BOOLEAN | 아니요 | - |
| `downscale_method` | 다운스케일링 작업에 사용되는 보간 방법 | COMBO | 아니요 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `upscale_method` | 업스케일링 작업에 사용되는 보간 방법 | COMBO | 아니요 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
| --- | --- | --- |
| `model` | 다운스케일 패치가 적용된 수정된 모델 | MODEL |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/ko.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
