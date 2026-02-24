> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/zh-TW.md)

HunyuanVideo15SuperResolution 節點為影片超解析度處理準備條件資料。它接收影片的潛在表徵，並可選擇性地接收起始圖像，將這些資料與雜訊增強和 CLIP 視覺資料一起封裝成可供模型用於生成更高解析度輸出的格式。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | N/A | 將使用潛在資料和增強資料進行修改的正向條件輸入。 |
| `negative` | CONDITIONING | 是 | N/A | 將使用潛在資料和增強資料進行修改的負向條件輸入。 |
| `vae` | VAE | 否 | N/A | 用於編碼可選參數 `start_image` 的 VAE。若提供了 `start_image` 則為必需。 |
| `start_image` | IMAGE | 否 | N/A | 用於引導超解析度的可選起始圖像。若提供，它將被放大並編碼到條件潛在空間中。 |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 否 | N/A | 可選的 CLIP 視覺嵌入資料，將添加到條件中。 |
| `latent` | LATENT | 是 | N/A | 將被整合到條件中的輸入潛在影片表徵。 |
| `noise_augmentation` | FLOAT | 否 | 0.0 - 1.0 | 應用於條件的雜訊增強強度（預設值：0.70）。 |

**注意：** 若您提供了 `start_image`，則必須同時連接一個 `vae` 以對其進行編碼。`start_image` 將被自動放大，以匹配輸入 `latent` 所隱含的尺寸。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 修改後的正向條件，現在包含了串聯的潛在資料、雜訊增強以及可選的 CLIP 視覺資料。 |
| `negative` | CONDITIONING | 修改後的負向條件，現在包含了串聯的潛在資料、雜訊增強以及可選的 CLIP 視覺資料。 |
| `latent` | LATENT | 輸入的潛在資料將保持不變地傳遞。 |
