> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/zh-TW.md)

# Kling 影像生成節點

Kling 影像生成節點可根據文字提示生成影像，並可選擇使用參考影像進行引導。此節點會根據您的文字描述和參考設定建立一或多張影像，然後將生成的影像作為輸出回傳。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 正向文字提示 |
| `negative_prompt` | STRING | 是 | - | 負向文字提示 |
| `image_type` | COMBO | 是 | `"subject_reference"`<br>`"style_reference"` | 影像參考類型選擇（進階）。當提供參考影像時為必要參數。 |
| `image_fidelity` | FLOAT | 是 | 0.0 - 1.0 | 使用者上傳影像的參考強度（預設值：0.5，進階） |
| `human_fidelity` | FLOAT | 是 | 0.0 - 1.0 | 主體參考相似度（預設值：0.45，進階） |
| `model_name` | COMBO | 是 | `"kling-v3"`<br>`"kling-v2"`<br>`"kling-v1-5"` | 影像生成的模型選擇（預設值："kling-v3"） |
| `aspect_ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` | 生成影像的長寬比（預設值："16:9"） |
| `n` | INT | 是 | 1 - 9 | 生成的影像數量（預設值：1） |
| `image` | IMAGE | 否 | - | 可選的參考影像 |
| `seed` | INT | 否 | 0 - 2147483647 | 種子碼控制節點是否應重新執行；無論種子碼為何，結果皆為非確定性（預設值：0） |

**參數限制：**

- `image` 參數為可選項目。當提供參考影像時，`image_type` 參數必須設定為 `"subject_reference"` 或 `"style_reference"`。
- 當未提供參考影像時，`image_type`、`image_fidelity` 和 `human_fidelity` 參數將不會被使用。
- 提示詞和負向提示詞的最大長度為 `MAX_PROMPT_LENGTH_IMAGE_GEN` 個字元。
- `seed` 參數為可選項目，且不保證產生確定性結果。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | IMAGE | 根據輸入參數生成的影像 |

---
**Source fingerprint (SHA-256):** `f25164f4007b1f62285e76519238b5061b63597e1a06365acf93d4289063bd3a`
