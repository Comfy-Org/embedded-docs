> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetModelHooksOnCond/zh-TW.md)

此節點將自訂鉤子附加到條件資料上，讓您能夠在模型執行期間攔截並修改條件處理流程。它接收一組鉤子，並將其應用於提供的條件資料，從而實現對文字到影像生成工作流程的高階自訂。附加鉤子後的修改條件資料會被回傳，以供後續處理步驟使用。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | 是 | - | 將附加鉤子的條件資料 |
| `hooks` | HOOKS | 是 | - | 將應用於條件資料的鉤子定義 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | 附加鉤子後的修改條件資料 |

---
**Source fingerprint (SHA-256):** `a6e63a3a4d94d1b66a82d449af5ae001e1fc4a04f0f81d9fb5c4f8c13e5bdf8b`
