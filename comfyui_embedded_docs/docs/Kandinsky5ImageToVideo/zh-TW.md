> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/zh-TW.md)

Kandinsky5ImageToVideo 節點為使用 Kandinsky 模型進行影片生成準備條件設定和潛在空間資料。它會建立一個空的影片潛在張量，並可選擇性地編碼起始圖像以引導生成影片的初始幀，從而相應地修改正向和負向條件設定。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | 是 | N/A | 用於引導影片生成的正向條件提示。 |
| `negative` | CONDITIONING | 是 | N/A | 用於使影片生成遠離特定概念的負向條件提示。 |
| `vae` | VAE | 是 | N/A | 用於將可選的起始圖像編碼到潛在空間的 VAE 模型。 |
| `width` | INT | 否 | 16 至 8192 (步長 16) | 輸出影片的寬度（像素），預設值為 768。 |
| `height` | INT | 否 | 16 至 8192 (步長 16) | 輸出影片的高度（像素），預設值為 512。 |
| `length` | INT | 否 | 1 至 8192 (步長 4) | 影片的幀數，預設值為 121。 |
| `batch_size` | INT | 否 | 1 至 4096 | 同時生成的影片序列數量，預設值為 1。 |
| `start_image` | IMAGE | 否 | N/A | 可選的起始圖像。若提供，將被編碼並用於替換模型輸出潛在張量的噪聲起始部分。 |

**注意：** 當提供 `start_image` 時，它會自動使用雙線性插值調整大小以匹配指定的 `width` 和 `height`。圖像批次的前 `length` 幀將用於編碼。編碼後的潛在張量隨後會被注入到 `positive` 和 `negative` 條件設定中，以引導影片的初始外觀。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 修改後的正向條件設定，可能已更新為編碼後的起始圖像資料。 |
| `negative` | CONDITIONING | 修改後的負向條件設定，可能已更新為編碼後的起始圖像資料。 |
| `latent` | LATENT | 一個由零值組成的空影片潛在張量，其形狀符合指定的維度。 |
| `cond_latent` | LATENT | 所提供起始圖像的乾淨、編碼後的潛在表示。這在內部用於替換生成影片潛在張量的噪聲起始部分。 |
