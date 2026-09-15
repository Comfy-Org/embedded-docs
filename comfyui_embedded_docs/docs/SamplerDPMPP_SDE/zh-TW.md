# SamplerDPMPP_SDE

## 概覽

SamplerDPMPP_SDE 建立一個 DPM++ SDE（隨機微分方程）取樣器，供取樣流程使用。此取樣器提供一種隨機取樣方法，可設定雜訊參數並選擇裝置。它會傳回一個可在取樣流程中使用的取樣器物件。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `eta` | 控制取樣過程的隨機性（預設：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `s_noise` | 控制取樣期間加入的雜訊量（預設：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `r` | 影響取樣行為的參數（預設：0.5） | FLOAT | 是 | 0.0 - 100.0 |
| `noise_device` | 選擇執行雜訊計算的裝置。設為 "cpu" 時，會建立 `dpmpp_sde` 取樣器；設為 "gpu" 時，會建立 `dpmpp_sde_gpu` 取樣器（預設："gpu"） | COMBO | 是 | "gpu"<br>"cpu" |

備註：所有輸入都標記為進階參數。`noise_device` 的選擇會改變所建立的取樣器變體："cpu" 對應至 `dpmpp_sde`，"gpu" 對應至 `dpmpp_sde_gpu`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 傳回已設定的 DPM++ SDE 取樣器物件，供取樣流程使用 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/zh-TW.md)

---
**Source fingerprint (SHA-256):** `56949712f245abfcc48c09d7d14a1a7778e80ba58535e538484c382d7e0d02c6`
