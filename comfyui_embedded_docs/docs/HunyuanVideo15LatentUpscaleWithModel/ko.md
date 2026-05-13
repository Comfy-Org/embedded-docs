> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/ko.md)

# Hunyuan Video 15 Latent Upscale With Model 노드

Hunyuan Video 15 Latent Upscale With Model 노드는 잠재 이미지 표현의 해상도를 높입니다. 먼저 선택한 보간 방법을 사용하여 잠재 샘플을 지정된 크기로 업스케일한 후, 전문화된 Hunyuan Video 1.5 업스케일 모델을 사용하여 업스케일된 결과를 정제하여 품질을 개선합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | LATENT_UPSCALE_MODEL | 예 | 해당 없음 | 업스케일된 샘플을 정제하는 데 사용되는 Hunyuan Video 1.5 잠재 업스케일 모델입니다. |
| `samples` | LATENT | 예 | 해당 없음 | 업스케일할 잠재 이미지 표현입니다. |
| `upscale_method` | COMBO | 아니요 | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` | 초기 업스케일 단계에 사용되는 보간 알고리즘입니다(기본값: `"bilinear"`). |
| `width` | INT | 아니요 | 0 ~ 16384 | 업스케일된 잠재의 목표 너비(픽셀 단위)입니다. 0으로 설정하면 목표 높이와 원본 종횡비를 기준으로 너비가 자동 계산됩니다. 최종 출력 너비는 16의 배수입니다(기본값: 1280). |
| `height` | INT | 아니요 | 0 ~ 16384 | 업스케일된 잠재의 목표 높이(픽셀 단위)입니다. 0으로 설정하면 목표 너비와 원본 종횡비를 기준으로 높이가 자동 계산됩니다. 최종 출력 높이는 16의 배수입니다(기본값: 720). |
| `crop` | COMBO | 아니요 | `"disabled"`<br>`"center"` | 업스케일된 잠재를 목표 크기에 맞게 자르는 방식을 결정합니다. |

**크기 참고 사항:** `width`와 `height`가 모두 0으로 설정되면 노드는 입력 `samples`를 변경하지 않고 반환합니다. 하나의 크기만 0으로 설정된 경우, 원본 종횡비를 유지하도록 다른 크기가 계산됩니다. 최종 크기는 항상 최소 64픽셀로 조정되며 16으로 나누어 떨어집니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `LATENT` | LATENT | 업스케일되고 모델로 정제된 잠재 이미지 표현입니다. |

---
**Source fingerprint (SHA-256):** `1de9e157c1a0433f1b3d5ff4d428a1aa392fd65da5e314e6e818ce66495d5ef4`
