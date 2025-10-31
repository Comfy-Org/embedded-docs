> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/zh-TW.md)

WanPhantomSubjectToVideo 節點透過處理條件輸入和可選的參考圖像來生成影片內容。它會為影片生成創建潛在表徵，並可在提供輸入圖像時納入視覺引導。該節點會為影片模型準備具有時間維度串接的條件資料，並輸出修改後的條件資料以及生成的潛在影片資料。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用於引導影片生成的正向條件輸入 |
| `negative` | CONDITIONING | 是 | - | 用於避免特定特徵的負向條件輸入 |
| `vae` | VAE | 是 | - | 用於在提供圖像時進行編碼的 VAE 模型 |
| `width` | INT | 否 | 16 至 MAX_RESOLUTION | 輸出影片的寬度（單位：像素，預設值：832，必須可被 16 整除） |
| `height` | INT | 否 | 16 至 MAX_RESOLUTION | 輸出影片的高度（單位：像素，預設值：480，必須可被 16 整除） |
| `length` | INT | 否 | 1 至 MAX_RESOLUTION | 生成影片的幀數（預設值：81，必須可被 4 整除） |
| `batch_size` | INT | 否 | 1 至 4096 | 同時生成的影片數量（預設值：1） |
| `images` | IMAGE | 否 | - | 用於時間維度條件的可選參考圖像 |

**注意：** 當提供 `images` 時，它們會自動放大以符合指定的 `width` 和 `height`，並且僅使用前 `length` 幀進行處理。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 修改後的正向條件資料，在提供圖像時包含時間維度串接 |
| `negative_text` | CONDITIONING | 修改後的負向條件資料，在提供圖像時包含時間維度串接 |
| `negative_img_text` | CONDITIONING | 負向條件資料，在提供圖像時包含歸零的時間維度串接 |
| `latent` | LATENT | 生成的潛在影片表徵，具有指定的尺寸和長度 |