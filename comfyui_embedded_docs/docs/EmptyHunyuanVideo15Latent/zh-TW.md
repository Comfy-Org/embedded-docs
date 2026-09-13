# 空白 HunyuanVideo 1.5 Latent

此節點會建立一個專為 HunyuanVideo 1.5 模型使用而格式化的空潛在張量。它透過配置具有正確通道數與模型潛在空間空間維度的全零張量，為影片生成產生空白起點。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 影片影格的寬度，以像素為單位。 | INT | 是 | - |
| `高度` | 影片影格的高度，以像素為單位。 | INT | 是 | - |
| `長度` | 影片序列中的影格數。 | INT | 是 | - |
| `批次大小` | 要在一個批次中生成的影片樣本數量（預設：1）。 | INT | 否 | - |

**注意：** 產生的潛在張量其空間維度是將輸入 `width` 和 `height` 除以 16 計算得出（此節點使用 16 的空間縮放因子，而非 8）。時間維度（影格數）的計算方式為 `((length - 1) // 4) + 1`。這些計算使用整數除法，因此 `width` 和 `height` 應為 16 的倍數，以避免截斷。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `samples` | 一個適用於 HunyuanVideo 1.5 模型的空潛在張量。此張量的形狀為 `[batch_size, 32, ((length - 1) // 4) + 1, height // 16, width // 16]`。輸出也包含 `downscale_ratio_spacial`，其值為 16。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ce7ec75e8433c778d175a3e2ea260a4397aa5507428908b9a32f50fbe9e184c6`
