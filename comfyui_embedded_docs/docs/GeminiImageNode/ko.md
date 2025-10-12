> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImageNode/ko.md)

GeminiImage 노드는 Google의 Gemini AI 모델을 사용하여 텍스트 및 이미지 응답을 생성합니다. 텍스트 프롬프트, 이미지, 파일을 포함한 다중 모드 입력을 제공하여 일관된 텍스트 및 이미지 출력을 생성할 수 있습니다. 이 노드는 최신 Gemini 모델과의 모든 API 통신 및 응답 구문 분석을 처리합니다.

## 입력

| 매개변수 | 데이터 타입 | 입력 타입 | 기본값 | 범위 | 설명 |
|-----------|-----------|------------|---------|-------|-------------|
| `prompt` | STRING | 필수 | "" | - | 생성을 위한 텍스트 프롬프트 |
| `model` | COMBO | 필수 | gemini_2_5_flash_image_preview | 사용 가능한 Gemini 모델<br>GeminiImageModel 열거형에서 추출된 옵션 | 응답 생성에 사용할 Gemini 모델 |
| `seed` | INT | 필수 | 42 | 0부터 18446744073709551615까지 | 시드를 특정 값으로 고정하면 모델은 반복된 요청에 대해 동일한 응답을 제공하기 위해 최선을 다합니다. 결정론적 출력은 보장되지 않습니다. 또한 모델이나 temperature와 같은 매개변수 설정을 변경하면 동일한 시드 값을 사용하더라도 응답에 변동이 발생할 수 있습니다. 기본적으로 무작위 시드 값이 사용됩니다 |
| `images` | IMAGE | 선택 | None | - | 모델의 컨텍스트로 사용할 선택적 이미지입니다. 여러 이미지를 포함하려면 Batch Images 노드를 사용할 수 있습니다 |
| `files` | GEMINI_INPUT_FILES | 선택 | None | - | 모델의 컨텍스트로 사용할 선택적 파일입니다. Gemini Generate Content Input Files 노드의 입력을 허용합니다 |

*참고: 이 노드에는 시스템에 의해 자동으로 처리되며 사용자 입력이 필요하지 않은 숨겨진 매개변수(`auth_token`, `comfy_api_key`, `unique_id`)가 포함되어 있습니다.*

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Gemini 모델에서 생성된 이미지 응답 |
| `STRING` | STRING | Gemini 모델에서 생성된 텍스트 응답 |
