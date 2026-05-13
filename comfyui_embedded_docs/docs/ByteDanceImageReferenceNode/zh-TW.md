> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/zh-TW.md)

# ByteDance 圖像參考節點

ByteDance 圖像參考節點使用文字提示和一至四張參考圖像來生成影片。它將圖像和提示發送到外部 API 服務，該服務會創建符合您描述的影片，同時融入參考圖像的視覺風格和內容。此節點提供多種控制選項，用於設定影片解析度、長寬比、時長和其他生成參數。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | STRING | 是 | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"` | 用於影片生成的 AI 模型（預設值：`"seedance-1-0-lite-i2v-250428"`）。 |
| `prompt` | STRING | 是 | - | 用於生成影片的文字提示。 |
| `images` | IMAGE | 是 | - | 一至四張圖像。每張圖像必須介於 300x300 到 6000x6000 像素之間，長寬比介於 0.4 到 2.5 之間。 |
| `resolution` | STRING | 是 | `"480p"`<br>`"720p"` | 輸出影片的解析度。 |
| `aspect_ratio` | STRING | 是 | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | 輸出影片的長寬比（預設值：`"adaptive"`）。 |
| `duration` | INT | 是 | 3 - 12 | 輸出影片的時長，單位為秒（預設值：5）。 |
| `seed` | INT | 否 | 0 - 2147483647 | 用於生成的種子值（預設值：0）。 |
| `watermark` | BOOLEAN | 否 | - | 是否在影片中添加「AI 生成」浮水印（預設值：False）。 |

**注意：** 提示文字不得包含以下參數字串：`--resolution`、`--ratio`、`--duration`、`--seed` 或 `--watermark`。這些值僅通過其專用的輸入小工具進行控制。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 根據輸入提示和參考圖像生成的影片檔案。 |

---
**Source fingerprint (SHA-256):** `d5d1292d6af2fe24dc5c8a10174204546a5a6054ea1f43db44a45ce1017957d6`
