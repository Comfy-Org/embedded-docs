# MinimaxHailuo03ReferenceNode

此節點使用 MiniMax H3 模型生成影片，並使用參考圖片、影片和音訊來條件化結果。參考內容在提示詞中按其連接順序引用，例如「Image 1」、「Image 2」、「Video 1」、「Audio 1」等。

## 輸入
| 參數 | 描述 | 資料類型 | 必需 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片生成的模型（預設："MiniMax H3"）。選擇 "MiniMax H3" 時，會提供以下設定：`prompt`、`duration`、`resolution`、`ratio`、`reference_images`、`reference_videos`、`reference_audios`。 | STRING | 是 | "MiniMax H3" |
| `prompt` | 欲生成影片的文字描述。可按順序引用參考媒體，例如「Image 1」、「Image 2」、「Video 1」或「Audio 1」。 | STRING | 是 | 最小長度：1 個字元 |
| `duration` | 生成影片的時長（秒）。 | INT | 是 | 提供多種選項 |
| `resolution` | 生成影片的輸出解析度。 | STRING | 是 | 提供多種選項 |
| `ratio` | 生成影片的寬高比。 | STRING | 是 | 提供多種選項 |
| `reference_images` | 主體或風格參考圖片，在提示詞中按連接順序引用為「Image 1」至「Image 9」。最多 9 張圖片。 | IMAGE | 否 | 0 至 9 張圖片 |
| `reference_videos` | 動作或場景參考影片，在提示詞中按連接順序引用為「Video 1」至「Video 3」。最多 3 個影片，每個 2-15 秒，總共 15 秒。 | VIDEO | 否 | 0 至 3 個影片 |
| `reference_audios` | 音訊參考，在提示詞中按連接順序引用為「Audio 1」至「Audio 3」。最多 3 個片段，每個 2-15 秒，總共 15 秒。沒有參考圖片或影片時無法使用。 | AUDIO | 否 | 0 至 3 個片段 |
| `seed` | 隨機種子。使用相同種子的相同請求會產生相似但不保證相同的結果（預設：42）。 | INT | 是 | 0 至 4294967295 |
| `watermark` | 是否在影片中新增 AIGC 浮水印（預設：false）。 | BOOLEAN | 否 | true<br>false |

### 參數限制

- 至少需要一張參考圖片或一個參考影片。僅使用參考音訊不被接受。
- 每張參考圖片的寬高比必須約在 0.4 到 2.5（2:5 到 5:2）之間，且最小寬度和高度為 256 像素。
- 每個參考影片的長度必須在 2 到 15 秒之間，幀率必須在 23.976 到 60 FPS 之間。所有參考影片的總時長不得超過 15 秒。
- 每個參考音訊片段必須在 2 到 15 秒之間。所有參考音訊片段的總時長不得超過 15 秒。

## 輸出
| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `beca020333a544188e6c21829eb8e63415aa5299efc676438e85662a5f08660d`
