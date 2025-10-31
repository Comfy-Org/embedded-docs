> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/zh-TW.md)

SamplerDPMPP_3M_SDE 節點建立一個 DPM++ 3M SDE 取樣器，用於取樣流程中。此取樣器採用三階多步隨機微分方程方法，並具有可配置的雜訊參數。該節點允許您選擇在 GPU 或 CPU 上執行雜訊計算。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | 是 | 0.0 - 100.0 | 控制取樣過程的隨機性（預設值：1.0） |
| `s_noise` | FLOAT | 是 | 0.0 - 100.0 | 控制取樣期間添加的雜訊量（預設值：1.0） |
| `noise_device` | COMBO | 是 | "gpu"<br>"cpu" | 選擇用於雜訊計算的設備，可選 GPU 或 CPU |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 返回一個已配置的取樣器物件，供取樣工作流程使用 |