# StableZero123 條件設定（批次）

StableZero123_Conditioning_Batched 節點負責準備使用 Stable Zero123 模型生成物體 3D 視圖所需的條件資料。它使用 CLIP 視覺模型和 VAE 對輸入影像進行編碼，將影像特徵與批次中每個項目的相機仰角和方位角結合，並輸出正向與負向條件以及一個空潛在張量。批次增量輸入會依序提高或降低批次中每個項目的相機角度。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip_vision` | 用於將輸入影像編碼為影像嵌入的 CLIP 視覺模型 | CLIP_VISION | 是 | - |
| `init_image` | 待處理及編碼的初始輸入影像 | IMAGE | 是 | - |
| `vae` | 用於將影像像素編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `width` | 處理後影像的目標寬度（預設值：256） | INT | 是 | 16 to MAX_RESOLUTION (step 8) |
| `height` | 處理後影像的目標高度（預設值：256） | INT | 是 | 16 to MAX_RESOLUTION (step 8) |
| `batch_size` | 批次中要產生的條件樣本數量（預設值：1） | INT | 是 | 1 to 4096 |
| `elevation` | 相機的起始仰角（度）（預設值：0.0） | FLOAT | 是 | -180.0 to 180.0 (step 0.1) |
| `azimuth` | 相機的起始方位角（度）（預設值：0.0） | FLOAT | 是 | -180.0 to 180.0 (step 0.1) |
| `elevation_batch_increment` | 批次中每個連續項目新增至仰角的數值（預設值：0.0，進階參數） | FLOAT | 是 | -180.0 to 180.0 (step 0.1) |
| `azimuth_batch_increment` | 批次中每個連續項目新增至方位角的數值（預設值：0.0，進階參數） | FLOAT | 是 | -180.0 to 180.0 (step 0.1) |

**注意：** `width` 和 `height` 值必須是 8 的倍數（選擇步驟為 8 即確保此條件），因為節點會將它們除以 8 來建立潛在維度。對於批次中的每個項目，`elevation` 和 `azimuth` 值會分別增加 `elevation_batch_increment` 和 `azimuth_batch_increment`，因此連續的批次項目會獲得逐步變化的相機角度。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 結合影像嵌入、相機嵌入，以及用於生成期間拼接的編碼輸入影像之正向條件 | CONDITIONING |
| `negative` | 使用零初始化的影像嵌入和零潛在張量進行拼接的負向條件 | CONDITIONING |
| `latent` | 具有維度 (batch_size, 4, height/8, width/8) 及批次索引資訊的空潛在張量 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/zh-TW.md)

---
**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`
