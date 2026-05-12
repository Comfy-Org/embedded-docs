> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/zh-TW.md)

VOIDInpaintConditioning 節點負責準備 CogVideoX 模型進行修補（inpainting）所需的條件資料（conditioning data）。它接收來源影片和預處理後的四遮罩（quadmask），透過 VAE 進行編碼，並將其組合成一個 32 通道的條件訊號，供模型用來填補遮罩區域。

## ## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 將要附加修補潛在資訊的正向條件資料 |
| `negative` | CONDITIONING | 是 | - | 將要附加修補潛在資訊的負向條件資料 |
| `vae` | VAE | 是 | - | 用於將遮罩和遮罩後的影片編碼到潛在空間的 VAE 模型 |
| `video` | IMAGE | 是 | - | 格式為 [T, H, W, 3] 的來源影片幀 |
| `quadmask` | MASK | 是 | - | 來自 VOIDQuadmaskPreprocess 的預處理四遮罩，格式為 [T, H, W] |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION（步長：8） | 影片和遮罩調整後的寬度（預設值：672） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION（步長：8） | 影片和遮罩調整後的高度（預設值：384） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION（步長：1） | 要處理的像素幀數。對於 CogVideoX-Fun-V1.5（patch_size_t=2），latent_t 必須為偶數 — 會將產生奇數 latent_t 的長度向下取整（例如 49 → 45）（預設值：45） |
| `batch_size` | INT | 是 | 1 至 64 | 輸出雜訊潛在的批次大小（預設值：1） |

## ## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 已附加修補潛在資訊的正向條件資料 |
| `negative` | CONDITIONING | 已附加修補潛在資訊的負向條件資料 |
| `latent` | LATENT | 一個形狀為 [batch_size, 16, latent_t, latent_h, latent_w] 的零填充雜訊潛在張量 |