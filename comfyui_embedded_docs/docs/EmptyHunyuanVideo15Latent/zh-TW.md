> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/zh-TW.md)

此節點創建一個專門為 HunyuanVideo 1.5 模型格式化的空潛在張量。它通過為模型潛在空間分配具有正確通道數和空間維度的零張量，為影片生成生成一個空白的起始點。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | 是 | - | 影片畫面的寬度（像素）。 |
| `height` | INT | 是 | - | 影片畫面的高度（像素）。 |
| `length` | INT | 是 | - | 影片序列的幀數。 |
| `batch_size` | INT | 否 | - | 批次中要生成的影片樣本數量（預設值：1）。 |

**注意：** 生成的潛在張量的空間維度是通過將輸入的 `width` 和 `height` 除以 16 來計算的。時間維度（幀數）計算方式為 `((length - 1) // 4) + 1`。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `samples` | LATENT | 一個適合 HunyuanVideo 1.5 模型維度的空潛在張量。張量形狀為 `[batch_size, 32, frames, height//16, width//16]`。 |
