# 潛空間應用操作

LatentApplyOperation 節點會對潛在樣本套用指定的操作。它接收潛在資料與操作作為輸入，使用提供的操作處理潛在樣本，並回傳修改後的潛在資料。此節點可讓您在工作流程中轉換或操作潛在表示。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `樣本` | 要由操作處理的潛在樣本 | LATENT | 是 | - |
| `操作` | 要套用至潛在樣本的操作 | LATENT_OPERATION | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 套用操作後修改的潛在樣本 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/zh-TW.md)

---
**Source fingerprint (SHA-256):** `77147b480fe8cb48eb26a31f6f0c7bc038e07d26e628ebe361861394946d8678`
