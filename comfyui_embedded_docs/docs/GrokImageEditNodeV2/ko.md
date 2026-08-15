# Grok 이미지 편집

텍스트 프롬프트를 기반으로 기존 이미지를 수정합니다. 이 노드는 사용자의 이미지와 텍스트 설명을 Grok API로 전송하며, Grok API는 사용자의 지침에 따라 이미지를 편집하고 결과를 반환합니다.

## 입력

### 공통 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `모델` | 사용할 Grok 이미지 모델입니다. 아래 표시되는 하위 매개변수는 선택한 모델에 따라 달라집니다. | MODEL | 예 | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `프롬프트` | 이미지를 생성하는 데 사용되는 텍스트 프롬프트입니다. (기본값: "") | STRING | 예 | N/A |
| `시드` | 노드 재실행 여부를 결정하는 시드입니다. 실제 결과는 시드와 관계없이 비결정적입니다. (기본값: 0) | INT | 예 | 0 ~ 2147483647 |

### grok-imagine-image-2.0 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `images` | 편집할 참조 이미지입니다. 최대 3개까지 가능합니다. | IMAGE | 예 | 1 ~ 3 개 이미지 |
| `resolution` | 편집된 이미지의 출력 해상도입니다. | STRING | 예 | "1K"<br>"2K" |
| `number_of_images` | 생성할 편집 이미지 수입니다. (기본값: 1) | INT | 예 | 1 ~ 10 |
| `quality` | 생성된 이미지의 품질 수준입니다. | STRING | 예 | "medium"<br>"low" |
| `aspect_ratio` | 편집된 이미지의 종횡비입니다. (기본값: "auto") | STRING | 예 | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-quality 및 grok-imagine-image 입력

grok-imagine-image-quality 및 grok-imagine-image에서 공유됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `images` | 편집할 참조 이미지입니다. 최대 3개까지 가능합니다. | IMAGE | 예 | 1 ~ 3 개 이미지 |
| `resolution` | 편집된 이미지의 출력 해상도입니다. | STRING | 예 | "1K"<br>"2K" |
| `number_of_images` | 생성할 편집 이미지 수입니다. (기본값: 1) | INT | 예 | 1 ~ 10 |
| `aspect_ratio` | 여러 이미지가 연결된 경우에만 허용됩니다. (기본값: "auto") | STRING | 예 | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-pro 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `images` | 편집할 참조 이미지입니다. | IMAGE | 예 | 이미지 1개 |
| `resolution` | 편집된 이미지의 출력 해상도입니다. | STRING | 예 | "1K"<br>"2K" |
| `number_of_images` | 생성할 편집 이미지 수입니다. (기본값: 1) | INT | 예 | 1 ~ 10 |

### 참조 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `images` | 확장 가능한 슬롯: 편집할 참조 이미지를 1개 이상 연결합니다. `image_1`, `image_2`, `image_3`과 같은 번호가 매겨진 슬롯을 추가할 수 있습니다. 최대 이미지 수는 선택한 모델에 따라 다릅니다(위의 모델 섹션 참조). | IMAGE | 예 | 모델에 따라 1~3개 이미지 |

**제약 사항 참고:**
- `prompt`에는 공백이 아닌 문자가 1개 이상 포함되어야 합니다.
- 편집에는 참조 이미지가 1개 이상 필요합니다. 이미지가 연결되지 않으면 노드에서 오류가 발생합니다.
- 입력 이미지의 최대 개수는 `grok-imagine-image-pro`의 경우 1개, `grok-imagine-image-2.0`, `grok-imagine-image-quality`, `grok-imagine-image`의 경우 3개입니다. 모델이 지원하는 것보다 더 많은 이미지를 연결하면 오류가 발생합니다.
- `grok-imagine-image-quality` 및 `grok-imagine-image`의 경우, "auto"가 아닌 사용자 지정 `aspect_ratio`는 여러 이미지가 연결된 경우에만 허용됩니다. 단일 이미지에서는 `aspect_ratio`가 "auto"여야 합니다.
- `grok-imagine-image-2.0`의 경우 단일 이미지에서도 `aspect_ratio`를 자유롭게 설정할 수 있습니다.
- `quality` 하위 매개변수는 `grok-imagine-image-2.0`에서만 사용할 수 있습니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `IMAGE` | Grok API가 반환한 편집된 이미지입니다. 단일 이미지가 생성된 경우에는 해당 이미지가 직접 반환됩니다. 여러 이미지가 생성된 경우에는 단일 배치 텐서로 연결됩니다. | IMAGE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/ko.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`
