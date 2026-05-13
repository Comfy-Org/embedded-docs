> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/zh-TW.md)

**ModelMergeCosmos14B** 節點採用專為 Cosmos 14B 模型架構設計的區塊式方法，合併兩個 AI 模型。您可以透過調整每個模型區塊和嵌入層的權重值（範圍介於 0.0 到 1.0 之間），來混合這兩個模型的不同組件。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | 是 | - | 要合併的第一個模型 |
| `model2` | MODEL | 是 | - | 要合併的第二個模型 |
| `pos_embedder.` | FLOAT | 是 | 0.0 - 1.0 | 位置嵌入器組件的權重（預設值：1.0） |
| `extra_pos_embedder.` | FLOAT | 是 | 0.0 - 1.0 | 額外位置嵌入器組件的權重（預設值：1.0） |
| `x_embedder.` | FLOAT | 是 | 0.0 - 1.0 | x 嵌入器組件的權重（預設值：1.0） |
| `t_embedder.` | FLOAT | 是 | 0.0 - 1.0 | t 嵌入器組件的權重（預設值：1.0） |
| `affline_norm.` | FLOAT | 是 | 0.0 - 1.0 | 仿射正規化組件的權重（預設值：1.0） |
| `blocks.block0.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 0 的權重（預設值：1.0） |
| `blocks.block1.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 1 的權重（預設值：1.0） |
| `blocks.block2.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 2 的權重（預設值：1.0） |
| `blocks.block3.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 3 的權重（預設值：1.0） |
| `blocks.block4.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 4 的權重（預設值：1.0） |
| `blocks.block5.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 5 的權重（預設值：1.0） |
| `blocks.block6.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 6 的權重（預設值：1.0） |
| `blocks.block7.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 7 的權重（預設值：1.0） |
| `blocks.block8.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 8 的權重（預設值：1.0） |
| `blocks.block9.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 9 的權重（預設值：1.0） |
| `blocks.block10.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 10 的權重（預設值：1.0） |
| `blocks.block11.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 11 的權重（預設值：1.0） |
| `blocks.block12.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 12 的權重（預設值：1.0） |
| `blocks.block13.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 13 的權重（預設值：1.0） |
| `blocks.block14.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 14 的權重（預設值：1.0） |
| `blocks.block15.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 15 的權重（預設值：1.0） |
| `blocks.block16.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 16 的權重（預設值：1.0） |
| `blocks.block17.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 17 的權重（預設值：1.0） |
| `blocks.block18.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 18 的權重（預設值：1.0） |
| `blocks.block19.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 19 的權重（預設值：1.0） |
| `blocks.block20.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 20 的權重（預設值：1.0） |
| `blocks.block21.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 21 的權重（預設值：1.0） |
| `blocks.block22.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 22 的權重（預設值：1.0） |
| `blocks.block23.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 23 的權重（預設值：1.0） |
| `blocks.block24.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 24 的權重（預設值：1.0） |
| `blocks.block25.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 25 的權重（預設值：1.0） |
| `blocks.block26.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 26 的權重（預設值：1.0） |
| `blocks.block27.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 27 的權重（預設值：1.0） |
| `blocks.block28.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 28 的權重（預設值：1.0） |
| `blocks.block29.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 29 的權重（預設值：1.0） |
| `blocks.block30.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 30 的權重（預設值：1.0） |
| `blocks.block31.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 31 的權重（預設值：1.0） |
| `blocks.block32.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 32 的權重（預設值：1.0） |
| `blocks.block33.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 33 的權重（預設值：1.0） |
| `blocks.block34.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 34 的權重（預設值：1.0） |
| `blocks.block35.` | FLOAT | 是 | 0.0 - 1.0 | 區塊 35 的權重（預設值：1.0） |
| `final_layer.` | FLOAT | 是 | 0.0 - 1.0 | 最終層的權重（預設值：1.0） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 合併後的模型，結合了兩個輸入模型的特徵 |

---
**Source fingerprint (SHA-256):** `6fcb4fefe7738d0addef49d386c0d3d22cda4c68f0e49ad003d1df595cf0e9d9`
