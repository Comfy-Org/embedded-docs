> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/zh-TW.md)

## 概述

SamplerDPMPP_2M_SDE 節點為擴散模型建立一個 DPM++ 2M SDE 取樣器。此取樣器使用二階微分方程求解器搭配隨機微分方程來生成樣本。它提供不同的求解器類型和雜訊處理選項，以控制取樣過程。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `solver_type` | STRING | 是 | `"midpoint"`<br>`"heun"` | 用於取樣過程的微分方程求解器類型 |
| `eta` | FLOAT | 是 | 0.0 - 100.0 | 控制取樣過程的隨機性（預設值：1.0） |
| `s_noise` | FLOAT | 是 | 0.0 - 100.0 | 控制取樣過程中添加的雜訊量（預設值：1.0） |
| `noise_device` | STRING | 是 | `"gpu"`<br>`"cpu"` | 執行雜訊計算的裝置。設定為 "cpu" 時，取樣器使用基於 CPU 的雜訊生成；設定為 "gpu" 時，則使用基於 GPU 的雜訊生成，以獲得潛在的更高效能 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 一個已配置的取樣器物件，可直接用於取樣流程 |

---
**Source fingerprint (SHA-256):** `4a6a16e3494e8270f3707e172f252e7fc4e1b65efbecd3dd086b1a1edc5ba23a`
