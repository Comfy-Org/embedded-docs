# 模型合併宇宙預測2_2B

ModelMergeCosmosPredict2_2B 節點採用基於區塊的方法合併兩個擴散模型，並可對不同模型元件進行精細控制。透過調整位置嵌入器、時間嵌入器、Transformer 區塊及最終層的插值權重，您可以混合兩個模型的特定部分，從而精確控制每個模型的各架構元件如何貢獻於最終的合併結果。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model1` | 要合併的第一個模型 | MODEL | 是 | - |
| `model2` | 要合併的第二個模型 | MODEL | 是 | - |
| `pos_embedder.` | 位置嵌入器插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `x_embedder.` | 輸入嵌入器插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `t_embedder.` | 時間嵌入器插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `t_embedding_norm.` | 時間嵌入歸一化插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.0.` | Transformer 區塊 0 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.1.` | Transformer 區塊 1 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.2.` | Transformer 區塊 2 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.3.` | Transformer 區塊 3 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.4.` | Transformer 區塊 4 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.5.` | Transformer 區塊 5 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.6.` | Transformer 區塊 6 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.7.` | Transformer 區塊 7 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.8.` | Transformer 區塊 8 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.9.` | Transformer 區塊 9 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.10.` | Transformer 區塊 10 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.11.` | Transformer 區塊 11 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.12.` | Transformer 區塊 12 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.13.` | Transformer 區塊 13 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.14.` | Transformer 區塊 14 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.15.` | Transformer 區塊 15 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.16.` | Transformer 區塊 16 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.17.` | Transformer 區塊 17 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.18.` | Transformer 區塊 18 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.19.` | Transformer 區塊 19 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.20.` | Transformer 區塊 20 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.21.` | Transformer 區塊 21 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.22.` | Transformer 區塊 22 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.23.` | Transformer 區塊 23 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.24.` | Transformer 區塊 24 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.25.` | Transformer 區塊 25 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.26.` | Transformer 區塊 26 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `blocks.27.` | Transformer 區塊 27 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `final_layer.` | 最終層插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 合併後的模型，結合了兩個輸入模型的特徵 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3586868201320ae9a326a08f6a9bd74511a5342bf8496e7efcb9f45cf4b7c55d`
