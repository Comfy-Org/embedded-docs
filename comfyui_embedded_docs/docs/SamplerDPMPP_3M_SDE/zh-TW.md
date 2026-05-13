> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/zh-TW.md)

## 概述

SamplerDPMPP_3M_SDE 節點建立一個用於取樣過程的 DPM++ 3M SDE 取樣器。此取樣器使用三階多步隨機微分方程方法，並配備可設定的噪聲參數。該節點允許您選擇噪聲計算是在 GPU 還是 CPU 上執行。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | 是 | 0.0 - 100.0 | 控制取樣過程的隨機性（預設值：1.0） |
| `s_noise` | FLOAT | 是 | 0.0 - 100.0 | 控制取樣過程中添加的噪聲量（預設值：1.0） |
| `noise_device` | COMBO | 是 | "gpu"<br>"cpu" | 選擇用於噪聲計算的裝置，可選 GPU 或 CPU（預設值："gpu"） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 返回一個已設定的取樣器物件，用於取樣工作流程中 |

---
**Source fingerprint (SHA-256):** `817ce8c12245063e5f2f3421f57dd55801aae96dfd8fe1bf3f88f814799b830a`
