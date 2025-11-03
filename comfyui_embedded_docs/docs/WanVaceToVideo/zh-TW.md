> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/zh-TW.md)

WanVaceToVideo 節點處理影片生成模型的影片條件資料。它接收正向和負向條件輸入以及影片控制資料，並準備用於影片生成的潛在表示。該節點處理影片放大、遮罩和 VAE 編碼，為影片模型創建適當的條件結構。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用於引導生成的正向條件輸入 |
| `negative` | CONDITIONING | 是 | - | 用於引導生成的負向條件輸入 |
| `vae` | VAE | 是 | - | 用於編碼圖像和影片幀的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片寬度（像素）（預設值：832，步長：16） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片高度（像素）（預設值：480，步長：16） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 影片中的幀數（預設值：81，步長：4） |
| `batch_size` | INT | 是 | 1 至 4096 | 同時生成的影片數量（預設值：1） |
| `strength` | FLOAT | 是 | 0.0 至 1000.0 | 影片條件控制的強度（預設值：1.0，步長：0.01） |
| `control_video` | IMAGE | 否 | - | 用於控制條件的可選輸入影片 |
| `control_masks` | MASK | 否 | - | 用於控制影片哪些部分需要修改的可選遮罩 |
| `reference_image` | IMAGE | 否 | - | 用於附加條件的可選參考圖像 |

**注意：** 當提供 `control_video` 時，它將被放大以符合指定的寬度和高度。如果提供 `control_masks`，則必須與控制影片的尺寸相符。當提供 `reference_image` 時，它會透過 VAE 進行編碼並附加到潛在序列的前面。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已應用影片控制資料的正向條件 |
| `negative` | CONDITIONING | 已應用影片控制資料的負向條件 |
| `latent` | LATENT | 準備用於影片生成的空潛在張量 |
| `trim_latent` | INT | 使用參考圖像時需要修剪的潛在幀數 |