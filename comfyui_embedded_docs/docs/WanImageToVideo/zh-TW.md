> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/zh-TW.md)

WanImageToVideo 節點為影片生成任務準備條件約束和潛在表示。它為影片生成創建一個空的潛在空間，並可選擇性地結合起始圖像和 CLIP 視覺輸出來引導影片生成過程。該節點根據提供的圖像和視覺資料修改正向和負向條件約束輸入。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用於引導生成的正向條件約束輸入 |
| `negative` | CONDITIONING | 是 | - | 用於引導生成的負向條件約束輸入 |
| `vae` | VAE | 是 | - | 用於將圖像編碼到潛在空間的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片的寬度（預設值：832，間距：16） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片的高度（預設值：480，間距：16） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 影片中的影格數量（預設值：81，間距：4） |
| `batch_size` | INT | 是 | 1 至 4096 | 批次中生成的影片數量（預設值：1） |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 否 | - | 可選的 CLIP 視覺輸出，用於附加條件約束 |
| `start_image` | IMAGE | 否 | - | 可選的起始圖像，用於初始化影片生成 |

**注意：** 當提供 `start_image` 時，節點會對圖像序列進行編碼並對條件約束輸入應用遮罩處理。當提供 `clip_vision_output` 參數時，會向正向和負向輸入添加基於視覺的條件約束。

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已整合圖像和視覺資料的修改後正向條件約束 |
| `negative` | CONDITIONING | 已整合圖像和視覺資料的修改後負向條件約束 |
| `latent` | LATENT | 準備用於影片生成的空潛在空間張量 |