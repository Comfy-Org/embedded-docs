# 解析度分桶

此節點會根據解析度來整理潛在影像清單及其對應的條件化資料。它會將具有相同高度與寬度的項目分組，為每個獨特的解析度建立獨立的批次。此過程有助於準備高效率的訓練資料，因為它允許模型同時處理多個相同尺寸的項目。

## 輸入

| 參數 | 說明 | 資料型態 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `latents` | 依解析度進行分組的潛在字典清單。 | LATENT | 是 | N/A |
| `conditioning` | 條件化清單的清單（必須與 `latents` 的長度相符）。 | CONDITIONING | 是 | N/A |

**注意：** `latents` 清單中的項目數量必須與 `conditioning` 清單中的項目數量完全相符。如果數量不符，節點會引發錯誤。每個潛在字典可以包含一批樣本，而對應的條件化清單必須包含與該批次相符數量的條件化項目。潛在樣本的形狀可能是圖像的 (B, C, H, W) 或影片的 (B, T, C, H, W)；節點僅依高度和寬度進行分組。

## 輸出

| 輸出名稱 | 說明 | 資料型態 |
| --- | --- | --- |
| `latents` | 批次化的潛在字典清單，每個解析度桶一個。 | LATENT |
| `conditioning` | 條件化清單的清單，每個解析度桶一個。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/zh-TW.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
