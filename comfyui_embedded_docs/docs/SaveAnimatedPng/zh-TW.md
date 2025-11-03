> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPNG/zh-TW.md)

SaveAnimatedPNG 節點專為從影格序列建立並儲存動態 PNG 影像而設計。它能將個別影像影格組合成連貫的動畫，並允許自訂影格持續時間、循環播放和元數據包含功能。

## 輸入參數

| 欄位名稱 | 資料類型 | 描述說明 |
|----------|-----------|----------|
| `images` | `IMAGE` | 要處理並儲存為動態 PNG 的影像列表。列表中的每個影像代表動畫中的一個影格。 |
| `filename_prefix` | `STRING` | 指定輸出檔案的基礎名稱，將作為生成動態 PNG 檔案的前綴。 |
| `fps` | `FLOAT` | 動畫的每秒影格速率，控制影格顯示的速度。 |
| `compress_level` | `INT` | 應用於動態 PNG 檔案的壓縮等級，會影響檔案大小和影像清晰度。 |

## 輸出結果

| 欄位名稱 | 資料類型 | 描述說明 |
|----------|-----------|----------|
| `ui` | N/A | 提供顯示生成動態 PNG 影像的 UI 組件，並指示動畫是單影格還是多影格。 |