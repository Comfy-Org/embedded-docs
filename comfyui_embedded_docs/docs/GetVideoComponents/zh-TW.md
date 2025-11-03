> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/zh-TW.md)

Get Video Components 節點可從影片檔案中提取所有主要元素。它會將影片分離為個別影格、提取音訊軌道，並提供影片的影格率資訊。這讓您能夠獨立處理每個組件，以進行後續處理或分析。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | 是 | - | 要從中提取組件的影片。 |

## 輸出參數

| 輸出名稱 | 資料類型 | 參數說明 |
|-------------|-----------|-------------|
| `images` | IMAGE | 從影片中提取的個別影格，以獨立影像形式呈現。 |
| `audio` | AUDIO | 從影片中提取的音訊軌道。 |
| `fps` | FLOAT | 影片的影格率，以每秒影格數為單位。 |