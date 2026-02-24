> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/zh-TW.md)

此節點根據文字描述生成帶有音訊的短片。它會向 Kling AI 服務發送請求，該服務處理提示詞並回傳一個視訊檔案。此節點還可以根據文字為視訊生成伴隨音訊。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | 是 | `"kling-v2-6"` | 用於視訊生成的特定 AI 模型。 |
| `prompt` | STRING | 是 | - | 正向文字提示詞。用於生成視訊的描述。長度必須介於 1 到 2500 個字元之間。 |
| `mode` | COMBO | 是 | `"pro"` | 視訊生成的操作模式。 |
| `aspect_ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` | 生成視訊所需的寬高比。 |
| `duration` | COMBO | 是 | `5`<br>`10` | 視訊的長度，單位為秒。 |
| `generate_audio` | BOOLEAN | 否 | - | 控制是否為視訊生成音訊。啟用後，AI 將根據提示詞創建聲音。(預設值：`True`) |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的視訊檔案。 |
