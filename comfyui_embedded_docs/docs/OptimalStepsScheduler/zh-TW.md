> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/zh-TW.md)

OptimalStepsScheduler 節點根據所選模型類型和步數配置，為擴散模型計算噪聲調度 sigma 值。它會根據降噪參數調整總步數，並對噪聲級別進行插值以匹配請求的步數。該節點返回一個 sigma 值序列，用於決定擴散採樣過程中的噪聲級別。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model_type` | COMBO | 是 | "FLUX"<br>"Wan"<br>"Chroma" | 用於計算噪聲級別的擴散模型類型 |
| `steps` | INT | 是 | 3-1000 | 要計算的總採樣步數（預設值：20） |
| `denoise` | FLOAT | 否 | 0.0-1.0 | 控制降噪強度，調整有效步數（預設值：1.0） |

**注意：** 當 `denoise` 設定為小於 1.0 時，節點會將有效步數計算為 `steps * denoise`。如果 `denoise` 設定為 0.0，節點將返回空張量。

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | 代表擴散採樣噪聲調度的 sigma 值序列 |