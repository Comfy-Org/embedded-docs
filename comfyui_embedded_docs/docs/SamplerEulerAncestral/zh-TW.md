# SamplerEulerAncestral

SamplerEulerAncestral 節點會建立一個 Euler Ancestral 取樣器，用於生成影像。此取樣器採用特定的數學方法，結合 Euler 積分與 ancestral 取樣技術來產生影像變體。此節點允許您透過調整控制生成過程中隨機性與步長的參數，來設定取樣行為。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `eta` | 控制取樣過程的步長與隨機性（預設值：1.0）。這是進階參數。 | FLOAT | 是 | 0.0 - 100.0 |
| `s_noise` | 控制取樣過程中加入的雜訊量（預設值：1.0）。這是進階參數。 | FLOAT | 是 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
| --- | --- | --- |
| `sampler` | 回傳一個已設定的 Euler Ancestral 取樣器，可用於取樣流程中。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0d3c1f0ffe01eb6cc17fd53e743713f659218ec19001c670440472ae7d0d3887`
