> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/zh-TW.md)

LTXVConcatAVLatent 節點將影片潛在表示與音訊潛在表示合併為單一、串接的潛在輸出。它會合併兩個輸入中的 `samples` 張量，如果存在的話，也會合併它們的 `noise_mask` 張量，為後續在影片生成流程中的處理做好準備。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `video_latent` | LATENT | 是 | | 影片資料的潛在表示。 |
| `audio_latent` | LATENT | 是 | | 音訊資料的潛在表示。 |

**注意：** 來自 `video_latent` 和 `audio_latent` 輸入的 `samples` 張量會被串接。如果任一輸入包含 `noise_mask`，則會使用該遮罩；如果缺少其中一個，則會為其建立一個全為 1 的遮罩（形狀與對應的 `samples` 相同）。接著，產生的遮罩也會被串接起來。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `latent` | LATENT | 一個單一的潛在字典，包含來自影片和音訊輸入的串接 `samples`，以及（如果適用的話）串接的 `noise_mask`。 |

---
**Source fingerprint (SHA-256):** `322d6870f110fb1ef8b472cb49649cc9fff7865f4c7a83fbfd536f1fdfd694f8`
