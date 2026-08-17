# OpenRouter LLM

OpenRouter LLM 노드는 텍스트 프롬프트(선택적으로 이미지 또는 비디오)를 OpenRouter 서비스를 통해 제공되는 선별된 언어 모델 세트에 전송하고 생성된 텍스트 응답을 반환합니다. 이 노드는 Anthropic(Claude), OpenAI(GPT), Google(Gemini), xAI(Grok), DeepSeek, Qwen, Mistral, Z.AI(GLM), Moonshot(Kimi) 및 Perplexity Sonar의 모델을 지원하며, 선택한 모델이 지원하는 경우 추론 노력 및 웹 검색 컨텍스트와 같은 모델별 옵션을 표시합니다.

## 입력

`model` 선택기는 동적입니다. 모델을 선택하면 아래의 공통 입력 외에도 모델별 위젯(추론 노력, 웹 검색 컨텍스트, 이미지 및 비디오 슬롯)이 표시됩니다.

### 공통 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `model` | 응답 생성에 사용되는 OpenRouter 모델입니다. 모델을 선택하면 해당 모델별 입력이 표시됩니다(아래 모델 섹션 참조). | DYNAMIC_COMBO | 예 | 선별된 OpenRouter 모델 옵션 34개 |
| `prompt` | 모델에 전달되는 텍스트 입력입니다. 공백이 아닌 문자가 하나 이상 포함되어야 합니다. | STRING | 예 | 여러 줄 텍스트 |
| `seed` | 샘플링을 위한 시드입니다. 생략하려면 0으로 설정하세요. 대부분의 모델은 이를 참고 힌트로만 취급합니다. (기본값: 0) | INT | 예 | 0 ~ 2147483647 |
| `system_prompt` | 모델의 동작을 결정하는 기본 지침입니다. (기본값: "") | STRING | 아니요 | 여러 줄 텍스트 |

**`seed` 참고 사항:** 이 매개변수는 "control_after_generate" 동작을 가지며, 사용자의 위젯 설정에 따라 각 노드 실행 후 자동으로 변경되도록(예: 무작위화, 증가 또는 고정) 설정할 수 있습니다.

**`system_prompt` 참고 사항:** 이 매개변수는 선택 사항이며 사용자 인터페이스에서 고급 매개변수로 표시됩니다.

### Anthropic Claude 입력

`anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5` 및 `anthropic/claude-haiku-4.5` 모델에서 공유됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 추론 노력입니다. 'off'로 설정하면 추론이 완전히 비활성화됩니다. (기본값: "off") | COMBO | 아니요 | "off"<br>"low"<br>"medium"<br>"high" |

### OpenAI GPT 입력

`openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro` 및 `openai/gpt-5.5` 모델에서 공유됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 추론 노력입니다. 'off'로 설정하면 추론이 완전히 비활성화됩니다. (기본값: "off") | COMBO | 아니요 | "off"<br>"low"<br>"medium"<br>"high" |

### Google Gemini 3.5 Flash 입력

`google/gemini-3.5-flash`에 적용됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 추론 노력입니다. 'off'로 설정하면 추론이 완전히 비활성화됩니다. (기본값: "off") | COMBO | 아니요 | "off"<br>"low"<br>"medium"<br>"high" |

### xAI Grok 입력

`x-ai/grok-4.5`, `x-ai/grok-4.20` 및 `x-ai/grok-4.3` 모델에서 공유됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 추론 노력입니다. 'off'로 설정하면 추론이 완전히 비활성화됩니다. (기본값: "off") | COMBO | 아니요 | "off"<br>"low"<br>"medium"<br>"high" |

### DeepSeek 입력

`deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash` 및 `deepseek/deepseek-v3.2` 모델에서 공유됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 추론 노력입니다. 'off'로 설정하면 추론이 완전히 비활성화됩니다. (기본값: "off") | COMBO | 아니요 | "off"<br>"low"<br>"medium"<br>"high" |

### Qwen 3.6 Plus 및 Flash 입력

`qwen/qwen3.6-plus` 및 `qwen/qwen3.6-flash` 모델에서 공유됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 추론 노력입니다. 'off'로 설정하면 추론이 완전히 비활성화됩니다. (기본값: "off") | COMBO | 아니요 | "off"<br>"low"<br>"medium"<br>"high" |

### Mistral Large 2512 입력

`mistralai/mistral-large-2512`에 적용됩니다. 이 모델은 모델별 매개변수 위젯을 추가하지 않습니다. 공통 입력과 `images` 참조 슬롯만 적용됩니다.

### Mistral Medium 3.5 입력

`mistralai/mistral-medium-3-5`에 적용됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 추론 노력입니다. 'off'로 설정하면 추론이 완전히 비활성화됩니다. (기본값: "off") | COMBO | 아니요 | "off"<br>"low"<br>"medium"<br>"high" |

