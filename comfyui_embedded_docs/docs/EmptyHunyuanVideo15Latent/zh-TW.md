# 空白 HunyuanVideo 1.5 Latent

此節點會建立一個空的潛在張量，其格式專為 HunyuanVideo 1.5 模型所設計。它會配置一個包含正確通道數與空間維度的零張量，為影片生成提供空白的起始點，以符合該模型的潛在空間。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 影片幀的寬度（像素）。 | INT | 是 | - |
| `高度` | 影片幀的高度（像素）。 | INT | 是 | - |
| `長度` | 影片序列中的幀數。 | INT | 是 | - |
| `批次大小` | 批次中要生成的影片樣本數量（預設值：1）。 | INT | 否 | - |

**注意：** 生成的潛在張量之空間維度是將輸入的 `width` 和 `height` 除以 16 後計算而得。時間維度（幀數）的計算方式為 `((length - 1) // 4) + 1`。這些計算使用整數除法，因此 `width` 和 `height` 應為 16 的倍數，以避免截斷。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `samples` | 一個空的潛在張量，其維度適合 HunyuanVideo 1.5 模型。張量的形狀為 `[batch_size, 32, frames, height//16, width//16]`。輸出同時包含一個值為 16 的 `downscale_ratio_spacial`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ce7ec75e8433c778d175a3e2ea260a4397aa5507428908b9a32f50fbe9e184c6`
