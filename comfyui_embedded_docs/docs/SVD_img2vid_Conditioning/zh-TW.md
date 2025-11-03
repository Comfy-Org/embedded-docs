> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/zh-TW.md)

SVD_img2vid_Conditioning 節點用於為 Stable Video Diffusion 影片生成準備條件資料。它接收初始圖像，並透過 CLIP 視覺和 VAE 編碼器進行處理，以建立正向和負向條件對，同時生成用於影片生成的空白潛在空間。此節點設定了控制生成影片中運動、幀率和增強等級的必要參數。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | 是 | - | 用於編碼輸入圖像的 CLIP 視覺模型 |
| `init_image` | IMAGE | 是 | - | 作為影片生成起點的初始圖像 |
| `vae` | VAE | 是 | - | 用於將圖像編碼到潛在空間的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片寬度（預設值：1024，間隔：8） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片高度（預設值：576，間隔：8） |
| `video_frames` | INT | 是 | 1 至 4096 | 影片中要生成的幀數（預設值：14） |
| `motion_bucket_id` | INT | 是 | 1 至 1023 | 控制生成影片中的運動量（預設值：127） |
| `fps` | INT | 是 | 1 至 1024 | 生成影片的每秒幀數（預設值：6） |
| `augmentation_level` | FLOAT | 是 | 0.0 至 10.0 | 應用於輸入圖像的噪聲增強等級（預設值：0.0，間隔：0.01） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 包含圖像嵌入和影片參數的正向條件資料 |
| `negative` | CONDITIONING | 具有歸零嵌入和影片參數的負向條件資料 |
| `latent` | LATENT | 準備用於影片生成的空白潛在空間張量 |