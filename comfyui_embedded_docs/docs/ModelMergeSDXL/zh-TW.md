ModelMergeSDXL 節點允許您透過調整每個模型對架構不同部分的影響力，將兩個 SDXL 模型混合在一起。您可以控制每個模型對時間嵌入、標籤嵌入以及模型結構中各個區塊的貢獻程度。這會建立一個結合兩個輸入模型特性的混合模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型 1` | 要合併的第一個 SDXL 模型 | MODEL | 是 | - |
| `模型 2` | 要合併的第二個 SDXL 模型 | MODEL | 是 | - |
| `time_embed.` | 時間嵌入層的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `label_emb.` | 標籤嵌入層的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.0` | 輸入區塊 0 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.1` | 輸入區塊 1 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.2` | 輸入區塊 2 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.3` | 輸入區塊 3 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.4` | 輸入區塊 4 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.5` | 輸入區塊 5 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.6` | 輸入區塊 6 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.7` | 輸入區塊 7 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `input_blocks.8` | 輸入區塊 8 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `middle_block.0` | 中間區塊 0 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `middle_block.1` | 中間區塊 1 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `middle_block.2` | 中間區塊 2 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.0` | 輸出區塊 0 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.1` | 輸出區塊 1 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.2` | 輸出區塊 2 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.3` | 輸出區塊 3 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.4` | 輸出區塊 4 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.5` | 輸出區塊 5 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.6` | 輸出區塊 6 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.7` | 輸出區塊 7 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `output_blocks.8` | 輸出區塊 8 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `out.` | 輸出層的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 合併後的 SDXL 模型，結合了兩個輸入模型的特性 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSDXL/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6c7572a6ed50534f2d9ad6f499146763457da58f0c9dd4b85204e67f7d3e9660`
