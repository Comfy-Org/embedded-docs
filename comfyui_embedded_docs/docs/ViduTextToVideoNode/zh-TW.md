> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/zh-TW.md)

Vidu 文字轉影片生成節點能根據文字描述建立影片。它使用各種影片生成模型，將您的文字提示轉換為影片內容，並提供可自訂的持續時間、長寬比和視覺風格設定。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `vidu_q1`<br>*其他 VideoModelName 選項* | 模型名稱（預設值：vidu_q1） |
| `prompt` | STRING | 是 | - | 用於影片生成的文字描述 |
| `duration` | INT | 否 | 5-5 | 輸出影片的持續時間（單位：秒）（預設值：5） |
| `seed` | INT | 否 | 0-2147483647 | 影片生成的隨機種子（0 表示隨機）（預設值：0） |
| `aspect_ratio` | COMBO | 否 | `r_16_9`<br>*其他 AspectRatio 選項* | 輸出影片的長寬比（預設值：r_16_9） |
| `resolution` | COMBO | 否 | `r_1080p`<br>*其他 Resolution 選項* | 支援的數值可能因模型和持續時間而異（預設值：r_1080p） |
| `movement_amplitude` | COMBO | 否 | `auto`<br>*其他 MovementAmplitude 選項* | 畫面中物體的運動幅度（預設值：auto） |

**注意：** `prompt` 欄位為必填且不能為空。`duration` 參數目前固定為 5 秒。

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 根據文字提示生成的影片 |