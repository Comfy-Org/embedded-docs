> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/zh-TW.md)

WanCameraImageToVideo 節點透過生成用於影片生成的潛在表徵，將圖像轉換為影片序列。它處理條件輸入和可選的起始圖像，以創建可用於影片模型的影片潛在表徵。該節點支援相機條件和 CLIP 視覺輸出，以增強影片生成的控制。

## 輸入參數

| 參數名稱 | 資料類型 | 是否必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用於影片生成的正面條件提示 |
| `negative` | CONDITIONING | 是 | - | 在影片生成中要避免的負面條件提示 |
| `vae` | VAE | 是 | - | 用於將圖像編碼到潛在空間的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片的寬度（像素）（預設值：832，間隔：16） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片的高度（像素）（預設值：480，間隔：16） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 影片序列中的幀數（預設值：81，間隔：4） |
| `batch_size` | INT | 是 | 1 至 4096 | 同時生成的影片數量（預設值：1） |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 否 | - | 可選的 CLIP 視覺輸出，用於附加條件控制 |
| `start_image` | IMAGE | 否 | - | 可選的起始圖像，用於初始化影片序列 |
| `camera_conditions` | WAN_CAMERA_EMBEDDING | 否 | - | 可選的相機嵌入條件，用於影片生成 |

**注意：** 當提供 `start_image` 時，該節點會使用它來初始化影片序列，並應用遮罩將起始幀與生成的內容混合。`camera_conditions` 和 `clip_vision_output` 參數是可選的，但當提供時，它們會修改正面和負面提示的條件。

## 輸出參數

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 應用相機條件和 CLIP 視覺輸出後的修改版正面條件 |
| `negative` | CONDITIONING | 應用相機條件和 CLIP 視覺輸出後的修改版負面條件 |
| `latent` | LATENT | 生成的影片潛在表徵，可供影片模型使用 |