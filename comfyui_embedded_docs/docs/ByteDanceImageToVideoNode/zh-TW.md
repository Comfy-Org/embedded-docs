> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/zh-TW.md)

# ByteDance 圖片轉影片節點

ByteDance 圖片轉影片節點透過 API 使用 ByteDance 模型，根據輸入圖片和文字提示來生成影片。它接收起始影格圖片，並根據提供的描述創建影片序列。此節點提供多種自訂選項，包括影片解析度、長寬比、時長及其他生成參數。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | STRING | 是 | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"`<br>`"seedance-1-0-pro-fast-251015"` | 用於影片生成的 ByteDance 模型（預設值：`"seedance-1-0-pro-fast-251015"`）。 |
| `prompt` | STRING | 是 | - | 用於生成影片的文字提示。去除前後空白後，長度必須至少為 1 個字元。 |
| `image` | IMAGE | 是 | - | 用於影片的起始影格。必須介於 300x300 到 6000x6000 像素之間，長寬比介於 0.4 到 2.5 之間。 |
| `resolution` | STRING | 是 | `"480p"`<br>`"720p"`<br>`"1080p"` | 輸出影片的解析度。 |
| `aspect_ratio` | STRING | 是 | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | 輸出影片的長寬比。 |
| `duration` | INT | 是 | 3 - 12 | 輸出影片的時長（秒），預設值為 5。對於 `seedance-1-5-pro-251215` 模型，最低支援時長為 4 秒。 |
| `seed` | INT | 否 | 0 - 2147483647 | 用於生成的隨機種子（預設值：0）。 |
| `camera_fixed` | BOOLEAN | 否 | - | 指定是否固定攝影機。平台會在你的提示中附加固定攝影機的指令，但不保證實際效果（預設值：False）。 |
| `watermark` | BOOLEAN | 否 | - | 是否在影片中添加「AI 生成」浮水印（預設值：False）。 |
| `generate_audio` | BOOLEAN | 否 | - | 此參數僅對 `seedance-1-5-pro-251215` 模型有效，其他模型將忽略此設定（預設值：False）。 |

**注意：** 提示中不得包含以下詞彙（不區分大小寫）：`resolution`、`ratio`、`duration`、`seed`、`camerafixed`、`watermark`。這些參數需透過專用輸入欄位設定。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 根據輸入圖片和提示參數生成的影片檔案。 |

---
**Source fingerprint (SHA-256):** `e47e14c69f4bdf4921a5a5eaec20fb775473483e80cdd9dd6700d2c7f9219e65`
