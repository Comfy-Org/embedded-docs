> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/zh-TW.md)

WanFunInpaintToVideo 節點透過在起始圖像和結束圖像之間進行修補來創建影片序列。它接收正向和反向條件提示以及可選的幀圖像，以生成影片潛在表示。該節點可處理具有可配置尺寸和長度參數的影片生成。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用於影片生成的正向條件提示 |
| `negative` | CONDITIONING | 是 | - | 在影片生成中要避免的反向條件提示 |
| `vae` | VAE | 是 | - | 用於編碼/解碼操作的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片的寬度（像素）（預設值：832，間隔：16） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片的高度（像素）（預設值：480，間隔：16） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 影片序列中的幀數（預設值：81，間隔：4） |
| `batch_size` | INT | 是 | 1 至 4096 | 單次批次中生成的影片數量（預設值：1） |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 否 | - | 用於額外條件提示的可選 CLIP 視覺輸出 |
| `start_image` | IMAGE | 否 | - | 用於影片生成的可選起始幀圖像 |
| `end_image` | IMAGE | 否 | - | 用於影片生成的可選結束幀圖像 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 處理後的正向條件輸出 |
| `negative` | CONDITIONING | 處理後的反向條件輸出 |
| `latent` | LATENT | 生成的影片潛在表示 |