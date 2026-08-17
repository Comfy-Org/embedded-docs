# 解析度分桶

此節點會根據解析度來整理 `latents` 清單及其對應的 `conditioning` 資料。它會將具有相同高度與寬度的項目分組在一起，為每個唯一的解析度建立獨立的批次。此過程有助於準備資料以進行高效訓練，因為它允許模型同時處理多個相同尺寸的項目。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `latents` | 按解析度分桶（bucket）的潛在變數字典清單。 | LATENT | 是 | N/A |
| `conditioning` | 條件資料清單的清單（長度必須與 `latents` 相符）。 | CONDITIONING | 是 | N/A |

**注意：** `latents` 清單中的項目數量必須與 `conditioning` 清單中的項目數量完全相符。每個潛在變數字典可包含一批樣本，對應的 `conditioning` 清單必須包含與該批次相匹配數量的條件項目。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `latents` | 批次化後的潛在變數字典清單，每個解析度分桶各一個。 | LATENT |
| `conditioning` | 條件清單的清單，每個解析度分桶各一個。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/zh-TW.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
