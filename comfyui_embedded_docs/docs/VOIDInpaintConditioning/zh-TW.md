# VOIDInpaintConditioning

VOIDInpaintConditioning 節點準備 CogVideoX 模型進行修補所需的條件資料。它接收來源影片和預處理的四遮罩，透過 VAE 進行編碼，並將其組合成一個 32 通道的條件訊號，供模型用來填補遮罩區域。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 將被修補潛在資訊增強的正面條件 | CONDITIONING | 是 | - |
| `negative` | 將被修補潛在資訊增強的負面條件 | CONDITIONING | 是 | - |
| `vae` | 用於將遮罩和遮罩影片編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `video` | 來源影片幀 [T, H, W, 3] | IMAGE | 是 | - |
| `quadmask` | 來自 VOIDQuadmaskPreprocess 的預處理四遮罩 [T, H, W] | MASK | 是 | - |
| `width` | 影片和遮罩調整後的寬度 (預設: 672) | INT | 是 | 16 至 MAX_RESOLUTION (步長: 8) |
| `height` | 影片和遮罩調整後的高度 (預設: 384) | INT | 是 | 16 至 MAX_RESOLUTION (步長: 8) |
| `length` | 要處理的像素幀數。對於 CogVideoX-Fun-V1.5 (patch_size_t=2)，latent_t 必須為偶數 — 產生奇數 latent_t 的長度會向下取整 (例如 49 → 45) (預設: 45) | INT | 是 | 1 至 MAX_RESOLUTION (步長: 1) |
| `batch_size` | 輸出雜訊潛在的批次大小 (預設: 1) | INT | 是 | 1 至 64 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `negative` | 已添加修補潛在資訊的正面條件 | CONDITIONING |
| `latent` | 已添加修補潛在資訊的負面條件 | CONDITIONING |
| `latent` | 形狀為 [batch_size, 16, latent_t, latent_h, latent_w] 的零填充雜訊潛在張量 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a1fe36376d7930286c7a288f261dcf2961d6b13cc412d1a0d42af8a4f9ebeeaf`
