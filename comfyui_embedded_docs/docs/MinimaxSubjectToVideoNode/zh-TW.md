> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/zh-TW.md)

此節點使用 MiniMax 的 API，根據圖像、提示文字以及可選參數同步生成影片。該節點透過輸入主體圖像和文字描述，利用 MiniMax 的影片生成服務來創建影片。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `subject` | IMAGE | 是 | - | 用於影片生成參考的主體圖像 |
| `prompt_text` | STRING | 是 | - | 引導影片生成的文字提示（預設值：空字串） |
| `model` | COMBO | 否 | "S2V-01"<br> | 用於影片生成的模型（預設值："S2V-01"） |
| `seed` | INT | 否 | 0 到 18446744073709551615 | 用於創建雜訊的隨機種子（預設值：0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 根據輸入的主體圖像和提示生成的影片 |