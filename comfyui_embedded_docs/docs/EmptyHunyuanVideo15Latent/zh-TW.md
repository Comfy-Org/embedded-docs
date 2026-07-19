# 空白 HunyuanVideo 1.5 Latent

此節點會建立一個專門為 HunyuanVideo 1.5 模型格式化的空潛在張量。它透過分配一個具有正確通道數和空間維度的零值張量，為影片生成產生一個空白起點，以符合模型的潛在空間要求。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 影片幀的寬度（以像素為單位）。 | INT | 是 | - |
| `高度` | 影片幀的高度（以像素為單位）。 | INT | 是 | - |
| `長度` | 影片序列中的幀數。 | INT | 是 | - |
| `批次大小` | 每個批次中生成的影片樣本數量（預設值：1）。 | INT | 否 | - |

**注意：** 生成的潛在張量的空間維度是透過將輸入的 `width` 和 `height` 除以 16 來計算。時間維度（幀數）則計算為 `((length - 1) // 4) + 1`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `samples` | 一個空的潛在張量，其維度適用於 HunyuanVideo 1.5 模型。該張量的形狀為 `[batch_size, 32, frames, height//16, width//16]`。輸出還包含一個值為 16 的 `downscale_ratio_spacial`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `eebc131adfe63f6bc8367f2a96b3ac7f3f3223c5b1fb308eda3ec09c94fff2ee`
