# MiniMax 文字轉影片節點

根據提示詞和可選參數，透過 MiniMax 的 API 同步生成影片。此節點透過連接到 MiniMax 的文字轉影片服務，從文字描述創建影片內容。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `提示文字` | 引導影片生成的文字提示詞 | STRING | 是 | - |
| `模型` | 用於影片生成的模型（預設值："T2V-01"） | COMBO | 否 | "T2V-01"<br>"T2V-01-Director" |
| `種子` | 用於創建噪聲的隨機種子（預設值：0） | INT | 否 | 0 到 18446744073709551615 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 根據輸入提示詞生成的影片 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxTextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bdbd8f9defc4c626f07b36c1ba9859155fa90a2d7ef9a491c30dac4d003d39be`
