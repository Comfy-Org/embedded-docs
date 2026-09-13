# SamplerEulerAncestralCFG++

SamplerEulerAncestralCFG++ 節點會建立一個取樣器，使用 Euler Ancestral 方法搭配無分類器引導（CFG++）來進行影像生成。此取樣器結合了祖先取樣技術與引導調節，可在維持連貫性的同時產生多樣的影像變化，並可透過控制雜訊與步長調整的參數進行微調。

## 輸入

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `eta` | 控制取樣期間的步長，數值越高會產生越積極的更新（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `s_noise` | 調整取樣過程中加入的雜訊量（預設值：1.0） | FLOAT | 是 | 0.0 - 10.0 |

## 輸出

| Output Name | Description | Data Type |
| --- | --- | --- |
| `sampler` | 傳回一個已配置的取樣器物件，可用於影像生成流程中 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/zh-TW.md)

---
**Source fingerprint (SHA-256):** `de83cb4c3e9aeee60f1554ad1af8181adb4fa62e3d23cec02a6f4396b96500c1`
