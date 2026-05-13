> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/zh-TW.md)

## 概述

此節點使用 HappyHorse 模型，根據參考圖片生成包含人物或物體的影片。它支援建立單一角色或多個角色互動的影片。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"happyhorse-1.0-r2v"` | 用於影片生成的 HappyHorse 模型。 |
| `prompt` | STRING | 是 | 不適用 | 您想要生成影片的文字描述。使用 'character1' 和 'character2' 等識別碼來指代參考角色。 |
| `resolution` | COMBO | 是 | `"720P"`<br>`"1080P"` | 生成影片的解析度。 |
| `ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | 生成影片的長寬比。 |
| `duration` | INT | 是 | 3 至 15 | 生成影片的長度，以秒為單位（預設值：5）。 |
| `reference_images` | IMAGE | 是 | 1 至 9 | 影片中要呈現的人物或物體的一張或多張參考圖片。您必須至少提供一張圖片。 |
| `seed` | INT | 否 | 0 至 2147483647 | 用於可重複生成的種子值（預設值：0）。種子可設定為在每次生成後自動變更。 |
| `watermark` | BOOLEAN | 否 | True 或 False | 是否在生成的影片中添加 AI 生成浮水印（預設值：False）。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `VIDEO` | VIDEO | 生成的影片檔案。 |

---
**Source fingerprint (SHA-256):** `9162e150aef4cbafa42d59055bdff953e9c21b1e5fbf7c800629e570ee4cd0f9`
