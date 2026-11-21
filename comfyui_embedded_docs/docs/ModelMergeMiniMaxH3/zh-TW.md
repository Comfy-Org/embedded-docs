# Model Merge MiniMax H3

此節點依架構元件分別合併兩個相容的 MiniMax H3 模型，並為架構中的每個部分設定獨立的比例。每個比例代表 `model1` 的佔比，因此您可以保留某個模型的 patch 投影與 refinement 區塊，同時以另一個模型替換 transformer 區塊。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model1` | 第一個 MiniMax H3 模型。每個元件都以它為起點，而各個比例決定該元件有多少部分改由 `model2` 提供。 | MODEL | 是 | - |
| `model2` | 第二個 MiniMax H3 模型，用來提供您要混合進去的元件。 | MODEL | 是 | - |
| `video_patch_proj.` | 影片 patch 投影中 `model1` 的佔比（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `audio_patch_proj.` | 音訊 patch 投影中 `model1` 的佔比（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `condition_proj.` | 條件投影中 `model1` 的佔比（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `time_embedder.` | 時間嵌入器中 `model1` 的佔比（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `token_refiner.blocks.0.` | 第一個 token refiner 區塊中 `model1` 的佔比（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `token_refiner.blocks.1.` | 第二個 token refiner 區塊中 `model1` 的佔比（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `token_refiner.final_norm.` | token refiner 最終正規化中 `model1` 的佔比（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `blocks.0.` 至 `blocks.49.` | 50 個 transformer 區塊各自中 `model1` 的佔比，每個區塊對應一個控制項（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `final_layer.norm.` | 最終層正規化中 `model1` 的佔比（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `final_layer.adaln_proj.` | 最終自適應正規化投影中 `model1` 的佔比（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `final_layer.video_out.` | 影片輸出層中 `model1` 的佔比（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |
| `final_layer.audio_out.` | 音訊輸出層中 `model1` 的佔比（預設：1.0）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |

比例為 1.0（預設值）時，該元件完全取自 `model1`；比例為 0.0 時，則完全取自 `model2`；介於兩者之間的值會混合兩者。不帶比例的张量（例如正規化統計量）一律取自 `model1`。兩個輸入都必須是架構相同的 MiniMax H3 模型，否則合併後的模型將無法執行。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 合併後的 MiniMax H3 模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMiniMaxH3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4fea4e588d16a8396c68aa071a59e671a2a0c645734606be6d7e221986ba88bd`
