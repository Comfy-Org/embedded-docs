> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/zh-TW.md)

此節點根據解析度組織潛在影像列表及其對應的條件化資料。它將具有相同高度和寬度的項目分組，為每個獨特的解析度建立單獨的批次。此過程有助於準備資料以進行高效訓練，因為它允許模型同時處理多個相同尺寸的項目。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | 是 | N/A | 要按解析度分桶的潛在字典列表。 |
| `conditioning` | CONDITIONING | 是 | N/A | 條件化列表的列表（必須與 `latents` 長度相符）。 |

**注意：** `latents` 列表中的項目數量必須與 `conditioning` 列表中的項目數量完全相符。每個潛在字典可以包含一批樣本，而對應的條件化列表必須包含與該批次相符數量的條件化項目。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `conditioning` | LATENT | 批次化潛在字典的列表，每個解析度桶一個。 |
| `conditioning` | CONDITIONING | 條件化列表的列表，每個解析度桶一個。 |

---
**Source fingerprint (SHA-256):** `2858de5f0827812002ca72ba5d7ce56411d1ef97e9a12a65fc4bea193a1a0ec0`
