根據輸入圖像和文字提示生成影片。此節點接收一張圖像，並透過套用指定的動態與品質設定，將靜態圖像轉換為動態序列，從而產生動畫影片。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `圖像` | 要轉換為影片的輸入圖像 | IMAGE | 是 | - |
| `提示詞` | 用於影片生成的提示詞 | STRING | 是 | - |
| `品質` | 影片品質設定（預設值：res_540p） | COMBO | 是 | `res_540p`<br>`res_1080p` |
| `持續秒數` | 生成影片的持續時間（秒） | COMBO | 是 | `dur_2`<br>`dur_5`<br>`dur_10` |
| `動作模式` | 套用於影片生成的動態風格 | COMBO | 是 | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` |
| `種子值` | 影片生成的隨機種子（預設值：0） | INT | 是 | 0-2147483647 |
| `負向提示詞` | 對圖像中不希望出現元素的選用文字描述 | STRING | 否 | - |
| `PixVerse 樣板` | 用於影響生成風格的選用範本，由 PixVerse 範本節點建立 | CUSTOM | 否 | - |

**注意：** 使用 1080p 品質時，動態模式會自動設為 normal，且持續時間限制為 5 秒。若持續時間非 5 秒，動態模式也會自動設為 normal。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 根據輸入圖像和參數生成的影片 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7630c662a2506fb0c8be0cb9c6bfdfcf0fc06d2b6f16b8636664d587affededc`
