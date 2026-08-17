# SamplerEulerAncestral

SamplerEulerAncestral 節點會建立一個 Euler Ancestral 取樣器，用於生成圖像。此取樣器使用一種特定的數學方法，結合 Euler 積分與祖先取樣技術來產生圖像變體。此節點允許您透過調整參數來配置取樣行為，這些參數控制生成過程中的隨機性與步長。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `eta` | 控制取樣過程的步長與隨機性（預設值：1.0）。此為進階參數。 | FLOAT | 否 | 0.0 - 100.0 |
| `s_noise` | 控制取樣期間添加的雜訊量（預設值：1.0）。此為進階參數。 | FLOAT | 否 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sampler` | 回傳一個已配置的 Euler Ancestral 取樣器，可用於取樣流程中。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0d3c1f0ffe01eb6cc17fd53e743713f659218ec19001c670440472ae7d0d3887`
