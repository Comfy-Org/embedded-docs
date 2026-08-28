# OpenRouter LLM

OpenRouter LLM 節點會將文字提示傳送給可透過 OpenRouter 服務使用的一組精選熱門語言模型，並回傳所產生的文字回應。它支援來自 Anthropic (Claude)、OpenAI (GPT)、Google (Gemini)、xAI (Grok)、DeepSeek、Qwen、Mistral、Z.AI (GLM)、Moonshot (Kimi) 和 Perplexity Sonar 的模型，並可選擇在請求中包含影像或影片作為參考輸入。

## 輸入
在 `model` 選取器中選取模型後，節點會視所選模型的能力，在通用輸入上方顯示模型專屬小工具——推理強度、網路搜尋規模，和/或參考媒體插槽。

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 提供給模型的文字輸入。 | STRING | 是 | N/A |
| `model` | 用於產生回應的 OpenRouter 模型。 | DYNAMIC_COMBO | 是 | 多個選項可供選擇（請參閱下方模型章節） |
| `seed` | 取樣用的種子。設為 0 可省略。大多數模型僅將此視為提示。（預設值：0） | INT | 是 | 0 至 2147483647 |
| `system_prompt` | 決定模型行為的基礎指令。（預設值：""） | STRING | 否 | N/A |

### Anthropic Claude 模型輸入

由 `anthropic/claude-opus-5`、`anthropic/claude-opus-4.8`、`anthropic/claude-opus-4.7`、`anthropic/claude-fable-5`、`anthropic/claude-sonnet-5` 和 `anthropic/claude-haiku-4.5` 共用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。設為 'off' 可完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

這些模型最多支援 20 張參考影像（請參閱「參考輸入」）。

### OpenAI GPT 模型輸入

由 `openai/gpt-5.6-sol-pro`、`openai/gpt-5.6-sol`、`openai/gpt-5.6-terra-pro`、`openai/gpt-5.6-terra`、`openai/gpt-5.6-luna-pro`、`openai/gpt-5.6-luna`、`openai/gpt-5.5-pro` 和 `openai/gpt-5.5` 共用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。設為 'off' 可完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

這些模型最多支援 20 張參考影像（請參閱「參考輸入」）。

### Google Gemini 3.5 Flash 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。設為 'off' 可完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

此模型最多支援 20 張參考影像和 4 段參考影片（請參閱「參考輸入」）。

### xAI Grok 模型輸入

由 `x-ai/grok-4.5`、`x-ai/grok-4.20` 和 `x-ai/grok-4.3` 共用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。設為 'off' 可完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

這些模型最多支援 20 張參考影像（請參閱「參考輸入」）。

### DeepSeek 模型輸入

由 `deepseek/deepseek-v4-pro`、`deepseek/deepseek-v4-flash` 和 `deepseek/deepseek-v3.2` 共用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。設為 'off' 可完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

僅限文字的模型——不支援參考影像或影片。

### Qwen 3.6 Max Preview 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。設為 'off' 可完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

僅限文字的模型——不支援參考影像或影片。

### Qwen 3.6 Plus 與 Qwen 3.6 Flash 輸入

由 `qwen/qwen3.6-plus` 和 `qwen/qwen3.6-flash` 共用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。設為 'off' 可完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

這些模型最多支援 10 張參考影像和 4 段參考影片（請參閱「參考輸入」）。

### Mistral Large 2512 輸入

無設定檔專屬輸入（標準設定檔）。此模型最多支援 8 張參考影像（請參閱「參考輸入」）。

### Mistral Medium 3.5 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。設為 'off' 可完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

此模型最多支援 8 張參考影像（請參閱「參考輸入」）。

### Z.AI GLM 模型輸入

由 `z-ai/glm-4.6` 和 `z-ai/glm-5` 共用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。設為 'off' 可完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

僅限文字的模型——不支援參考影像或影片。

