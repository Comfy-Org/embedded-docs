# SamplerEulerAncestral

SamplerEulerAncestral 節點會建立一個可用於影像生成期間的 Euler Ancestral 取樣器。此取樣器結合 Euler 積分與祖先取樣，會在每個步驟加入一定程度的隨機性，以產生多樣化的結果。此節點可讓你透過其設定調整套用的隨機性程度。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `eta` | 控制取樣過程的步長與隨機性（預設：1.0）。這是進階參數。 | FLOAT | 是 | 0.0 - 100.0 |
| `s_noise` | 控制取樣期間加入的雜訊量（預設：1.0）。這是進階參數。 | FLOAT | 是 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 傳回一個已設定的 Euler Ancestral 取樣器，可用於取樣流程中。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0d3c1f0ffe01eb6cc17fd53e743713f659218ec19001c670440472ae7d0d3887`
