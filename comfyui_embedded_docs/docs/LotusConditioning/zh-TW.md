# LotusConditioning

LotusConditioning 節點為 Lotus 模型提供預先計算好的 conditioning 嵌入。它使用凍結的編碼器搭配 null conditioning，並回傳硬編碼的 prompt 嵌入，以在不需要執行推論或載入大型張量檔案的情況下，達成與參考實作一致的效果。此節點輸出一個固定的 conditioning 張量，可直接用於生成流程。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| *無輸入* | 此節點不接受任何輸入參數。 | - | - | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `conditioning` | 為 Lotus 模型預先計算的 conditioning 嵌入，包含固定的 prompt 嵌入與一個空字典。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`
