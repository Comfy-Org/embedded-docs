> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/zh-TW.md)

WanSCAILToVideo 節點為影片生成準備條件化輸入和空潛在空間。它處理可選輸入，如參考圖像、姿勢影片和 CLIP 視覺輸出，將它們嵌入到影片模型的正向與負向條件化中。此節點輸出修改後的條件化以及指定影片尺寸的空白潛在張量。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 正向條件化輸入。 |
| `negative` | CONDITIONING | 是 | - | 負向條件化輸入。 |
| `vae` | VAE | 是 | - | 用於編碼圖像和影片影格的 VAE 模型。 |
| `width` | INT | 是 | 32 至 MAX_RESOLUTION | 輸出影片的寬度（單位：像素，預設值：512）。必須能被 8 整除。 |
| `height` | INT | 是 | 32 至 MAX_RESOLUTION | 輸出影片的高度（單位：像素，預設值：896）。必須能被 8 整除。 |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 影片的總影格數（預設值：81）。 |
| `batch_size` | INT | 是 | 1 至 4096 | 批次中要生成的影片數量（預設值：1）。 |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 否 | - | 用於條件化的可選 CLIP 視覺輸出。 |
| `reference_image` | IMAGE | 否 | - | 用於條件化的可選參考圖像。 |
| `pose_video` | IMAGE | 否 | - | 用於姿勢條件化的影片。將被縮小至主影片解析度的一半。 |
| `pose_strength` | FLOAT | 是 | 0.0 至 10.0 | 姿勢潛在的強度（預設值：1.0）。 |
| `pose_start` | FLOAT | 是 | 0.0 至 1.0 | 開始使用姿勢條件化的步驟（預設值：0.0）。 |
| `pose_end` | FLOAT | 是 | 0.0 至 1.0 | 結束使用姿勢條件化的步驟（預設值：1.0）。 |

**注意：** `pose_video` 輸入僅處理前 `length` 個影格。`reference_image` 僅處理批次中的第一張圖像。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 修改後的正向條件化，可能包含嵌入的參考圖像潛在、CLIP 視覺輸出或姿勢影片潛在。 |
| `negative` | CONDITIONING | 修改後的負向條件化，可能包含嵌入的參考圖像潛在、CLIP 視覺輸出或姿勢影片潛在。 |
| `latent` | LATENT | 一個形狀為 `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` 的空潛在張量。 |