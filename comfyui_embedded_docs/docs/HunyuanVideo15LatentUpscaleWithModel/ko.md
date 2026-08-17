# Hunyuan Video 15 Latent Upscale With Model

Hunyuan Video 15 Latent Upscale With Model 노드는 잠재 이미지 표현의 해상도를 높입니다. 먼저 선택한 보간 방법을 사용하여 잠재 샘플을 지정된 크기로 업스케일한 다음, 전용 Hunyuan Video 1.5 업스케일 모델을 사용하여 업스케일된 결과를 정제하여 품질을 개선합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
| --- | --- | --- | --- | --- |
| `model` | 업스케일된 샘플을 정제하는 데 사용되는 Hunyuan Video 1.5 잠재 업스케일 모델입니다. | LATENT_UPSCALE_MODEL | 예 | N/A |
| `samples` | 업스케일할 잠재 이미지 표현입니다. | LATENT | 예 | N/A |
| `upscale_method` | 초기 업스케일 단계에서 사용되는 보간 알고리즘입니다(기본값: `"bilinear"`). | COMBO | 아니요 | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `width` | 업스케일된 잠재 표현의 목표 너비(픽셀)입니다. 값이 0이면 목표 높이와 원본 종횡비를 기준으로 너비가 자동으로 계산됩니다. 최종 출력 너비는 16의 배수입니다(기본값: 1280). | INT | 아니요 | 0~16384(간격 8) |
| `height` | 업스케일된 잠재 표현의 목표 높이(픽셀)입니다. 값이 0이면 목표 너비와 원본 종횡비를 기준으로 높이가 자동으로 계산됩니다. 최종 출력 높이는 16의 배수입니다(기본값: 720). | INT | 아니요 | 0~16384(간격 8) |
| `crop` | 업스케일된 잠재 표현을 목표 크기에 맞게 크롭하는 방법을 결정합니다. | COMBO | 아니요 | `"disabled"`<br>`"center"` |

**크기 참고 사항:** `width`와 `height`가 모두 0으로 설정된 경우, 노드는 입력된 `samples`를 변경하지 않고 반환합니다. 한쪽 크기만 0으로 설정된 경우, 원본 종횡비를 유지하도록 다른 쪽 크기가 계산됩니다. 최종 크기는 항상 64픽셀 이상이 되도록 조정되며 16으로 나누어 떨어집니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
| --- | --- | --- |
| `LATENT` | 업스케일과 모델 정제를 거친 잠재 이미지 표현입니다. | LATENT |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/ko.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
