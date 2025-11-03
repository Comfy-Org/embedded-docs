> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/zh-TW.md)

EmptyHunyuanImageLatent 節點會建立一個具有特定維度的空潛在張量，專用於渾元影像生成模型。它生成一個空白的起始點，可在工作流程中透過後續節點進行處理。此節點允許您指定潛在空間的寬度、高度和批次大小。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | 是 | 64 至 MAX_RESOLUTION | 生成潛在影像的寬度（單位：像素，預設值：2048，間距：32） |
| `height` | INT | 是 | 64 至 MAX_RESOLUTION | 生成潛在影像的高度（單位：像素，預設值：2048，間距：32） |
| `batch_size` | INT | 是 | 1 至 4096 | 單次批次中生成的潛在樣本數量（預設值：1） |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `LATENT` | LATENT | 具有指定維度的空潛在張量，用於渾元影像處理 |