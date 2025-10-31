> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/zh-TW.md)

{heading_overview}

根據輸入圖像和文字提示生成影片。此節點接收一張圖像，並透過套用指定的動畫和品質設定，將靜態圖像轉換為動態序列來創建動畫影片。

{heading_inputs}

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `圖像` | IMAGE | 是 | - | 要轉換為影片的輸入圖像 |
| `提示詞` | STRING | 是 | - | 影片生成的提示文字 |
| `品質` | COMBO | 是 | `res_540p`<br>`res_1080p` | 影片品質設定（預設值：res_540p） |
| `持續秒數` | COMBO | 是 | `dur_2`<br>`dur_5`<br>`dur_10` | 生成影片的持續時間（單位：秒） |
| `動作模式` | COMBO | 是 | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` | 套用於影片生成的動畫風格 |
| `種子值` | INT | 是 | 0-2147483647 | 影片生成的種子值（預設值：0） |
| `負向提示詞` | STRING | 否 | - | 圖像中不希望出現元素的選擇性文字描述 |
| `PixVerse 樣板` | CUSTOM | 否 | - | 影響生成風格的選擇性模板，由 PixVerse Template 節點創建 |

**注意：** 使用 1080p 品質時，動畫模式會自動設定為 normal，且持續時間限制為 5 秒。對於非 5 秒的持續時間，動畫模式也會自動設定為 normal。

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 根據輸入圖像和參數生成的影片 |