> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/ko.md)

이 문서는 AI가 생성했습니다. 오류를 발견하거나 개선 제안이 있으시면 언제든지 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/en.md)

이 노드는 참조 이미지의 시각적 스타일을 입력 이미지에 적용합니다. 외부 AI 서비스를 사용하여 이미지를 처리하며, 스타일 전이의 강도와 원본 이미지 구조 보존 정도를 제어할 수 있습니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 여부 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 예 | - | 스타일 전이를 적용할 이미지입니다. |
| `reference_image` | IMAGE | 예 | - | 스타일을 추출할 참조 이미지입니다. |
| `prompt` | STRING | 아니요 | - | 스타일 전이를 안내하는 선택적 텍스트 프롬프트입니다. |
| `style_strength` | INT | 아니요 | 0 ~ 100 | 스타일 강도 비율입니다(기본값: 100). |
| `structure_strength` | INT | 아니요 | 0 ~ 100 | 원본 이미지의 구조를 유지하는 정도입니다(기본값: 50). |
| `flavor` | COMBO | 아니요 | "faithful"<br>"gen_z"<br>"psychedelia"<br>"detaily"<br>"clear"<br>"donotstyle"<br>"donotstyle_sharp" | 스타일 전이의 유형입니다. |
| `engine` | COMBO | 아니요 | "balanced"<br>"definio"<br>"illusio"<br>"3d_cartoon"<br>"colorful_anime"<br>"caricature"<br>"real"<br>"super_real"<br>"softy" | 처리 엔진 선택입니다. |
| `portrait_mode` | COMBO | 아니요 | "disabled"<br>"enabled" | 얼굴 향상을 위한 초상화 모드를 활성화합니다. |
| `portrait_style` | COMBO | 아니요 | "standard"<br>"pop"<br>"super_pop" | 초상화 이미지에 적용되는 시각적 스타일입니다. 이 입력은 `portrait_mode`가 "enabled"로 설정된 경우에만 사용할 수 있습니다. |
| `portrait_beautifier` | COMBO | 아니요 | "none"<br>"beautify_face"<br>"beautify_face_max" | 초상화에 적용되는 얼굴 미화 강도입니다. 이 입력은 `portrait_mode`가 "enabled"로 설정된 경우에만 사용할 수 있습니다. |
| `fixed_generation` | BOOLEAN | 아니요 | - | 비활성화하면 각 생성에 일정 수준의 무작위성이 도입되어 더 다양한 결과를 얻을 수 있습니다(기본값: True). |

**제약 사항:**

* 정확히 하나의 `image`와 하나의 `reference_image`가 필요합니다.
* 두 이미지 모두 가로 세로 비율이 1:3에서 3:1 사이여야 합니다.
* 두 이미지 모두 최소 높이와 너비가 160픽셀이어야 합니다.
* `portrait_style` 및 `portrait_beautifier` 매개변수는 `portrait_mode`가 "enabled"로 설정된 경우에만 활성화되며 필수입니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `image` | IMAGE | 스타일 전이가 적용된 결과 이미지입니다. |

---
**Source fingerprint (SHA-256):** `4ae400183618953c369d089d39b878f0a24592967c29d779c577fb8b7339dea8`
