# 模型合併 (SD3 2B)

ModelMergeSD3_2B 節點可讓您透過以可調整的權重混合兩個 Stable Diffusion 3 2B 模型的各個元件來合併它們。它提供對嵌入層、transformer 區塊以及最終層的個別控制，實現兩個模型的精細組合。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型 1` | 要合併的第一個模型 | MODEL | 是 | - |
| `模型 2` | 要合併的第二個模型 | MODEL | 是 | - |
| `pos_embed.` | 位置嵌入插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `x_embedder.` | 輸入嵌入插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `context_embedder.` | 上下文嵌入插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `y_embedder.` | Y 嵌入插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `t_embedder.` | 時間嵌入插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.0.` | 聯合區塊 0 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.1.` | 聯合區塊 1 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.2.` | 聯合區塊 2 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.3.` | 聯合區塊 3 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.4.` | 聯合區塊 4 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.5.` | 聯合區塊 5 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.6.` | 聯合區塊 6 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.7.` | 聯合區塊 7 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.8.` | 聯合區塊 8 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.9.` | 聯合區塊 9 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.10.` | 聯合區塊 10 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.11.` | 聯合區塊 11 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.12.` | 聯合區塊 12 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.13.` | 聯合區塊 13 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.14.` | 聯合區塊 14 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.15.` | 聯合區塊 15 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.16.` | 聯合區塊 16 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.17.` | 聯合區塊 17 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.18.` | 聯合區塊 18 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.19.` | 聯合區塊 19 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.20.` | 聯合區塊 20 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.21.` | 聯合區塊 21 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.22.` | 聯合區塊 22 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `joint_blocks.23.` | 聯合區塊 23 插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `final_layer.` | 最終層插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 合併後的模型，結合了兩個輸入模型的特徵 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/zh-TW.md)

---
**Source fingerprint (SHA-256):** `db27b10ade457933f6225218bb806aafcf9fc4478cac85b1623a75d110103529`
