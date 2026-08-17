# 空白 HunyuanVideo 1.5 Latent

此節點建立一個專為 HunyuanVideo 1.5 模型格式化使用的空潛在張量。它會配置一個零張量，使其具有正確的通道數及符合模型潛在空間的空間維度，為影片生成提供空白起點。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `width` | 影片影格的寬度（像素）。 | INT | 是 | - |
| `height` | 影片影格的高度（像素）。 | INT | 是 | - |
| `length` | 影片序列中的影格數。 | INT | 是 | - |
| `batch_size` | 批次中要生成的影片樣本數（預設值：1）。 | INT | 否 | - |

**注意：** 生成的潛在張量之空間維度，是將輸入的 `width` 和 `height` 除以 16 來計算。時間維度（影格數）的計算方式為 `((length - 1) // 4) + 1`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `samples` | 一個空潛在張量，其維度適合 HunyuanVideo 1.5 模型使用。該張量的形狀為 `[batch_size, 32, frames, height//16, width//16]`。輸出還包含一個數值為 16 的 `downscale_ratio_spacial`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ce7ec75e8433c778d175a3e2ea260a4397aa5507428908b9a32f50fbe9e184c6`
