# PixVerse 影像轉影片

根據輸入的圖片與文字提示詞生成影片。此節點接收一張圖片，套用指定的動態與品質設定，將靜態圖片轉換為連續動態畫面，進而產生動畫影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `圖像` | 要轉換成影片的輸入圖片 | IMAGE | 是 | - |
| `提示詞` | 影片生成的提示詞 | STRING | 是 | - |
| `品質` | 影片品質設定（預設：res_540p） | COMBO | 是 | `res_540p`<br>`res_1080p` |
| `持續秒數` | 生成影片的時長（秒） | COMBO | 是 | `dur_2`<br>`dur_5`<br>`dur_10` |
| `動作模式` | 套用於影片生成的動態風格 | COMBO | 是 | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` |
| `種子值` | 影片生成的種子（預設：0） | INT | 是 | 0-2147483647 |
| `負向提示詞` | 可選的負面提示詞，描述圖片中不希望出現的元素 | STRING | 否 | - |
| `PixVerse 樣板` | 可選範本，用於影響生成風格，由 PixVerse Template 節點建立 | CUSTOM | 否 | - |

**注意：** 使用 1080p 品質時，動態模式會自動設為 normal，且時長限制為 5 秒。若時長不是 5 秒，動態模式也會自動設為 normal。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 根據輸入圖片與參數生成的影片 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `93ea662a27159f55bf12e49ea230f0005813614ad07f5189d1fd61e7b937fd4b`
