> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/zh-TW.md)

SamplerDPMPP_2M_SDE 節點為擴散模型創建一個 DPM++ 2M SDE 取樣器。此取樣器使用帶有隨機微分方程的二階微分方程求解器來生成樣本。它提供不同的求解器類型和噪聲處理選項來控制取樣過程。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `solver_type` | STRING | 是 | `"midpoint"`<br>`"heun"` | 用於取樣過程的微分方程求解器類型 |
| `eta` | FLOAT | 是 | 0.0 - 100.0 | 控制取樣過程的隨機性（預設值：1.0） |
| `s_noise` | FLOAT | 是 | 0.0 - 100.0 | 控制取樣過程中添加的噪聲量（預設值：1.0） |
| `noise_device` | STRING | 是 | `"gpu"`<br>`"cpu"` | 執行噪聲計算的裝置 |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 已配置的取樣器物件，準備好用於取樣流程 |