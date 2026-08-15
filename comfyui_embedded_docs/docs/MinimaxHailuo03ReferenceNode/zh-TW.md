# MiniMax H3 參考生成影片

此節點使用 MiniMax H3 模型生成影片，並透過參考圖片、影片和音訊來控制結果。參考資料在提示詞中按其連接順序被引用：「Image 1」、「Image 2」、「Video 1」、「Audio 1」，以此類推。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於影片生成的模型（預設值："MiniMax H3"）。選擇「MiniMax H3」會提供以下設定：`prompt`、`resolution`、`ratio`、`duration`、`reference_images`、`reference_videos` 和 `reference_audios`。 | STRING | 是 | "MiniMax H3" |
| `隨機種子` | 隨機種子。使用相同種子的相同請求會產生相似但不保證相同的結果（預設值：42）。 | INT | 是 | 0 至 4294967295 |
| `浮水印` | 是否在影片中加入 AIGC 浮水印（預設值：false）。 | BOOLEAN | 否 | true<br>false |

### MiniMax H3 輸入

當選擇「MiniMax H3」作為模型時，會出現這些輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。可以按順序引用參考媒體，例如「Image 1」、「Image 2」、「Video 1」或「Audio 1」。 | STRING | 是 | Min length: 1 character |
| `resolution` | 輸出影片的解析度（預設值："768P"）。 | STRING | 是 | "768P"<br>"2K" |
| `ratio` | 輸出影片的寬高比（預設值："adaptive"）。 | STRING | 是 | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | 輸出影片的時長（秒）（預設值：5）。 | INT | 是 | 4 至 15 |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可擴充插槽：連接 1..9 個項目（`image_1`...`image_9`）。主體或風格參考圖片，在提示詞中按連接順序引用為「Image 1」至「Image 9」。最多 9 張圖片。 | IMAGE | 否 | 0 至 9 images |
| `reference_videos` | 可擴充插槽：連接 1..3 個項目（`video_1`...`video_3`）。動作或場景參考影片，在提示詞中按連接順序引用為「Video 1」至「Video 3」。最多 3 部影片，每部 2-15 秒，總計 15 秒。 | VIDEO | 否 | 0 至 3 videos |
| `reference_audios` | 可擴充插槽：連接 1..3 個項目（`audio_1`...`audio_3`）。音訊參考，在提示詞中按連接順序引用為「Audio 1」至「Audio 3」。最多 3 個音訊片段，每個 2-15 秒，總計 15 秒。沒有參考圖片或影片時無法使用。 | AUDIO | 否 | 0 至 3 clips |

### 參數約束

- 至少需要一張參考圖片或一部參考影片。單獨的參考音訊不被接受。
- 每張參考圖片的寬高比必須介於約 0.4 至 2.5（2:5 至 5:2）之間，且最小寬度和高度為 256 像素。
- 每部參考影片的時長必須在 2 至 15 秒之間，幀率必須在 23.976 至 60 FPS 之間。所有參考影片的總時長不得超過 15 秒。
- 每個參考音訊片段的時長必須在 2 至 15 秒之間。所有參考音訊片段的總時長不得超過 15 秒。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f7e9c68addda6b48a2366139ecfa28ee57e6cda4aa5cd775c2d769517366573f`
