# SamplerLMS

SamplerLMS 節點為擴散模型建立一個最小均方（LMS）取樣器。它會產生一個可在取樣過程中使用的取樣器物件，讓您控制 LMS 演算法的階數，以達到數值穩定性與準確性。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `order` | LMS 取樣器演算法的階數參數，控制數值方法的準確性與穩定性（預設值：4；進階參數） | INT | 是 | 1 to 100 |

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `sampler` | 已設定的 LMS 取樣器物件，可在取樣流程中使用 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLMS/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3d59fbbd5b9b0bfa2ee3b384aca08855988d0b7a2a94d805f978b9dd7caa0f39`
