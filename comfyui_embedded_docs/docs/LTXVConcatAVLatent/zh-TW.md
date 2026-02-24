> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/zh-TW.md)

LTXVConcatAVLatent 節點將影片潛在表示和音訊潛在表示合併為一個單一的、串聯的潛在輸出。它合併了兩個輸入的 `samples` 張量，如果存在的話，也會合併它們的 `noise_mask` 張量，為影片生成流程中的後續處理做好準備。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `video_latent` | LATENT | 是 | | 影片資料的潛在表示。 |
| `audio_latent` | LATENT | 是 | | 音訊資料的潛在表示。 |

**注意：** `video_latent` 和 `audio_latent` 輸入中的 `samples` 張量會被串聯起來。如果任一輸入包含 `noise_mask`，則會使用該遮罩；如果缺少遮罩，則會為其創建一個全為 1 的遮罩（形狀與對應的 `samples` 相同）。然後，產生的遮罩也會被串聯起來。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `latent` | LATENT | 一個包含串聯後的 `samples` 的潛在字典，如果適用的話，還包含來自影片和音訊輸入的串聯後的 `noise_mask`。 |
