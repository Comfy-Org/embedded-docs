> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/zh-TW.md)

此節點使用 Grok API 根據文字提示編輯現有影片。它會上傳您的影片，向 AI 模型發送請求以根據您的描述進行修改，並返回新生成的影片。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"grok-imagine-video"`<br>`"grok-imagine-video-beta"` | 用於影片編輯的 AI 模型（預設值：`"grok-imagine-video"`）。 |
| `prompt` | STRING | 是 | 不適用 | 所需影片的文字描述。 |
| `video` | VIDEO | 是 | 不適用 | 要編輯的輸入影片。支援的最大時長為 8.7 秒，檔案大小為 50MB。 |
| `seed` | INT | 否 | 0 到 2147483647 | 決定節點是否應重新執行的種子值。無論種子值為何，實際結果都是非確定性的（預設值：0）。 |

**限制條件：**

* 輸入 `video` 的時長必須在 1 到 8.7 秒之間。
* 輸入 `video` 的檔案大小不得超過 50MB。
* `prompt` 不得為空。

## 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `video` | VIDEO | 由 AI 模型生成的編輯後影片。 |

---
**Source fingerprint (SHA-256):** `dfe52a089f7bfe7abc7f40ef113c44aef2dded828221d9d1acf0ddb6a167c33f`
