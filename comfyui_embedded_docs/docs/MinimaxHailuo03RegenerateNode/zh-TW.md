# MinimaxHailuo03RegenerateNode

此節點會以 2K 解析度重新渲染 MiniMax H3 768P 影片輸出。它會上傳未修改的 768P 影片以及用於產生該影片的原始提示詞，啟動 MiniMax H3 重新生成任務，並傳回重新渲染後的 2K 影片。如果原始生成使用了首幀、尾幀或參考媒體，請附加相同的輸入。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片重新生成的模型。選擇「MiniMax H3」會顯示提示詞、解析度及參考媒體設定。 | DYNAMIC_COMBO | 是 | "MiniMax H3" |
| `video` | 要重新渲染的 MiniMax H3 768P 輸出影片。請連接 MiniMax H3 影片節點的未修改輸出（24 FPS，4-15 秒）。2K 輸出無法使用。 | VIDEO | 是 | 24 FPS, 4-15 seconds |
| `first_frame` | 原始生成所使用的首幀影像（若有使用）。 | IMAGE | 否 | Image |
| `last_frame` | 原始生成所使用的尾幀影像（若有使用）。 | IMAGE | 否 | Image |
| `watermark` | 是否在影片中加入 AIGC 浮水印。預設為 false。 | BOOLEAN | 是 | false / true |

### MiniMax H3 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於產生來源影片的原始提示詞。不可為空。 | STRING | 是 | Text (multiline) |
| `resolution` | 重新渲染來源影片時使用的解析度。 | COMBO | 是 | "2K" |

### 參考輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可擴充插槽：連接 `image_1` 至 `image_9`（最多 9 張影像）。原始生成中的參考影像，依相同順序排列。 | IMAGE | 否 | 0-9 images |
| `reference_videos` | 可擴充插槽：連接 `video_1` 至 `video_3`（最多 3 部影片）。原始生成中的參考影片，依相同順序排列。 | VIDEO | 否 | 0-3 videos |
| `reference_audios` | 可擴充插槽：連接 `audio_1` 至 `audio_3`（最多 3 個片段）。原始生成中的音訊參考，依相同順序排列。若沒有參考影像或影片，則無法使用。 | AUDIO | 否 | 0-3 clips |

### 限制

- `prompt` 不可為空。
- 來源 `video` 必須是未修改的 MiniMax H3 768P 輸出：24 FPS、寬高皆可被 32 整除、總像素不超過 1,032,192，且幀數為 107 至 362，以 17 為步進（24 FPS 下為 4 至 15 秒）。2K 輸出不能作為來源。
- `first_frame` 與 `last_frame` 和參考媒體（`reference_images`、`reference_videos`、`reference_audios`）互斥。針對影像轉影片（image-to-video）提示詞請使用幀，針對參考轉影片（reference-to-video）提示詞請使用參考媒體。
- `reference_audios` 需要至少一個 `reference_images` 或 `reference_videos` 輸入。
- `first_frame`、`last_frame` 以及每個 `reference_image` 的長寬比必須介於 0.4 至 2.5 之間，且至少為 256x256 像素。
- `reference_videos`：每部影片必須為 23.976 至 60 FPS，長度為 2-15 秒；總時長不得超過 15 秒。
- `reference_audios`：每個片段長度必須為 2-15 秒；總時長不得超過 15 秒。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 以 2K 解析度重新渲染的 MiniMax H3 影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`
