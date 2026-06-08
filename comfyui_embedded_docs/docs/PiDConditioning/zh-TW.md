## 概述

將潛在影像與退化 sigma 值附加到 CONDITIONING 資料中。此功能用於 PiD（像素細節）解碼或放大，讓您能夠控制潛在影像在處理前的退化程度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 要附加潛在影像與退化 sigma 值的條件資料。 | CONDITIONING | 是 | - |
| `latent` | 要附加到條件資料中的潛在影像（來自 VAEEncode 或 KSampler）。 | LATENT | 是 | - |
| `latent 格式` | 潛在影像的格式。Flux1 與 Flux2 的潛在影像會根據通道維度自動偵測。SD3 則需手動選擇（預設值："flux"）。 | COMBO | 是 | `"flux"`<br>`"sd3"` |
| `degrade_sigma` | 要套用的退化程度。0 表示乾淨的潛在影像。增加此數值可對受損的潛在輸出進行去噪處理（預設值：0.0）。 | FLOAT | 是 | 0.0 至 1.0（步進：0.01） |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 附加了潛在影像與退化 sigma 值的原始條件資料。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7c8de543629c2299fc2c1e035e433dfc249af594773a77e65c69dde67eb104d7`
