# 停用雜訊

DisableNoise 節點提供一個空的噪聲配置，可用於在取樣過程中停用噪聲生成。它會回傳一個不包含任何噪聲數據的特殊噪聲物件，讓其他節點在連接此輸出時能夠跳過與噪聲相關的操作。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| *無輸入參數* | 此節點不需要任何輸入參數。 | - | - | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `NOISE` | 回傳一個空的噪聲配置，可用於在取樣過程中停用噪聲生成。 | NOISE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `527152dff69bd5c55c622c634b87e625eb16708f8595fa02d69cf38f1125c5eb`
