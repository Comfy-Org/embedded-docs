> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationTonemapReinhard/zh-TW.md)

LatentOperationTonemapReinhard 節點對潛在向量應用 Reinhard 色調映射技術。此方法會對潛在向量進行歸一化處理，並基於平均值和標準差的統計方法調整其幅度，調整強度由乘數參數控制。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `multiplier` | FLOAT | 否 | 0.0 至 100.0 | 控制色調映射效果的強度（預設值：1.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `operation` | LATENT_OPERATION | 返回可應用於潛在向量的色調映射操作 |