> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxTextToVideoNode/zh-TW.md)

{heading_overview}

基於提示文字和可選參數，使用 MiniMax 的 API 同步生成影片。此節點透過連接 MiniMax 的文字轉影片服務，從文字描述建立影片內容。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `提示文字` | STRING | 是 | - | 用於引導影片生成的文字提示 |
| `模型` | COMBO | 否 | "T2V-01"<br>"T2V-01-Director" | 用於影片生成的模型（預設："T2V-01"） |
| `種子` | INT | 否 | 0 到 18446744073709551615 | 用於建立雜訊的隨機種子（預設：0） |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 基於輸入提示生成的影片 |