### Moonshot Kimi K3 및 K2.6 입력

`moonshotai/kimi-k3` 및 `moonshotai/kimi-k2.6` 모델에서 공유됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 추론 노력입니다. 'off'로 설정하면 추론이 완전히 비활성화됩니다. (기본값: "off") | COMBO | 아니요 | "off"<br>"low"<br>"medium"<br>"high" |

### Perplexity Sonar Pro 입력

`perplexity/sonar-pro`에 적용됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | 검색할 웹 검색 컨텍스트의 양입니다. 클수록 더 근거가 확실하지만 더 느리고 비쌉니다. (기본값: "medium") | COMBO | 아니요 | "low"<br>"medium"<br>"high" |

### Perplexity Sonar Reasoning Pro 및 Deep Research 입력

`perplexity/sonar-reasoning-pro` 및 `perplexity/sonar-deep-research` 모델에서 공유됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | 검색할 웹 검색 컨텍스트의 양입니다. 클수록 더 근거가 확실하지만 더 느리고 비쌉니다. (기본값: "medium") | COMBO | 아니요 | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | 추론 노력입니다. 'off'로 설정하면 추론이 완전히 비활성화됩니다. (기본값: "off") | COMBO | 아니요 | "off"<br>"low"<br>"medium"<br>"high" |

### 추론 전용 모델

`qwen/qwen3.6-max-preview`, `z-ai/glm-4.6`, `z-ai/glm-5` 및 `moonshotai/kimi-k2-thinking` 모델에서 공유됩니다.

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 추론 노력입니다. 'off'로 설정하면 추론이 완전히 비활성화됩니다. (기본값: "off") | COMBO | 아니요 | "off"<br>"low"<br>"medium"<br>"high" |

### 참조 입력

| 매개변수 | 설명 | 데이터 타입 | 필수 여부 | 범위 |
|-----------|-------------|-----------|----------|-------|
| `images` | 선택적 참조 이미지이며 URL로 전송됩니다. 확장 가능한 슬롯: `image_1`부터 `image_N`까지 연결합니다. 여기서 N은 선택한 모델에 따라 달라집니다. | IMAGE | 아니요 | 0~N개 이미지 (N = 모델에 따라 8, 10 또는 20) |
| `videos` | 선택적 참조 비디오이며 URL로 전송됩니다. 확장 가능한 슬롯: `video_1`부터 `video_N`까지 연결합니다. 비디오를 지원하는 모델에서만 사용할 수 있습니다. | VIDEO | 아니요 | 0~4개 비디오 |

**모델 기능 및 제한 사항 참고:**

- 이미지 지원: Anthropic Claude, OpenAI GPT, Google Gemini 3.5 Flash 및 xAI Grok 모델은 최대 20개 이미지를 지원합니다. Qwen 3.6 Plus/Flash 및 Moonshot Kimi K3/K2.6은 최대 10개 이미지를 지원합니다. Mistral Large 2512 및 Mistral Medium 3.5는 최대 8개 이미지를 지원합니다. DeepSeek, Qwen 3.6 Max Preview, Z.AI GLM, Moonshot Kimi K2 Thinking 및 Perplexity Sonar 모델은 이미지를 허용하지 않습니다.
- 비디오 지원: `google/gemini-3.5-flash`, `qwen/qwen3.6-plus` 및 `qwen/qwen3.6-flash` 모델만 비디오를 허용하며, 최대 4개입니다.
- 선택한 모델이 지원하는 것보다 더 많은 이미지나 비디오가 연결되면 노드는 오류를 발생시킵니다.
- `reasoning_effort`가 "low", "medium" 또는 "high"로 설정되면 모델은 내부적으로 추론하지만 추론 과정을 반환하지 않습니다. "off"는 추론을 완전히 비활성화합니다.
- `search_context_size` 위젯은 Perplexity Sonar 모델에서만 나타납니다. `reasoning_effort` 및 `search_context_size` 위젯은 고급 매개변수로 표시됩니다.
- 노드는 선택한 모델을 기반으로 대략적인 가격 배지(1K 토큰당 USD)를 표시합니다.

## 출력

| 출력 이름 | 설명 | 데이터 타입 |
|-------------|-------------|-----------|
| `output` | 선택한 OpenRouter 모델에서 생성된 텍스트 응답입니다. | STRING |

**오류 참고 사항:** OpenRouter가 API 오류, 빈 응답(선택 항목 없음) 또는 모델의 거부를 반환하면 노드는 오류를 발생시킵니다.

> 이 문서는 AI에 의해 생성되었습니다. 오류를 발견하거나 개선 제안이 있으시면 기여해 주세요! [GitHub에서 편집](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/ko.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
