> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/ko.md)

이 노드는 사용자가 Google의 Gemini AI 모델과 상호작용하여 텍스트 응답을 생성할 수 있도록 합니다. 모델이 더 관련성 있고 의미 있는 응답을 생성하도록 텍스트, 이미지, 오디오, 비디오, 파일 등 여러 유형의 입력을 컨텍스트로 제공할 수 있습니다. 이 노드는 모든 API 통신과 응답 구문 분석을 자동으로 처리합니다.

## 입력

| 매개변수 | 데이터 타입 | 필수 | 범위 | 설명 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 예 | - | 모델에 대한 텍스트 입력으로, 응답을 생성하는 데 사용됩니다. 모델에 대한 상세한 지시사항, 질문 또는 컨텍스트를 포함할 수 있습니다. 기본값: 빈 문자열. |
| `model` | COMBO | 예 | `gemini-2.0-flash-exp`<br>`gemini-2.0-flash-thinking-exp`<br>`gemini-2.5-pro-exp`<br>`gemini-2.0-flash`<br>`gemini-2.0-flash-thinking`<br>`gemini-2.5-pro`<br>`gemini-2.0-flash-lite`<br>`gemini-1.5-flash`<br>`gemini-1.5-flash-8b`<br>`gemini-1.5-pro`<br>`gemini-1.0-pro` | 응답 생성에 사용할 Gemini 모델입니다. 기본값: gemini-2.5-pro. |
| `seed` | INT | 예 | 0 ~ 18446744073709551615 | 시드를 특정 값으로 고정하면, 모델은 반복된 요청에 대해 동일한 응답을 제공하기 위해 최선을 다합니다. 결정론적 출력은 보장되지 않습니다. 또한 모델이나 온도와 같은 매개변수 설정을 변경하면 동일한 시드 값을 사용하더라도 응답에 변동이 생길 수 있습니다. 기본적으로 무작위 시드 값이 사용됩니다. 기본값: 42. |
| `images` | IMAGE | 아니오 | - | 모델의 컨텍스트로 사용할 선택적 이미지입니다. 여러 이미지를 포함하려면 Batch Images 노드를 사용할 수 있습니다. 기본값: 없음. |
| `audio` | AUDIO | 아니오 | - | 모델의 컨텍스트로 사용할 선택적 오디오입니다. 기본값: 없음. |
| `video` | VIDEO | 아니오 | - | 모델의 컨텍스트로 사용할 선택적 비디오입니다. 기본값: 없음. |
| `files` | GEMINI_INPUT_FILES | 아니오 | - | 모델의 컨텍스트로 사용할 선택적 파일입니다. Gemini Generate Content Input Files 노드의 입력을 허용합니다. 기본값: 없음. |

## 출력

| 출력 이름 | 데이터 타입 | 설명 |
|-------------|-----------|-------------|
| `STRING` | STRING | Gemini 모델에 의해 생성된 텍스트 응답입니다. |