### Moonshot Kimi K3 與 K2.6 輸入

由 `moonshotai/kimi-k3` 和 `moonshotai/kimi-k2.6` 共用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。設為 'off' 可完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

這些模型最多支援 10 張參考影像（請參閱「參考輸入」）。

### Moonshot Kimi K2 Thinking 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。設為 'off' 可完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

僅限文字的模型——不支援參考影像或影片。

### Perplexity Sonar Pro 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | 要檢索多少網路搜尋上下文。越大表示越有依據，但速度較慢且成本較高。（預設值："medium"） | COMBO | 否 | "low"<br>"medium"<br>"high" |

僅限文字的模型——不支援參考影像或影片。

### Perplexity Sonar Reasoning Pro 與 Sonar Deep Research 輸入

由 `perplexity/sonar-reasoning-pro` 和 `perplexity/sonar-deep-research` 共用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | 要檢索多少網路搜尋上下文。越大表示越有依據，但速度較慢且成本較高。（預設值："medium"） | COMBO | 否 | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | 推理強度。設為 'off' 可完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

僅限文字的模型——不支援參考影像或影片。

### 參考輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 選用的參考影像，以 URL 形式傳送。可成長插槽：可連接 1..N 個影像輸入（`image_1`、`image_2`……）；數量上限取決於所選模型（請參閱模型章節）。 | IMAGE | 否 | 0 至 20（依模型而定：8、10 或 20） |
| `videos` | 選用的參考影片，以 URL 形式傳送。可成長插槽：可連接 1..N 個影片輸入（`video_1`、`video_2`……）；數量上限取決於所選模型（請參閱模型章節）。 | VIDEO | 否 | 0 至 4（依模型而定） |

**附註：**

- **可用模型：** 可用模型選項會動態建立，並包含具有不同能力的模型。完整的 34 個模型清單如下：

  - Anthropic: `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5`, `anthropic/claude-haiku-4.5`
  - OpenAI: `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro`, `openai/gpt-5.5`
  - Google: `google/gemini-3.5-flash`
  - xAI: `x-ai/grok-4.5`, `x-ai/grok-4.20`, `x-ai/grok-4.3`
  - DeepSeek: `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash`, `deepseek/deepseek-v3.2`
  - Qwen: `qwen/qwen3.6-max-preview`, `qwen/qwen3.6-plus`, `qwen/qwen3.6-flash`
  - Mistral: `mistralai/mistral-large-2512`, `mistralai/mistral-medium-3-5`
  - Z.AI: `z-ai/glm-4.6`, `z-ai/glm-5`
  - Moonshot: `moonshotai/kimi-k3`, `moonshotai/kimi-k2.6`, `moonshotai/kimi-k2-thinking`
  - Perplexity: `perplexity/sonar-pro`, `perplexity/sonar-reasoning-pro`, `perplexity/sonar-deep-research`

- **影像與影片限制：** 參考影像和影片的數量上限取決於所選模型。如果提供的影像或影片總數超過模型限制，節點會拋出錯誤。不支援影像或影片的模型不會顯示對應的參考插槽。

- **推理行為：** 當 `reasoning_effort` 設為 "off" 以外的任何值時，請求會要求提供者進行內部推理，而不回傳推理軌跡。

- **種子行為：** `seed` 參數具有「產生後控制」（"control_after_generate"）行為，亦即可以設定為在每次節點執行後自動變更（例如隨機化、遞增或固定），視使用者的小工具設定而定。

- **系統提示：** `system_prompt` 參數為選用，並在使用者介面中標記為進階參數。

- **錯誤情況：** 如果提示在去除前後空白後為空、OpenRouter 回傳錯誤、所選模型拒絕回應，或回應中沒有 choices 或 message，節點就會拋出錯誤。節點上的價格徽章會根據所選模型顯示每 1K tokens 的近似成本估算。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | OpenRouter 模型產生的文字回應。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
