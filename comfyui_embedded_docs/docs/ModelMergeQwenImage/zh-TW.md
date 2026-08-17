# 模型合併Qwen圖像

ModelMergeQwenImage 節點透過以可調整的權重組合兩個 AI 模型的元件來合併它們。它讓您能夠混合 Qwen 影像模型的特定部分，包括 Transformer 區塊、位置嵌入與文字處理元件。您可以控制每個模型對合併結果中不同部分的影響程度。

## 輸入
| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model1` | 要合併的第一個模型（預設：無） | MODEL | 是 | - |
| `model2` | 要合併的第二個模型（預設：無） | MODEL | 是 | - |
| `pos_embeds.` | 位置嵌入混合的權重（預設：1.0） | FLOAT | 是 | 0.0 to 1.0 |
| `img_in.` | 影像輸入處理混合的權重（預設：1.0） | FLOAT | 是 | 0.0 to 1.0 |
| `txt_norm.` | 文字正規化混合的權重（預設：1.0） | FLOAT | 是 | 0.0 to 1.0 |
| `txt_in.` | 文字輸入處理混合的權重（預設：1.0） | FLOAT | 是 | 0.0 to 1.0 |
| `time_text_embed.` | 時間與文字嵌入混合的權重（預設：1.0） | FLOAT | 是 | 0.0 to 1.0 |
| `transformer_blocks.0.` 至 `transformer_blocks.59.` | 每個 Transformer 區塊混合的權重（預設：1.0） | FLOAT | 是 | 0.0 to 1.0 |
| `proj_out.` | 輸出投影混合的權重（預設：1.0） | FLOAT | 是 | 0.0 to 1.0 |

注意：共有 60 個獨立的 Transformer 區塊權重輸入（`transformer_blocks.0.` 至 `transformer_blocks.59.`），對應模型中的每個 Transformer 區塊。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 合併後的模型，以指定的權重結合兩個輸入模型的元件 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
