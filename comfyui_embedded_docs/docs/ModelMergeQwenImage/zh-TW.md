> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/zh-TW.md)

ModelMergeQwenImage 節點透過以可調權重組合兩個 AI 模型的組件來合併它們。它允許您混合 Qwen 圖像模型的特定部分，包括轉換器區塊、位置嵌入和文字處理組件。您可以控制每個模型在合併結果的不同部分中所具有的影響程度。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | 是 | - | 要合併的第一個模型（預設：無） |
| `model2` | MODEL | 是 | - | 要合併的第二個模型（預設：無） |
| `pos_embeds.` | FLOAT | 是 | 0.0 至 1.0 | 位置嵌入混合的權重（預設：1.0） |
| `img_in.` | FLOAT | 是 | 0.0 至 1.0 | 圖像輸入處理混合的權重（預設：1.0） |
| `txt_norm.` | FLOAT | 是 | 0.0 至 1.0 | 文字標準化混合的權重（預設：1.0） |
| `txt_in.` | FLOAT | 是 | 0.0 至 1.0 | 文字輸入處理混合的權重（預設：1.0） |
| `time_text_embed.` | FLOAT | 是 | 0.0 至 1.0 | 時間和文字嵌入混合的權重（預設：1.0） |
| `transformer_blocks.0.` 至 `transformer_blocks.59.` | FLOAT | 是 | 0.0 至 1.0 | 每個轉換器區塊混合的權重（預設：1.0） |
| `proj_out.` | FLOAT | 是 | 0.0 至 1.0 | 輸出投影混合的權重（預設：1.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 使用指定權重合併兩個輸入模型組件後的合併模型 |