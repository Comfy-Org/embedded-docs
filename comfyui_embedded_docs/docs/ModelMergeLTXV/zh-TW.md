# 模型合併 (LTXV)

ModelMergeLTXV 節點執行專為 LTXV 模型架構設計的高階模型合併操作。它允許您透過調整各種模型元件的插值權重來混合兩個不同的模型，包括 Transformer 區塊、投影層和其他專門模組。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型 1` | 要合併的第一個模型 | MODEL | 是 | - |
| `模型 2` | 要合併的第二個模型 | MODEL | 是 | - |
| `patchify_proj.` | patchify 投影層的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `adaln_single.` | 自適應層歸一化單層的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `caption_projection.` | 標題投影層的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.0.` | Transformer 區塊 0 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.1.` | Transformer 區塊 1 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.2.` | Transformer 區塊 2 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.3.` | Transformer 區塊 3 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.4.` | Transformer 區塊 4 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.5.` | Transformer 區塊 5 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.6.` | Transformer 區塊 6 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.7.` | Transformer 區塊 7 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.8.` | Transformer 區塊 8 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.9.` | Transformer 區塊 9 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.10.` | Transformer 區塊 10 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.11.` | Transformer 區塊 11 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.12.` | Transformer 區塊 12 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.13.` | Transformer 區塊 13 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.14.` | Transformer 區塊 14 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.15.` | Transformer 區塊 15 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.16.` | Transformer 區塊 16 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.17.` | Transformer 區塊 17 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.18.` | Transformer 區塊 18 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.19.` | Transformer 區塊 19 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.20.` | Transformer 區塊 20 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.21.` | Transformer 區塊 21 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.22.` | Transformer 區塊 22 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.23.` | Transformer 區塊 23 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.24.` | Transformer 區塊 24 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.25.` | Transformer 區塊 25 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.26.` | Transformer 區塊 26 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.27.` | Transformer 區塊 27 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `scale_shift_table` | 縮放平移表的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `proj_out.` | 投影輸出層的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 根據指定的插值權重，合併兩個輸入模型特徵的模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0ff5f93aee831259066679a27fff8f7cbd4a9686242091f1bc7dd3805725566e`
