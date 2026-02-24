> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreativeUpscaleNode/zh-TW.md)

Recraft Creative Upscale Image 節點透過提高解析度來增強點陣圖影像。它使用一種「創意放大」流程，專注於改善影像中的細小細節和臉部。此操作透過外部 API 同步執行。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `影像` | IMAGE | 是 | | 要進行放大的輸入影像。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `影像` | IMAGE | 經過放大且細節增強後產生的影像。 |
