# Vidu 文字轉影片節點

Vidu 文字轉影片生成節點可根據文字描述建立影片。它使用 Vidu 影片生成模型，將您的文字提示轉換為影片內容，並可自訂持續時間、長寬比和視覺風格。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 模型名稱 | COMBO | 是 | `viduq1` |
| `提示詞` | 用於影片生成的文字描述 | STRING | 是 | - |
| `持續時間` | 輸出影片的持續時間（秒）（預設值：5） | INT | 否 | 5-5 |
| `種子值` | 影片生成的隨機種子（0 表示隨機）（預設值：0） | INT | 否 | 0-2147483647 |
| `長寬比` | 輸出影片的長寬比 | COMBO | 否 | `16:9`<br>`9:16`<br>`1:1` |
| `解析度` | 支援的解析度可能因模型和持續時間而異 | COMBO | 否 | `1080p` |
| `移動幅度` | 畫面中物體的移動幅度 | COMBO | 否 | `auto`<br>`small`<br>`medium`<br>`large` |

**注意：** `prompt` 欄位為必填，且不可為空。`duration` 參數目前固定為 5 秒。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 根據文字提示生成的影片 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0d331d3eab8a4af9c90831f3f8fd8ae34aa0c393142cb6f89404edc94024d95f`
