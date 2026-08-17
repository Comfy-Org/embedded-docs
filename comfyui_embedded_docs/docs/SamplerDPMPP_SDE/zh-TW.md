# SamplerDPMPP_SDE

The SamplerDPMPP_SDE 節點建立一個 DPM++ SDE（隨機微分方程）採樣器，用於取樣過程。此採樣器提供具有可配置雜訊參數和裝置選擇的隨機取樣方法。它返回一個可用於取樣管線的採樣器物件。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 數值範圍 |
| --- | --- | --- | --- | --- |
| `eta` | 控制取樣過程的隨機性（預設：1.0） | FLOAT | Yes | 0.0 - 100.0 |
| `s_noise` | 控制取樣期間添加的雜訊量（預設：1.0） | FLOAT | Yes | 0.0 - 100.0 |
| `r` | 影響取樣行為的參數（預設：0.5） | FLOAT | Yes | 0.0 - 100.0 |
| `noise_device` | 選擇執行雜訊計算的裝置（預設："gpu"）。設定為 "cpu" 時，使用標準 `dpmpp_sde` 採樣器；設定為 "gpu" 時，使用 `dpmpp_sde_gpu` 採樣器。 | COMBO | Yes | "gpu"<br>"cpu" |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 返回一個已配置的 DPM++ SDE 採樣器物件，可用於取樣管線 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/zh-TW.md)

---
**Source fingerprint (SHA-256):** `56949712f245abfcc48c09d7d14a1a7778e80ba58535e538484c382d7e0d02c6`
