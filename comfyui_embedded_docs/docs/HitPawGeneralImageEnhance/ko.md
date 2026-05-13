> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/ko.md)

이 문서는 AI가 생성했습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/en.md)

이 노드는 저해상도 이미지를 업스케일링하여 초고해상도로 향상시키고, 아티팩트와 노이즈를 제거합니다. 외부 API를 사용하여 이미지를 처리하며, 처리 제한을 초과하지 않도록 입력 크기를 자동으로 조정할 수 있습니다. 최대 허용 출력 크기는 4메가픽셀입니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `model` | STRING | 예 | `"generative_portrait"`<br>`"generative"` | 사용할 향상 모델입니다. `generative_portrait` 모델은 인물 사진에 최적화되어 있으며, `generative`는 범용 모델입니다. |
| `image` | IMAGE | 예 | - | 향상할 입력 이미지입니다. |
| `upscale_factor` | INT | 예 | `1`<br>`2`<br>`4` | 이미지 크기를 업스케일링할 배수입니다. 1배는 업스케일링 없음, 2배는 크기를 두 배, 4배는 네 배로 확대합니다. |
| `auto_downscale` | BOOLEAN | 아니요 | - | 출력이 제한을 초과할 경우 입력 이미지를 자동으로 다운스케일링합니다. 활성화하면 노드가 요청된 업스케일링 배수를 적용하기 전에 입력 이미지 크기를 4메가픽셀 출력 제한에 맞게 줄이려고 시도합니다. (기본값: `False`) |

**참고:** 계산된 출력 크기(입력 높이 × 업스케일링 배수 × 입력 너비 × 업스케일링 배수)가 4,000,000픽셀(4MP)을 초과하고 `auto_downscale`이 비활성화된 경우, 노드에서 오류가 발생합니다. `auto_downscale`이 활성화되면 노드는 요청된 업스케일링 배수를 적용하기 전에 입력 이미지를 제한에 맞게 다운스케일링하려고 시도합니다. 2배 이상의 다운스케일링이 필요한 경우, 노드는 대신 업스케일링 배수를 줄입니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `image` | IMAGE | 향상 및 업스케일링된 출력 이미지입니다. |

---
**Source fingerprint (SHA-256):** `29f927d39777acdfba2aad107027672d281c202ec78e04942e405c2cc64fcee4`
