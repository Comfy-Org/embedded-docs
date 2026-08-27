# ModelMergeCosmos14B

**ModelMergeCosmos14B** 節點使用專門為 Cosmos 14B 模型架構設計的區塊式方法合併兩個 AI 模型。您可以透過調整每個模型區塊和嵌入層的權重值（介於 0.0 到 1.0 之間），來混合模型的各個組成部分。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型 1` | 要合併的第一個模型 | MODEL | 是 | - |
| `模型 2` | 要合併的第二個模型 | MODEL | 是 | - |
| `pos_embedder.` | 位置嵌入器元件的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `extra_pos_embedder.` | 額外位置嵌入器元件的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `x_embedder.` | x 嵌入器元件的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `t_embedder.` | t 嵌入器元件的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `affline_norm.` | 仿射正規化元件的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block0.` | 區塊 0 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block1.` | 區塊 1 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block2.` | 區塊 2 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block3.` | 區塊 3 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block4.` | 區塊 4 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block5.` | 區塊 5 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block6.` | 區塊 6 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block7.` | 區塊 7 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block8.` | 區塊 8 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block9.` | 區塊 9 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block10.` | 區塊 10 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block11.` | 區塊 11 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block12.` | 區塊 12 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block13.` | 區塊 13 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block14.` | 區塊 14 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block15.` | 區塊 15 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block16.` | 區塊 16 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block17.` | 區塊 17 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block18.` | 區塊 18 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block19.` | 區塊 19 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block20.` | 區塊 20 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block21.` | 區塊 21 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block22.` | 區塊 22 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block23.` | 區塊 23 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block24.` | 區塊 24 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block25.` | 區塊 25 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block26.` | 區塊 26 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block27.` | 區塊 27 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block28.` | 區塊 28 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block29.` | 區塊 29 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block30.` | 區塊 30 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block31.` | 區塊 31 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block32.` | 區塊 32 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block33.` | 區塊 33 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block34.` | 區塊 34 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `blocks.block35.` | 區塊 35 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `final_layer.` | 最終層的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `model` | 合併兩個輸入模型特徵後產生的合併模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1d1e5dc176643f577723bb0bb9375748a392a6fafa5c9e5e78ef4c4d8289f77c`
