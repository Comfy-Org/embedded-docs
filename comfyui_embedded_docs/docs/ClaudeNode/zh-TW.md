# Anthropic Claude

從 Anthropic 的 Claude 模型產生文字回應。提供文字提示詞，並可選擇性提供一張或多張圖片作為多模態上下文，節點會傳回模型產生的文字回應。

## 輸入

輸入分為通用設定、選取模型後顯示的模型特定設定，以及選擇性的參考圖片。

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於產生回應的 Claude 模型。選取模型後會顯示下方的模型特定設定。 | DYNAMIC_COMBO | 是 | `"Opus 5.5"`<br>`"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5.1"`<br>`"Fable 5"`<br>`"Sonnet 5.5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `prompt` | 提供給模型的文字輸入。（預設值：空字串） | STRING | 是 | N/A |
| `seed` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果都是非確定性的。（預設值：0） | INT | 是 | 0 至 2147483647 |
| `system_prompt` | 決定模型行為的基礎指示。（預設值：空字串） | STRING | 否 | N/A |

### Opus 5.5、Opus 5、Fable 5.1 與 Fable 5 輸入

這四個模型共用相同設定。它們不會提供 `temperature` 設定，且推理永遠啟用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 最大產生 token 數量（啟用時包含推理 token）。（預設值：32768） | INT | 是 | 1024 至 64000（Opus 5.5）<br>4096 至 64000（Opus 5、Fable 5.1、Fable 5） |
| `reasoning_effort` | 擴展思考強度。此模型的推理永遠啟用。（預設值："high"） | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |

### Opus 4.8、Sonnet 5.5 與 Sonnet 5 輸入

這三個模型共用相同設定。它們不會提供 `temperature` 設定。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 最大產生 token 數量（啟用時包含推理 token）。（預設值：32768） | INT | 是 | 1024 至 64000（Sonnet 5.5）<br>4096 至 64000（Opus 4.8、Sonnet 5） |
| `reasoning_effort` | 擴展思考強度。`"off"` 會停用推理。（預設值："off"） | COMBO | 是 | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |

### Opus 4.7、Opus 4.6、Sonnet 4.6 與 Sonnet 4.5 輸入

這四個模型共用相同設定。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 最大產生 token 數量（啟用時包含推理 token）。（預設值：32768） | INT | 是 | 4096 至 64000 |
| `temperature` | 控制隨機性。0.0 為確定性，1.0 為最隨機。對 Opus 4.7 以及任何已設定 `reasoning_effort` 的模型，此參數會被忽略。（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |
| `reasoning_effort` | 擴展思考強度。`"off"` 會停用推理。（預設值："off"） | COMBO | 是 | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

這四個模型上的 `reasoning_effort` 均提供 `"off"`、`"low"`、`"medium"` 與 `"high"`。Opus 4.7、Opus 4.6 與 Sonnet 4.6 另外接受 `"max"`，而 Opus 4.7 也接受 `"xhigh"`。

### Haiku 4.5 輸入

此模型不會提供 `reasoning_effort` 設定。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | 最大產生 token 數量（啟用時包含推理 token）。（預設值：32768） | INT | 是 | 4096 至 64000 |
| `temperature` | 控制隨機性。0.0 為確定性，1.0 為最隨機。對 Opus 4.7 以及任何已設定 `reasoning_effort` 的模型，此參數會被忽略。（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 選擇性的一或多張圖片，用於作為模型的上下文。最多 20 張圖片。可擴充插槽：連接 1 到 20 個項目（`image_1` ... `image_20`）。 | IMAGE | 否 | 0 至 20 張圖片 |

### 參數限制

- **圖片限制：** 每次請求最多可提供 20 張圖片。連接超過 20 張圖片會引發錯誤。
- **提示詞必填：** `prompt` 必須包含至少一個非空白字元。空的 `prompt` 會引發驗證錯誤。
- **Temperature 處理：** 啟用思考時，Anthropic API 要求 `temperature` 必須未設定（預設為 1.0）。Opus 5.5、Opus 5、Opus 4.8、Fable 5.1、Fable 5、Sonnet 5.5 與 Sonnet 5 不會提供 `temperature` 設定。Opus 4.7 會忽略 `temperature`，而任何將 `reasoning_effort` 設為 `"off"` 以外值的模型也會忽略它。
- **推理/思考行為：** `reasoning_effort` 設定會控制是否啟用思考。Opus 5.5、Opus 5、Fable 5.1 與 Fable 5 永遠啟用推理。Haiku 4.5 不支援推理。啟用思考時，節點會為所選模型使用適當的思考模式，可能是自適應或基於預算。在預算模式下，推理 token 預算會設定上限，以保留至少 1024 個 token 給實際回應。當 Sonnet 5.5 的 `reasoning_effort` 為 `"off"` 時，請求會使用 `between_tools` 思考，而非停用思考，因此回應仍不包含推理。
- **Max tokens 最小值：** `max_tokens` 在 Opus 5.5 與 Sonnet 5.5 上接受從 1024 起的值，而在其他每個模型上接受從 4096 起的值。
- **安全拒絕：** 如果 Claude 基於安全理由拒絕回答請求，節點會引發錯誤，要求您改寫提示詞或嘗試不同的模型。
- **輸出文字：** 思考與推理區塊不會包含在輸出中；只會傳回產生的文字。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 來自 Claude 模型產生的文字回應。思考/推理區塊不會包含在內。如果沒有產生文字，會傳回 "Empty response from Claude model." | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `35b737da0f4c3a9da72910bf2053b18ae6a5c60989dc9607b61037623bc94e38`
