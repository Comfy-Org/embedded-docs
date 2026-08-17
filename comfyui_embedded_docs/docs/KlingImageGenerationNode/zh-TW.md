# Kling 圖像生成

Kling 影像生成節點可根據文字提示產生影像，並可選擇使用參考影像作為引導。它會根據您的文字描述與參考設定建立一或多張影像，然後將產生的影像作為輸出回傳。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|------|-------|
| `prompt` | 正向文字提示 | STRING | 是 | 最多 500 個字元 |
| `negative_prompt` | 負向文字提示 | STRING | 是 | 最多 500 個字元 |
| `image_type` | 影像參考類型選擇（進階）。當提供參考影像時使用。 | COMBO | 是 | `"subject_reference"`<br>`"style_reference"` |
| `image_fidelity` | 使用者上傳影像的參考強度（預設值：0.5，進階） | FLOAT | 是 | 0.0 - 1.0 |
| `human_fidelity` | 主體參考相似度（預設值：0.45，進階） | FLOAT | 是 | 0.0 - 1.0 |
| `model_name` | 影像生成的模型選擇（預設值："kling-v3"） | COMBO | 是 | `"kling-v3"`<br>`"kling-v2"` |
| `aspect_ratio` | 產生影像的長寬比（預設值："16:9"） | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"`<br>`"9:21"` |
| `n` | 產生影像的數量（預設值：1） | INT | 是 | 1 - 9 |
| `image` | 選用的參考影像 | IMAGE | 否 | - |
| `seed` | 種子值控制節點是否應重新執行；無論種子值為何，結果皆非確定性（預設值：0） | INT | 否 | 0 - 2147483647 |

**參數限制：**

- `image` 參數為選用。當提供參考影像時，`image_type` 會決定其作為主體參考或風格參考。若未提供參考影像，則不會套用 `image_type`。
- `prompt` 必須包含至少 1 個字元，最多 500 個字元。`negative_prompt` 可為空白，但限制為 500 個字元。
- `seed` 參數為選用，且不保證結果具有確定性。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `output` | 根據輸入參數所產生的影像。當要求多張影像時，所有影像會堆疊在單一批次中回傳。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `165d18244870b5b4f34587633a5492e733ad0b0a923bb8c3e506319460321906`
