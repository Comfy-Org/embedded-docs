# Qwen Image 3 文生圖

Qwen Image 3 Text to Image 使用 Qwen-Image 3.0 模型，透過文字提示生成一張或多張圖片。您選擇一個模型並提供提示，節點便會以批次形式返回生成的圖片。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型（預設："qwen-image-3.0-pro"）。此複合選擇器也提供提示、負面提示、圖片寬度與圖片高度。 | DYNAMIC_COMBO | 是 | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | 要生成的圖片數量，以批次形式返回（預設：1）。 | INT | 否 | 1 到 6 |
| `seed` | 用於生成的種子（預設：42）。可設定為在每次生成後自動更新。 | INT | 否 | 0 到 2147483647 |
| `prompt_extend` | 是否使用 AI 輔助增強提示（預設：true）。進階選項。 | BOOLEAN | 否 | true<br>false |
| `watermark` | 是否在結果中加入 AI 生成的浮水印（預設：false）。進階選項。 | BOOLEAN | 否 | true<br>false |

### qwen-image-3.0-pro 和 qwen-image-3.0 輸入

由 qwen-image-3.0-pro 和 qwen-image-3.0 共用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述圖片的提示。支援英文與中文。必須至少包含 1 個字元。 | STRING | 是 | 自由文字 |
| `negative_prompt` | 描述要避免內容的負面提示（預設：""）。 | STRING | 否 | 自由文字 |
| `width` | 總像素面積必須介於 512x512 與 2560x2560 之間；該範圍內的任何長寬比皆可。（預設：1024） | INT | 否 | 256 到 2560（步長 16） |
| `height` | 總像素面積必須介於 512x512 與 2560x2560 之間；該範圍內的任何長寬比皆可。（預設：1024） | INT | 否 | 256 到 2560（步長 16） |

備註：`model` 輸入是複合選擇器，其子欄位包括 `model`（模型 ID）、`prompt`（必填，必須至少包含 1 個字元）、`negative_prompt`（選填）、`width` 與 `height`。`width` 與 `height` 的合併像素面積必須介於 262,144 像素（512x512）與 6,553,600 像素（2560x2560）之間，且長寬比必須維持在 1:8 到 8:1 之間。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 生成的圖片，以批次形式返回。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`
