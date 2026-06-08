此節點將參考圖片的視覺風格套用到您的輸入圖片上。它使用外部 AI 服務來處理圖片，讓您能控制風格轉換的強度以及原始圖片結構的保留程度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要套用風格轉換的圖片。 | IMAGE | 是 | - |
| `reference_image` | 用來提取風格的參考圖片。 | IMAGE | 是 | - |
| `prompt` | 可選的文字提示，用於引導風格轉換。 | STRING | 否 | - |
| `style_strength` | 風格強度百分比（預設值：100）。 | INT | 否 | 0 至 100 |
| `structure_strength` | 維持原始圖片結構的程度（預設值：50）。 | INT | 否 | 0 至 100 |
| `flavor` | 風格轉換的風味。 | COMBO | 否 | "faithful"<br>"gen_z"<br>"psychedelia"<br>"detaily"<br>"clear"<br>"donotstyle"<br>"donotstyle_sharp" |
| `engine` | 處理引擎的選擇。 | COMBO | 否 | "balanced"<br>"definio"<br>"illusio"<br>"3d_cartoon"<br>"colorful_anime"<br>"caricature"<br>"real"<br>"super_real"<br>"softy" |
| `portrait_mode` | 啟用人像模式以進行臉部增強。 | COMBO | 否 | "disabled"<br>"enabled" |
| `portrait_style` | 套用於人像圖片的視覺風格。此輸入僅在 `portrait_mode` 設定為 "enabled" 時可用。 | COMBO | 否 | "standard"<br>"pop"<br>"super_pop" |
| `portrait_beautifier` | 人像的臉部美化強度。此輸入僅在 `portrait_mode` 設定為 "enabled" 時可用。 | COMBO | 否 | "none"<br>"beautify_face"<br>"beautify_face_max" |
| `fixed_generation` | 停用時，每次生成都會引入一定程度的隨機性，從而產生更多樣化的結果（預設值：True）。 | BOOLEAN | 否 | - |

**限制條件：**

* 必須恰好提供一個 `image` 和一個 `reference_image`。
* 兩張圖片的長寬比必須介於 1:3 和 3:1 之間。
* 兩張圖片的最小高度和寬度必須為 160 像素。
* `portrait_style` 和 `portrait_beautifier` 參數僅在 `portrait_mode` 設定為 "enabled" 時才啟用且為必要。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `image` | 套用風格轉換後產生的結果圖片。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageStyleTransferNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4ae400183618953c369d089d39b878f0a24592967c29d779c577fb8b7339dea8`
