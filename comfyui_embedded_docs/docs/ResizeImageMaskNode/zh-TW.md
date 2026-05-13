> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/zh-TW.md)

# 調整影像/遮罩節點

調整影像/遮罩節點提供多種方法來改變輸入影像或遮罩的尺寸。它可以透過倍數縮放、設定特定尺寸、匹配另一個輸入的大小，或根據像素數量進行調整，並使用各種插值方法來確保品質。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `input` | IMAGE 或 MASK | 是 | 不適用 | 要調整大小的影像或遮罩。 |
| `resize_type` | COMBO | 是 | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE` | 用於決定新尺寸的方法。根據所選類型，必要參數會隨之改變。 |
| `multiplier` | FLOAT | 否 | 0.01 至 8.0 | 縮放倍數。當 `resize_type` 為 `SCALE_BY` 時為必要參數（預設值：1.00）。 |
| `width` | INT | 否 | 0 至 8192 | 目標寬度（像素）。當 `resize_type` 為 `SCALE_DIMENSIONS` 或 `SCALE_WIDTH` 時為必要參數（預設值：512）。 |
| `height` | INT | 否 | 0 至 8192 | 目標高度（像素）。當 `resize_type` 為 `SCALE_DIMENSIONS` 或 `SCALE_HEIGHT` 時為必要參數（預設值：512）。 |
| `crop` | COMBO | 否 | `"disabled"`<br>`"center"` | 當尺寸與長寬比不符時應用的裁切方法。僅在 `resize_type` 為 `SCALE_DIMENSIONS` 或 `MATCH_SIZE` 時可用（預設值："center"）。 |
| `longer_size` | INT | 否 | 0 至 8192 | 影像較長邊的目標尺寸。當 `resize_type` 為 `SCALE_LONGER_DIMENSION` 時為必要參數（預設值：512）。 |
| `shorter_size` | INT | 否 | 0 至 8192 | 影像較短邊的目標尺寸。當 `resize_type` 為 `SCALE_SHORTER_DIMENSION` 時為必要參數（預設值：512）。 |
| `megapixels` | FLOAT | 否 | 0.01 至 16.0 | 目標總百萬像素數。當 `resize_type` 為 `SCALE_TOTAL_PIXELS` 時為必要參數（預設值：1.0）。 |
| `match` | IMAGE 或 MASK | 否 | 不適用 | 輸入將調整尺寸以匹配其尺寸的影像或遮罩。當 `resize_type` 為 `MATCH_SIZE` 時為必要參數。 |
| `scale_method` | COMBO | 是 | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` | 用於縮放的插值演算法（預設值："area"）。 |

**注意：** `crop` 參數僅在 `resize_type` 設定為 `SCALE_DIMENSIONS` 或 `MATCH_SIZE` 時可用且相關。使用 `SCALE_WIDTH` 或 `SCALE_HEIGHT` 時，另一個維度會自動縮放以保持原始長寬比。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `resized` | IMAGE 或 MASK | 調整尺寸後的影像或遮罩，與輸入的資料類型一致。 |

---
**Source fingerprint (SHA-256):** `9ac0b153608ac971bb11d9d12ebd1f0f4d6e926604e8727a1bc3a311d95fbc03`
