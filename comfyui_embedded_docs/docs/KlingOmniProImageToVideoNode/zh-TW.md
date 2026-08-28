# Kling Omni 圖像轉影片 (Pro)

此節點使用 Kling AI 模型，根據文字提示和最多七張參考圖片生成影片。您可以控制影片的寬高比、時長和解析度，並可選擇使用分鏡或生成音訊。此節點會將請求傳送至外部 API，並回傳生成的影片。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_name` | 用於影片生成的特定 Kling 模型（預設：`"kling-v3-omni"`）。 | COMBO | 是 | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `提示詞` | 描述影片內容的文字提示。可包含正面和負面的描述。啟用分鏡時此欄位會被忽略。像是 `@image` 或 `@video`（可選擇編號）這類佔位符會自動轉換為 API 相容格式。長度必須介於 1 到 2500 個字元之間（啟用分鏡時可留空）。 | STRING | 是 | 1 到 2500 個字元 |
| `長寬比` | 生成影片所需的寬高比。 | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `時長` | 影片的長度（秒），可使用滑桿調整（預設：5）。 | INT | 是 | 3 到 15 |
| `參考圖片` | 最多 7 張參考圖片。每張圖片至少必須為 300x300 像素，且寬高比介於 1:2.5 與 2.5:1 之間。 | IMAGE | 是 | 1 到 7 張圖片 |
| `解析度` | 影片的輸出解析度（預設：`"1080p"`）。 | COMBO | 否 | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `分鏡腳本` | 生成一系列具有各自提示與時長的影片片段。僅支援 `kling-v3-omni`。啟用時，全域的 `prompt` 會被忽略，且所有分鏡片段的總時長必須等於全域的 `duration`（預設：`"disabled"`）。 | DYNAMIC_COMBO | 否 | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `產生音訊` | 為影片生成音訊。僅支援 `kling-v3-omni`（預設：false）。 | BOOLEAN | 否 | `true`<br>`false` |
| `種子` | 種子控制節點是否應重新執行；無論種子為何，結果皆不具確定性（預設：0）。 | INT | 否 | 0 到 2147483647 |

### 分鏡輸入

啟用 `storyboards` 時，每個選取的分鏡片段會出現以下輸入。N 的範圍從 1 到所選的分鏡數量。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | 分鏡片段 N 的提示。最多 512 個字元。 | STRING | 是 | 1 到 512 個字元 |
| `storyboard_N_duration` | 分鏡片段 N 的時長（秒）（預設：4）。 | INT | 是 | 1 到 15 |

**注意：** `reference_images` 輸入最多接受 7 張圖片。如果提供更多，節點會引發錯誤。每張圖片都會驗證最小尺寸與寬高比。

**模型特定限制：**
- `kling-video-o1` 不支援超過 10 秒的時長。
- `kling-video-o1` 不支援音訊生成。
- `kling-video-o1` 不支援 4k 解析度。
- `kling-video-o1` 不支援分鏡。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ccf7881065d2a365cdaa0e164b8b1d46c67985067866ab0fe91d492a62015f07`
