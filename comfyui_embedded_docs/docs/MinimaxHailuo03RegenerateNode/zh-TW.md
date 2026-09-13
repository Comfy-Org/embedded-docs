# MiniMax H3 重新生成至 2K

此節點會將 MiniMax H3 768P 影片輸出重新渲染為 2K 解析度。它會上傳未經修改的 768P 影片以及用於生成該影片的完全相同提示詞，啟動 MiniMax H3 重新生成作業，並傳回重新渲染後的 2K 影片。如果原始生成使用了首幀、尾幀或參考媒體，請連接相同的輸入。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片重新生成的模型。選擇 "MiniMax H3" 會顯示提示詞、解析度與參考媒體設定。 | DYNAMIC_COMBO | 是 | "MiniMax H3" |
| `video` | 要重新渲染的 MiniMax H3 768P 輸出影片。連接 MiniMax H3 影片節點未經修改的輸出（24 FPS，4-15 秒）。無法使用 2K 輸出。 | VIDEO | 是 | 24 FPS, 4-15 seconds |
| `first_frame` | 原始生成時使用的首幀影像（若有使用）。 | IMAGE | 否 | Image |
| `last_frame` | 原始生成時使用的尾幀影像（若有使用）。 | IMAGE | 否 | Image |
| `watermark` | 是否要在影片中加入 AIGC 浮水印。預設為 false。 | BOOLEAN | 是 | false / true |

### MiniMax H3 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於生成來源影片的完全相同提示詞。不得為空。 | STRING | 是 | Text (multiline) |
| `resolution` | 要將來源影片重新渲染成的解析度。 | COMBO | 是 | "2K" |

### 參考輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可擴充插槽：連接 `image_1` 至 `image_9`（最多 9 張影像）。原始生成時使用的參考影像，順序需相同。 | IMAGE | 否 | 0-9 images |
| `reference_videos` | 可擴充插槽：連接 `video_1` 至 `video_3`（最多 3 部影片）。原始生成時使用的參考影片，順序需相同。 | VIDEO | 否 | 0-3 videos |
| `reference_audios` | 可擴充插槽：連接 `audio_1` 至 `audio_3`（最多 3 段音訊）。原始生成時使用的音訊參考，順序需相同。若沒有參考影像或影片則無法使用。 | AUDIO | 否 | 0-3 clips |

### 限制

- `prompt` 不得為空。
- 來源 `video` 必須是未經修改的 MiniMax H3 768P 輸出：24 FPS，寬度和高度可被 32 整除，總像素最多 1,032,192，且影格數為 107 到 362，間隔為 17（24 FPS 下為 4 到 15 秒）。2K 輸出不能作為來源。
- `first_frame` 和 `last_frame` 與參考媒體（`reference_images`、`reference_videos`、`reference_audios`）互斥。若是圖片轉影片提示詞，請使用影格；若是參考轉影片提示詞，請使用參考媒體。
- `reference_audios` 至少需要一個 `reference_images` 或 `reference_videos` 輸入。
- `first_frame`、`last_frame` 以及每個 `reference_image` 的長寬比必須介於 0.4 與 2.5 之間，且至少為 256x256 像素。
- `reference_videos`：每部影片必須為 23.976 至 60 FPS，且長度為 2-15 秒；總時長不得超過 15 秒。
- `reference_audios`：每段音訊必須為 2-15 秒；總時長不得超過 15 秒。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 以 2K 解析度重新渲染的 MiniMax H3 影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`
