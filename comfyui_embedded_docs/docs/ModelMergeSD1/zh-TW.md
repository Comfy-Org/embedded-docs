# 模型合併 (SD1)

ModelMergeSD1 節點透過調整每個模型元件對結果的貢獻程度，將兩個 Stable Diffusion 1.x 模型混合在一起。它提供對時間嵌入、標籤嵌入以及每個輸入、中間和輸出區塊的個別控制，允許針對特定用例進行微調模型合併。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型 1` | 要合併的第一個模型 | MODEL | 是 | - |
| `模型 2` | 要合併的第二個模型 | MODEL | 是 | - |
| `time_embed.` | 時間嵌入層混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `label_emb.` | 標籤嵌入層混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.0.` | 輸入區塊 0 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.1.` | 輸入區塊 1 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.2.` | 輸入區塊 2 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.3.` | 輸入區塊 3 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.4.` | 輸入區塊 4 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.5.` | 輸入區塊 5 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.6.` | 輸入區塊 6 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.7.` | 輸入區塊 7 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.8.` | 輸入區塊 8 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.9.` | 輸入區塊 9 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.10.` | 輸入區塊 10 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `input_blocks.11.` | 輸入區塊 11 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `middle_block.0.` | 中間區塊 0 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `middle_block.1.` | 中間區塊 1 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `middle_block.2.` | 中間區塊 2 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.0.` | 輸出區塊 0 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.1.` | 輸出區塊 1 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.2.` | 輸出區塊 2 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.3.` | 輸出區塊 3 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.4.` | 輸出區塊 4 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.5.` | 輸出區塊 5 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.6.` | 輸出區塊 6 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.7.` | 輸出區塊 7 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.8.` | 輸出區塊 8 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.9.` | 輸出區塊 9 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.10.` | 輸出區塊 10 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `output_blocks.11.` | 輸出區塊 11 混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |
| `out.` | 輸出力層混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 (step: 0.01) |

所有混合權重接受 0.0 到 1.0 之間的值，預設為 1.0，表示除非調整，否則第一個模型的每個元件都會被完整使用。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 結合兩個輸入模型特徵的合併模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
