> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/zh-TW.md)

LatentOperationSharpen 節點使用高斯核心對潛在表徵應用銳化效果。它通過將潛在數據標準化、應用自定義銳化核心的卷積運算，然後恢復原始亮度來實現。這能增強潛在空間表徵中的細節和邊緣。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `sharpen_radius` | INT | 否 | 1-31 | 銳化核心的半徑（預設值：9） |
| `sigma` | FLOAT | 否 | 0.1-10.0 | 高斯核心的標準差（預設值：1.0） |
| `alpha` | FLOAT | 否 | 0.0-5.0 | 銳化強度因子（預設值：0.1） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `operation` | LATENT_OPERATION | 返回可應用於潛在數據的銳化操作 |