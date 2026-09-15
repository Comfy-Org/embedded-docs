# PiD 條件設定

將 `latent` 與 `degrade_sigma` 值附加到 CONDITIONING，使其可用於 PiD 解碼或放大。這讓你能控制 latent 在處理前被降質的程度。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `正向` | 要附加 `latent` 與 `degrade_sigma` 的 CONDITIONING 資料。 | CONDITIONING | 是 | - |
| `latent` | 要附加到 CONDITIONING 的 latent（來自 VAEEncode 或 KSampler）。 | LATENT | 是 | - |
| `latent 格式` | latent 的格式。Flux1（16 通道）與 Flux2（128 通道）的 latent 會在 `"flux"` 下由通道維度自動偵測。若為 SD3（16 通道）、SDXL（4 通道）或 QwenImage（16 通道），請手動選擇（預設值：`"flux"`）。 | COMBO | 是 | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | 要套用的降質程度。0 代表乾淨的 latent。提高此值可對損壞的 latent 輸出進行去雜訊（預設值：0.0）。 | FLOAT | 是 | 0.0 至 1.0 （步進值：0.01） |

注意：當 `latent_format` 設為 `"flux"` 時，節點會自動從通道維度偵測 latent 類型：128 個通道視為 Flux2 latent，而 16 個通道視為 Flux1 latent。

注意：不支援的 `latent_format` 值會引發錯誤，但節點已處理所有可用的選項。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `CONDITIONING` | 已附加 latent 與 degrade sigma 值的原始 CONDITIONING 資料。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
