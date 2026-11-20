# Model Merge MiniMax H3

依元件合併兩個相容的 MiniMax H3 模型，並為架構中的每個部分設定各自獨立的比例。提高某個比例，代表該元件有更多部分取自 `model2`，因此你可以保留某個模型的 patch 投影與精化區塊，同時以另一個模型替換 transformer 區塊。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model1` | 第一個 MiniMax H3 模型，也就是所有元件取用的基礎模型（在未使用 `model2` 的部分套用預設權重）。 | MODEL | 是 | - |
| `model2` | 第二個 MiniMax H3 模型，提供要混合進來的元件。 | MODEL | 是 | - |
| `video_patch_proj.` | `model2` 在 video patch 投影中所佔的比例（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `audio_patch_proj.` | `model2` 在 audio patch 投影中所佔的比例（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `condition_proj.` | `model2` 在條件投影中所佔的比例（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `time_embedder.` | `model2` 在時間嵌入器中所佔的比例（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `token_refiner.blocks.0.` | `model2` 在第一個 token refiner 區塊中所佔的比例（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `token_refiner.blocks.1.` | `model2` 在第二個 token refiner 區塊中所佔的比例（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `token_refiner.final_norm.` | `model2` 在 token refiner 最終正規化中所佔的比例（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `blocks.0.` 至 `blocks.49.` | 50 個 transformer 區塊各自取自 `model2` 的比例，每個區塊對應一個控制項（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `final_layer.norm.` | `model2` 在最終層正規化中所佔的比例（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `final_layer.adaln_proj.` | `model2` 在最終自適應正規化投影中所佔的比例（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `final_layer.video_out.` | `model2` 在視訊輸出層中所佔的比例（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `final_layer.audio_out.` | `model2` 在音訊輸出層中所佔的比例（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |

比例為 0.0 時，該元件完全取自 `model1`；比例為 1.0 時，則完全取自 `model2`；介於兩者之間的值會混合兩者。沒有對應比例的張量（例如正規化統計值）一律取自 `model1`。兩個輸入都必須是架構相同的 MiniMax H3 模型，否則合併後產生的模型將無法執行。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 合併後的 MiniMax H3 模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMiniMaxH3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4fea4e588d16a8396c68aa071a59e671a2a0c645734606be6d7e221986ba88bd`
