# OpenAI ChatGPT

此節點會從 OpenAI 模型生成文字回應。它會將您的文字提示（以及可選的圖片或檔案）傳送給 OpenAI 模型，並返回生成的文字回應。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 提供給模型的文字輸入，用於生成回應（預設：空） | STRING | 是 | - |
| `persist_context` | 此參數已棄用且無效果（預設：False） | BOOLEAN | 是 | - |
| `model` | 用於生成回應的模型（預設：`gpt-5`） | COMBO | 是 | `gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `images` | 可選的圖片，作為模型的上下文。若要包含多張圖片，可以使用 Batch Images 節點 | IMAGE | 否 | - |
| `files` | 可選的檔案，作為模型的上下文。接受來自 OpenAI Chat Input Files 節點的輸入 | OPENAI_INPUT_FILES | 否 | - |
| `advanced_options` | 可選的模型配置。接受來自 OpenAI Chat Advanced Options 節點的輸入 | OPENAI_CHAT_CONFIG | 否 | - |

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output_text` | OpenAI 模型生成的文字回應 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `25bb3648a4e1ea5668486375153ac4c96b542082c88958d4f62b93adf1db5b2a`
