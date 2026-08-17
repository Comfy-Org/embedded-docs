# SamplerDPMPP_3M_SDE

SamplerDPMPP_3M_SDE 節點會建立一個 DPM++ 3M SDE 取樣器，用於取樣流程。此取樣器使用三階多步隨機微分方程式方法，並具備可設定的雜訊參數。此節點可讓您選擇在 GPU 或 CPU 上執行雜訊計算。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `eta` | 控制取樣過程的隨機性（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `s_noise` | 控制取樣期間新增的雜訊量（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `noise_device` | 選擇用於雜訊計算的裝置，可為 GPU 或 CPU（預設值："gpu"） | COMBO | 是 | "gpu"<br>"cpu" |

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `sampler` | 傳回已設定的取樣器物件，供取樣工作流程使用 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0f624398c67e50639fc41384b50b91bab93797bd785dda25f1f5fc649e46825b`
