SamplerEulerAncestralCFGPP 節點建立一個取樣器，使用歐拉祖先法搭配無分類器引導（CFG++）進行影像生成。此取樣器結合祖先取樣技術與引導條件，在保持一致性的同時產生多樣化的影像變體，並可透過控制雜訊與步長調整的參數進行微調。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `eta` | 控制取樣過程中的步長，數值越高會產生更激進的更新（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `s_noise` | 調整取樣過程中添加的雜訊量（預設值：1.0） | FLOAT | 是 | 0.0 - 10.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 回傳一個已配置的取樣器物件，可用於影像生成流程中 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7eceec539a6a045db4d9953214add17011ef9d17e663dbbbbbb2bae0cbe40aa2`
