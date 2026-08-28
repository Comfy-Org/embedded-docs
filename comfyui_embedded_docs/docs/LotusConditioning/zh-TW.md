# LotusConditioning

LotusConditioning 節點為 Lotus 模型提供預先計算的條件嵌入。它使用具有空條件的凍結編碼器，並返回硬編碼的提示詞嵌入，以與參考實作達到一致，無需執行推理或載入大型張量檔案。此節點輸出一個固定的條件張量，可直接用於生成流程。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| *無輸入* | 此節點不接受任何輸入參數。 | - | - | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `條件` | Lotus 模型的預先計算條件嵌入，包含固定的提示詞嵌入和一個空字典。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`
