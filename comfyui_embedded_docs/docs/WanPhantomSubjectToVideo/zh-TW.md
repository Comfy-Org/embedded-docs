# 萬幻影主體轉影片

The WanPhantomSubjectToVideo 節點透過處理 conditioning 輸入與可選的參考圖像來生成影片內容。它會建立用於影片生成的 latent 表示，並在提供輸入圖像時納入視覺引導。此節點會為 Wan 影片模型準備帶有時間維度串接的 conditioning 資料，並輸出修改後的 conditioning 以及生成的 latent 影片資料。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 用於引導影片生成的正向 conditioning 輸入 | CONDITIONING | 是 | - |
| `negative` | 用於避免特定特徵的負向 conditioning 輸入 | CONDITIONING | 是 | - |
| `vae` | 用於在提供圖像時進行編碼的 VAE 模型 | VAE | 是 | - |
| `width` | 輸出影片的寬度（像素，預設值：832，必須可被 16 整除） | INT | 是 | 16 至 MAX_RESOLUTION |
| `height` | 輸出影片的高度（像素，預設值：480，必須可被 16 整除） | INT | 是 | 16 至 MAX_RESOLUTION |
| `length` | 生成影片的幀數（預設值：81，必須可被 4 整除） | INT | 是 | 1 至 MAX_RESOLUTION |
| `batch_size` | 同時生成的影片數量（預設值：1） | INT | 是 | 1 至 4096 |
| `images` | 用於時間維度 conditioning 的可選參考圖像 | IMAGE | 否 | - |

**注意：** 當提供 `images` 時，這些圖像會自動放大以符合指定的 `width` 和 `height`，且僅使用前 `length` 幀進行處理。每張圖像在由 VAE 編碼前，會先被縮減為前 3 個色彩通道。當未提供 `images` 時，conditioning 輸入會原樣傳遞。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 在提供圖像時，經時間維度串接修改後的正向 conditioning | CONDITIONING |
| `negative_text` | 在提供圖像時，經時間維度串接修改後的負向 conditioning | CONDITIONING |
| `negative_img_text` | 在提供圖像時，帶有歸零時間維度串接的負向 conditioning | CONDITIONING |
| `latent` | 零填充的 latent 影片表示，具有 16 個通道、時間維度為 ((length - 1) // 4) + 1、空間維度為 height // 8 和 width // 8 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
