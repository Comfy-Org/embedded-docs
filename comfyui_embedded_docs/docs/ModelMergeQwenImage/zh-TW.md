# 模型合併Qwen圖像

ModelMergeQwenImage 通過以可調整的權重組合兩個 AI 模型的組件來合併它們。它允許您混合 Qwen 圖像模型的特定部分，包括 Transformer 區塊、位置嵌入和文本處理組件。您可以控制每個模型對合併結果不同部分的影響程度。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型1` | 要合併的第一個模型 | MODEL | 是 | - |
| `模型2` | 要合併的第二個模型 | MODEL | 是 | - |
| `pos_embeds.` | 位置嵌入混合的權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 (step: 0.01) |
| `img_in.` | 圖像輸入處理混合的權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 (step: 0.01) |
| `txt_norm.` | 文本正規化混合的權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 (step: 0.01) |
| `txt_in.` | 文本輸入處理混合的權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 (step: 0.01) |
| `time_text_embed.` | 時間和文本嵌入混合的權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 (step: 0.01) |
| `transformer_blocks.0.` to `transformer_blocks.59.` | 每個 Transformer 區塊混合的權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 (step: 0.01) |
| `proj_out.` | 輸出投影混合的權重（預設值：1.0） | FLOAT | 是 | 0.0 至 1.0 (step: 0.01) |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 合併後的模型，以指定權重結合兩個輸入模型的組件 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
