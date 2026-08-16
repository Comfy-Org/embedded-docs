# Vidu Q3 文字轉影片生成

Vidu Q3 文字轉影片生成節點會根據文字描述建立影片。它使用 Vidu Q3 Pro 或 Q3 Turbo 模型，根據您的提示詞生成影片內容，讓您能夠控制影片的長度、解析度、寬高比，以及是否包含音訊。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的模型。選取模型後會顯示額外的設定參數，包括寬高比、解析度、時長和音訊。 | DYNAMIC_COMBO | 是 | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `prompt` | 用於影片生成的一段文字描述，最大長度為 2000 個字元。 | STRING | 是 | N/A |
| `seed` | 用於控制生成隨機性的種子值（預設值：1）。 | INT | 是 | 0 到 2147483647 |

### viduq3-pro 與 viduq3-turbo 輸入

以下設定參數由 `viduq3-pro` 與 `viduq3-turbo` 模型共用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | 輸出影片的寬高比。 | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | `"720p"`<br>`"1080p"` |
| `duration` | 輸出影片的時長（以秒為單位，預設值：5）。 | INT | 是 | 1 到 16 |
| `audio` | 啟用後，會輸出包含聲音的影片（包括對話和音效）（預設值：False）。 | BOOLEAN | 是 | True/False |

**注意：** 一旦選取 `model`，參數 `aspect_ratio`、`resolution`、`duration` 和 `audio` 即為必填，因為它們屬於該模型設定的一部分。`prompt` 不可為空，且不得超過 2000 個字元。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `video` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `89c23454375a43cdfaf46c9e0e55a8a8166d02ada47ca2e237bd9f73fa4d78db`
