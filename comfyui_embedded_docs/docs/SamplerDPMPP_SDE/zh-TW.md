> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/zh-TW.md)

SamplerDPMPP_SDE 節點建立一個 DPM++ SDE（隨機微分方程）取樣器，用於取樣過程中。此取樣器提供一種隨機取樣方法，具有可設定的雜訊參數和裝置選擇功能。它會傳回一個可用於取樣管線的取樣器物件。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | 是 | 0.0 - 100.0 | 控制取樣過程的隨機性（預設值：1.0） |
| `s_noise` | FLOAT | 是 | 0.0 - 100.0 | 控制取樣期間添加的雜訊量（預設值：1.0） |
| `r` | FLOAT | 是 | 0.0 - 100.0 | 影響取樣行為的參數（預設值：0.5） |
| `noise_device` | COMBO | 是 | "gpu"<br>"cpu" | 選擇執行雜訊計算的裝置（預設值："gpu"） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 傳回一個已設定的 DPM++ SDE 取樣器物件，用於取樣管線中 |

---
**Source fingerprint (SHA-256):** `43b3b3c4b2756a6e7979c12418de1dba79e3e0c0fde2a06505cf0a6825e6ebbf`
