# ModelMergeCosmos7B

ModelMergeCosmos7B 節點透過對特定元件進行加權混合，將兩個 AI 模型合併在一起。它允許透過調整位置嵌入、Transformer 區塊和最終層的個別權重，來精細控制模型不同部分的組合方式。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型 1` | 要合併的第一個模型 | MODEL | 是 | - |
| `模型 2` | 要合併的第二個模型 | MODEL | 是 | - |
| `pos_embedder.` | 位置嵌入元件的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `extra_pos_embedder.` | 額外位置嵌入元件的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `x_embedder.` | x 嵌入元件的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `t_embedder.` | t 嵌入元件的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `affline_norm.` | 仿射正規化元件的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block0.` | Transformer 區塊 0 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block1.` | Transformer 區塊 1 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block2.` | Transformer 區塊 2 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block3.` | Transformer 區塊 3 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block4.` | Transformer 區塊 4 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block5.` | Transformer 區塊 5 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block6.` | Transformer 區塊 6 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block7.` | Transformer 區塊 7 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block8.` | Transformer 區塊 8 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block9.` | Transformer 區塊 9 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block10.` | Transformer 區塊 10 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block11.` | Transformer 區塊 11 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block12.` | Transformer 區塊 12 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block13.` | Transformer 區塊 13 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block14.` | Transformer 區塊 14 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block15.` | Transformer 區塊 15 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block16.` | Transformer 區塊 16 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block17.` | Transformer 區塊 17 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block18.` | Transformer 區塊 18 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block19.` | Transformer 區塊 19 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block20.` | Transformer 區塊 20 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block21.` | Transformer 區塊 21 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block22.` | Transformer 區塊 22 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block23.` | Transformer 區塊 23 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block24.` | Transformer 區塊 24 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block25.` | Transformer 區塊 25 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block26.` | Transformer 區塊 26 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.block27.` | Transformer 區塊 27 的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `final_layer.` | 最終層元件的權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 合併後的模型，結合了兩個輸入模型的特徵 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0721b047933179706c76f622efb5b7425aad530d302d8b33ec12dd68513dec0b`
