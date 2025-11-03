> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetModelHooksOnCond/zh-TW.md)

此節點將自定義掛鉤附加到條件資料上，讓您能夠在模型執行期間攔截並修改條件處理過程。它接收一組掛鉤並將其應用於提供的條件資料，從而實現對文字生成圖像工作流程的高級自定義。附加了掛鉤的修改後條件資料將返回供後續處理步驟使用。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | 是 | - | 將要附加掛鉤的條件資料 |
| `hooks` | HOOKS | 是 | - | 將應用於條件資料的掛鉤定義 |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | 附帶掛鉤的修改後條件資料 |