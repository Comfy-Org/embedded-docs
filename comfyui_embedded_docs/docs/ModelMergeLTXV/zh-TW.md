# 模型合併 (LTXV)

ModelMergeLTXV 透過混合兩個 LTXV 模型的內部元件，將它們合併為一個模型。每個權重參數控制 `model2` 的特定部分被混入 `model1` 的強度，數值越低越傾向 `model1`，數值越高越傾向 `model2`。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model1` | 要合併的第一個模型 | MODEL | 是 | - |
| `model2` | 要合併的第二個模型 | MODEL | 是 | - |
| `patchify_proj.` | 用於 patchify 投影層的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `adaln_single.` | 用於自適應層歸一化單層的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `caption_projection.` | 用於字幕投影層的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.0.` | 用於 Transformer 區塊 0 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.1.` | 用於 Transformer 區塊 1 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.2.` | 用於 Transformer 區塊 2 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.3.` | 用於 Transformer 區塊 3 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.4.` | 用於 Transformer 區塊 4 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.5.` | 用於 Transformer 區塊 5 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.6.` | 用於 Transformer 區塊 6 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.7.` | 用於 Transformer 區塊 7 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.8.` | 用於 Transformer 區塊 8 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.9.` | 用於 Transformer 區塊 9 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.10.` | 用於 Transformer 區塊 10 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.11.` | 用於 Transformer 區塊 11 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.12.` | 用於 Transformer 區塊 12 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.13.` | 用於 Transformer 區塊 13 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.14.` | 用於 Transformer 區塊 14 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.15.` | 用於 Transformer 區塊 15 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.16.` | 用於 Transformer 區塊 16 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.17.` | 用於 Transformer 區塊 17 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.18.` | 用於 Transformer 區塊 18 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.19.` | 用於 Transformer 區塊 19 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.20.` | 用於 Transformer 區塊 20 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.21.` | 用於 Transformer 區塊 21 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.22.` | 用於 Transformer 區塊 22 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.23.` | 用於 Transformer 區塊 23 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.24.` | 用於 Transformer 區塊 24 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.25.` | 用於 Transformer 區塊 25 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.26.` | 用於 Transformer 區塊 26 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.27.` | 用於 Transformer 區塊 27 的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `scale_shift_table` | 用於縮放位移表的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `proj_out.` | 用於投影輸出層的內插權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 根據指定內插權重合併兩個輸入模型特徵後得到的模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0ff5f93aee831259066679a27fff8f7cbd4a9686242091f1bc7dd3805725566e`
