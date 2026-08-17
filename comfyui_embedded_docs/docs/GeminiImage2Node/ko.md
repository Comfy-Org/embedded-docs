# Nano Banana Pro (Google Gemini Image)

## 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|---|---|---|---|---|
| `prompt` | 생성할 이미지나 적용할 편집을 설명하는 텍스트 프롬프트입니다. 모델이 따라야 할 제약 조건, 스타일 또는 세부 사항을 포함합니다. 기본값: 빈 문자열입니다. | STRING | 예 | 해당 없음 |
| `model` | 사용할 Gemini 이미지 모델입니다. "Nano Banana 2 (Gemini 3.1 Flash Image)" 옵션은 API에 `gemini-3.1-flash-image`로 전송되고, "gemini-3-pro-image-preview"는 `gemini-3-pro-image`로 전송됩니다. | COMBO | 예 | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | 시드가 특정 값으로 고정되면 모델은 반복 요청에 대해 동일한 응답을 제공하기 위해 최선을 다합니다. 결정적 출력은 보장되지 않습니다. 모델이나 다른 매개변수 설정을 변경하면 동일한 시드 값에서도 응답이 달라질 수 있습니다. 기본값: 42입니다. | INT | 예 | 0 ~ 18446744073709551615 |
| `aspect_ratio` | 출력 이미지의 원하는 화면 비율입니다. "auto"로 설정하면 입력 이미지의 화면 비율에 맞춰지고, 이미지가 제공되지 않으면 일반적으로 16:9 비율의 이미지가 생성됩니다. 기본값: "auto"입니다. | COMBO | 예 | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | 대상 출력 해상도입니다. 2K/4K의 경우 기본 Gemini 업스케일러가 사용됩니다. | COMBO | 예 | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | 이미지만 출력하려면 "IMAGE"를 선택하고, 생성된 이미지와 텍스트 응답을 모두 반환하려면 "IMAGE+TEXT"를 선택합니다. | COMBO | 예 | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | 시각적 컨텍스트로 사용되는 선택적 참조 이미지입니다. 여러 이미지를 포함하려면 Batch Images 노드를 사용하세요(최대 14개). | IMAGE | 아니요 | 해당 없음 |
| `files` | 모델의 컨텍스트로 사용할 선택적 파일입니다. Gemini Generate Content Input Files 노드의 입력을 허용합니다. | GEMINI_INPUT_FILES | 아니요 | 해당 없음 |
| `system_prompt` | 모델의 동작을 결정하는 기본 지침입니다. 기본값: 모델이 항상 이미지를 생성하도록 지시하는 사전 정의된 시스템 프롬프트입니다. | STRING | 아니요 | 해당 없음 |

**제약 사항:**

* `prompt`는 앞뒤 공백을 제거한 후 비어 있지 않아야 합니다. 그렇지 않으면 오류가 발생합니다.
* `images` 입력은 최대 14개의 이미지를 허용합니다. 14개를 초과하면 오류가 발생합니다.
* `files` 입력은 `GEMINI_INPUT_FILES` 데이터 타입을 출력하는 노드에 연결되어야 합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|---|---|---|
| `image` | Gemini 모델이 생성하거나 편집한 이미지입니다. | IMAGE |
| `string` | 모델의 텍스트 응답입니다. `response_modalities`가 "IMAGE"로 설정된 경우 이 출력은 비어 있습니다. | STRING |

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/ko.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
