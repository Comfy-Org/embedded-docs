# 潛空間應用操作

LatentApplyOperation 節點將指定的操作套用到潛在樣本上。它接收潛在資料和一個操作作為輸入，複製輸入的潛在樣本，將操作套用到潛在張量上，並回傳修改後的潛在資料。此節點可讓您在工作流程中轉換或操控潛在表示。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `samples` | 要由操作處理的潛在樣本 | LATENT | 是 | - |
| `operation` | 要套用到潛在樣本的操作 | LATENT_OPERATION | 是 | - |

注意：此節點標記為實驗性。操作會套用於潛在結構中 `samples` 鍵所儲存的潛在張量。輸入的潛在樣本會在套用操作前複製，因此原始輸入的潛在資料不會被修改。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
| --- | --- | --- |
| `output` | 套用操作後修改的潛在樣本 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cba55d019793fde8dcc0d4aeb4eb6020b6149f523c6bffc65d73c533aa2e2c6c`
