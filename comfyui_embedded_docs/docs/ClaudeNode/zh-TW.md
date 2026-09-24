# Anthropic Claude

從 Anthropic 的 Claude 模型產生文字回應。提供文字提示詞，並可選擇性地提供一張或多張圖片作為多模態上下文，節點會傳回模型產生的文字回應。

## 輸入

輸入分為通用設定、選取模型後顯示的模型專屬設定，以及選用的參考圖片。

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於產生回應的 Claude 模型。選取模型後，下方會顯示模型專屬設定。 | DYNAMIC_COMBO | 是 | `"Opus 5.5"`<br>`"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5.1"`<br>`"Fable 5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `prompt` | 模型的文字輸入。（預設值：空字串） | STRING | 是 | N/A |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果皆為非確定性。（預設值：0） | INT | 是 | 0 至 2147483647 |
| `system_prompt` | 決定模型行為的基礎指示。（預設值：空字串） | STRING | 否 | N/A |

### Opus 5.5、Opus 5、Fable 5.1 與 Fable 5 輸入

這四個模型共用相同設定。它們不提供 `temperature` 設定，且推理一律啟用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 要產生的最大 token 數（啟用時包含推理 token）。（預設值：32768） | INT | 是 | 4096 至 64000 |
| `reasoning_effort` | 延伸思考強度。此模型的推理一律啟用。（預設值："high"） | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |

### Opus 4.8 與 Sonnet 5 輸入

這兩個模型共用相同設定。它們不提供 `temperature` 設定。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 要產生的最大 token 數（啟用時包含推理 token）。（預設值：32768） | INT | 是 | 4096 至 64000 |
| `reasoning_effort` | 延伸思考強度。`"off"` 會停用推理。（預設值："off"） | COMBO | 是 | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |

### Opus 4.7、Opus 4.6、Sonnet 4.6 與 Sonnet 4.5 輸入

這四個模型共用相同設定。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 要產生的最大 token 數（啟用時包含推理 token）。（預設值：32768） | INT | 是 | 4096 至 64000 |
| `temperature` | 控制隨機性。0.0 為確定性，1.0 為最隨機。對 Opus 4.7 以及任何已設定 `reasoning_effort` 的模型會忽略此設定。（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |
| `reasoning_effort` | 延伸思考強度。`"off"` 會停用推理。（預設值："off"） | COMBO | 是 | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

在全部四個模型上，`reasoning_effort` 提供 `"off"`、`"low"`、`"medium"` 與 `"high"`。Opus 4.7、Opus 4.6 與 Sonnet 4.6 另外接受 `"max"`，而 Opus 4.7 也接受 `"xhigh"`。

### Haiku 4.5 輸入

此模型不提供 `reasoning_effort` 設定。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 要產生的最大 token 數（啟用時包含推理 token）。（預設值：32768） | INT | 是 | 4096 至 64000 |
| `temperature` | 控制隨機性。0.0 為確定性，1.0 為最隨機。對 Opus 4.7 以及任何已設定 `reasoning_effort` 的模型會忽略此設定。（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 可選擇性地提供一張或多張圖片，作為模型的上下文。最多 20 張圖片。可擴充插槽：連接 1 到 20 個項目（`image_1` ... `image_20`）。 | IMAGE | 否 | 0 至 20 images |

### 參數限制

- **圖片限制：** 每次請求最多可提供 20 張圖片。連接超過 20 張圖片會引發錯誤。
- **必須提供提示詞：** `prompt` 必須包含至少一個非空白字元。空提示詞會引發驗證錯誤。
- **temperature 處理：** 當啟用思考時，Anthropic API 要求不要設定 `temperature`（其預設值為 1.0）。Opus 5.5、Opus 5、Opus 4.8、Fable 5.1、Fable 5 與 Sonnet 5 不提供 `temperature` 設定。Opus 4.7 會忽略 `temperature`，而任何將 `reasoning_effort` 設為 `"off"` 以外值的模型也會忽略它。
- **推理/思考行為：** `reasoning_effort` 設定控制是否啟用思考。Opus 5.5、Opus 5、Fable 5.1 與 Fable 5 一律啟用推理。Haiku 4.5 不支援推理。當啟用思考時，節點會針對所選模型使用適當的思考模式，可能是自適應或基於預算。在預算模式下，推理 token 預算會受到上限限制，以保留至少 1024 個 token 給實際回應。
- **安全拒絕：** 如果 Claude 基於安全理由拒絕回答請求，節點會引發錯誤，要求您改寫提示詞或嘗試其他模型。
- **輸出文字：** 思考與推理區塊不會包含在輸出中；只會傳回產生的文字。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 由 Claude 模型產生的文字回應。思考/推理區塊不會包含在內。如果沒有產生任何文字，會傳回 "Empty response from Claude model." | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f6d9353025598bbed1aca7bdeb56ac59f5e4c26dd5b8e29359e97ef29e35bee7`
