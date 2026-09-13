# SD_4XUpscale_Conditioning

SD_4XUpscale_Conditioning 節點會準備 conditioning 資料，以便使用擴散模型放大影像。它會依所選比例縮放輸入影像，加入可選的雜訊增強，並傳回修改後的正向與負向 conditioning，以及對應放大尺寸的空 latent。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 要放大的輸入影像。 | IMAGE | 是 | - |
| `正向` | 正向 conditioning 資料，可引導生成朝向想要的內容。 | CONDITIONING | 是 | - |
| `負向` | 負向 conditioning 資料，可引導生成遠離不想要的內容。 | CONDITIONING | 是 | - |
| `縮放比例` | 準備放大後的 conditioning 與 latent 時，套用於輸入影像尺寸的乘數（預設值：4.0）。 | FLOAT | 是 | 0.0 - 10.0 （步進值：0.01） |
| `雜訊增強` | 在放大過程中加入的雜訊量（預設值：0.0）。 | FLOAT | 是 | 0.0 - 1.0 （步進值：0.001） |

注意：`noise_augmentation` 是進階參數，會顯示在節點介面的「Advanced」切換項下。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 已套用縮放後影像資料與雜訊增強設定的修改後正向 conditioning。 | CONDITIONING |
| `negative` | 已套用縮放後影像資料與雜訊增強設定的修改後負向 conditioning。 | CONDITIONING |
| `latent` | 符合放大後尺寸的空 latent 表示。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
