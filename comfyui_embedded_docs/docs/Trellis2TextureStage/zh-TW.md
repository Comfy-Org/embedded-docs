# Trellis2TextureStage

此節點為 Trellis2 生成設定紋理階段的取樣 pass。它會從傳入的 shape latent 中讀取座標佈局與逐體素（per-voxel）shape latent，在相同的座標佈局下建立具有 32 個通道的空稀疏 latent，並將所需的紋理階段元資料附加到 conditioning 上。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `正向` | 用於紋理生成 pass 的正向 conditioning。紋理階段元資料會附加到其上。 | CONDITIONING | 是 | - |
| `負向` | 用於紋理生成 pass 的負向 conditioning。紋理階段元資料會附加到其上。 | CONDITIONING | 是 | - |
| `shape_latent` | 由 Trellis2ShapeStage 或 Trellis2UpsampleStage 產生的 latent 字典。其中必須包含 `coords`（座標佈局，形狀為 [N, 4]）與 `samples`（逐體素 shape latent）；`coord_resolution` 與 `model_frame` 為可選。 | LATENT | 是 | - |

備註：
- `shape_latent` 必須是 Trellis2ShapeStage 或 Trellis2UpsampleStage 的輸出；它提供紋理 pass 所使用的座標佈局與逐體素 shape latent。
- 座標佈局會經過驗證：`coords` 第一欄中的批次 ID 必須為非負且連續，且總行數必須與座標計數相符。
- 當 `positive` 帶有投影特徵包（Pixal3D conditioning），且 `shape_latent` 包含 `coord_resolution` 時，會計算 1024 紋理解析度的投影特徵，並將其附加到 conditioning。
- 模型座標系會從 `shape_latent` 中讀取；若缺少該值，則在存在投影特徵時預設為 `"y_up"`，否則預設為 `"z_up"`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `正向` | 附加了紋理階段元資料（生成模式、座標、座標計數、shape latent、模型座標系，以及適用的投影特徵）的正向 conditioning。 | CONDITIONING |
| `負向` | 附加了相同紋理階段元資料的負向 conditioning。 | CONDITIONING |
| `latent` | 一個新的空稀疏 latent，具有 32 個通道，座標佈局與傳入的 shape latent 相同。其字典包含 `samples`、`type`（`"trellis2"`）、`coords`、`coord_counts` 與 `model_frame`；若可用時也包含 `coord_resolution`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2TextureStage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ae612021af7c74cd09206d905e7b800fa48367a22daf9b0335b444c854a78b1e`
