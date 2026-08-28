# PiD 條件設定

將潛在圖像與退化 sigma 值附加到 CONDITIONING 資料上。此功能用於 PiD（Pixel-in-Detail）解碼或放大，讓您能控制潛在變量在處理前的退化程度。

## 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `正向` | 要附加潛在圖像與退化 sigma 的 CONDITIONING 資料。 | CONDITIONING | 是 | - |
| `latent` | 要附加到 conditioning 的潛在圖像（來自 VAEEncode 或 KSampler）。 | LATENT | 是 | - |
| `latent 格式` | 潛在圖像的格式。Flux1（16 通道）與 Flux2（128 通道）潛在圖像會依「flux」下的通道維度自動偵測。對於 SD3（16 通道）、SDXL（4 通道）或 QwenImage（16 通道），請手動選擇（預設值：「flux」）。 | COMBO | 是 | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | 要套用的退化程度。0 表示乾淨的潛在圖像。提高此值可對損壞的潛在輸出進行去噪（預設值：0.0）。 | FLOAT | 是 | 0.0 至 1.0 (step: 0.01) |

注意：當 `latent_format` 設定為 `"flux"` 時，節點會依通道維度自動偵測潛在類型：128 通道視為 Flux2 潛在圖像，16 通道視為 Flux1 潛在圖像。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `CONDITIONING` | 原始 CONDITIONING 資料，附加了潛在圖像與退化 sigma 值。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
