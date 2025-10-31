> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplingPercentToSigma/zh-TW.md)

{heading_overview}

SamplingPercentToSigma 節點使用模型的採樣參數將採樣百分比值轉換為對應的 sigma 值。它接收一個介於 0.0 到 1.0 之間的百分比值，並將其映射到模型噪聲調度中的適當 sigma 值，可選擇返回計算出的 sigma 值或邊界處的實際最大/最小 sigma 值。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 包含用於轉換的採樣參數的模型 |
| `sampling_percent` | FLOAT | 是 | 0.0 至 1.0 | 要轉換為 sigma 的採樣百分比（預設值：0.0） |
| `return_actual_sigma` | BOOLEAN | 是 | - | 返回實際的 sigma 值而非用於區間檢查的值。這僅影響 0.0 和 1.0 處的結果。（預設值：False） |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `sigma_value` | FLOAT | 對應輸入採樣百分比的轉換後 sigma 值 |