> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/zh-TW.md)

ModelMergeLTXV 節點執行專為 LTXV 模型架構設計的進階模型合併操作。它允許您透過調整各種模型組件的插值權重來融合兩個不同的模型，這些組件包括轉換器區塊、投影層和其他專門模組。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `模型 1` | MODEL | 是 | - | 要合併的第一個模型 |
| `模型 2` | MODEL | 是 | - | 要合併的第二個模型 |
| `patchify_proj.` | FLOAT | 是 | 0.0 - 1.0 | 分塊投影層的插值權重（預設值：1.0） |
| `adaln_single.` | FLOAT | 是 | 0.0 - 1.0 | 自適應層歸一化單層的插值權重（預設值：1.0） |
| `caption_projection.` | FLOAT | 是 | 0.0 - 1.0 | 標題投影層的插值權重（預設值：1.0） |
| `transformer_blocks.0.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 0 的插值權重（預設值：1.0） |
| `transformer_blocks.1.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 1 的插值權重（預設值：1.0） |
| `transformer_blocks.2.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 2 的插值權重（預設值：1.0） |
| `transformer_blocks.3.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 3 的插值權重（預設值：1.0） |
| `transformer_blocks.4.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 4 的插值權重（預設值：1.0） |
| `transformer_blocks.5.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 5 的插值權重（預設值：1.0） |
| `transformer_blocks.6.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 6 的插值權重（預設值：1.0） |
| `transformer_blocks.7.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 7 的插值權重（預設值：1.0） |
| `transformer_blocks.8.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 8 的插值權重（預設值：1.0） |
| `transformer_blocks.9.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 9 的插值權重（預設值：1.0） |
| `transformer_blocks.10.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 10 的插值權重（預設值：1.0） |
| `transformer_blocks.11.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 11 的插值權重（預設值：1.0） |
| `transformer_blocks.12.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 12 的插值權重（預設值：1.0） |
| `transformer_blocks.13.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 13 的插值權重（預設值：1.0） |
| `transformer_blocks.14.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 14 的插值權重（預設值：1.0） |
| `transformer_blocks.15.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 15 的插值權重（預設值：1.0） |
| `transformer_blocks.16.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 16 的插值權重（預設值：1.0） |
| `transformer_blocks.17.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 17 的插值權重（預設值：1.0） |
| `transformer_blocks.18.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 18 的插值權重（預設值：1.0） |
| `transformer_blocks.19.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 19 的插值權重（預設值：1.0） |
| `transformer_blocks.20.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 20 的插值權重（預設值：1.0） |
| `transformer_blocks.21.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 21 的插值權重（預設值：1.0） |
| `transformer_blocks.22.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 22 的插值權重（預設值：1.0） |
| `transformer_blocks.23.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 23 的插值權重（預設值：1.0） |
| `transformer_blocks.24.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 24 的插值權重（預設值：1.0） |
| `transformer_blocks.25.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 25 的插值權重（預設值：1.0） |
| `transformer_blocks.26.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 26 的插值權重（預設值：1.0） |
| `transformer_blocks.27.` | FLOAT | 是 | 0.0 - 1.0 | 轉換器區塊 27 的插值權重（預設值：1.0） |
| `scale_shift_table` | FLOAT | 是 | 0.0 - 1.0 | 縮放偏移表的插值權重（預設值：1.0） |
| `proj_out.` | FLOAT | 是 | 0.0 - 1.0 | 投影輸出層的插值權重（預設值：1.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 根據指定的插值權重合併兩個輸入模型特徵後產生的模型 |