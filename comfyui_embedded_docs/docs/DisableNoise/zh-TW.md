# 停用雜訊

DisableNoise 節點提供一個空白的雜訊設定，可用於在取樣過程中停用雜訊產生。它會回傳一個不包含任何雜訊資料的特殊雜訊物件，讓其他節點在連接到此輸出時，可以跳過與雜訊相關的操作。

## 輸入

| 參數 | 描述 | 資料型態 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| *無輸入參數* | 此節點不需要任何輸入參數。 | - | - | - |

## 輸出

| 輸出名 | 描述 | 資料型態 |
| --- | --- | --- |
| `NOISE` | 回傳一個空白的雜訊設定，可用於在取樣過程中停用雜訊產生。 | NOISE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b9edcda655dab3196233b6c66fdb41eb0585b153616b793016d532992b922934`
