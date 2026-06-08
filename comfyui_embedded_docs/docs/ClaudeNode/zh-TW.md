## 概述

從 Anthropic Claude 模型生成文字回應。此節點將文字提示和可選圖片發送到 Claude 模型，並返回生成的文字回應。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | 輸入到模型的文字。（預設：空字串） | STRING | 是 | 不適用 |
| `model` | 用於生成回應的 Claude 模型。 | COMBO | 是 | `"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果皆非確定性。（預設：0） | INT | 是 | 0 到 2147483647 |
| `images` | 可選的圖片，作為模型的上下文。最多 20 張圖片。 | IMAGE | 否 | 0 到 20 張圖片 |
| `system_prompt` | 決定模型行為的基礎指令。（預設：空字串） | STRING | 否 | 不適用 |

### 參數限制

- **圖片限制**：每次請求最多可提供 20 張圖片。
- **溫度處理**：當啟用思考功能或使用「Opus 4.7」模型時，溫度參數會自動取消設定（預設為 1.0），這是 Anthropic API 的要求。對於其他模型，可透過模型配置設定溫度。
- **思考/推理**：模型配置包含一個 `reasoning_effort` 設定，用於控制是否啟用思考功能。啟用時，節點會根據所選模型自動配置適當的思考模式（自適應或基於預算）。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 從 Claude 模型生成的文字回應。若未生成文字，則返回「來自 Claude 模型的空回應。」 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e3bab004535d4d406582aa42f28bb64a2988f8331788d51ec1fa4e943d8d4382`
