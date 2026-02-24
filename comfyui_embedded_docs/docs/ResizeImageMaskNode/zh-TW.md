> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/zh-TW.md)

Resize Image/Mask 節點提供多種方法來改變輸入圖像或遮罩的尺寸。它可以透過倍率縮放、設定特定尺寸、匹配另一輸入的尺寸，或根據像素總數進行調整，並使用多種插值方法來確保品質。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `input` | IMAGE 或 MASK | 是 | N/A | 需要調整尺寸的圖像或遮罩。 |
| `resize_type` | COMBO | 是 | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE` | 用於決定新尺寸的方法。所需的參數會根據選擇的類型而改變。 |
| `multiplier` | FLOAT | 否 | 0.01 至 8.0 | 縮放倍率。當 `resize_type` 為 `SCALE_BY` 時需要此參數（預設值：1.00）。 |
| `width` | INT | 否 | 0 至 8192 | 目標寬度（像素）。當 `resize_type` 為 `SCALE_DIMENSIONS` 或 `SCALE_WIDTH` 時需要此參數（預設值：512）。 |
| `height` | INT | 否 | 0 至 8192 | 目標高度（像素）。當 `resize_type` 為 `SCALE_DIMENSIONS` 或 `SCALE_HEIGHT` 時需要此參數（預設值：512）。 |
| `crop` | COMBO | 否 | `"disabled"`<br>`"center"` | 當尺寸與長寬比不匹配時應用的裁切方法。僅在 `resize_type` 為 `SCALE_DIMENSIONS` 或 `MATCH_SIZE` 時可用（預設值："center"）。 |
| `longer_size` | INT | 否 | 0 至 8192 | 圖像長邊的目標尺寸。當 `resize_type` 為 `SCALE_LONGER_DIMENSION` 時需要此參數（預設值：512）。 |
| `shorter_size` | INT | 否 | 0 至 8192 | 圖像短邊的目標尺寸。當 `resize_type` 為 `SCALE_SHORTER_DIMENSION` 時需要此參數（預設值：512）。 |
| `megapixels` | FLOAT | 否 | 0.01 至 16.0 | 目標總像素數（百萬像素）。當 `resize_type` 為 `SCALE_TOTAL_PIXELS` 時需要此參數（預設值：1.0）。 |
| `match` | IMAGE 或 MASK | 否 | N/A | 一個圖像或遮罩，輸入將調整尺寸以匹配其尺寸。當 `resize_type` 為 `MATCH_SIZE` 時需要此參數。 |
| `scale_method` | COMBO | 是 | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` | 用於縮放的插值演算法（預設值："area"）。 |

**注意：** `crop` 參數僅在 `resize_type` 設定為 `SCALE_DIMENSIONS` 或 `MATCH_SIZE` 時可用且相關。當使用 `SCALE_WIDTH` 或 `SCALE_HEIGHT` 時，另一維度會自動縮放以保持原始長寬比。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `resized` | IMAGE 或 MASK | 調整尺寸後的圖像或遮罩，其資料類型與輸入相同。 |
