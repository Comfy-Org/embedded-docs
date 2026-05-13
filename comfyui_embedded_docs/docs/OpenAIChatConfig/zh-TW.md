> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/zh-TW.md)

## 概述

OpenAIChatConfig 節點允許為 OpenAI 聊天節點設定額外的配置選項。它提供進階設定，用於控制模型生成回應的方式，包括截斷行為、輸出長度限制和自訂指令。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `truncation` | COMBO | 是 | `"auto"`<br>`"disabled"` | 用於模型回應的截斷策略。auto：如果此回應與先前回應的上下文超過模型的上下文視窗大小，模型將透過刪除對話中間的輸入項目來截斷回應，以適應上下文視窗。disabled：如果模型回應將超過模型的上下文視窗大小，請求將失敗並回傳 400 錯誤（預設值："auto"） |
| `max_output_tokens` | INT | 否 | 16 至 16384 | 可為回應生成的 token 數量上限，包括可見的輸出 token（預設值：4096） |
| `instructions` | STRING | 否 | - | 提供給模型關於如何生成回應的指令（支援多行輸入） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `OPENAI_CHAT_CONFIG` | OPENAI_CHAT_CONFIG | 包含指定設定的配置物件，用於 OpenAI 聊天節點 |

---
**Source fingerprint (SHA-256):** `6d956aa1bc7f822c18ddaa55cd2345dad947fd93833de25a957f49878484af97`
