> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/ko.md)

PatchModelAddDownscale 노드는 모델의 특정 블록에 다운스케일링 및 업스케일링 연산을 적용하여 Kohya Deep Shrink 기능을 구현합니다. 처리 과정에서 중간 특징의 해상도를 낮춘 후 원래 크기로 복원함으로써 품질을 유지하면서 성능을 향상시킬 수 있습니다. 이 노드는 모델 실행 중 이러한 스케일링 연산이 발생하는 시점과 방식을 정밀하게 제어할 수 있도록 합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 예 | - | 다운스케일 패치를 적용할 모델 |
| `block_number` | INT | 아니요 | 1-32 | 다운스케일링이 적용될 특정 블록 번호 (기본값: 3) |
| `downscale_factor` | FLOAT | 아니요 | 0.1-9.0 | 특징을 다운스케일할 비율 (기본값: 2.0) |
| `start_percent` | FLOAT | 아니요 | 0.0-1.0 | 노이즈 제거 과정에서 다운스케일링이 시작되는 지점 (기본값: 0.0) |
| `end_percent` | FLOAT | 아니요 | 0.0-1.0 | 노이즈 제거 과정에서 다운스케일링이 종료되는 지점 (기본값: 0.35) |
| `downscale_after_skip` | BOOLEAN | 아니요 | - | 스킵 연결 후 다운스케일링을 적용할지 여부 (기본값: True) |
| `downscale_method` | COMBO | 아니요 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | 다운스케일링 연산에 사용되는 보간 방법 |
| `upscale_method` | COMBO | 아니요 | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | 업스케일링 연산에 사용되는 보간 방법 |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `model` | MODEL | 다운스케일 패치가 적용된 수정된 모델 |

---
**Source fingerprint (SHA-256):** `93ece77ad2dce3c1cdd554583ae1f2e6be51a43ab072d408869dddbcc7798c40`
