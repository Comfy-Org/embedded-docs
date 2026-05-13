> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/zh-TW.md)

此節點將參考圖片的視覺風格套用到您的輸入圖片上。它使用外部 AI 服務來處理圖片，讓您能控制風格轉換的強度以及原始圖片結構的保留程度。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要套用風格轉換的圖片。 |
| `reference_image` | IMAGE | 是 | - | 用來提取風格的參考圖片。 |
| `prompt` | STRING | 否 | - | 可選的文字提示，用於引導風格轉換。 |
| `style_strength` | INT | 否 | 0 至 100 | 風格強度百分比（預設值：100）。 |
| `structure_strength` | INT | 否 | 0 至 100 | 維持原始圖片結構的程度（預設值：50）。 |
| `flavor` | COMBO | 否 | "faithful"<br>"gen_z"<br>"psychedelia"<br>"detaily"<br>"clear"<br>"donotstyle"<br>"donotstyle_sharp" | 風格轉換的風味。 |
| `engine` | COMBO | 否 | "balanced"<br>"definio"<br>"illusio"<br>"3d_cartoon"<br>"colorful_anime"<br>"caricature"<br>"real"<br>"super_real"<br>"softy" | 處理引擎的選擇。 |
| `portrait_mode` | COMBO | 否 | "disabled"<br>"enabled" | 啟用人像模式以進行臉部增強。 |
| `portrait_style` | COMBO | 否 | "standard"<br>"pop"<br>"super_pop" | 套用於人像圖片的視覺風格。此輸入僅在 `portrait_mode` 設定為 "enabled" 時可用。 |
| `portrait_beautifier` | COMBO | 否 | "none"<br>"beautify_face"<br>"beautify_face_max" | 人像的臉部美化強度。此輸入僅在 `portrait_mode` 設定為 "enabled" 時可用。 |
| `fixed_generation` | BOOLEAN | 否 | - | 停用時，每次生成都會引入一定程度的隨機性，從而產生更多樣化的結果（預設值：True）。 |

**限制條件：**

* 必須恰好提供一個 `image` 和一個 `reference_image`。
* 兩張圖片的長寬比必須介於 1:3 和 3:1 之間。
* 兩張圖片的最小高度和寬度必須為 160 像素。
* `portrait_style` 和 `portrait_beautifier` 參數僅在 `portrait_mode` 設定為 "enabled" 時才啟用且為必要。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `image` | IMAGE | 套用風格轉換後產生的結果圖片。 |

---
**Source fingerprint (SHA-256):** `4ae400183618953c369d089d39b878f0a24592967c29d779c577fb8b7339dea8`
