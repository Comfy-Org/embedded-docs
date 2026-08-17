# PiD 條件設定

將潛在影像（latent image）與衰減 sigma 值附加至 CONDITIONING 資料。此功能用於 PiD（Pixel-in-Detail）解碼或放大，可讓您控制在處理前潛在影像的衰減程度。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 要附加潛在影像與衰減 sigma 值的 conditioning 資料。 | CONDITIONING | 是 | - |
| `latent` | 要附加至 conditioning 的潛在影像（來自 VAEEncode 或 KSampler）。 | LATENT | 是 | - |
| `latent_format` | 潛在影像的格式。Flux1（16 通道）與 Flux2（128 通道）潛在影像會根據「flux」下的通道維度自動偵測。對於 SD3（16 通道）、SDXL（4 通道）或 QwenImage（16 通道），請手動選取（預設值：「flux」）。 | COMBO | 是 | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | 0 = 乾淨的潛在影像。提高此值可對損壞的潛在影像輸出進行去噪（預設值：0.0）。 | FLOAT | 是 | 0.0 至 1.0（步進：0.01） |

注意：當 `latent_format` 為「flux」時，節點會根據通道維度自動偵測潛在影像是 Flux1（16 通道）或 Flux2（128 通道）。如果處理後的潛在影像具有 5 個維度，則僅使用最後一個維度的第一個切片。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `CONDITIONING` | 原始 conditioning 資料，已附加潛在影像與衰減 sigma 值。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
