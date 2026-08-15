# Vidu Q3 文字轉影片生成

Vidu Q3 文字轉影片生成節點會根據文字描述建立影片。它使用 Vidu Q3 Pro 或 Q3 Turbo 模型，依據您的提示詞產生影片內容，讓您能控制影片的長度、解析度、畫面比例，以及是否包含音訊。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的模型。選擇模型後，會顯示額外的配置參數，包含畫面比例、解析度、時長與音訊。 | COMBO | 是 | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `prompt` | 用於影片生成的一段文字描述，最大長度為 2000 個字元。 | STRING | 是 | N/A |
| `seed` | 用於控制生成隨機性的種子值（預設：1）。 | INT | 是 | 0 至 2147483647 |

### viduq3-pro 與 viduq3-turbo 輸入

以下配置參數由 `viduq3-pro` 與 `viduq3-turbo` 模型共用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.aspect_ratio` | 輸出影片的畫面比例。 | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `model.resolution` | 輸出影片的解析度。 | COMBO | 是 | `"720p"`<br>`"1080p"` |
| `model.duration` | 輸出影片的時長（秒）（預設：5）。 | INT | 是 | 1 至 16 |
| `model.audio` | 啟用後，輸出影片將包含聲音（包括對白與音效）（預設：False）。 | BOOLEAN | 是 | True/False |

**注意：** 一旦選定 `model`，`aspect_ratio`、`resolution`、`duration` 與 `audio` 即為必填參數，因為它們是該模型配置的一部分。`prompt` 不得為空，且不得超過 2000 個字元。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `89c23454375a43cdfaf46c9e0e55a8a8166d02ada47ca2e237bd9f73fa4d78db`
