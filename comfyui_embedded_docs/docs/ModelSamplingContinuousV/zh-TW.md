> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousV/zh-TW.md)

ModelSamplingContinuousV 節點透過應用連續 V-prediction 採樣參數來修改模型的採樣行為。它會創建輸入模型的副本，並使用自定義的 sigma 範圍設定進行配置，以實現進階的採樣控制。這讓使用者能夠透過特定的最小和最大 sigma 值來微調採樣過程。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要使用連續 V-prediction 採樣進行修改的輸入模型 |
| `sampling` | STRING | 是 | "v_prediction" | 要應用的採樣方法（目前僅支援 V-prediction） |
| `sigma_max` | FLOAT | 是 | 0.0 - 1000.0 | 採樣的最大 sigma 值（預設值：500.0） |
| `sigma_min` | FLOAT | 是 | 0.0 - 1000.0 | 採樣的最小 sigma 值（預設值：0.03） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用連續 V-prediction 採樣的修改後模型 |