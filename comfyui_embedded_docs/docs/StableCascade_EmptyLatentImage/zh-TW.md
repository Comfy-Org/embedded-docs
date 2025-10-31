> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/zh-TW.md)

StableCascade_EmptyLatentImage 節點為 Stable Cascade 模型建立空的潛在張量。它會根據輸入解析度和壓縮設定，產生兩個獨立的潛在表示 - 一個用於階段 C，另一個用於階段 B，並具有適當的維度。此節點為 Stable Cascade 生成流程提供了起始點。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `寬度` | INT | 是 | 256 至 MAX_RESOLUTION | 輸出圖像的寬度（單位：像素）（預設值：1024，間隔：8） |
| `高度` | INT | 是 | 256 至 MAX_RESOLUTION | 輸出圖像的高度（單位：像素）（預設值：1024，間隔：8） |
| `壓縮` | INT | 是 | 4 至 128 | 決定階段 C 潛在維度的壓縮係數（預設值：42，間隔：1） |
| `批次大小` | INT | 否 | 1 至 4096 | 單次批次中要生成的潛在樣本數量（預設值：1） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `stage_b` | LATENT | 階段 C 潛在張量，維度為 [batch_size, 16, height//compression, width//compression] |
| `stage_b` | LATENT | 階段 B 潛在張量，維度為 [batch_size, 4, height//4, width//4] |