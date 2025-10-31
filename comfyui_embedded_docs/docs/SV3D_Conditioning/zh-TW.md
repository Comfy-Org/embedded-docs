> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/zh-TW.md)

{heading_overview}

SV3D_Conditioning 節點用於為 SV3D 模型的 3D 影片生成準備條件資料。它接收初始圖像，並透過 CLIP 視覺和 VAE 編碼器進行處理，以創建正向和負向條件資料，以及潛在表示。該節點根據指定的影片幀數生成用於多幀影片生成的攝影機仰角和方位角序列。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | 是 | - | 用於編碼輸入圖像的 CLIP 視覺模型 |
| `初始影像` | IMAGE | 是 | - | 作為 3D 影片生成起點的初始圖像 |
| `vae` | VAE | 是 | - | 用於將圖像編碼到潛在空間的 VAE 模型 |
| `寬度` | INT | 否 | 16 至 MAX_RESOLUTION | 生成影片幀的輸出寬度（預設值：576，必須能被 8 整除） |
| `高度` | INT | 否 | 16 至 MAX_RESOLUTION | 生成影片幀的輸出高度（預設值：576，必須能被 8 整除） |
| `影片幀數` | INT | 否 | 1 至 4096 | 為影片序列生成的幀數（預設值：21） |
| `仰角` | FLOAT | 否 | -90.0 至 90.0 | 3D 視圖的攝影機仰角（單位：度，預設值：0.0） |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 包含圖像嵌入和攝影機參數的正向條件資料，用於生成 |
| `negative` | CONDITIONING | 帶有零值嵌入的負向條件資料，用於對比生成 |
| `latent` | LATENT | 空潛在張量，其維度與指定的影片幀數和解析度相符 |