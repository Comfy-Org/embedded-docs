# Trellis2TextureStage

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 用於紋理生成階段的正向條件。紋理階段元數據會附加到其中。 | CONDITIONING | 是 | - |
| `negative` | 用於紋理生成階段的負向條件。紋理階段元數據會附加到其中。 | CONDITIONING | 是 | - |
| `shape_latent` | 由 Trellis2ShapeStage 或 Trellis2UpsampleStage 產生的潛在字典。它必須包含 `coords`（座標佈局，形狀 [N, 4]）和 `samples`（逐體素形狀潛在變量）；`coord_resolution` 和 `model_frame` 為可選。 | LATENT | 是 | - |

備註：
- `shape_latent` 必須是 Trellis2ShapeStage 或 Trellis2UpsampleStage 的輸出；它提供紋理階段使用的座標佈局與逐體素形狀潛在變量。
- 座標佈局會經過驗證：`coords` 第一欄中的批次 ID 必須為非負且連續，且總資料列數必須與座標數量一致。
- 當 `positive` 帶有投影特徵包（Pixal3D conditioning）且 `shape_latent` 包含 `coord_resolution` 時，會計算 1024 紋理解析度的投影特徵，並將其附加到條件上。
- 模型座標系會從 `shape_latent` 讀取；若不存在，則在存在投影特徵時預設為 `"y_up"`，否則為 `"z_up"`。

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 帶有紋理階段元數據的正向條件（包括生成模式、座標、座標數量、形狀潛在變量、模型座標系，以及適用的投影特徵）。 | CONDITIONING |
| `negative` | 帶有相同紋理階段元數據的負向條件。 | CONDITIONING |
| `latent` | 一個新的空稀疏潛在變量，與傳入的形狀潛在變量具有相同座標佈局，包含 32 個通道。其字典包含 `samples`、`type`（"trellis2"）、`coords`、`coord_counts` 與 `model_frame`；若有 `coord_resolution` 也會包含在內。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2TextureStage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ae612021af7c74cd09206d905e7b800fa48367a22daf9b0335b444c854a78b1e`
