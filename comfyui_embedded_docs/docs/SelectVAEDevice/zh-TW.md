# 選擇 VAE 裝置

## 概述

此節點允許您手動選擇 VAE 模型應放置在哪個 GPU 裝置上。預設情況下，VAE 會放置在模型載入器所指定的裝置上，但您可以將其固定到特定的 GPU（例如：`gpu:0`、`gpu:1`）。如果所選裝置在您的機器上不可用，此節點將直接傳遞 VAE 而不做任何更改，並記錄一則訊息，而非導致錯誤。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `vae` | 要指派到特定裝置的 VAE 模型。 | VAE | 是 |  |
| `裝置` | VAE 的目標裝置。`"default"` 會恢復載入器所指定的裝置。`"gpu:N"` 會將 VAE 固定到第 N 個可用的 GPU。CPU 不是支援的選項，如果提供將會被忽略。（預設值：`"default"`） | COMBO | 是 | `"default"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `vae` | 已指派到所選裝置的 VAE 模型。如果請求的裝置不可用或無效，則 VAE 會直接傳遞而不做任何更改。 | VAE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectVAEDevice/zh-TW.md)

---
**Source fingerprint (SHA-256):** `011154043fc02f930b0074de656bb24baf4dfe74bcfd2e89ea76284f0a5b7d8e`
