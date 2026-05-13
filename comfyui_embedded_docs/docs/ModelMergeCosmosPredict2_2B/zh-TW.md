> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/zh-TW.md)

## 概述

ModelMergeCosmosPredict2_2B 節點採用基於區塊的方法合併兩個擴散模型，並對不同模型組件提供精細控制。透過調整位置嵌入器、時間嵌入器、Transformer 區塊和最終層的插值權重，您可以混合兩個模型的特定部分。這使得您能夠精確控制每個模型的不同架構組件對最終合併結果的貢獻程度。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `模型1` | MODEL | 是 | - | 要合併的第一個模型 |
| `模型2` | MODEL | 是 | - | 要合併的第二個模型 |
| `pos_embedder.` | FLOAT | 是 | 0.0 - 1.0 | 位置嵌入器插值權重（預設值：1.0） |
| `x_embedder.` | FLOAT | 是 | 0.0 - 1.0 | 輸入嵌入器插值權重（預設值：1.0） |
| `t_embedder.` | FLOAT | 是 | 0.0 - 1.0 | 時間嵌入器插值權重（預設值：1.0） |
| `t_embedding_norm.` | FLOAT | 是 | 0.0 - 1.0 | 時間嵌入正規化插值權重（預設值：1.0） |
| `blocks.0.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 0 插值權重（預設值：1.0） |
| `blocks.1.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 1 插值權重（預設值：1.0） |
| `blocks.2.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 2 插值權重（預設值：1.0） |
| `blocks.3.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 3 插值權重（預設值：1.0） |
| `blocks.4.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 4 插值權重（預設值：1.0） |
| `blocks.5.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 5 插值權重（預設值：1.0） |
| `blocks.6.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 6 插值權重（預設值：1.0） |
| `blocks.7.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 7 插值權重（預設值：1.0） |
| `blocks.8.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 8 插值權重（預設值：1.0） |
| `blocks.9.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 9 插值權重（預設值：1.0） |
| `blocks.10.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 10 插值權重（預設值：1.0） |
| `blocks.11.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 11 插值權重（預設值：1.0） |
| `blocks.12.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 12 插值權重（預設值：1.0） |
| `blocks.13.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 13 插值權重（預設值：1.0） |
| `blocks.14.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 14 插值權重（預設值：1.0） |
| `blocks.15.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 15 插值權重（預設值：1.0） |
| `blocks.16.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 16 插值權重（預設值：1.0） |
| `blocks.17.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 17 插值權重（預設值：1.0） |
| `blocks.18.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 18 插值權重（預設值：1.0） |
| `blocks.19.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 19 插值權重（預設值：1.0） |
| `blocks.20.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 20 插值權重（預設值：1.0） |
| `blocks.21.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 21 插值權重（預設值：1.0） |
| `blocks.22.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 22 插值權重（預設值：1.0） |
| `blocks.23.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 23 插值權重（預設值：1.0） |
| `blocks.24.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 24 插值權重（預設值：1.0） |
| `blocks.25.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 25 插值權重（預設值：1.0） |
| `blocks.26.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 26 插值權重（預設值：1.0） |
| `blocks.27.` | FLOAT | 是 | 0.0 - 1.0 | Transformer 區塊 27 插值權重（預設值：1.0） |
| `final_layer.` | FLOAT | 是 | 0.0 - 1.0 | 最終層插值權重（預設值：1.0） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 合併後的模型，結合了兩個輸入模型的特徵 |

---
**Source fingerprint (SHA-256):** `53a8de66d6b731f5b29af326832f66cc973284bc8fdf09d779575f2346cc75a7`
