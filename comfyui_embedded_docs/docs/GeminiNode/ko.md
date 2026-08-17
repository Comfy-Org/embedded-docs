# Google Gemini

이 노드를 사용하면 Google의 Gemini AI 모델과 상호작용하여 텍스트 응답을 생성할 수 있습니다. 텍스트, 이미지, 오디오, 비디오, 파일 등 다양한 유형의 입력을 모델의 컨텍스트로 제공하여 더 관련성 있고 의미 있는 응답을 생성할 수 있습니다. 이 노드는 모든 API 통신과 응답 파싱을 자동으로 처리합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 모델에 전달하는 텍스트 입력으로, 응답을 생성하는 데 사용됩니다. 자세한 지침, 질문 또는 모델에 대한 컨텍스트를 포함할 수 있습니다. 기본값: 빈 문자열. | STRING | 예 | - |
| `model` | 응답 생성에 사용할 Gemini 모델입니다. 기본값: gemini-3-1-pro. | COMBO | 예 | "gemini-2.5-pro"<br>"gemini-2.5-flash"<br>"gemini-3-pro-preview"<br>"gemini-3-1-pro"<br>"gemini-3-1-flash-lite" |
| `seed` | 시드를 특정 값으로 고정하면 반복 요청 시 모델이 동일한 응답을 제공하기 위해 최선을 다합니다. 결정적 출력은 보장되지 않습니다. 또한 모델이나 온도와 같은 매개변수 설정을 변경하면 동일한 시드 값을 사용하더라도 응답이 달라질 수 있습니다. 기본적으로 무작위 시드 값이 사용됩니다. 기본값: 42. | INT | 예 | 0 to 18446744073709551615 |
| `images` | 모델의 컨텍스트로 사용할 선택적 이미지입니다. 여러 이미지를 포함하려면 Batch Images 노드를 사용할 수 있습니다. 기본값: 없음. | IMAGE | 아니요 | - |
| `audio` | 모델의 컨텍스트로 사용할 선택적 오디오입니다. 기본값: 없음. | AUDIO | 아니요 | - |
| `video` | 모델의 컨텍스트로 사용할 선택적 비디오입니다. 기본값: 없음. | VIDEO | 아니요 | - |
| `files` | 모델의 컨텍스트로 사용할 선택적 파일입니다. Gemini Generate Content Input Files 노드의 입력을 허용합니다. 기본값: 없음. | GEMINI_INPUT_FILES | 아니요 | - |
| `system_prompt` | AI의 동작을 결정하는 기본 지침입니다. 기본값: 빈 문자열. 이는 고급 매개변수입니다. | STRING | 아니요 | - |

참고: 이 노드는 더 이상 사용되지 않음(deprecated)으로 표시되어 있습니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
|-------------|-------------|-----------|
| STRING | Gemini 모델이 생성한 텍스트 응답입니다. 모델이 텍스트를 반환하지 않으면 노드는 "Empty response from Gemini model..."을 출력합니다. | STRING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/ko.md)

---
**Source fingerprint (SHA-256):** `d1c53a5d80182085a36302867c8875df696adec6aaea9a9519a21bd6b9543d8f`
