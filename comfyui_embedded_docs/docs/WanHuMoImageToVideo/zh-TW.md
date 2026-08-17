# WanHuMo圖像轉影片

WanHuMoImageToVideo 節點為影像轉影片生成準備條件資料與潛在空間。它會建立空的潛在影片張量，可選擇性地使用 VAE 編碼參考影像，並可選擇性地將音訊編碼器輸出轉換為影片時間對齊的條件。此節點輸出正向與負向條件流，以及可供後續影片取樣使用的潛在張量。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 正向條件輸入，用於引導影片生成朝向所需的內容。 | CONDITIONING | 是 | - |
| `negative` | 負向條件輸入，用於使影片生成避開不需要的內容。 | CONDITIONING | 是 | - |
| `vae` | 用於將參考影像編碼至潛在空間的 VAE 模型。 | VAE | 是 | - |
| `width` | 輸出影片影格的寬度（像素，預設值：832；必須可被 16 整除）。 | INT | 是 | 16 to MAX_RESOLUTION (step 16) |
| `height` | 輸出影片影格的高度（像素，預設值：480；必須可被 16 整除）。 | INT | 是 | 16 to MAX_RESOLUTION (step 16) |
| `length` | 生成的影片序列中的影格數量（預設值：97；必須滿足 `(length - 1)` 可被 4 整除）。 | INT | 是 | 1 to MAX_RESOLUTION (step 4) |
| `batch_size` | 同時生成的影片序列數量（預設值：1）。 | INT | 是 | 1 to 4096 |
| `audio_encoder_output` | 可選的音訊編碼器輸出，用於根據音訊內容影響影片生成。 | AUDIO_ENCODER_OUTPUT | 否 | - |
| `ref_image` | 可選的參考影像，用於引導影片生成的風格與內容。 | IMAGE | 否 | - |

**注意：** 當提供 `ref_image` 時，它會調整為 `width` x `height` 的大小，使用 `vae` 編碼，並作為參考潛在變數添加到正向與負向條件中。當未提供參考影像時，會使用零參考潛在變數。當提供 `audio_encoder_output` 時，其音訊嵌入會經過處理並作為音訊嵌入添加到兩條條件流中；否則使用零音訊嵌入。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 已加入參考潛在變數與音訊嵌入資訊的正向條件。 | CONDITIONING |
| `negative` | 已加入參考潛在變數與音訊嵌入資訊的負向條件。 | CONDITIONING |
| `latent` | 表示影片序列的潛在張量，根據 `batch_size`、`length`、`height` 和 `width` 初始化為零。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
