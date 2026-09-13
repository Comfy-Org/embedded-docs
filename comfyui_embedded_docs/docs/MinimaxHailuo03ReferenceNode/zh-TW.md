# MiniMax H3 參考生成影片

此節點使用 MiniMax H3 模型生成影片，並以參考圖像、影片和音訊作為條件。提示中會依連接順序以 "Image 1"、"Image 2"、"Video 1"、"Audio 1" 等方式引用參考。提供兩個模型："MiniMax H3" 和 "MiniMax H3 Max"。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 用於影片生成的模型（預設："MiniMax H3"）。選擇 "MiniMax H3" 會提供下方的 MiniMax H3 生成與參考輸入。選擇 "MiniMax H3 Max" 會提供下方的 MiniMax H3 Max 生成與參考輸入。 | DYNAMIC_COMBO | 是 | "MiniMax H3"<br>"MiniMax H3 Max" |
| `隨機種子` | 隨機種子。相同請求搭配相同種子會產生相似但不保證完全相同的結果（預設：42）。 | INT | 是 | 0 到 4294967295 |
| `浮水印` | 是否在影片中加入 AIGC 浮水印（預設：false）。僅 MiniMax H3 模型支援。 | BOOLEAN | 否 | true<br>false |

### MiniMax H3 輸入

當選擇 "MiniMax H3" 作為模型時，可使用這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。可依參考媒體的順序引用，例如 "Image 1"、"Image 2"、"Video 1" 或 "Audio 1"。 | STRING | 是 | 最少 1 個字元 |
| `resolution` | 輸出影片的解析度（預設："768P"）。 | COMBO | 是 | "768P"<br>"2K" |
| `ratio` | 輸出影片的長寬比（預設："adaptive"）。 | COMBO | 是 | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | 輸出影片的長度，以秒為單位（預設：5）。 | INT | 是 | 4 到 15 |

### MiniMax H3 Max 輸入

當選擇 "MiniMax H3 Max" 作為模型時，可使用這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。可依參考媒體的順序引用，例如 "Image 1"、"Image 2"、"Video 1" 或 "Audio 1"。 | STRING | 是 | 1 到 50000 個字元 |
| `resolution` | 輸出影片的解析度（預設："768P"）。 | COMBO | 是 | "480P"<br>"768P" |
| `ratio` | 輸出影片的長寬比（預設："adaptive"）。 | COMBO | 是 | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | 輸出影片的長度，以秒為單位（預設：5）。 | INT | 是 | 5 到 15 |
| `prompt_expansion_mode` | 生成前改寫提示所投入的程度（預設："balanced"）。 | COMBO | 是 | "balanced"<br>"quality" |
| `reference_detail` | 傳送參考圖像的細節等級。"high" 會以模型使用的最大尺寸傳送（短邊最高 2048 像素）；"standard" 會將它們縮小至最多 2048x1024，以降低參考成本（預設："standard"）。 | COMBO | 是 | "high"<br>"standard" |

### 參考輸入

這些參考輸入由兩個模型共用。每個都是可擴充插槽。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | 可擴充插槽：最多連接 9 個項目（`image_1`...`image_9`）。主體或風格參考圖像，在提示中依連接順序以 "Image 1".."Image 9" 引用。最多 9 張圖像。 | IMAGE | 否 | 0 到 9 張圖像 |
| `reference_videos` | 可擴充插槽：最多連接 3 個項目（`video_1`...`video_3`）。動作或場景參考影片，在提示中依連接順序以 "Video 1".."Video 3" 引用。最多 3 段影片，每段 2-15 秒，總計 15 秒。 | VIDEO | 否 | 0 到 3 段影片 |
| `reference_audios` | 可擴充插槽：最多連接 3 個項目（`audio_1`...`audio_3`）。音訊參考，在提示中依連接順序以 "Audio 1".."Audio 3" 引用。最多 3 段音訊，每段 2-15 秒，總計 15 秒。若沒有參考圖像或影片，則無法使用。 | AUDIO | 否 | 0 到 3 段音訊 |

### 參數限制

- 至少需要一張參考圖像或一段參考影片。不接受只有參考音訊。
- 每張參考圖像的長寬比必須介於約 0.4 和 2.5 之間（2:5 到 5:2），且寬度和高度至少為 256 像素。
- 每段參考影片的長度必須介於 2 到 15 秒之間，影格率介於 23.976 和 60 FPS 之間。所有參考影片的總長度不能超過 15 秒。
- 每段參考音訊的長度必須介於 2 到 15 秒之間。所有參考音訊的總長度不能超過 15 秒。
- 當選擇 "MiniMax H3 Max" 時，`watermark` 設定必須停用。
- 當選擇 "MiniMax H3 Max" 時，參考檔案總數（圖像、影片和音訊合計）不能超過 12。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-----------|-----------|
| `video` | 生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b77eedb1f7757e60518c04484f1cc24c27cf6886b3ae31c15207ea49fd436a73`
