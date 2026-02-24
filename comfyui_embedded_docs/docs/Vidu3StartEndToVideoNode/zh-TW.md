> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/zh-TW.md)

此節點透過在提供的起始影格和結束影格之間進行插值，並以文字提示為引導來生成影片。它使用 Vidu Q3 模型在兩張影像之間創建無縫過渡，產生指定時長和解析度的影片。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"viduq3-pro"`<br>`"viduq3-turbo"` | 用於影片生成的模型。選擇選項後，會顯示 `resolution`、`duration` 和 `audio` 的額外配置參數。 |
| `model.resolution` | COMBO | 是 | `"720p"`<br>`"1080p"` | 輸出影片的解析度。此參數在選擇 `model` 後顯示。 |
| `model.duration` | INT | 是 | 1 到 16 | 輸出影片的時長（單位：秒，預設值：5）。此參數在選擇 `model` 後顯示。 |
| `model.audio` | BOOLEAN | 是 | `True` / `False` | 啟用時，輸出帶有聲音（包括對話和音效）的影片（預設值：False）。此參數在選擇 `model` 後顯示。 |
| `first_frame` | IMAGE | 是 | - | 影片序列的起始影像。 |
| `end_frame` | IMAGE | 是 | - | 影片序列的結束影像。 |
| `prompt` | STRING | 是 | - | 引導影片生成的文字描述（最多 2000 個字元）。 |
| `seed` | INT | 否 | 0 到 2147483647 | 用於控制生成隨機性的種子值（預設值：1）。 |

**注意：** 為獲得最佳效果，`first_frame` 和 `end_frame` 影像應具有相似的寬高比。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `video` | VIDEO | 生成的影片檔案。 |