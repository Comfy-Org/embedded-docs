# MiniMax 圖像轉影片

根據圖片、提示詞及可選參數，透過 MiniMax 的 API 同步生成影片。此節點接收輸入圖片和文字描述來建立影片序列，並提供多種模型選項與配置設定。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `圖像` | 作為影片生成第一幀的圖片 | IMAGE | 是 | - |
| `提示文字` | 引導影片生成的文字提示詞（預設：空字串） | STRING | 是 | - |
| `模型` | 用於影片生成的模型（預設："I2V-01"） | COMBO | 是 | "I2V-01-Director"<br>"I2V-01"<br>"I2V-01-live" |
| `種子` | 用於產生雜訊的隨機種子（預設：0） | INT | 否 | 0 到 18446744073709551615 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片輸出 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxImageToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9ad1659352e363361f09d6a7a0e24835056b20cc84532247251f516b0ac284e8`
