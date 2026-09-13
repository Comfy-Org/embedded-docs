# WanHuMo圖像轉影片

WanHuMoImageToVideo 節點會為 Wan HuMo 影片生成流程準備條件資料與空白 latent 影片。它可以將參考影像與音訊嵌入附加到正向與負向條件輸入，並根據請求的 `width`、`height`、`length` 與 `batch_size` 建立大小相符的零填充 latent。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正面提示詞` | 正向條件輸入，用於引導影片生成朝向期望內容。 | CONDITIONING | 是 | - |
| `負面提示詞` | 負向條件輸入，用於引導影片生成遠離不想要的內容。 | CONDITIONING | 是 | - |
| `VAE` | 用於將參考影像編碼至 latent 空間的 VAE 模型。 | VAE | 是 | - |
| `寬度` | 輸出影片影格的寬度（像素）。預設：832。 | INT | 是 | 16 to MAX_RESOLUTION, step 16 |
| `高度` | 輸出影片影格的高度（像素）。預設：480。 | INT | 是 | 16 to MAX_RESOLUTION, step 16 |
| `長度` | 生成的影片序列中的影格數。預設：97。 | INT | 是 | 1 to MAX_RESOLUTION, step 4 |
| `批次大小` | 同時生成的影片序列數量。預設：1。 | INT | 是 | 1 至 4096 |
| `音訊編碼器輸出` | 可選的音訊編碼資料，可根據音訊內容影響影片生成。 | AUDIOENCODEROUTPUT | 否 | - |
| `參考圖像` | 可選的參考影像，用於引導影片生成的風格與內容。僅使用批次中的第一張影像。 | IMAGE | 否 | - |

**注意：** 當提供參考影像時，批次中的第一張影像會使用雙線性插值放大至請求的 `width` 與 `height`，並以 VAE 編碼。該參考 latent 會附加到正向條件，而相同形狀的零填充 latent 會附加到負向條件。當提供 `audio_encoder_output` 時，音訊嵌入會進行插值並附加到正向條件，而零填充的音訊嵌入會附加到負向條件。若省略任一可選輸入，則會使用零填充的佔位張量：形狀為 `[batch_size, 16, 1, height // 8, width // 8]` 的零參考 latent，和/或形狀為 `[batch_size, latent_t + 1, 8, 5, 1280]` 的零音訊嵌入，其中 `latent_t = ((length - 1) // 4) + 1`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 已修改的正向條件，並納入參考影像和/或音訊嵌入。 | CONDITIONING |
| `negative` | 已修改的負向條件，並納入參考影像和/或音訊嵌入。 | CONDITIONING |
| `latent` | 影片序列的零初始化 latent 表示，大小依據 `width`、`height`、`length` 與 `batch_size` 決定。形狀：`[batch_size, 16, latent_t, height // 8, width // 8]`，其中 `latent_t = ((length - 1) // 4) + 1`。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
