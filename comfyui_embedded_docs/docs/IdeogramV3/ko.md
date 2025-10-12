> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV3/ko.md)

Ideogram V3 노드는 Ideogram V3 모델을 사용하여 이미지를 생성합니다. 텍스트 프롬프트로부터의 일반적인 이미지 생성과, 이미지와 마스크가 모두 제공되었을 때의 이미지 편집을 모두 지원합니다. 이 노드는 화면비, 해상도, 생성 속도, 그리고 선택적인 캐릭터 참조 이미지에 대한 다양한 제어 기능을 제공합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 예 | - | 이미지 생성 또는 편집을 위한 프롬프트 (기본값: 빈 값) |
| `image` | IMAGE | 아니오 | - | 이미지 편집을 위한 선택적 참조 이미지 |
| `mask` | MASK | 아니오 | - | 인페인팅을 위한 선택적 마스크 (흰색 영역이 대체됨) |
| `aspect_ratio` | COMBO | 아니오 | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | 이미지 생성을 위한 화면비. 해상도가 Auto로 설정되지 않은 경우 무시됨 (기본값: "1:1") |
| `resolution` | COMBO | 아니오 | "Auto"<br>"1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | 이미지 생성을 위한 해상도. Auto로 설정되지 않으면 aspect_ratio 설정을 재정의함 (기본값: "Auto") |
| `magic_prompt_option` | COMBO | 아니오 | "AUTO"<br>"ON"<br>"OFF" | 생성 시 MagicPrompt 사용 여부를 결정함 (기본값: "AUTO") |
| `seed` | INT | 아니오 | 0-2147483647 | 생성을 위한 랜덤 시드 (기본값: 0) |
| `num_images` | INT | 아니오 | 1-8 | 생성할 이미지의 수 (기본값: 1) |
| `rendering_speed` | COMBO | 아니오 | "DEFAULT"<br>"TURBO"<br>"QUALITY" | 생성 속도와 품질 간의 트레이드오프를 제어함 (기본값: "DEFAULT") |
| `character_image` | IMAGE | 아니오 | - | 캐릭터 참조로 사용할 이미지 |
| `character_mask` | MASK | 아니오 | - | 캐릭터 참조 이미지에 대한 선택적 마스크 |

**매개변수 제약 조건:**
- `image`와 `mask`가 모두 제공되면 노드는 편집 모드로 전환됩니다.
- `image` 또는 `mask` 중 하나만 제공되면 오류가 발생합니다.
- `character_mask`는 `character_image`가 존재해야 사용할 수 있습니다.
- `resolution`이 "Auto"로 설정되지 않으면 `aspect_ratio` 매개변수는 무시됩니다.
- 마스크의 흰색 영역은 인페인팅 중에 대체됩니다.
- 캐릭터 마스크와 캐릭터 이미지는 같은 크기여야 합니다.

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | IMAGE | 생성되거나 편집된 이미지(들) |