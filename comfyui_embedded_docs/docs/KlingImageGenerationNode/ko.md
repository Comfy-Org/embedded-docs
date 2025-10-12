> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/ko.md)

Kling Image Generation Node는 텍스트 프롬프트에서 이미지를 생성하며, 참조 이미지를 사용하여 안내하는 옵션을 제공합니다. 이 노드는 사용자의 텍스트 설명과 참조 설정을 기반으로 하나 이상의 이미지를 생성한 후, 생성된 이미지를 출력으로 반환합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 예 | - | 긍정적 텍스트 프롬프트 |
| `negative_prompt` | STRING | 예 | - | 부정적 텍스트 프롬프트 |
| `image_type` | COMBO | 예 | KlingImageGenImageReferenceType의 옵션들<br>(소스 코드에서 추출됨) | 이미지 참조 타입 선택 |
| `image_fidelity` | FLOAT | 예 | 0.0 - 1.0 | 사용자 업로드 이미지에 대한 참조 강도 (기본값: 0.5) |
| `human_fidelity` | FLOAT | 예 | 0.0 - 1.0 | 주체 참조 유사도 (기본값: 0.45) |
| `model_name` | COMBO | 예 | "kling-v1"<br>(및 KlingImageGenModelName의 다른 옵션들) | 이미지 생성을 위한 모델 선택 (기본값: "kling-v1") |
| `aspect_ratio` | COMBO | 예 | "16:9"<br>(및 KlingImageGenAspectRatio의 다른 옵션들) | 생성된 이미지의 화면비 (기본값: "16:9") |
| `n` | INT | 예 | 1 - 9 | 생성할 이미지 수 (기본값: 1) |
| `image` | IMAGE | 아니오 | - | 선택적 참조 이미지 |

**매개변수 제약사항:**
- `image` 매개변수는 선택사항이지만, 제공될 경우 kling-v1 모델은 참조 이미지를 지원하지 않음
- 프롬프트와 부정 프롬프트에는 최대 길이 제한이 있음 (MAX_PROMPT_LENGTH_IMAGE_GEN)
- 참조 이미지가 제공되지 않을 경우, `image_type` 매개변수는 자동으로 None으로 설정됨

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `output` | IMAGE | 입력 매개변수를 기반으로 생성된 이미지(들) |