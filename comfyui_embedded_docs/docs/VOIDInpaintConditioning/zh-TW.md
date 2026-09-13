# VOIDInpaintConditioning

VOIDInpaintConditioning 節點會準備使用 CogVideoX 模型進行 inpainting 所需的條件資料。它接收來源影片與預處理的 quadmask，透過 VAE 將其編碼，並組合成 32 通道條件訊號（16 通道來自遮罩 + 16 通道來自遮罩後的影片），模型會使用此訊號填補遮罩區域。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 要加入修補潛在資訊的正向條件 | CONDITIONING | 是 | - |
| `negative` | 要加入修補潛在資訊的負向條件 | CONDITIONING | 是 | - |
| `vae` | 用於將遮罩與遮罩後影片編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `video` | 來源影片影格 [T, H, W, 3] | IMAGE | 是 | - |
| `quadmask` | 來自 VOIDQuadmaskPreprocess 的預處理 quadmask [T, H, W] | MASK | 是 | - |
| `width` | 將影片與遮罩調整到的寬度（預設：672） | INT | 是 | 16 to MAX_RESOLUTION （步進值：8） |
| `height` | 將影片與遮罩調整到的高度（預設：384） | INT | 是 | 16 to MAX_RESOLUTION （步進值：8） |
| `length` | 要處理的像素影格數。對於 CogVideoX-Fun-V1.5（`patch_size_t=2`），`latent_t` 必須為偶數 — 會產生奇數 `latent_t` 的長度會向下捨入（例如 49 → 45）（預設：45） | INT | 是 | 1 to MAX_RESOLUTION （步進值：1） |
| `batch_size` | 輸出噪聲潛在張量的批次大小（預設：1） | INT | 是 | 1 至 64 |

**注意：** 因為 CogVideoX-Fun-V1.5 使用 `patch_size_t=2`，編碼後的潛在表徵必須具有偶數的時間維度。如果 `length` 會產生奇數 `latent_t`，節點會自動將其向下捨入至最接近的有效值並記錄警告。使用奇數 `latent_t` 會透過循環填充損壞最後一個影格，這可能導致解碼後影片接近結尾處出現明顯抖動或主體消失。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 已加入修補潛在資訊的正向條件 | CONDITIONING |
| `negative` | 已加入修補潛在資訊的負向條件 | CONDITIONING |
| `latent` | 形狀為 [batch_size, 16, latent_t, latent_h, latent_w] 的全零填充噪聲潛在張量 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDInpaintConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `885e462c0f17a3e9610146a05ba3b9c879db0112d3961c95a83f63ba2cd511f1`
