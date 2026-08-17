# OpenRouter LLM

OpenRouter LLM 節點會將文字提示（以及可選的圖片或影片）傳送到可透過 OpenRouter 服務取得的精選語言模型集合，並傳回產生的文字回應。它支援來自 Anthropic（Claude）、OpenAI（GPT）、Google（Gemini）、xAI（Grok）、DeepSeek、Qwen、Mistral、Z.AI（GLM）、Moonshot（Kimi）與 Perplexity Sonar 的模型，並在所選模型支援時顯示模型專屬選項，例如推理強度與網路搜尋上下文。

## 輸入

`model` 選擇器是動態的：選取模型後，除了下列通用輸入之外，還會顯示模型專屬的控制項（推理強度、網路搜尋上下文、圖片與影片插槽）。

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於產生回應的 OpenRouter 模型。選取模型後會顯示其模型專屬輸入（請參閱下方各模型區段）。 | DYNAMIC_COMBO | 是 | 34 個精選的 OpenRouter 模型選項 |
| `prompt` | 輸入給模型的文字。必須包含至少一個非空白字元。 | STRING | 是 | 多行文字 |
| `seed` | 取樣用的種子。設為 0 以省略。大多數模型僅將此視為提示。（預設值：0） | INT | 是 | 0 到 2147483647 |
| `system_prompt` | 決定模型行為的基礎指令。（預設值：""） | STRING | 否 | 多行文字 |

**關於 `seed` 的說明：** 此參數具有 `control_after_generate` 行為，表示可以根據使用者的控制項設定，在每次節點執行後自動變更（例如隨機化、遞增或固定）。

**關於 `system_prompt` 的說明：** 此參數為選用，並在使用者介面中標示為進階參數。

### Anthropic Claude 輸入

由 `anthropic/claude-opus-5`、`anthropic/claude-opus-4.8`、`anthropic/claude-opus-4.7`、`anthropic/claude-fable-5`、`anthropic/claude-sonnet-5` 與 `anthropic/claude-haiku-4.5` 共用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。'off' 會完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### OpenAI GPT 輸入

由 `openai/gpt-5.6-sol-pro`、`openai/gpt-5.6-sol`、`openai/gpt-5.6-terra-pro`、`openai/gpt-5.6-terra`、`openai/gpt-5.6-luna-pro`、`openai/gpt-5.6-luna`、`openai/gpt-5.5-pro` 與 `openai/gpt-5.5` 共用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。'off' 會完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### Google Gemini 3.5 Flash 輸入

適用於 `google/gemini-3.5-flash`。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。'off' 會完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### xAI Grok 輸入

由 `x-ai/grok-4.5`、`x-ai/grok-4.20` 與 `x-ai/grok-4.3` 共用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。'off' 會完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### DeepSeek 輸入

由 `deepseek/deepseek-v4-pro`、`deepseek/deepseek-v4-flash` 與 `deepseek/deepseek-v3.2` 共用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。'off' 會完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### Qwen 3.6 Plus 與 Flash 輸入

由 `qwen/qwen3.6-plus` 與 `qwen/qwen3.6-flash` 共用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。'off' 會完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### Mistral Large 2512 輸入

適用於 `mistralai/mistral-large-2512`。此模型不會新增任何模型專屬的參數控制項；僅適用通用輸入與 `images` 參考插槽。

### Mistral Medium 3.5 輸入

適用於 `mistralai/mistral-medium-3-5`。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。'off' 會完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### Moonshot Kimi K3 與 K2.6 輸入

由 `moonshotai/kimi-k3` 與 `moonshotai/kimi-k2.6` 共用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。'off' 會完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### Perplexity Sonar Pro 輸入

適用於 `perplexity/sonar-pro`。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | 要擷取多少網路搜尋上下文。愈大愈有依據，但速度較慢且成本較高。（預設值："medium"） | COMBO | 否 | "low"<br>"medium"<br>"high" |

### Perplexity Sonar Reasoning Pro 與 Deep Research 輸入

由 `perplexity/sonar-reasoning-pro` 與 `perplexity/sonar-deep-research` 共用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | 要擷取多少網路搜尋上下文。愈大愈有依據，但速度較慢且成本較高。（預設值："medium"） | COMBO | 否 | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | 推理強度。'off' 會完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### 僅限推理模型

由 `qwen/qwen3.6-max-preview`、`z-ai/glm-4.6`、`z-ai/glm-5` 與 `moonshotai/kimi-k2-thinking` 共用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | 推理強度。'off' 會完全停用推理。（預設值："off"） | COMBO | 否 | "off"<br>"low"<br>"medium"<br>"high" |

### 參考輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 選用的參考圖片 — 以 URL 傳送。可擴充插槽：連接 `image_1` 到 `image_N`，其中 N 取決於所選模型。 | IMAGE | 否 | 0 到 N 張圖片（N = 8、10 或 20，視模型而定） |
| `videos` | 選用的參考影片 — 以 URL 傳送。可擴充插槽：連接 `video_1` 到 `video_N`。僅在支援影片的模型上提供。 | VIDEO | 否 | 0 到 4 部影片 |

**關於模型能力與限制的說明：**

- 圖片支援：Anthropic Claude、OpenAI GPT、Google Gemini 3.5 Flash 與 xAI Grok 模型最多 20 張圖片；Qwen 3.6 Plus/Flash 與 Moonshot Kimi K3/K2.6 最多 10 張圖片；Mistral Large 2512 與 Mistral Medium 3.5 最多 8 張圖片。DeepSeek、Qwen 3.6 Max Preview、Z.AI GLM、Moonshot Kimi K2 Thinking 與 Perplexity Sonar 模型不接受圖片。
- 影片支援：僅 `google/gemini-3.5-flash`、`qwen/qwen3.6-plus` 與 `qwen/qwen3.6-flash` 接受影片，最多 4 部影片。
- 如果連接的圖片或影片數量超過所選模型支援的上限，節點會拋出錯誤。
- 當 `reasoning_effort` 設為 "low"、"medium" 或 "high" 時，模型會在內部進行推理，但不會傳回推理追蹤；設為 "off" 則完全停用推理。
- `search_context_size` 控制項僅會出現在 Perplexity Sonar 模型上。`reasoning_effort` 與 `search_context_size` 控制項會標示為進階參數。
- 節點會根據所選模型顯示近似價格徽章（以每 1K tokens 的 USD 計）。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 從所選 OpenRouter 模型產生的文字回應。 | STRING |

**關於錯誤的說明：** 如果 OpenRouter 回傳 API 錯誤、空回應（沒有 choices），或模型拒絕回應，節點會拋出錯誤。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
