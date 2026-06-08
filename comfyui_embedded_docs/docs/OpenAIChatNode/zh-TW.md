## 概述

此節點從 OpenAI 模型生成文字回應。它將您的文字提示（以及可選的圖片或檔案）發送到 OpenAI 模型，並返回生成的文字回應。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | 輸入給模型的文字，用於生成回應（預設值：空） | STRING | 是 | - |
| `persist_context` | 此參數已棄用，無實際作用（預設值：False） | BOOLEAN | 是 | - |
| `model` | 用於生成回應的模型 | COMBO | 是 | 多個可用的 OpenAI 模型 |
| `images` | 可選的圖片，作為模型的上下文。若要包含多張圖片，可以使用批次圖片節點 | IMAGE | 否 | - |
| `files` | 可選的檔案，作為模型的上下文。接受來自 OpenAI 聊天輸入檔案節點的輸入 | OPENAI_INPUT_FILES | 否 | - |
| `advanced_options` | 可選的模型配置。接受來自 OpenAI 聊天進階選項節點的輸入 | OPENAI_CHAT_CONFIG | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output_text` | OpenAI 模型生成的文字回應 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ea66b58b23305b0d97bfc76cc39cfdfe8e01b70edcbfd60c2c640a07ad507ee6`
