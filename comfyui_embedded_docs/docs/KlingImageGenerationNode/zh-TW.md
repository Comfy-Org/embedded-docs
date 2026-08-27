# Kling 圖像生成

Kling 影像生成節點可根據文字提示生成影像，並可選擇使用參考影像來引導生成。此節點會根據您的文字描述與參考設定建立一或多張影像，然後將生成的影像作為輸出回傳。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 正向文字提示 | STRING | 是 | 最多 500 個字元 |
| `負向提示詞` | 負向文字提示 | STRING | 是 | 最多 500 個字元 |
| `image_type` | 影像參考類型選擇（進階）。當提供參考影像時必填。 | COMBO | 是 | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | 使用者上傳影像的參考強度（預設：0.5，進階） | FLOAT | 是 | 0.0 - 1.0 |
| `human_fidelity` | 主體參考相似度（預設：0.45，進階） | FLOAT | 是 | 0.0 - 1.0 |
| `model_name` | 影像生成的模型選擇（預設："kling-v3"） | COMBO | 是 | `"kling-v3"` |
| `aspect_ratio` | 生成影像的長寬比（預設："16:9"） | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | 生成的影像數量（預設：1） | INT | 是 | 1 - 9 |
| `影像` | 可選的參考影像 | IMAGE | 否 | - |
| `種子` | 種子控制節點是否應重新執行；無論種子為何，結果都不具確定性（預設：0） | INT | 否 | 0 - 2147483647 |

**參數約束：**

- `image` 參數為選用。當提供參考影像時，`image_type` 參數決定該參考影像是作為主體參考還是風格參考。
- 當未提供參考影像時，與參考相關的設定（`image_type`、`image_fidelity`、`human_fidelity`）不會對結果產生影響。
- `prompt` 與 `negative_prompt` 的最大長度為 500 個字元。
- `seed` 參數為選用，且不保證產生確定性結果。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 根據輸入參數生成的影像。當 `n` 大於 1 時，會以批次方式回傳多張影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fd344519346f63ac03975b93f03725749ed9697245d6dfa2378884c59a5325cd`
