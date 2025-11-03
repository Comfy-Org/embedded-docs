> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/zh-TW.md)

PixVerse Template 節點允許您從可用的 PixVerse 影片生成模板中進行選擇。它會將您選擇的模板名稱轉換為 PixVerse API 建立影片所需的相應模板 ID。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `template` | STRING | 是 | 提供多個選項 | 用於 PixVerse 影片生成的模板。可用選項對應於 PixVerse 系統中的預定義模板。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `pixverse_template` | INT | 對應於所選模板名稱的模板 ID，可供其他 PixVerse 節點用於影片生成。 |