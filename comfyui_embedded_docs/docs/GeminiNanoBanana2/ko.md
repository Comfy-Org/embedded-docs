# Nano Banana 2

이 노드는 Google의 Vertex AI Gemini 모델(Nano Banana 2 / Gemini 3.1 Flash Image)을 사용하여 이미지를 동기식으로 생성하거나 편집합니다. 텍스트 프롬프트와 선택적 참조 이미지 또는 파일을 API에 전송하고, 생성된 이미지, 함께 반환되는 텍스트, 그리고 선택적으로 모델의 추론 과정에서 생성된 이미지를 반환합니다.

## 입력

| 매개변수 | 설명 | 데이터 유형 | 필수 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 생성할 이미지 또는 적용할 편집 내용을 설명하는 텍스트 프롬프트입니다. 모델이 따라야 할 제약 조건, 스타일, 세부 사항을 포함하세요. 공백이 아닌 문자가 하나 이상 포함되어야 합니다. | STRING | 예 | N/A |
| `model` | 이미지 생성에 사용할 특정 Gemini 모델입니다. 사용 가능한 유일한 옵션은 `gemini-3.1-flash-image-preview` 모델에 매핑됩니다. | COMBO | 예 | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | 시드가 특정 값으로 고정되면 모델은 반복 요청에 대해 동일한 응답을 제공하기 위해 최선을 다합니다. 결정적 출력은 보장되지 않습니다. 또한 모델이나 온도와 같은 매개변수 설정을 변경하면 동일한 시드 값을 사용하더라도 응답이 달라질 수 있습니다. 기본적으로 무작위 시드 값이 사용됩니다. (기본값: 42) | INT | 예 | 0 ~ 18446744073709551615 |
| `aspect_ratio` | 'auto'로 설정하면 입력 이미지의 종횡비와 일치합니다. 이미지가 제공되지 않으면 일반적으로 16:9 이미지가 생성됩니다. (기본값: "auto") | COMBO | 예 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | 대상 출력 해상도입니다. 2K/4K의 경우 네이티브 Gemini 업스케일러가 사용됩니다. | COMBO | 예 | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | 모델이 반환하는 콘텐츠 유형을 결정합니다. `IMAGE`는 이미지만 반환하고, `IMAGE+TEXT`는 모델의 추론 텍스트도 반환합니다. (고급) | COMBO | 예 | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `thinking_level` | 모델의 추론 과정 깊이를 제어합니다. | COMBO | 예 | `"MINIMAL"`<br>`"HIGH"` |
| `images` | 선택적 참조 이미지입니다. 여러 이미지를 포함하려면 Batch Images 노드를 사용하세요(최대 14개). | IMAGE | 아니요 | 최대 14개 |
| `files` | 모델의 컨텍스트로 사용할 선택적 파일입니다. Gemini Generate Content Input Files 노드의 입력을 허용합니다. | GEMINI_INPUT_FILES | 아니요 | N/A |
| `system_prompt` | AI의 동작을 결정하는 기본 지침입니다. (기본값: 모델이 항상 이미지를 생성하도록 요구하는 기본 제공 지침) (고급) | STRING | 아니요 | N/A |

**참고:** `images` 입력은 최대 14개의 이미지를 허용하며, 초과 시 오류가 발생합니다. 참조 이미지가 10개를 초과하면 처음 10개는 파일 URL로 전송되고 나머지 이미지는 인라인 데이터로 전송됩니다. `prompt`는 공백을 제거한 후 비어 있으면 안 됩니다. 이 노드는 deprecated(더 이상 사용되지 않음)로 표시되어 있습니다.

## 출력

| 출력 이름 | 설명 | 데이터 유형 |
|-------------|-----------|-----------|
| `image` | 모델이 생성하거나 편집한 기본 이미지입니다. | IMAGE |
| `string` | 모델이 반환한 모든 텍스트 콘텐츠입니다. | STRING |
| `thought_image` | 모델의 추론 과정에서 나온 첫 번째 이미지입니다. thinking_level HIGH 및 IMAGE+TEXT 모드에서만 사용할 수 있습니다. | IMAGE |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/ko.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
