# Trellis2TextureStage

此節點為 Trellis2 生成設定紋理階段的取樣流程。它會從輸入的 shape latent 讀取座標佈局與逐體素的 shape latent，建立一個具有 32 個通道、位於相同座標佈局的空稀疏 latent，並將所需的紋理階段中繼資料附加至條件。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `正向` | 用於紋理生成階段的正向條件。紋理階段中繼資料會附加至其上。 | CONDITIONING | 是 | - |
| `負向` | 用於紋理生成階段的負向條件。紋理階段中繼資料會附加至其上。 | CONDITIONING | 是 | - |
| `shape_latent` | 由 Trellis2ShapeStage 或 Trellis2UpsampleStage 產生的 latent 字典。它必須包含 `coords`（座標佈局，形狀 [N, 4]）與 `samples`（逐體素的 shape latent）；`coord_resolution` 和 `model_frame` 為選用。 | LATENT | 是 | - |

備註：
- `shape_latent` 必須是 Trellis2ShapeStage 或 Trellis2UpsampleStage 的輸出；它提供紋理階段所使用的座標佈局與逐體素 shape latent。
- 座標佈局會經過驗證：`coords` 第一欄的批次 ID 必須為非負且連續，且總列數必須符合座標計數。
- shape latent 可接受為 4D 稀疏張量（會與其座標一起被展平），或已是展平形式。
- 當 `positive` 帶有投影特徵包（Pixal3D 條件）且 `shape_latent` 包含 `coord_resolution` 時，會計算 1024 紋理解析度的投影特徵並附加至條件。
- 模型框架會從 `shape_latent` 讀取；若不存在，當有投影特徵時預設為 `"y_up"`，否則預設為 `"z_up"`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 已附加紋理階段中繼資料的正向條件（生成模式、座標、座標計數、shape latent、模型框架，以及適用時的投影特徵）。 | CONDITIONING |
| `negative` | 已附加相同紋理階段中繼資料的負向條件。 | CONDITIONING |
| `latent` | 一個新的空稀疏 latent，具有 32 個通道，並與輸入 shape latent 位於相同座標佈局。其字典包含 `samples`、`type`（"trellis2"）、`coords`、`coord_counts` 與 `model_frame`；`coord_resolution` 會在可用時包含。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2TextureStage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ae612021af7c74cd09206d905e7b800fa48367a22daf9b0335b444c854a78b1e`
