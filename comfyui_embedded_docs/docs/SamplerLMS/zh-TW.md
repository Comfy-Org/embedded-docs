# SamplerLMS

SamplerLMS 節點會建立一個最小均方（LMS）取樣器，用於擴散模型中。它會產生一個可用於取樣過程的取樣器物件，讓您能夠控制 LMS 演算法的階數，以達到數值穩定性與準確性。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `順序` | LMS 取樣器演算法的階數參數，用於控制數值方法的準確性與穩定性（預設值：4） | INT | 是 | 1 至 100 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sampler` | 一個已設定的 LMS 取樣器物件，可用於取樣流程中 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0c045ef15890fe611dc0b9d455bafa313d28373a29c881a0c8bf5d80e69bc114`
