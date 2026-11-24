# OpenAI ChatGPT

此節點使用 OpenAI 的 GPT 模型產生文字回應。它會傳送文字提示，並可選擇性地將影像或檔案作為上下文，然後以字串形式傳回答案。所有設定都位於 `model` 選擇器內：選取模型後，會顯示該模型自身的 `reasoning_effort` 等級、Token 上限、`seed` 與系統提示，因此不需要另外的設定節點。此節點取代先前的 OpenAI ChatGPT 節點；原始碼現在已將其標示為已棄用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於產生回應的模型。每個模型會提供其支援的 `reasoning_effort` 等級（預設：`"gpt-6.2-sol"`）。 | DYNAMIC_COMBO | 是 | `"gpt-6.2-sol"`<br>`"gpt-6.2-astra"`<br>`"gpt-6-astra"`<br>`"gpt-6.1-sol"`<br>`"gpt-6.1-terra"`<br>`"gpt-6-sol"`<br>`"gpt-6-luna"`<br>`"gpt-5.6-sol"`<br>`"gpt-5.6-terra"`<br>`"gpt-5.6-luna"`<br>`"gpt-5.5-pro"`<br>`"gpt-5.5"` |
| `prompt` | 提供給模型的文字輸入（預設：空字串）。 | STRING | 是 | - |
| `images` | 可擴充插槽：連接 1 至 16 個項目（`image_1`、`image_2`、...）。可選的一或多張影像，用作模型的上下文。 | IMAGE | 否 | 0 至 16 張影像 |
| `files` | 可選的一或多個檔案，用作模型的上下文。接受來自 OpenAI ChatGPT Input Files 節點的輸入。 | OPENAI_INPUT_FILES | 否 | - |
| `reasoning_effort` | 模型在回答前進行推理的程度。等級越高，使用的 Token 越多且耗時越長。提供的等級取決於所選模型（預設：`"medium"`；`gpt-5.5-pro` 為 `"high"`）。 | COMBO | 是 | 請參閱下方各模型列表 |
| `max_output_tokens` | 要產生的最大 Token 數量，包含推理 Token。若數值偏低且 `reasoning_effort` 偏高，可能會沒有空間留給答案（預設：32768）。 | INT | 是 | 16 至 128000 |
| `seed` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果都是非確定性的（預設：42）。 | INT | 是 | 0 至 2147483647 |
| `system_prompt` | 決定模型行為的基礎指示（預設：空字串）。 | STRING | 否 | - |

### 各模型的推理強度等級

- `gpt-6.2-sol`、`gpt-6.2-astra`、`gpt-6-astra`、`gpt-6.1-sol`：`"low"`、`"medium"`、`"high"`、`"xhigh"`、`"max"`，預設 `"medium"`。
- `gpt-6.1-terra`、`gpt-6-sol`、`gpt-6-luna`、`gpt-5.6-sol`、`gpt-5.6-terra`、`gpt-5.6-luna`：`"none"`、`"low"`、`"medium"`、`"high"`、`"xhigh"`、`"max"`，預設 `"medium"`。
- `gpt-5.5-pro`：`"medium"`、`"high"`、`"xhigh"`，預設 `"high"`。
- `gpt-5.5`：`"none"`、`"low"`、`"medium"`、`"high"`、`"xhigh"`，預設 `"medium"`。

### 行為說明

- 只會傳回答案文字。模型在思考期間的評論階段所發出的訊息會被略過。
- 如果在答案寫出之前 Token 預算就用盡，節點會引發錯誤，提示您增加 `max_output_tokens`。
- 影像會以其自身解析度傳送，並使用 API 的自動細節等級，因此大型影像會使用更多 Token。
- 每個請求都會儲存在 OpenAI 端，且傳回的文字會以換行符號連接答案的各個部分。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 由 OpenAI 模型產生的文字回應。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `129c13a6c7b76d142c0a23234ab5e707a1dd39a99055974277d46a39593aa7ba`
