# 潛空間應用操作 CFG

LatentApplyOperationCFG 節點會在模型取樣流程的無分類器引導（CFG）步驟中套用潛在操作。它會攔截在 CFG 之前產生的條件（conditioning）輸出，將連接的操作套用至潛在值，並傳回具有此修改後取樣行為的模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 將套用 CFG 操作的模型 | MODEL | 是 | - |
| `operation` | 在 CFG 取樣流程中要套用的潛在操作 | LATENT_OPERATION | 是 | - |

注意：此節點標記為實驗性。在 CFG 取樣流程中，操作會套用至模型的條件輸出。當存在兩個條件輸出時，操作會套用至第一個與第二個輸出之間的差異，並將第二個輸出加回結果。當只有一個條件輸出時，操作會直接套用至該輸出。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已將 CFG 操作套用至其取樣流程的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
