> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/zh-TW.md)

# ModelMergeQwenImage 節點

ModelMergeQwenImage 節點透過以可調整的權重組合其元件來合併兩個 AI 模型。它允許您混合 Qwen 圖像模型的特定部分，包括 transformer 區塊、位置嵌入和文字處理元件。您可以控制每個模型對合併結果不同部分的影響程度。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | 是 | - | 要合併的第一個模型（預設：無） |
| `model2` | MODEL | 是 | - | 要合併的第二個模型（預設：無） |
| `pos_embeds.` | FLOAT | 是 | 0.0 至 1.0 | 位置嵌入混合的權重（預設：1.0） |
| `img_in.` | FLOAT | 是 | 0.0 至 1.0 | 圖像輸入處理混合的權重（預設：1.0） |
| `txt_norm.` | FLOAT | 是 | 0.0 至 1.0 | 文字正規化混合的權重（預設：1.0） |
| `txt_in.` | FLOAT | 是 | 0.0 至 1.0 | 文字輸入處理混合的權重（預設：1.0） |
| `time_text_embed.` | FLOAT | 是 | 0.0 至 1.0 | 時間與文字嵌入混合的權重（預設：1.0） |
| `transformer_blocks.0.` 至 `transformer_blocks.59.` | FLOAT | 是 | 0.0 至 1.0 | 每個 transformer 區塊混合的權重（預設：1.0） |
| `proj_out.` | FLOAT | 是 | 0.0 至 1.0 | 輸出投影混合的權重（預設：1.0） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 合併後的模型，以指定的權重組合兩個輸入模型的元件 |

---
**Source fingerprint (SHA-256):** `a0424a3f4d4ffe170471ba463350d741f67ff1b1f5a8a016ad844c111033f97c`
