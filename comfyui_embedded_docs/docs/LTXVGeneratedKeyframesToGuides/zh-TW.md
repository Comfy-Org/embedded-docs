# LTXV 將生成的關鍵影格轉為引導

LTXV Generated Keyframes to Guides 節點會將較早階段產生的關鍵影格釘選為後續畫布上的凍結圖像引導。它會將關鍵影格解碼為獨立影格，必要時調整其大小，並以雜訊遮罩 0 寫入，使其不會再次被去雜訊。經過時間軸放大後，已記錄的索引會從產生它們的畫布縮放到此畫布；使用 `override_frame_indices` 可明確設定位置。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `positive` | 要加入關鍵影格引導的正向條件。 | CONDITIONING | 是 | |
| `negative` | 要加入關鍵影格引導的負向條件。 | CONDITIONING | 是 | |
| `vae` | 如果需要調整大小，用於解碼關鍵影格的 VAE。 | VAE | 是 | |
| `latent` | 要加入引導的目標影片 latent，例如經時間軸放大的 latent。 | LATENT | 是 | |
| `keyframes` | LTXV Separate Generated Keyframes 的 `keyframes` 輸出，其中帶有每個關鍵影格產生時的像素影格索引。 | LATENT | 是 | |
| `strength` | 引導強度。1.0 是強制釘選；較低的值會使其放寬。（預設：1.0） | FLOAT | 是 | 0.0 - 10.0 （步進值：0.01） |
| `override_frame_indices` | 選填 — 改為釘選在這些像素影格，而非已記錄（或自動縮放）的位置。為每個關鍵影格提供一個索引。留空以重複使用已記錄的位置，或在目標畫布長度不同時（例如時間軸 x2 後）縮放它們。（預設：""） | STRING | 否 | |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `positive` | 已將關鍵影格釘選為圖像引導的正向條件。 | CONDITIONING |
| `negative` | 已將關鍵影格釘選為圖像引導的負向條件。 | CONDITIONING |
| `latent` | 已加入關鍵影格作為凍結引導的目標影片 latent。 | LATENT |

## 備註

- `keyframes` 輸入必須連接到 LTXV Separate Generated Keyframes 的 `keyframes` 輸出。如果 latent 未帶有產生的關鍵影格位置，節點會引發錯誤。
- `positive` 和 `negative` 條件輸入必須來自 LTXV Separate Generated Keyframes 的 `positive` 和 `negative` 輸出。如果正向條件仍帶有產生的關鍵影格，節點會引發錯誤。
- `latent` 輸入必須是純影片 latent（5D 張量）。必須在使用 Concat AV Latent 合併影片與音訊 latent 之前加入引導。
- 僅支援批次大小為 1。每個引導都是從一張圖像編碼而來，因此無法在批次元素之間有所不同。
- `keyframes` latent 中的關鍵影格數量必須與已記錄位置的數量相符；否則會引發錯誤。
- 如果 `override_frame_indices` 留空，則會使用已記錄的位置。如果目標畫布的影格數與產生關鍵影格時的畫布不同，已記錄的索引會自動縮放。
- 如果提供了 `override_frame_indices`，它必須為每個關鍵影格包含一個整數索引，並以逗號或空格分隔。索引必須唯一，且介於 1 與（目標 latent 中的像素影格數 - 1）之間。否則會引發錯誤。
- 如果任何最終關鍵影格索引大於或等於目標 latent 中的像素影格數，節點會引發錯誤。當目標在關鍵影格產生後經過時間軸調整大小時，可能會發生這種情況。
- `strength` 參數的最小值為 0.0，最大值為 10.0。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVGeneratedKeyframesToGuides/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b5dbf302fad5a7ffd3522d468d1a51b993145d90277592058315499f08e17e7b`
