# FluxKontext 多重參考潛在方法

FluxKontextMultiReferenceLatentMethod 節點會將所選的參考潛在向量方法儲存在條件資料中，以更新條件資料。儲存的方法會在後續生成步驟處理參考潛在向量時使用。此節點標記為實驗性，並屬於 Flux 條件系統。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `條件化` | 要使用參考潛在向量方法修改的條件資料 | CONDITIONING | 是 | - |
| `參考潛在方法` | 用於處理參考潛在向量的方法。若選取包含 "uxo" 或 "uso" 的值，儲存前會將其轉換為 "uxo"。此參數標記為進階。 | COMBO | 是 | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `conditioning` | 已套用參考潛在向量方法的修改後條件資料 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
