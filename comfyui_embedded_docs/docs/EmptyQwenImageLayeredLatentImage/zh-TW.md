> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/zh-TW.md)

Empty Qwen Image Layered Latent 節點會建立一個空白的多層潛在表徵，供 Qwen 圖像模型使用。它會產生一個填滿零值的張量，其結構包含指定的層數、批次大小和空間維度。這個空白的潛在表徵可作為後續圖像生成或處理工作流程的起點。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 要建立的潛在圖像寬度。該值必須能被 16 整除。(預設值: 640) |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 要建立的潛在圖像高度。該值必須能被 16 整除。(預設值: 640) |
| `layers` | INT | 是 | 0 至 MAX_RESOLUTION | 要添加到潛在結構中的額外層數。這定義了潛在表徵的深度。(預設值: 3) |
| `batch_size` | INT | 否 | 1 至 4096 | 要在一個批次中生成的潛在樣本數量。(預設值: 1) |

**注意：** `width` 和 `height` 參數在內部會除以 8，以決定輸出潛在張量的空間維度。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `samples` | LATENT | 一個填滿零值的潛在張量。其形狀為 `[batch_size, 16, layers + 1, height // 8, width // 8]`。 |
