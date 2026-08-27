# SamplerEulerAncestralCFG++

SamplerEulerAncestralCFGPP 節點創建了一個使用 Euler Ancestral 方法並結合無分類器引導（CFG++）的取樣器，用於圖像生成。此取樣器將祖先取樣技術與引導條件相結合，以產生多樣化的圖像變體，同時保持一致性，並可透過控制噪聲和步長調整的參數進行微調。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `eta` | 控制取樣期間的步長，數值越高更新越激進（預設：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `s_noise` | 調整取樣過程中添加的噪聲量（預設：1.0） | FLOAT | 是 | 0.0 - 10.0 |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 回傳一個已設定的取樣器物件，可用於圖像生成流程 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/zh-TW.md)

---
**Source fingerprint (SHA-256):** `de83cb4c3e9aeee60f1554ad1af8181adb4fa62e3d23cec02a6f4396b96500c1`
