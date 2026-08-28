# Trellis2ShapeStage

此節點會設定 Trellis2 管線中第一個形狀生成取樣遍次。它會取得 VaeDecodeStructureTrellis2 產生的密集結構體素，提取已填充體素的稀疏座標，建立空的稀疏潛在張量，並將取樣元資料附加到條件，以便模型在取樣期間讀取。若要在上取樣後進行第二次形狀遍次，請改用 Trellis2UpsampleStage，它會結合級聯與第二遍階段設定。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `正向` | 要為形狀階段準備的正向條件。可以是標準 Trellis2 條件，也可以是提供投影特徵包的 Pixal3D 條件；當存在投影特徵時，會為所選階段計算這些特徵，並附加到輸出的條件。 | CONDITIONING | 是 | 任何 Trellis2 或 Pixal3D 條件 |
| `負向` | 要為形狀階段準備的負向條件。與正向條件相同，會附加相同的形狀階段元資料。 | CONDITIONING | 是 | 任何 Trellis2 或 Pixal3D 條件 |
| `體素` | 來自 VaeDecodeStructureTrellis2 的密集結構體素。 | VOXEL | 是 | 任何體素網格；網格解析度（每軸體素數）會選擇管線階段 |

### 備註

- 體素網格解析度會選擇管線階段：解析度為 32 或更低時，使用 `shape_generation_512` 模式搭配 `shape_512` 階段；解析度大於 32 時，使用 `shape_generation` 模式搭配 `shape_1024` 階段。
- 體素網格必須至少包含一個已填充的體素；空的體素網格會引發錯誤。從體素網格推導出的批次索引必須為非負且連續。
- 當 `positive` 條件包含 `proj_feat_pack`（由 Pixal3D 條件提供）時，會為所選階段計算投影特徵，並將輸出潛在張量的模型框架設為 `y_up`。否則，不會附加投影特徵，且模型框架設為 `z_up`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `正向` | 已附加形狀階段元資料的正向條件：生成模式、稀疏座標、每個批次的座標計數，以及來源條件提供時的投影特徵。 | CONDITIONING |
| `負向` | 已附加相同形狀階段元資料的負向條件。 | CONDITIONING |
| `latent` | 一個空的稀疏潛在張量（形狀：批次大小, 32, token 數量, 1），以及提取出的稀疏座標、每個批次的座標計數、座標解析度、類型標記 `trellis2` 和模型框架方向。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2ShapeStage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7dbee8a5b6ef7111f07def4dbe1cc4908533e00ffcb775f5a284099360c7eed3`
