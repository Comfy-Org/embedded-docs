# QwenImageTextToImageApi

Qwen Image 3 Text to Image 使用 Qwen-Image 3.0 模型，根據文字提示產生一張或多張圖片。您選擇模型並提供提示詞，節點會將產生的圖片以批次形式回傳。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型（預設值："qwen-image-3.0-pro"）。此複合選擇器也提供提示詞、圖片寬度、圖片高度及可選的負面提示詞。 | MODEL | 是 | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | 要產生的圖片數量，以批次形式回傳（預設值：1）。 | INT | 否 | 1 至 6 |
| `seed` | 用於產生的隨機種子（預設值：42）。可設定為每次產生後自動更新。 | INT | 否 | 0 至 2147483647 |
| `prompt_extend` | 是否使用 AI 輔助增強提示詞（預設值：true）。進階選項。 | BOOLEAN | 否 | true<br>false |
| `watermark` | 是否在結果中加入 AI 生成的浮水印（預設值：false）。進階選項。 | BOOLEAN | 否 | true<br>false |

注意：`model` 輸入是一個複合選擇器，包含以下子欄位：`model`（模型 ID）、`prompt`（文字提示詞，必須至少包含 1 個字元）、`width` 和 `height`（圖片尺寸，由節點驗證），以及 `negative_prompt`（可選的負面提示詞）。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `image` | 產生的圖片，以批次形式回傳。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`
