> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/zh-TW.md)

ModelMergeSD1 節點允許您透過調整不同模型元件的影響力，將兩個 Stable Diffusion 1.x 模型混合在一起。它提供了對時間嵌入、標籤嵌入以及所有輸入、中間和輸出區塊的個別控制，從而能夠針對特定使用案例進行精細調整的模型合併。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | 是 | - | 要合併的第一個模型 |
| `model2` | MODEL | 是 | - | 要合併的第二個模型 |
| `time_embed.` | FLOAT | 是 | 0.0 - 1.0 | 時間嵌入層混合權重（預設值：1.0） |
| `label_emb.` | FLOAT | 是 | 0.0 - 1.0 | 標籤嵌入層混合權重（預設值：1.0） |
| `input_blocks.0.` | FLOAT | 是 | 0.0 - 1.0 | 輸入區塊 0 混合權重（預設值：1.0） |
| `input_blocks.1.` | FLOAT | 是 | 0.0 - 1.0 | 輸入區塊 1 混合權重（預設值：1.0） |
| `input_blocks.2.` | FLOAT | 是 | 0.0 - 1.0 | 輸入區塊 2 混合權重（預設值：1.0） |
| `input_blocks.3.` | FLOAT | 是 | 0.0 - 1.0 | 輸入區塊 3 混合權重（預設值：1.0） |
| `input_blocks.4.` | FLOAT | 是 | 0.0 - 1.0 | 輸入區塊 4 混合權重（預設值：1.0） |
| `input_blocks.5.` | FLOAT | 是 | 0.0 - 1.0 | 輸入區塊 5 混合權重（預設值：1.0） |
| `input_blocks.6.` | FLOAT | 是 | 0.0 - 1.0 | 輸入區塊 6 混合權重（預設值：1.0） |
| `input_blocks.7.` | FLOAT | 是 | 0.0 - 1.0 | 輸入區塊 7 混合權重（預設值：1.0） |
| `input_blocks.8.` | FLOAT | 是 | 0.0 - 1.0 | 輸入區塊 8 混合權重（預設值：1.0） |
| `input_blocks.9.` | FLOAT | 是 | 0.0 - 1.0 | 輸入區塊 9 混合權重（預設值：1.0） |
| `input_blocks.10.` | FLOAT | 是 | 0.0 - 1.0 | 輸入區塊 10 混合權重（預設值：1.0） |
| `input_blocks.11.` | FLOAT | 是 | 0.0 - 1.0 | 輸入區塊 11 混合權重（預設值：1.0） |
| `middle_block.0.` | FLOAT | 是 | 0.0 - 1.0 | 中間區塊 0 混合權重（預設值：1.0） |
| `middle_block.1.` | FLOAT | 是 | 0.0 - 1.0 | 中間區塊 1 混合權重（預設值：1.0） |
| `middle_block.2.` | FLOAT | 是 | 0.0 - 1.0 | 中間區塊 2 混合權重（預設值：1.0） |
| `output_blocks.0.` | FLOAT | 是 | 0.0 - 1.0 | 輸出區塊 0 混合權重（預設值：1.0） |
| `output_blocks.1.` | FLOAT | 是 | 0.0 - 1.0 | 輸出區塊 1 混合權重（預設值：1.0） |
| `output_blocks.2.` | FLOAT | 是 | 0.0 - 1.0 | 輸出區塊 2 混合權重（預設值：1.0） |
| `output_blocks.3.` | FLOAT | 是 | 0.0 - 1.0 | 輸出區塊 3 混合權重（預設值：1.0） |
| `output_blocks.4.` | FLOAT | 是 | 0.0 - 1.0 | 輸出區塊 4 混合權重（預設值：1.0） |
| `output_blocks.5.` | FLOAT | 是 | 0.0 - 1.0 | 輸出區塊 5 混合權重（預設值：1.0） |
| `output_blocks.6.` | FLOAT | 是 | 0.0 - 1.0 | 輸出區塊 6 混合權重（預設值：1.0） |
| `output_blocks.7.` | FLOAT | 是 | 0.0 - 1.0 | 輸出區塊 7 混合權重（預設值：1.0） |
| `output_blocks.8.` | FLOAT | 是 | 0.0 - 1.0 | 輸出區塊 8 混合權重（預設值：1.0） |
| `output_blocks.9.` | FLOAT | 是 | 0.0 - 1.0 | 輸出區塊 9 混合權重（預設值：1.0） |
| `output_blocks.10.` | FLOAT | 是 | 0.0 - 1.0 | 輸出區塊 10 混合權重（預設值：1.0） |
| `output_blocks.11.` | FLOAT | 是 | 0.0 - 1.0 | 輸出區塊 11 混合權重（預設值：1.0） |
| `out.` | FLOAT | 是 | 0.0 - 1.0 | 輸出層混合權重（預設值：1.0） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `MODEL` | MODEL | 合併後的模型，結合了兩個輸入模型的特性 |

---
**Source fingerprint (SHA-256):** `512c62fb5a4e1b7f90f5ad5b80de5818659a20c8f4b024cfa33ca13b823efad8`
