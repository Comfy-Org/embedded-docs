# 停用雜訊

此節點提供一個空的雜訊配置，可在取樣期間停用雜訊生成。它會輸出一個不含任何雜訊資料的特殊雜訊物件，因此任何連接到它的節點都會略過與雜訊相關的操作。它也可以透過別名 "zero noise" 搜尋。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| *無輸入參數* | 此節點不需要任何輸入參數。 | - | - | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `NOISE` | 傳回一個空的雜訊配置，可用於在取樣過程中停用雜訊生成。 | NOISE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b9edcda655dab3196233b6c66fdb41eb0585b153616b793016d532992b922934`
