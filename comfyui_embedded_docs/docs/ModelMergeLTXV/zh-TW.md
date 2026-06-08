## 概述

ModelMergeLTXV 節點執行專為 LTXV 模型架構設計的先進模型合併操作。它允許您透過調整各種模型組件（包括 transformer 區塊、投影層和其他專門模組）的插值權重，將兩個不同的模型混合在一起。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型 1` | 要合併的第一個模型 | MODEL | 是 | - |
| `模型 2` | 要合併的第二個模型 | MODEL | 是 | - |
| `patchify_proj.` | patchify 投影層的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `adaln_single.` | 自適應層歸一化單層的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `caption_projection.` | 標題投影層的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.0.` | transformer 區塊 0 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.1.` | transformer 區塊 1 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.2.` | transformer 區塊 2 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.3.` | transformer 區塊 3 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.4.` | transformer 區塊 4 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.5.` | transformer 區塊 5 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.6.` | transformer 區塊 6 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.7.` | transformer 區塊 7 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.8.` | transformer 區塊 8 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.9.` | transformer 區塊 9 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.10.` | transformer 區塊 10 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.11.` | transformer 區塊 11 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.12.` | transformer 區塊 12 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.13.` | transformer 區塊 13 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.14.` | transformer 區塊 14 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.15.` | transformer 區塊 15 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.16.` | transformer 區塊 16 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.17.` | transformer 區塊 17 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.18.` | transformer 區塊 18 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.19.` | transformer 區塊 19 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.20.` | transformer 區塊 20 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.21.` | transformer 區塊 21 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.22.` | transformer 區塊 22 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.23.` | transformer 區塊 23 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.24.` | transformer 區塊 24 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.25.` | transformer 區塊 25 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.26.` | transformer 區塊 26 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `transformer_blocks.27.` | transformer 區塊 27 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `scale_shift_table` | 縮放偏移表的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `proj_out.` | 投影輸出層的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 根據指定的插值權重，結合兩個輸入模型特徵的合併模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `29ef8750b6e88f71abca10c8aaad5d75c9c32afec057af78842ca82441438922`
