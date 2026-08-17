# Anthropic Claude

## 輸入
`model` 參數是動態選取器：當您選擇模型時，下方會出現額外的模型專屬設定，例如 token 數量上限、溫度與推理強度。

### 通用輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 傳送給模型的文字輸入。去除前後空白後不得為空。（預設值：空字串） | STRING | 是 | N/A |
| `model` | 用於產生回應的 Claude 模型。 | DYNAMIC_COMBO | 是 | `"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `seed` | `seed` 控制節點是否應重新執行；無論種子值為何，結果都是非確定性的。（預設值：0） | INT | 是 | 0 to 2147483647 |
| `images` | 作為模型上下文的選用圖片。可擴充的輸入槽位：可連接 `image_1` 到 `image_20`；最多 20 張圖片。（預設值：無） | IMAGE | 否 | 0 to 20 images |
| `system_prompt` | 決定模型行為的基礎指令。（預設值：空字串） | STRING | 否 | N/A |

### Opus 5 和 Fable 5 輸入

由 Opus 5 和 Fable 5 共用。這些模型一律使用延伸思考，且不提供溫度設定。

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 要產生的最大 token 數（啟用時包含推理 token）。（預設值：32768） | INT | 是 | 4096 to 64000 |
| `reasoning_effort` | 延伸思考強度。此模型一律啟用推理。（預設值："high"） | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |

### Opus 4.8 和 Sonnet 5 輸入

由 Opus 4.8 和 Sonnet 5 共用。這些模型不提供溫度設定。

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 要產生的最大 token 數（啟用時包含推理 token）。（預設值：32768） | INT | 是 | 4096 to 64000 |
| `reasoning_effort` | 延伸思考強度。"off" 會停用推理。（預設值："off"） | COMBO | 是 | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Opus 4.7、Opus 4.6、Sonnet 4.6 和 Sonnet 4.5 輸入

由 Opus 4.7、Opus 4.6、Sonnet 4.6 和 Sonnet 4.5 共用。對於 Opus 4.7，溫度輸入會顯示但會被忽略，API 會使用預設值 1.0。

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 要產生的最大 token 數（啟用時包含推理 token）。（預設值：32768） | INT | 是 | 4096 to 64000 |
| `temperature` | 控制隨機性。0.0 為確定性，1.0 隨機性最高。在 Opus 4.7 以及任何設定了 `reasoning_effort` 的模型中，此值會被忽略。（預設值：1.0） | FLOAT | 是 | 0.0 to 1.0 (step 0.01) |
| `reasoning_effort` | 延伸思考強度。"off" 會停用推理。（預設值："off"） | COMBO | 是 | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Haiku 4.5 輸入

此模型不支援延伸思考，因此沒有提供 `reasoning_effort` 設定。

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 要產生的最大 token 數（啟用時包含推理 token）。（預設值：32768） | INT | 是 | 4096 to 64000 |
| `temperature` | 控制隨機性。0.0 為確定性，1.0 隨機性最高。（預設值：1.0） | FLOAT | 是 | 0.0 to 1.0 (step 0.01) |

### 參數限制

- 每個請求最多可提供 20 張圖片。上傳圖片的總像素數限制為 1568 × 1568 像素。
- Opus 5、Fable 5、Opus 4.8 和 Sonnet 5 無法設定溫度。當溫度輸入可用時，對於 Opus 4.7，以及任何將 `reasoning_effort` 設為 "off" 以外數值的模型，該輸入會被忽略。
- Opus 5 和 Fable 5 一律啟用推理，因此這些模型的 `reasoning_effort` 選項不包含 "off"。Haiku 4.5 模型不支援延伸思考，因此沒有 `reasoning_effort` 設定。
- 如果 Claude 基於安全考量拒絕回答請求，節點會拋出錯誤，而不是傳回文字。

## 輸出
| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `output` | Claude 模型產生的文字回應。如果未產生任何可見文字，輸出會是 `"Empty response from Claude model."`。思考或推理區塊不會包含在輸出中。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b0381e7981e5886d66b6976c7ddcad3f142bdd803271a6ac8567293dcddaa98a`
