# 模型合併 (LTXV)

ModelMergeLTXV 節點透過混合兩個 LTXV 模型中相對應的元件來合併它們。每個模型部分（例如 transformer 區塊、投影層與縮放偏移表）都可以使用各自的權重個別混合，讓你精細控制兩個模型的結合方式。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型 1` | 要合併的第一個模型 | MODEL | 是 | - |
| `模型 2` | 要合併的第二個模型 | MODEL | 是 | - |
| `patchify_proj.` | 用於 patchify 投影層的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `adaln_single.` | 用於自適應層歸一化單層的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `caption_projection.` | 用於 caption 投影層的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.0.` | 用於 transformer 區塊 0 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.1.` | 用於 transformer 區塊 1 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.2.` | 用於 transformer 區塊 2 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.3.` | 用於 transformer 區塊 3 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.4.` | 用於 transformer 區塊 4 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.5.` | 用於 transformer 區塊 5 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.6.` | 用於 transformer 區塊 6 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.7.` | 用於 transformer 區塊 7 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.8.` | 用於 transformer 區塊 8 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.9.` | 用於 transformer 區塊 9 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.10.` | 用於 transformer 區塊 10 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.11.` | 用於 transformer 區塊 11 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.12.` | 用於 transformer 區塊 12 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.13.` | 用於 transformer 區塊 13 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.14.` | 用於 transformer 區塊 14 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.15.` | 用於 transformer 區塊 15 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.16.` | 用於 transformer 區塊 16 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.17.` | 用於 transformer 區塊 17 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.18.` | 用於 transformer 區塊 18 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.19.` | 用於 transformer 區塊 19 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.20.` | 用於 transformer 區塊 20 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.21.` | 用於 transformer 區塊 21 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.22.` | 用於 transformer 區塊 22 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.23.` | 用於 transformer 區塊 23 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.24.` | 用於 transformer 區塊 24 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.25.` | 用於 transformer 區塊 25 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.26.` | 用於 transformer 區塊 26 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `transformer_blocks.27.` | 用於 transformer 區塊 27 的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `scale_shift_table` | 用於縮放偏移表的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `proj_out.` | 用於投影輸出層的插值權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 合併後的模型，根據指定的插值權重結合兩個輸入模型的特徵 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0ff5f93aee831259066679a27fff8f7cbd4a9686242091f1bc7dd3805725566e`
