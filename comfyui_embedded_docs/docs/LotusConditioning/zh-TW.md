# LotusConditioning

這份文件是由 AI 生成的。如果您發現任何錯誤或有改進建議，歡迎隨時貢獻！[在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/en.md)

LotusConditioning 節點為 Lotus 模型提供預先計算的條件嵌入。它使用帶有空條件（null conditioning）的凍結編碼器，並返回硬編碼的提示詞嵌入，以達到與參考實作一致的效果，無需進行推理或載入大型張量檔案。此節點輸出一個固定的條件張量，可直接用於生成流程中。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| *無輸入* | 此節點不接受任何輸入參數。 | - | - | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `條件` | Lotus 模型的預先計算條件嵌入，包含固定的提示詞嵌入和一個空字典。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `aa428f8c355e2840dadbf634fe27d20c7c323dbe8c21255b40f4dafa12e4a0d0`
