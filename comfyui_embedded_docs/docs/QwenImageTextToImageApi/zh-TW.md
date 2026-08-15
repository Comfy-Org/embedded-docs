# Qwen Image 3 文生圖

Qwen Image 3 Text to Image 使用 Qwen-Image 3.0 模型，根據文字提示生成一或多張影像。您選擇模型並提供提示，節點便會將產生的影像以批次形式回傳。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型（預設："qwen-image-3.0-pro"）。此複合選擇器也提供提示、影像寬度、影像高度及選用的負面提示。 | DYNAMIC_COMBO | 是 | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | 要產生的影像數量，以批次形式回傳（預設：1）。 | INT | 否 | 1 to 6 |
| `seed` | 用於生成的種子（預設：42）。可設定為在每次生成後自動更新。 | INT | 否 | 0 to 2147483647 |
| `prompt_extend` | 是否使用 AI 輔助增強提示（預設：true）。進階選項。 | BOOLEAN | 否 | true<br>false |
| `watermark` | 是否在結果中加入 AI 產生的浮水印（預設：false）。進階選項。 | BOOLEAN | 否 | true<br>false |

### qwen-image-3.0-pro 與 qwen-image-3.0 輸入

由 qwen-image-3.0-pro 與 qwen-image-3.0 共用。

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述影像的提示。支援英文與中文。必須包含至少 1 個字元。 | STRING | 是 | Free text |
| `negative_prompt` | 描述要避免內容的負面提示（預設：""）。 | STRING | 否 | Free text |
| `width` | 總像素面積必須介於 512x512 與 2560x2560 之間；寬高比必須介於 1:8 與 8:1 之間。（預設：1024） | INT | 否 | 256 to 2560 (step 16) |
| `height` | 總像素面積必須介於 512x512 與 2560x2560 之間；寬高比必須介於 1:8 與 8:1 之間。（預設：1024） | INT | 否 | 256 to 2560 (step 16) |

注意：`model` 輸入是一個複合選擇器，包含子欄位 `model`（模型 ID）、`prompt`（必要，必須包含至少 1 個字元）、`width` 與 `height`（影像尺寸），以及 `negative_prompt`（選用）。`width` 與 `height` 合計的像素面積必須介於 262,144 像素（512x512）與 6,553,600 像素（2560x2560）之間，且寬高比必須保持在 1:8 到 8:1 之間。

## 輸出

| 輸出名 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `image` | 產生的單張或多張影像，以批次形式回傳。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`
