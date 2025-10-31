> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/zh-TW.md)

根據提示和輸出尺寸生成影片。此節點使用文字描述和各種生成參數來創建影片內容，透過 PixVerse API 產生影片輸出。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `提示詞` | STRING | 是 | - | 影片生成的提示文字（預設：""） |
| `長寬比` | COMBO | 是 | 來自 PixverseAspectRatio 的選項 | 生成影片的長寬比 |
| `品質` | COMBO | 是 | 來自 PixverseQuality 的選項 | 影片品質設定（預設：PixverseQuality.res_540p） |
| `影片長度（秒）` | COMBO | 是 | 來自 PixverseDuration 的選項 | 生成影片的持續時間（單位：秒） |
| `動作模式` | COMBO | 是 | 來自 PixverseMotionMode 的選項 | 影片生成的動畫風格 |
| `種子值` | INT | 是 | 0 到 2147483647 | 影片生成的種子值（預設：0） |
| `負向提示詞` | STRING | 否 | - | 可選的文字描述，用於指定圖像中不希望出現的元素（預設：""） |
| `PixVerse 樣板` | CUSTOM | 否 | - | 可選的模板，用於影響生成風格，由 PixVerse Template 節點創建 |

**注意：** 當使用 1080p 品質時，動畫模式會自動設定為 normal，且持續時間限制為 5 秒。對於非 5 秒的持續時間，動畫模式也會自動設定為 normal。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案 |