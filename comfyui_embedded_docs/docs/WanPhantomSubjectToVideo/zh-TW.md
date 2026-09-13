# 萬幻影主體轉影片

WanPhantomSubjectToVideo 節點會準備條件資料與潛在資料，以供 Wan 影片生成使用。它會根據請求的 `width`、`height`、`length` 與 `batch_size` 建立空白的潛在影片；當提供參考影像時，會使用 VAE 對其進行編碼，並將其作為時間維度的視覺引導加入條件中。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正面提示` | 用於引導影片生成的正向條件輸入 | CONDITIONING | 是 | - |
| `負面提示` | 用於避免特定特徵的負向條件輸入 | CONDITIONING | 是 | - |
| `VAE` | 當提供參考影像時，用於編碼這些參考影像的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片寬度，單位為像素（預設：832） | INT | 是 | 16 to MAX_RESOLUTION （步進值：16） |
| `高度` | 輸出影片高度，單位為像素（預設：480） | INT | 是 | 16 to MAX_RESOLUTION （步進值：16） |
| `長度` | 生成影片中的影格數（預設：81） | INT | 是 | 1 to MAX_RESOLUTION （步進值：4） |
| `批次大小` | 同時生成的影片數量（預設：1） | INT | 是 | 1 至 4096 |
| `圖片` | 可選的參考影像，用作時間維度的視覺引導 | IMAGE | 否 | - |

**注意：** 當提供 `images` 時，它們會自動放大以符合指定的 `width` 與 `height`，且僅會使用前 `length` 張影像進行處理。每張影像會使用 `vae` 編碼，並沿時間維度串接，且僅使用每張影像的 RGB 通道。未提供 `images` 時，三個條件輸出都會原樣返回輸入的條件。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 當提供影像時，為正向條件，並會將編碼後的參考影像沿時間維度串接；否則會原樣返回輸入的 `positive` | CONDITIONING |
| `negative_text` | 當提供影像時，為負向條件，並會將編碼後的參考影像沿時間維度串接；否則會原樣返回輸入的 `negative` | CONDITIONING |
| `negative_img_text` | 當提供影像時，為帶有歸零時間維度串接的負向條件；否則會原樣返回輸入的 `negative` | CONDITIONING |
| `latent` | 以零填充、具有 16 個通道的潛在影片張量；其影格數衍生自 `length`，空間維度則衍生自 `height` 與 `width` | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
