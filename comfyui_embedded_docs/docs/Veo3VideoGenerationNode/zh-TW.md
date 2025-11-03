> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/zh-TW.md)

使用 Google 的 Veo 3 API 從文字提示生成影片。此節點支援兩種 Veo 3 模型：veo-3.0-generate-001 和 veo-3.0-fast-generate-001。它擴展了基礎 Veo 節點的功能，加入了 Veo 3 特有的功能，包括音訊生成和固定的 8 秒時長。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 影片的文字描述 (預設值: "") |
| `aspect_ratio` | COMBO | 是 | "16:9"<br>"9:16" | 輸出影片的長寬比 (預設值: "16:9") |
| `negative_prompt` | STRING | 否 | - | 負向文字提示，用於引導影片中應避免的內容 (預設值: "") |
| `duration_seconds` | INT | 否 | 8-8 | 輸出影片的持續時間（單位：秒）（Veo 3 僅支援 8 秒）(預設值: 8) |
| `enhance_prompt` | BOOLEAN | 否 | - | 是否透過 AI 輔助增強提示 (預設值: True) |
| `person_generation` | COMBO | 否 | "ALLOW"<br>"BLOCK" | 是否允許在影片中生成人物 (預設值: "ALLOW") |
| `seed` | INT | 否 | 0-4294967295 | 影片生成的種子值（0 表示隨機）(預設值: 0) |
| `image` | IMAGE | 否 | - | 用於引導影片生成的參考影像（可選） |
| `model` | COMBO | 否 | "veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" | 用於影片生成的 Veo 3 模型 (預設值: "veo-3.0-generate-001") |
| `generate_audio` | BOOLEAN | 否 | - | 為影片生成音訊。所有 Veo 3 模型均支援此功能。(預設值: False) |

**注意：** `duration_seconds` 參數在所有 Veo 3 模型中固定為 8 秒，無法更改。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案 |