> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/zh-TW.md)

# PixVerse 文字轉影片節點

根據文字提示和各種生成參數產生影片。此節點使用 PixVerse API 建立影片內容，可控制長寬比、品質、持續時間、動作風格等。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 影片生成的提示詞（預設值：""） |
| `aspect_ratio` | COMBO | 是 | 來自 PixverseAspectRatio 的選項 | 生成影片的長寬比 |
| `quality` | COMBO | 是 | 來自 PixverseQuality 的選項 | 影片品質設定（預設值：PixverseQuality.res_540p） |
| `duration_seconds` | COMBO | 是 | 來自 PixverseDuration 的選項 | 生成影片的持續時間（秒） |
| `motion_mode` | COMBO | 是 | 來自 PixverseMotionMode 的選項 | 影片生成的動作風格 |
| `seed` | INT | 是 | 0 到 2147483647 | 影片生成的隨機種子（預設值：0） |
| `negative_prompt` | STRING | 否 | - | 可選的負面提示詞，描述影像中不希望出現的元素（預設值：""） |
| `pixverse_template` | CUSTOM | 否 | - | 可選的範本，用於影響生成風格，由 PixVerse 範本節點建立 |

**注意：** 使用 1080p 品質時，動作模式會自動設定為正常，持續時間限制為 5 秒。對於非 5 秒的持續時間，動作模式也會自動設定為正常。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案 |

---
**Source fingerprint (SHA-256):** `ab9264668f48533cb139abfb322e9a6e425a2ad7280da103a7fe0a7704158762`
