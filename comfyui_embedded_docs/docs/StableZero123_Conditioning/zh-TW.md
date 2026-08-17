# StableZero123 條件設定

StableZero123_Conditioning 節點會處理輸入影像與攝影機角度，以產生用於 3D 模型生成的條件資料與潛在表示。它使用 CLIP 視覺模型來編碼影像特徵，並根據俯仰角與方位角結合攝影機嵌入資訊，產生正向與負向條件資料，以及用於後續 3D 生成任務的潛在表示。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip_vision` | 用於編碼影像特徵的 CLIP 視覺模型 | CLIP_VISION | 是 | - |
| `init_image` | 要處理並編碼的輸入影像 | IMAGE | 是 | - |
| `vae` | 用於將像素編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `width` | 潛在表示的輸出寬度（預設：256，必須能被 8 整除） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 潛在表示的輸出高度（預設：256，必須能被 8 整除） | INT | 是 | 16 to MAX_RESOLUTION |
| `batch_size` | 批次中要產生的樣本數（預設：1） | INT | 是 | 1 to 4096 |
| `elevation` | 攝影機俯仰角（以度為單位，預設：0.0） | FLOAT | 是 | -180.0 to 180.0 |
| `azimuth` | 攝影機方位角（以度為單位，預設：0.0） | FLOAT | 是 | -180.0 to 180.0 |

**注意：** `width` 與 `height` 參數必須能被 8 整除，因為節點會自動將它們除以 8，以建立潛在表示的尺寸。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 結合影像特徵與攝影機嵌入資訊的正向條件資料 | CONDITIONING |
| `negative` | 具有零初始化特徵的負向條件資料 | CONDITIONING |
| `latent` | 維度為 [batch_size, 4, height//8, width//8] 的潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`
