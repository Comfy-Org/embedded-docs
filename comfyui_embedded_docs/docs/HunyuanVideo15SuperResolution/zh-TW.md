# HunyuanVideo15SuperResolution

HunyuanVideo15SuperResolution 節點為影片超解析度流程準備條件資料。它接受影片的潛在表示，並可選擇性地接受起始影像，將它們與雜訊增強值及選用的 CLIP 視覺資料打包成模型可用於產生更高解析度輸出的格式。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 要透過串接的潛在表示與雜訊增強資料修改的正向條件輸入。 | CONDITIONING | 是 | N/A |
| `negative` | 要透過串接的潛在表示與雜訊增強資料修改的負向條件輸入。 | CONDITIONING | 是 | N/A |
| `vae` | 用於對選用的 `start_image` 進行編碼的 VAE。若提供了 `start_image`，則為必填。 | VAE | 否 | N/A |
| `start_image` | 用於引導超解析度流程的選用起始影像。若提供，會先放大，再用 `vae` 編碼，並置於條件潛在表示的開頭。 | IMAGE | 否 | N/A |
| `clip_vision_output` | 選用的 CLIP 視覺嵌入。提供時，會同時加入正向與負向條件。 | CLIP_VISION_OUTPUT | 否 | N/A |
| `latent` | 要納入條件中的潛在視訊表示。 | LATENT | 是 | N/A |
| `noise_augmentation` | 套用於條件的雜訊增強強度（預設值：0.70）。這是一個進階參數。 | FLOAT | 是 | 0.0 - 1.0 (step 0.01) |

**注意：** 若提供了 `start_image`，也必須連接 `vae` 才能進行編碼。`start_image` 會自動放大以符合輸入 `latent` 所隱含的尺寸，且 VAE 只會使用其前三個色彩通道（RGB）。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 修改後的正向條件，現在包含串接的潛在表示、雜訊增強，以及選用的 CLIP 視覺資料。 | CONDITIONING |
| `negative` | 修改後的負向條件，現在包含串接的潛在表示、雜訊增強，以及選用的 CLIP 視覺資料。 | CONDITIONING |
| `latent` | 輸入的潛在表示，原封不動地傳遞出去。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
