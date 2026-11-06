# VSR Decode

VSR Decode 會使用 RelayVSR Flash 解碼器，將來自 RelayVSR Conditioning 的關鍵影格潛在表示轉換回完整影片。解碼器會在你傳入的低品質影格經雙三次（bicubic）放大後的結果上疊加其細節，放大倍率為解碼器的 x2 或 x4。影格數保持不變。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `vae` | RelayVSR Flash 解碼器，需使用 Load VAE 載入：`relayvsr_flash_vae_x2_fp32.safetensors` 或 `relayvsr_flash_vae_x4_fp32.safetensors`。檔案的元資料會設定放大倍率，因此必須與模型相符。 | VAE | 是 | N/A |
| `samples` | 取樣器回傳的潛在表示，每個關鍵影格對應一個影格。 | LATENT | 是 | N/A |
| `images` | 提供給 RelayVSR Conditioning 的同一段低品質影片。 | IMAGE | 是 | N/A |
| `detail` | 在雙三次放大結果上保留多少解碼器細節：1 為完整模型輸出，0 為單純放大。（預設：1.0） | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `images` | 已還原每一影格的放大影片。 | IMAGE |

## 備註

- 將同一段低品質影片傳給這兩個節點。解碼器會逐影格讀取，因此長度或解析度不一致會產生錯誤或損壞的結果。
- 降低 `detail` 會使還原的細節變柔和，並讓輸出更接近單純的雙三次放大，這對雜訊很多的來源可能有幫助。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VSRDecode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `946ac04bc9f205fd6d1088554caaa16238086e570f212e747b166e3fb0d9b3c5`
