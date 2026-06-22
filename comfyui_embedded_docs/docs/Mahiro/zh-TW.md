# Mahiro 太可愛了，應該要有更好的引導功能!! (。・ω・。)

Mahiro 節點會修改引導函數，使其更專注於正向提示的方向，而非正向與負向提示之間的差異。它會建立一個經過修補的模型，利用正規化條件與非條件去噪輸出之間的餘弦相似度，來應用自訂的引導縮放方法。這個實驗性節點有助於更強烈地將生成結果導向正向提示的預期方向。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用修改後引導函數進行修補的模型 | MODEL | 是 |  |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `patched_model` | 已套用 Mahiro 引導函數的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Mahiro/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8b4a73cfa488f97d87e5a18d5ab30765055b5d5a66c6c2f1a5f016eed2af0300`
