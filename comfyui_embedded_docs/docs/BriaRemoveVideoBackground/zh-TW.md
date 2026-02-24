> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/zh-TW.md)

此節點使用 Bria AI 服務來移除影片背景。它會處理輸入影片，並將原始背景替換為您選擇的純色背景。此操作透過外部 API 執行，結果會以新的影片檔案形式返回。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | 是 | N/A | 將要移除背景的輸入影片檔案。 |
| `background_color` | STRING | 是 | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` | 用作輸出影片新背景的純色。 |
| `seed` | INT | 否 | 0 至 2147483647 | 控制節點是否應重新執行的種子值。無論種子值為何，結果都是非確定性的。(預設值: 0) |

**注意：** 輸入影片的長度必須在 60 秒或以下。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 經過處理的影片檔案，背景已移除並替換為所選顏色。 |