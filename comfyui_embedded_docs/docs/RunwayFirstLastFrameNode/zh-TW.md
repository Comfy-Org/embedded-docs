> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/zh-TW.md)

Runway First-Last-Frame to Video 節點透過上傳首尾關鍵影格及文字提示來生成影片。它使用 Runway 的 Gen-3 模型在提供的起始影格和結束影格之間建立平滑過渡。這在結束影格與起始影格差異較大的複雜過渡場景中特別有用。

## 輸入參數

| 參數名稱 | 資料類型 | 是否必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | N/A | 用於生成影片的文字提示（預設值：空字串） |
| `start_frame` | IMAGE | 是 | N/A | 用於影片生成的起始影格 |
| `end_frame` | IMAGE | 是 | N/A | 用於影片生成的結束影格。僅支援 gen3a_turbo 模型 |
| `duration` | COMBO | 是 | 多個選項可用 | 從可用的 Duration 選項中選擇影片時長 |
| `ratio` | COMBO | 是 | 多個選項可用 | 從可用的 RunwayGen3aAspectRatio 選項中選擇畫面比例 |
| `seed` | INT | 否 | 0-4294967295 | 用於生成過程的隨機種子（預設值：0） |

**參數限制條件：**

- `prompt` 必須包含至少 1 個字元
- `start_frame` 和 `end_frame` 的最大尺寸必須為 7999x7999 像素
- `start_frame` 和 `end_frame` 的畫面比例必須在 0.5 到 2.0 之間
- `end_frame` 參數僅在使用 gen3a_turbo 模型時支援

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 在起始影格和結束影格之間過渡生成的影片 |