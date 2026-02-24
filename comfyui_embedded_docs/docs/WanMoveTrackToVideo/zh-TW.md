> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/zh-TW.md)

WanMoveTrackToVideo 節點為影片生成準備條件設定和潛在空間資料，並可整合可選的運動追蹤資訊。它將起始影像序列編碼為潛在表示，並能混合來自物件追蹤的位置資料來引導生成影片中的運動。該節點輸出修改後的正向與負向條件設定，以及一個準備供影片模型使用的空潛在張量。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 待修改的正向條件設定輸入。 |
| `negative` | CONDITIONING | 是 | - | 待修改的負向條件設定輸入。 |
| `vae` | VAE | 是 | - | 用於將起始影像編碼至潛在空間的 VAE 模型。 |
| `tracks` | TRACKS | 否 | - | 包含物件路徑的可選運動追蹤資料。 |
| `strength` | FLOAT | 否 | 0.0 - 100.0 | 追蹤條件設定的強度。(預設值: 1.0) |
| `width` | INT | 否 | 16 - MAX_RESOLUTION | 輸出影片的寬度。必須能被 16 整除。(預設值: 832) |
| `height` | INT | 否 | 16 - MAX_RESOLUTION | 輸出影片的高度。必須能被 16 整除。(預設值: 480) |
| `length` | INT | 否 | 1 - MAX_RESOLUTION | 影片序列的幀數。(預設值: 81) |
| `batch_size` | INT | 否 | 1 - 4096 | 潛在輸出的批次大小。(預設值: 1) |
| `start_image` | IMAGE | 是 | - | 要編碼的起始影像或影像序列。 |
| `clip_vision_output` | CLIPVISIONOUTPUT | 否 | - | 可選的 CLIP 視覺模型輸出，將被添加到條件設定中。 |

**注意：** `strength` 參數僅在提供 `tracks` 時有效。如果未提供 `tracks` 或 `strength` 為 0.0，則不會套用追蹤條件設定。`start_image` 用於為條件設定建立潛在影像和遮罩；如果未提供，節點僅會傳遞條件設定並輸出一個空的潛在張量。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 修改後的正向條件設定，可能包含 `concat_latent_image`、`concat_mask` 和 `clip_vision_output`。 |
| `negative` | CONDITIONING | 修改後的負向條件設定，可能包含 `concat_latent_image`、`concat_mask` 和 `clip_vision_output`。 |
| `latent` | LATENT | 一個空的潛在張量，其維度由 `batch_size`、`length`、`height` 和 `width` 輸入參數決定。 |
