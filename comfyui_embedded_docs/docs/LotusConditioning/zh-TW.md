# LotusConditioning

LotusConditioning 節點為 Lotus 模型提供固定、預先計算的 conditioning 嵌入。由於 Lotus 使用帶有 null conditioning 的凍結編碼器，此節點會直接內嵌產生的提示詞嵌入，而不是執行推論或載入大型張量檔案，因此其輸出永遠不會改變。回傳的 conditioning 可直接接入需要 Lotus 相容 conditioning 的生成管線。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| *無輸入* | 此節點不接受任何輸入參數。 | - | - | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `conditioning` | Lotus 模型的預先計算 conditioning 嵌入。以 conditioning 清單形式回傳，其中包含固定的提示詞嵌入以及一個空字典。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`
