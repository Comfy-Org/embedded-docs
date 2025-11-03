> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageToVideoNode/zh-TW.md)

基於提示詞、輸入圖像和輸出尺寸同步生成影片。此節點透過使用 Luma API，提供文字提示詞和可選的起始/結束圖像來定義影片內容和結構，從而創建影片。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 影片生成的提示詞（預設：""） |
| `model` | COMBO | 是 | 多個可用選項 | 從可用的 Luma 模型中選擇影片生成模型 |
| `resolution` | COMBO | 是 | 多個可用選項 | 生成影片的輸出解析度（預設：540p） |
| `duration` | COMBO | 是 | 多個可用選項 | 生成影片的時長 |
| `loop` | BOOLEAN | 是 | - | 生成的影片是否應循環播放（預設：False） |
| `seed` | INT | 是 | 0 到 18446744073709551615 | 決定節點是否應重新執行的種子值；無論種子為何，實際結果都是非確定性的（預設：0） |
| `first_image` | IMAGE | 否 | - | 生成影片的第一幀（可選） |
| `last_image` | IMAGE | 否 | - | 生成影片的最後一幀（可選） |
| `luma_concepts` | CUSTOM | 否 | - | 可選的相機概念，透過 Luma Concepts 節點來控制相機運動（可選） |

**注意：** 必須提供 `first_image` 或 `last_image` 中的至少一個。如果兩者都缺失，節點將引發異常。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案 |