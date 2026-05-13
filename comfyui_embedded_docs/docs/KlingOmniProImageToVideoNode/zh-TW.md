> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/zh-TW.md)

此節點使用 Kling AI 模型，根據文字提示和最多七張參考圖片來生成影片。您可以控制影片的長寬比、時長、解析度，並可選擇使用分鏡或生成音訊。該節點會將請求發送到外部 API，並返回生成的影片。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | 是 | `"kling-v3-omni"`<br>`"kling-video-o1"` | 用於影片生成的特定 Kling 模型（預設值："kling-v3-omni"）。 |
| `prompt` | STRING | 是 | - | 描述影片內容的文字提示。可包含正面和負面描述。文字會自動標準化，長度必須在 1 到 2500 個字元之間。啟用分鏡時此參數會被忽略。 |
| `aspect_ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` | 生成影片的目標長寬比。 |
| `duration` | INT | 是 | 3 到 15 | 影片的長度，單位為秒。可使用滑桿調整數值（預設值：5）。 |
| `reference_images` | IMAGE | 是 | - | 最多 7 張參考圖片。每張圖片至少需為 300x300 像素，長寬比需介於 1:2.5 與 2.5:1 之間。 |
| `resolution` | COMBO | 否 | `"4k"`<br>`"1080p"`<br>`"720p"` | 影片的輸出解析度。此參數為可選（預設值："1080p"）。 |
| `storyboards` | DYNAMIC_COMBO | 否 | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` | 生成一系列帶有各自提示和時長的影片片段。僅 `kling-v3-omni` 支援此功能。啟用時，全域 `prompt` 會被忽略，且所有分鏡片段的總時長必須等於全域 `duration`。 |
| `generate_audio` | BOOLEAN | 否 | `true`<br>`false` | 為影片生成音訊。僅 `kling-v3-omni` 支援此功能（預設值：false）。 |
| `seed` | INT | 否 | 0 到 2147483647 | 種子值控制節點是否應重新執行；無論種子值為何，結果皆非確定性（預設值：0）。 |

**注意：** `reference_images` 輸入最多接受 7 張圖片。如果提供更多圖片，節點將會報錯。每張圖片都會驗證其最小尺寸和長寬比。

**模型特定限制：**
- `kling-video-o1` 不支援超過 10 秒的時長。
- `kling-video-o1` 不支援音訊生成。
- `kling-video-o1` 不支援 4k 解析度。
- `kling-video-o1` 不支援分鏡功能。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案。 |

---
**Source fingerprint (SHA-256):** `80f4568be81b23c75bfff2bd3f21a61b242563c3c9fb1985a03e76ace24dceb2`
