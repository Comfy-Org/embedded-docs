# 潛空間應用操作 CFG

## 概述

LatentApplyOperationCFG 節點會套用潛在操作，以修改模型中的條件引導（conditioning guidance）過程。其運作方式是攔截無分類器引導（CFG）取樣過程中的條件輸出，並在潛在表示用於生成之前，對其套用指定的操作。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 將套用 CFG 操作的模型 | MODEL | 是 | - |
| `operation` | 在 CFG 取樣過程中套用的潛在操作 | LATENT_OPERATION | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已將 CFG 操作套用至其取樣過程的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9fbcc9183abf89bb93e55263bb655e931549360c05a561f7dacae8723db62e52`
