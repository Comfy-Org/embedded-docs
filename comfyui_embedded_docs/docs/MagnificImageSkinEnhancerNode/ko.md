> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageSkinEnhancerNode/ko.md)

# Magnific Image Skin Enhancer 노드

Magnific Image Skin Enhancer 노드는 인물 이미지에 특화된 AI 처리를 적용하여 피부 외관을 개선합니다. 세 가지 고유한 모드를 제공하여 각기 다른 향상 목표를 달성할 수 있습니다: 창의적인 예술 효과를 위한 creative 모드, 원본을 보존하는 faithful 모드, 조명이나 사실감 같은 특정 개선을 위한 flexible 모드입니다. 이 노드는 이미지를 외부 API에 업로드하여 처리한 후 향상된 결과를 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | 향상시킬 인물 이미지입니다. |
| `sharpen` | INT | 아니요 | 0 ~ 100 | 선명도 강도 수준입니다(기본값: 0). |
| `smart_grain` | INT | 아니요 | 0 ~ 100 | 스마트 그레인 강도 수준입니다(기본값: 2). |
| `mode` | COMBO | 예 | `"creative"`<br>`"faithful"`<br>`"flexible"` | 사용할 처리 모드입니다. `"creative"`는 예술적 향상, `"faithful"`은 원본 외관 보존, `"flexible"`은 특정 최적화를 위한 모드입니다. |
| `skin_detail` | INT | 아니요 | 0 ~ 100 | 피부 디테일 향상 수준입니다. 이 입력은 `mode`가 `"faithful"`로 설정된 경우에만 사용 가능하며 필수입니다(기본값: 80). |
| `optimized_for` | COMBO | 아니요 | `"enhance_skin"`<br>`"improve_lighting"`<br>`"enhance_everything"`<br>`"transform_to_real"`<br>`"no_make_up"` | 향상 최적화 대상을 지정합니다. 이 입력은 `mode`가 `"flexible"`로 설정된 경우에만 사용 가능하며 필수입니다. |

**제약 사항:**

* 노드는 정확히 하나의 입력 이미지를 받습니다.
* 입력 이미지의 최소 높이와 너비는 160픽셀 이상이어야 합니다.
* 입력 이미지의 종횡비는 1:3에서 3:1 사이여야 합니다(엄격하지 않은 검증).
* `skin_detail` 매개변수는 `mode`가 `"faithful"`로 설정된 경우에만 활성화됩니다.
* `optimized_for` 매개변수는 `mode`가 `"flexible"`로 설정된 경우에만 활성화됩니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `image` | IMAGE | 향상된 인물 이미지입니다. |

---
**Source fingerprint (SHA-256):** `e02cae2e119ddab931b790865889adf53f47a2ebb03d488477c289dfda7204f5`
