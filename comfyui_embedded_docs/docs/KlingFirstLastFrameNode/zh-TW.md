> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/zh-TW.md)

# Kling 首尾影格節點

此節點使用 Kling 3.0 模型來生成影片。它根據文字提示、指定的持續時間以及兩個提供的圖片（起始影格和結束影格）來建立影片。此節點還可以為影片生成伴隨的音訊。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | N/A | 引導影片生成的文字描述。長度必須在 1 到 2500 個字元之間。 |
| `duration` | INT | 否 | 3 到 15 | 影片的長度，以秒為單位（預設值：5）。 |
| `first_frame` | IMAGE | 是 | N/A | 影片的起始圖片。必須至少為 300x300 像素，且長寬比介於 1:2.5 到 2.5:1 之間。 |
| `end_frame` | IMAGE | 是 | N/A | 影片的結束圖片。必須至少為 300x300 像素，且長寬比介於 1:2.5 到 2.5:1 之間。 |
| `generate_audio` | BOOLEAN | 否 | N/A | 控制是否為影片生成音訊（預設值：True）。 |
| `model` | COMBO | 否 | `"kling-v3"` | 模型與生成設定。選擇此選項會顯示一個巢狀的 `resolution` 參數。 |
| `model.resolution` | COMBO | 否 | `"4k"`<br>`"1080p"`<br>`"720p"` | 生成影片的解析度。此參數僅在 `model` 設定為 `"kling-v3"` 時可用（預設值：`"1080p"`）。 |
| `seed` | INT | 否 | 0 到 2147483647 | 用於控制節點是否應重新執行的數字。無論種子值為何，結果都是非確定性的（預設值：0）。 |

**注意：** `first_frame` 和 `end_frame` 圖片必須符合指定的最小尺寸和長寬比要求，節點才能正常運作。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案。 |

---
**Source fingerprint (SHA-256):** `5c904fec35b2bb41cf521263b1b06fd36ba227400b4cec24e79a4e80618e4bae`
