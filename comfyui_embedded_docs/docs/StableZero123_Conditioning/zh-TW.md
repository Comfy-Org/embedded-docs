> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/zh-TW.md)

# StableZero123_Conditioning 節點

StableZero123_Conditioning 節點處理輸入圖像和相機角度，以生成用於 3D 模型生成的條件數據和潛在表示。它使用 CLIP 視覺模型編碼圖像特徵，根據仰角和方位角將這些特徵與相機嵌入資訊結合，並生成正向和負向條件數據，以及用於下游 3D 生成任務的潛在表示。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | 是 | - | 用於編碼圖像特徵的 CLIP 視覺模型 |
| `init_image` | IMAGE | 是 | - | 待處理和編碼的輸入圖像 |
| `vae` | VAE | 是 | - | 用於將像素編碼到潛在空間的 VAE 模型 |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 潛在表示的輸出寬度（預設：256，必須能被 8 整除） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 潛在表示的輸出高度（預設：256，必須能被 8 整除） |
| `batch_size` | INT | 是 | 1 至 4096 | 批次中生成的樣本數量（預設：1） |
| `elevation` | FLOAT | 是 | -180.0 至 180.0 | 相機仰角（度）（預設：0.0） |
| `azimuth` | FLOAT | 是 | -180.0 至 180.0 | 相機方位角（度）（預設：0.0） |

**注意：** `width` 和 `height` 參數必須能被 8 整除，因為節點會自動將它們除以 8 以創建潛在表示的維度。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 結合圖像特徵和相機嵌入的正向條件數據 |
| `negative` | CONDITIONING | 使用零初始化特徵的負向條件數據 |
| `latent` | LATENT | 維度為 [batch_size, 4, height//8, width//8] 的潛在表示 |

---
**Source fingerprint (SHA-256):** `a9d6619c800119c9a619665f322d49ded1478ceb40df56ca5707b31242cb0e47`
