# 潛空間應用操作 CFG

LatentApplyOperationCFG 節點透過套用潛在操作來修改模型中的條件引導過程。其運作方式是在無分類器引導（CFG）取樣過程中攔截條件輸出，並在潛在表示用於生成之前，對其套用指定的操作。當取樣器產生兩個條件輸出時，操作會套用於兩者之間的差異，然後將第二個輸出加回結果中。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 將套用 CFG 操作的模型 | MODEL | 是 | - |
| `operation` | 在 CFG 取樣過程中套用的潛在操作 | LATENT_OPERATION | 是 | - |

注意：此節點標記為實驗性。在 CFG 取樣過程中，操作會套用於模型的條件輸出。當存在兩個條件輸出時，操作會套用於第一個和第二個輸出之間的差異，並將第二個輸出加回。當僅存在一個條件輸出時，操作會直接套用於該輸出。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已在其取樣過程套用 CFG 操作的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
