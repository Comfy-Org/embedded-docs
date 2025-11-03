> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/zh-TW.md)

SamplerLCMUpscale 節點提供了一種專門的取樣方法，結合了潛在一致性模型（LCM）取樣與圖像放大功能。它允許您在取樣過程中使用各種插值方法來放大圖像，這對於生成更高解析度的輸出同時保持圖像品質非常有用。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `scale_ratio` | FLOAT | 否 | 0.1 - 20.0 | 放大過程中應用的縮放比例因子（預設值：1.0） |
| `scale_steps` | INT | 否 | -1 - 1000 | 用於放大過程的步驟數量。使用 -1 表示自動計算（預設值：-1） |
| `upscale_method` | COMBO | 是 | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" | 用於放大圖像的插值方法 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 返回一個已配置的取樣器物件，可在取樣管線中使用 |