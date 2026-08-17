# 模型合併 (SD1)

ModelMergeSD1 允許您透過調整兩個 Stable Diffusion 1.x 模型各自組成部分的影響力來將它們合併在一起。它為時間嵌入、標籤嵌入、每個輸入區塊、每個中間區塊、每個輸出區塊以及最終輸出層提供單獨的混合權重，使您能夠精細控制兩個模型的組合方式。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model1` | 要合併的第一個模型 | MODEL | 是 | - |
| `model2` | 要合併的第二個模型 | MODEL | 是 | - |
| `time_embed.` | 時間嵌入層的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `label_emb.` | 標籤嵌入層的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.0.` | 輸入區塊 0 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.1.` | 輸入區塊 1 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.2.` | 輸入區塊 2 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.3.` | 輸入區塊 3 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.4.` | 輸入區塊 4 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.5.` | 輸入區塊 5 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.6.` | 輸入區塊 6 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.7.` | 輸入區塊 7 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.8.` | 輸入區塊 8 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.9.` | 輸入區塊 9 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.10.` | 輸入區塊 10 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.11.` | 輸入區塊 11 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `middle_block.0.` | 中間區塊 0 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `middle_block.1.` | 中間區塊 1 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `middle_block.2.` | 中間區塊 2 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.0.` | 輸出區塊 0 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.1.` | 輸出區塊 1 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.2.` | 輸出區塊 2 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.3.` | 輸出區塊 3 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.4.` | 輸出區塊 4 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.5.` | 輸出區塊 5 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.6.` | 輸出區塊 6 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.7.` | 輸出區塊 7 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.8.` | 輸出區塊 8 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.9.` | 輸出區塊 9 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.10.` | 輸出區塊 10 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.11.` | 輸出區塊 11 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `out.` | 輸出層的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 合併後的模型，結合了兩個輸入模型的特徵 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
