> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/zh-TW.md)

根據提示和輸出尺寸生成影片。此節點使用 PixVerse API 在兩個輸入圖像之間建立轉場影片，允許您指定影片品質、持續時間、動畫風格和生成參數。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `first_frame` | IMAGE | 是 | - | 影片轉場的起始圖像 |
| `last_frame` | IMAGE | 是 | - | 影片轉場的結束圖像 |
| `prompt` | STRING | 是 | - | 影片生成的提示詞（預設：空字串） |
| `quality` | COMBO | 是 | 來自 PixverseQuality 枚舉的可用品質選項<br>預設：res_540p | 影片品質設定 |
| `duration_seconds` | COMBO | 是 | 來自 PixverseDuration 枚舉的可用持續時間選項 | 影片持續時間（秒） |
| `motion_mode` | COMBO | 是 | 來自 PixverseMotionMode 枚舉的可用動畫模式選項 | 轉場的動畫風格 |
| `seed` | INT | 是 | 0 到 2147483647 | 影片生成的種子值（預設：0） |
| `negative_prompt` | STRING | 否 | - | 圖像中不希望出現元素的文字描述（可選，預設：空字串） |

**注意：** 使用 1080p 品質時，動畫模式會自動設定為 normal，且持續時間限制為 5 秒。對於非 5 秒的持續時間，動畫模式也會自動設定為 normal。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的轉場影片 |