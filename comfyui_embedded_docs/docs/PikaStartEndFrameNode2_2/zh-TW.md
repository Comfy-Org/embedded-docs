> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/zh-TW.md)

PikaFrames v2.2 節點透過結合您的起始幀和結束幀來生成影片。您上傳兩張圖像來定義起始點和結束點，AI 會在它們之間創建平滑的過渡，從而產生完整的影片。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image_start` | IMAGE | 是 | - | 要組合的第一張圖像。 |
| `image_end` | IMAGE | 是 | - | 要組合的最後一張圖像。 |
| `prompt_text` | STRING | 是 | - | 描述期望影片內容的文字提示。 |
| `negative_prompt` | STRING | 是 | - | 描述影片中應避免內容的文字。 |
| `seed` | INT | 是 | - | 用於生成一致性的隨機種子值。 |
| `resolution` | STRING | 是 | - | 輸出影片的解析度。 |
| `duration` | INT | 是 | - | 生成影片的持續時間。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 透過 AI 過渡結合起始幀和結束幀所生成的影片。 |