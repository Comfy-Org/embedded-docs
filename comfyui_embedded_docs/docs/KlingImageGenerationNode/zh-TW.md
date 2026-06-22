# Kling 圖像生成

Kling 影像生成節點可根據文字提示生成影像，並可選擇使用參考影像進行引導。此節點會根據您的文字描述和參考設定建立一或多張影像，然後將生成的影像作為輸出回傳。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | 正向文字提示 | STRING | 是 | - |
| `負向提示詞` | 負向文字提示 | STRING | 是 | - |
| `image_type` | 影像參考類型選擇（進階）。當提供參考影像時為必要參數。 | COMBO | 是 | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | 使用者上傳影像的參考強度（預設值：0.5，進階） | FLOAT | 是 | 0.0 - 1.0 |
| `human_fidelity` | 主體參考相似度（預設值：0.45，進階） | FLOAT | 是 | 0.0 - 1.0 |
| `model_name` | 影像生成的模型選擇（預設值："kling-v3"） | COMBO | 是 | `"kling-v3"`<br>`"kling-v2"`<br>`"kling-v1-5"` |
| `aspect_ratio` | 生成影像的長寬比（預設值："16:9"） | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | 生成的影像數量（預設值：1） | INT | 是 | 1 - 9 |
| `影像` | 可選的參考影像 | IMAGE | 否 | - |
| `種子` | 種子碼控制節點是否應重新執行；無論種子碼為何，結果皆為非確定性（預設值：0） | INT | 否 | 0 - 2147483647 |

**參數限制：**

- `image` 參數為可選項目。當提供參考影像時，`image_type` 參數必須設定為 `"subject_reference"` 或 `"style_reference"`。
- 當未提供參考影像時，`image_type`、`image_fidelity` 和 `human_fidelity` 參數將不會被使用。
- 提示詞和負向提示詞的最大長度為 `MAX_PROMPT_LENGTH_IMAGE_GEN` 個字元。
- `seed` 參數為可選項目，且不保證產生確定性結果。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 根據輸入參數生成的影像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f25164f4007b1f62285e76519238b5061b63597e1a06365acf93d4289063bd3a`
