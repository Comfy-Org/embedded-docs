> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageNode/zh-TW.md)

# ByteDance 圖片節點

ByteDance 圖片節點透過 API 使用 ByteDance 模型，根據文字提示生成圖片。它允許您選擇模型、指定圖片尺寸，並控制各種生成參數，如種子和引導比例。該節點連接到 ByteDance 的圖片生成服務，並返回創建的圖片。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | STRING | 是 | `"seedream-3-0-t2i-250415"` | 用於圖片生成的 ByteDance 模型。目前僅提供一個模型選項。 |
| `prompt` | STRING | 是 | - | 用於生成圖片的文字提示。去除空白後長度必須至少為 1 個字元。 |
| `size_preset` | STRING | 是 | 請參閱說明 | 選擇推薦的尺寸。選擇「自訂」以使用下方的寬度和高度。可用預設由 `RECOMMENDED_PRESETS` 列表定義。 |
| `width` | INT | 是 | 512 至 2048（步長 64） | 圖片的自訂寬度。僅當 `size_preset` 設定為「自訂」時使用此值。預設值：1024。 |
| `height` | INT | 是 | 512 至 2048（步長 64） | 圖片的自訂高度。僅當 `size_preset` 設定為「自訂」時使用此值。預設值：1024。 |
| `seed` | INT | 否 | 0 至 2147483647（步長 1） | 用於生成的種子。預設值：0。 |
| `guidance_scale` | FLOAT | 否 | 1.0 至 10.0（步長 0.01） | 數值越高，圖片越貼近提示內容。預設值：2.5。 |
| `watermark` | BOOLEAN | 否 | True / False | 是否在圖片上添加「AI 生成」浮水印。預設值：False。此為進階參數。 |

**關於尺寸參數的說明：** `width` 和 `height` 參數僅在 `size_preset` 設定為「自訂」時使用。如果選擇了預設尺寸，則預設的尺寸會覆蓋自訂的寬度和高度值。使用自訂尺寸時，寬度和高度都必須在 512 至 2048 像素之間。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 從 ByteDance API 返回的生成圖片，以張量形式呈現。 |

---
**Source fingerprint (SHA-256):** `6ad3011ae942e81bc5e5296fa7120ee89637ef7487e2f12822d84b6917ec211e`
