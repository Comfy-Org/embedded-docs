# MinimaxHailuo03RegenerateNode

此節點會將 MiniMax H3 768P 影片輸出以 2K 解析度重新渲染。它會上傳來源影片及用於建立該影片的確切提示詞，啟動 MiniMax H3 重新生成任務，並傳回重新渲染後的 2K 影片。如果原始生成使用了首幀、尾幀或參考媒體，請附加相同的輸入。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要用於影片重新生成的模型。選取此模型會顯示以下記載的提示詞、解析度與參考媒體設定。 | COMBO | 是 | "MiniMax H3" |
| `prompt` | 用於生成來源影片的確切提示詞。不得為空。 | STRING | 是 | Text |
| `resolution` | 要重新渲染來源影片的解析度。 | COMBO | 是 | "2K" |
| `reference_images` | 原始生成中的參考圖片，依相同順序。最多 9 張圖片。 | IMAGE | 否 | 0-9 images |
| `reference_videos` | 原始生成中的參考影片，依相同順序。最多 3 段影片，每段 2-15 秒，總長 15 秒。 | VIDEO | 否 | 0-3 videos |
| `reference_audios` | 原始生成中的音訊參考，依相同順序。最多 3 段音訊，每段 2-15 秒，總長 15 秒。不能沒有參考圖片或影片而單獨使用。 | AUDIO | 否 | 0-3 clips |
| `video` | 要重新渲染的 MiniMax H3 768P 輸出影片。請連接 MiniMax H3 影片節點未經修改的輸出（24 FPS，4-15 秒）。無法使用 2K 輸出。 | VIDEO | 是 | 24 FPS, 4-15 seconds |
| `first_frame` | 原始生成中使用的首幀圖片（若有使用）。 | IMAGE | 否 | Image |
| `last_frame` | 原始生成中使用的尾幀圖片（若有使用）。 | IMAGE | 否 | Image |
| `watermark` | 是否在影片中加入 AIGC 浮水印。預設為 false。 | BOOLEAN | 是 | false / true |

### 限制條件

- 來源 `video` 必須是未經修改的 MiniMax H3 768P 輸出：寬高可被 32 整除，總畫素不超過 1,032,192，24 FPS，且幀數為 107 至 362，以 17 為步進（即 24 FPS 下的 4 至 15 秒）。無法將 2K 輸出作為來源。
- `first_frame` / `last_frame` 與參考媒體（`reference_images`、`reference_videos`、`reference_audios`）為互斥關係。若為圖片轉影片提示詞，請使用幀；若為參考轉影片提示詞，請使用參考媒體。
- `reference_audios` 需要至少一個 `reference_images` 或 `reference_videos` 輸入。
- `reference_images`：每張圖片的寬高比必須介於 0.4 至 2.5 之間，且至少為 256x256 像素。
- `reference_videos`：每段影片必須為 23.976 至 60 FPS，長度 2-15 秒；總時長不得超過 15 秒。
- `reference_audios`：每段音訊必須為 2-15 秒；總時長不得超過 15 秒。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 重新渲染後的 2K 解析度 MiniMax H3 影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`
