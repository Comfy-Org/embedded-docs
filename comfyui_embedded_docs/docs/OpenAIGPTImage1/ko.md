# OpenAI GPT Image 2

OpenAI의 GPT Image 엔드포인트를 통해 이미지를 동기적으로 생성합니다. 이 노드는 텍스트 프롬프트에서 새 이미지를 생성하거나, 입력 이미지와 선택적 마스크가 제공되면 기존 이미지를 편집할 수 있습니다. gpt-image-1, gpt-image-1.5, gpt-image-2를 포함한 여러 GPT Image 모델을 지원합니다. 이 노드는 더 이상 사용되지 않습니다.

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | GPT Image용 텍스트 프롬프트입니다 (기본값: "") | STRING | 예 | - |
| `seed` | 생성용 무작위 시드입니다 (기본값: 0) - 백엔드에서 아직 구현되지 않았습니다 | INT | 아니요 | 0 to 2147483647 |
| `quality` | 이미지 품질입니다. 비용과 생성 시간에 영향을 줍니다 (기본값: "low") | COMBO | 아니요 | "low"<br>"medium"<br>"high" |
| `background` | 배경이 있는 이미지 또는 배경이 없는 이미지를 반환합니다 (기본값: "auto") | COMBO | 아니요 | "auto"<br>"opaque"<br>"transparent" |
| `size` | 이미지 크기입니다. 사용자 정의 너비와 높이를 사용하려면 "Custom"을 선택하세요 (GPT Image 2 전용) (기본값: "auto") | COMBO | 아니요 | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `n` | 생성할 이미지 수입니다 (기본값: 1) | INT | 아니요 | 1 to 8 |
| `image` | 이미지 편집을 위한 선택적 참조 이미지입니다 | IMAGE | 아니요 | - |
| `mask` | 인페인팅을 위한 선택적 마스크입니다 (흰색 영역이 대체됩니다) | MASK | 아니요 | - |
| `model` | 사용할 GPT Image 모델입니다 (기본값: "gpt-image-2") | COMBO | 아니요 | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `custom_width` | `size`가 "Custom"일 때만 사용됩니다. 16의 배수여야 합니다 (GPT Image 2 전용) (기본값: 1024) | INT | 아니요 | 1024 to 3840 |
| `custom_height` | `size`가 "Custom"일 때만 사용됩니다. 16의 배수여야 합니다 (GPT Image 2 전용) (기본값: 1024) | INT | 아니요 | 1024 to 3840 |

**매개변수 제약 조건:**

- `image`가 제공되면 노드가 이미지 편집 모드로 전환됩니다
- `mask`는 `image`가 제공될 때만 사용할 수 있습니다
- `mask`를 사용할 때는 단일 이미지만 지원됩니다 (배치 크기는 1이어야 합니다)
- `mask`와 `image`는 크기가 같아야 합니다
- 사용자 정의 해상도 (`size` = "Custom")는 gpt-image-2 모델에서만 지원됩니다
- 사용자 정의 너비와 높이는 16의 배수여야 합니다
- 사용자 정의 해상도의 종횡비는 3:1을 초과할 수 없습니다
- 사용자 정의 해상도의 총 픽셀 수는 655,360 이상 8,294,400 이하여야 합니다
- 투명 배경은 gpt-image-2 모델에서 지원되지 않습니다
- 1536x1024보다 큰 크기(예: 2048x2048, 3840x2160)는 gpt-image-2 모델에서만 지원됩니다

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `IMAGE` | 생성되거나 편집된 이미지입니다 | IMAGE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/ko.md)

---
**Source fingerprint (SHA-256):** `bf588bffced6e66536b4cb54655ef6ebb9cf988d9739e3c379a8ebda1486e20a`
