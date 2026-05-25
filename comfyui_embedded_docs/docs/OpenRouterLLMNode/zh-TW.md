> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/zh-TW.md)

## 概述

OpenRouter LLM 節點將文字提示發送到透過 OpenRouter 服務提供的精選熱門語言模型集合，並返回生成的文字回應。它支援來自 xAI、DeepSeek、Qwen、Mistral、Z.AI (GLM)、Moonshot (Kimi) 和 Perplexity Sonar 等提供商的模型，並且可以選擇在請求中包含圖片或影片。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | 不適用 | 輸入到模型的文字。 |
| `model` | STRING | 是 | 提供多個選項（請參閱下方備註） | 用於生成回應的 OpenRouter 模型。 |
| `seed` | INT | 是 | 0 到 2147483647 | 用於取樣的種子。設定為 0 則省略。大多數模型僅將其視為提示。 (預設值：0) |
| `system_prompt` | STRING | 否 | 不適用 | 決定模型行為的基礎指令。 (預設值："") |

**關於 `model` 參數的備註：** 可用的模型選項是動態建構的，可能包含具有不同能力的模型。某些模型支援額外功能，例如推理努力、網路搜尋或圖片/影片輸入。此節點將驗證提供的圖片或影片數量是否超過模型支援的最大數量。

**關於 `seed` 參數的備註：** `seed` 參數具有「生成後控制」行為，這意味著它可以設定為在每次節點執行後自動更改（例如隨機化、遞增或固定），具體取決於使用者的小工具設定。

**關於 `system_prompt` 的備註：** 此參數為可選，並在使用者介面中標記為進階參數。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | STRING | 從 OpenRouter 模型生成的文字回應。 |

---
**Source fingerprint (SHA-256):** `24757e36bf2356cc1805a6f071db88ca455e17944695672f19845a4cd1826c8a`
