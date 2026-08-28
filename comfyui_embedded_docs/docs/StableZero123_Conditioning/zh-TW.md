# StableZero123 條件設定

StableZero123_Conditioning 節點處理輸入圖像與相機角度，以生成 3D 模型生成所需的條件資料與潛在表示。它使用 CLIP 視覺模型編碼圖像特徵，並根據 `elevation` 與 `azimuth` 角度將這些特徵與相機嵌入資訊結合，產生正向與負向條件，以及供下游 3D 生成任務使用的潛在表示。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip_vision` | 用於編碼圖像特徵的 CLIP 視覺模型 | CLIP_VISION | 是 | - |
| `初始影像` | 要處理並編碼的輸入圖像 | IMAGE | 是 | - |
| `vae` | 用於將像素編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 潛在表示的輸出寬度（預設：256，必須可被 8 整除） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 潛在表示的輸出高度（預設：256，必須可被 8 整除） | INT | 是 | 16 to MAX_RESOLUTION |
| `批次大小` | 批次中要生成的樣本數（預設：1） | INT | 是 | 1 至 4096 |
| `仰角` | 相機仰角，單位為度（預設：0.0） | FLOAT | 是 | -180.0 至 180.0 |
| `方位角` | 相機方位角，單位為度（預設：0.0） | FLOAT | 是 | -180.0 至 180.0 |

**注意：** `width` 與 `height` 參數必須可被 8 整除，因為節點會自動將它們除以 8，以建立潛在表示的維度。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `正向` | 正向條件資料，結合圖像特徵與相機嵌入資訊，並包含經 VAE 編碼的輸入圖像作為要拼接的潛在表示 | CONDITIONING |
| `負向` | 負向條件資料，包含初始化為零的特徵與初始化為零的潛在表示 | CONDITIONING |
| `潛在空間` | 初始化為零的潛在表示，維度為 [batch_size, 4, height//8, width//8] | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`
