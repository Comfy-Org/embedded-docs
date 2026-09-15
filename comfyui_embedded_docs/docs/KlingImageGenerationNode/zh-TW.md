# Kling 圖像生成

Kling Image Generation 節點會根據文字提示生成圖像，並可選擇使用參考圖像作為引導。它會根據您的文字描述與參考設定建立一張或多張圖像，然後將生成的圖像作為輸出傳回。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 正向文字提示。必填，長度必須介於 1 到 500 個字元之間。 | STRING | 是 | 最多 500 個字元 |
| `負向提示詞` | 負向文字提示。 | STRING | 是 | 最多 500 個字元 |
| `image_type` | 圖像參考類型選擇（進階）。提供參考圖像時必填。 | COMBO | 是 | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | 使用者上傳圖像的參考強度（預設值：0.5，進階） | FLOAT | 是 | 0.0 - 1.0 |
| `human_fidelity` | 主體參考相似度（預設值：0.45，進階） | FLOAT | 是 | 0.0 - 1.0 |
| `model_name` | 用於圖像生成的模型選擇（預設值："kling-v3"） | COMBO | 是 | `"kling-v3"` |
| `aspect_ratio` | 生成圖像的長寬比（預設值："16:9"） | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | 生成圖像的數量（預設值：1） | INT | 是 | 1 - 9 |
| `影像` | 可選的參考圖像 | IMAGE | 否 | - |
| `種子` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果皆不具確定性（預設值：0） | INT | 否 | 0 - 2147483647 |

**參數限制：**

- `image` 參數為選填。提供參考圖像時，`image_type` 參數會決定參考圖像要用作主體參考還是風格參考。
- 未提供參考圖像時，參考相關設定（`image_type`、`image_fidelity`、`human_fidelity`）不會影響結果。
- `prompt` 與 `negative_prompt` 的最大長度為 500 個字元。
- `seed` 參數為選填，且不保證結果具確定性。
- `n` 參數控制產生的圖像數量，也會決定請求的價格。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 根據輸入參數生成的圖像。當 `n` 大於 1 時，會以批次形式傳回多張圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fd344519346f63ac03975b93f03725749ed9697245d6dfa2378884c59a5325cd`
