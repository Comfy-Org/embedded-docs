# Trellis2ShapeStage

此節點負責設定 Trellis2 管線的第一個形狀生成取樣遍次。它接收 VaeDecodeStructureTrellis2 產生的稠密結構體素，擷取已填充體素的稀疏座標，建立空的稀疏潛在張量，並將取樣元資料附加到 conditioning，使模型能在取樣過程中讀取該資訊。若要設定上取樣後的第二個形狀遍次，請改用 Trellis2UpsampleStage，它會結合級聯與第二遍次的階段設定。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 要為形狀階段準備的正向 conditioning。可以是標準的 Trellis2 conditioning，或是提供投影特徵包的 Pixal3D conditioning；當存在投影特徵時，系統會為選定的階段計算這些特徵，並將其附加到輸出的 conditioning。 | CONDITIONING | 是 | 任何 Trellis2 或 Pixal3D conditioning |
| `negative` | 要為形狀階段準備的負向 conditioning。與正向 conditioning 相同，形狀階段的元資料也會附加到其中。 | CONDITIONING | 是 | 任何 Trellis2 或 Pixal3D conditioning |
| `voxel` | 來自 VaeDecodeStructureTrellis2 的稠密結構體素。 | VOXEL | 是 | 任何體素網格；網格解析度（每軸體素數）會決定所使用的管線階段 |

### 注意事項

- 體素網格解析度會決定所使用的管線階段：解析度為 32 或更低時，使用 `shape_generation_512` 模式搭配 `shape_512` 階段；解析度高於 32 時，使用 `shape_generation` 模式搭配 `shape_1024` 階段。
- 體素中至少必須包含一個已填充的體素；空的體素會引發錯誤。從體素推導出的批次索引必須為非負且連續。
- 當 `positive` conditioning 包含 `proj_feat_pack`（由 Pixal3D conditioning 提供）時，系統會為選定的階段計算投影特徵，並將輸出潛在張量的模型座標系設定為 `y_up`。否則，不會附加投影特徵，且模型座標系會設定為 `z_up`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 已附加形狀階段元資料的正向 conditioning，包括：生成模式、稀疏座標、各批次座標計數，以及來源 conditioning 有提供時的投影特徵。 | CONDITIONING |
| `negative` | 已附加相同形狀階段元資料的負向 conditioning。 | CONDITIONING |
| `latent` | 一個空的稀疏潛在張量（形狀：批次大小、32、token 數量、1），以及擷取出的稀疏座標、各批次座標計數、座標解析度、型別標記 `trellis2` 與模型座標系方向。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2ShapeStage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7dbee8a5b6ef7111f07def4dbe1cc4908533e00ffcb775f5a284099360c7eed3`
