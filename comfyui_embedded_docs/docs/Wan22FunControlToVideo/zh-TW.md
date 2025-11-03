> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/zh-TW.md)

Wan22FunControlToVideo 節點使用 Wan 視訊模型架構，為視訊生成準備條件調控和潛在表示。它處理正向和負向條件調控輸入，以及可選的參考圖像和控制視訊，以創建視訊合成所需的潛在空間表示。該節點處理空間縮放和時間維度，為視訊模型生成適當的條件調控資料。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | - | 用於引導視訊生成的正向條件調控輸入 |
| `negative` | CONDITIONING | 是 | - | 用於引導視訊生成的負向條件調控輸入 |
| `vae` | VAE | 是 | - | 用於將圖像編碼到潛在空間的 VAE 模型 |
| `width` | INT | 否 | 16 至 MAX_RESOLUTION | 輸出視訊寬度（像素）（預設值：832，步長：16） |
| `height` | INT | 否 | 16 至 MAX_RESOLUTION | 輸出視訊高度（像素）（預設值：480，步長：16） |
| `length` | INT | 否 | 1 至 MAX_RESOLUTION | 視訊序列中的幀數（預設值：81，步長：4） |
| `batch_size` | INT | 否 | 1 至 4096 | 要生成的視訊序列數量（預設值：1） |
| `ref_image` | IMAGE | 否 | - | 用於提供視覺引導的可選參考圖像 |
| `control_video` | IMAGE | 否 | - | 用於引導生成過程的可選控制視訊 |

**注意：** `length` 參數以 4 幀為單位進行處理，節點會自動處理潛在空間的時間縮放。當提供 `ref_image` 時，它會透過參考潛在表示影響條件調控。當提供 `control_video` 時，它會直接影響條件調控中使用的串接潛在表示。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 包含視訊專用潛在資料的修改後正向條件調控 |
| `negative` | CONDITIONING | 包含視訊專用潛在資料的修改後負向條件調控 |
| `latent` | LATENT | 具有適當維度的空潛在張量，用於視訊生成 |