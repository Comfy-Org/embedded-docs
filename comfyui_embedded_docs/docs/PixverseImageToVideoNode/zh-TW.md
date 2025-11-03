> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/zh-TW.md)

根據輸入的影像和文字提示生成影片。此節點接收一張影像，並透過套用指定的動畫和品質設定，將靜態影像轉換為動態序列來創建動畫影片。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要轉換為影片的輸入影像 |
| `prompt` | STRING | 是 | - | 影片生成的提示文字 |
| `quality` | COMBO | 是 | `res_540p`<br>`res_1080p` | 影片品質設定（預設值：res_540p） |
| `duration_seconds` | COMBO | 是 | `dur_2`<br>`dur_5`<br>`dur_10` | 生成影片的持續時間（單位：秒） |
| `motion_mode` | COMBO | 是 | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` | 套用於影片生成的動畫風格 |
| `seed` | INT | 是 | 0-2147483647 | 影片生成的種子值（預設值：0） |
| `negative_prompt` | STRING | 否 | - | 影像中不希望出現元素的文字描述（可選） |
| `pixverse_template` | CUSTOM | 否 | - | 影響生成風格的可選模板，由 PixVerse Template 節點創建 |

**注意：** 當使用 1080p 品質時，動畫模式會自動設定為 normal，且持續時間限制為 5 秒。對於非 5 秒的持續時間，動畫模式也會自動設定為 normal。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 根據輸入影像和參數生成的影片 |