# VOIDInpaintConditioning

VOIDInpaintConditioning 節點準備 CogVideoX 模型進行修補（inpainting）所需的 conditioning 資料。它接收來源影片和已預處理的 quadmask，透過 VAE 進行編碼，並將其組合成 32 通道的 conditioning 訊號（16 通道遮罩 + 16 通道遮罩影片），供模型用來填補遮罩區域。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 要透過修補潛在資訊增強的正向 conditioning | CONDITIONING | 是 | - |
| `negative` | 要透過修補潛在資訊增強的負向 conditioning | CONDITIONING | 是 | - |
| `vae` | 用於將遮罩和遮罩影片編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `video` | 來源影片影格 [T, H, W, 3] | IMAGE | 是 | - |
| `quadmask` | 來自 VOIDQuadmaskPreprocess 的已預處理 quadmask [T, H, W] | MASK | 是 | - |
| `width` | 要將影片和遮罩調整到的寬度（預設值：672） | INT | 是 | 16 to MAX_RESOLUTION (step: 8) |
| `height` | 要將影片和遮罩調整到的高度（預設值：384） | INT | 是 | 16 to MAX_RESOLUTION (step: 8) |
| `length` | 要處理的像素影格數量。對於 CogVideoX-Fun-V1.5（patch_size_t=2），latent_t 必須為偶數——產生奇數 latent_t 的長度會向下取整（例如 49 → 45）（預設值：45） | INT | 是 | 1 to MAX_RESOLUTION (step: 1) |
| `batch_size` | 輸出雜訊潛在的批次大小（預設值：1） | INT | 是 | 1 to 64 |

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `positive` | 已添加修補潛在資訊的正向 conditioning | CONDITIONING |
| `negative` | 已添加修補潛在資訊的負向 conditioning | CONDITIONING |
| `latent` | 形狀為 [batch_size, 16, latent_t, latent_h, latent_w] 的零填充雜訊潛在張量 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
