# SamplerLMS

SamplerLMS 節點用於建立擴散模型中使用的最小均方（LMS）採樣器。它會產生一個可用於取樣過程的採樣器物件，讓您能夠控制 LMS 演算法的階數，以達到數值穩定性和準確性。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `順序` | LMS 採樣器演算法的階數參數，控制數值方法的準確性與穩定性（預設值：4）。此參數顯示在節點介面的進階區段中。 | INT | 是 | 1 到 100 |

## 輸出

| 輸出名 | 說明 | 資料型別 |
| --- | --- | --- |
| `sampler` | 一個已配置的 LMS 採樣器物件，可用於取樣流程中 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3d59fbbd5b9b0bfa2ee3b384aca08855988d0b7a2a94d805f978b9dd7caa0f39`
