> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/zh-TW.md)

ModelSamplingLTXV 節點根據 token 數量對模型應用進階採樣參數。它使用基礎位移值和最大位移值之間的線性插值來計算位移值，該計算取決於輸入潛在表示中的 token 數量。該節點隨後創建一個專門的模型採樣配置並將其應用於輸入模型。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要應用採樣參數的輸入模型 |
| `max_shift` | FLOAT | 否 | 0.0 至 100.0 | 計算中使用的最大位移值（預設值：2.05） |
| `base_shift` | FLOAT | 否 | 0.0 至 100.0 | 計算中使用的基礎位移值（預設值：0.95） |
| `latent` | LATENT | 否 | - | 用於確定位移計算的 token 數量的可選潛在表示輸入 |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用採樣參數的修改後模型 |