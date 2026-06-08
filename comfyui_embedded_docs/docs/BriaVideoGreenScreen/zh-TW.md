# Bria 影片綠幕

此節點使用 Bria API 將影片背景替換為純色色鍵螢幕。它處理輸入影片並回傳一個新影片，其中原始背景已被移除並替換為統一的綠色或藍色螢幕顏色。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 要處理的輸入影片 | VIDEO | 是 | 影片檔案 |
| `green_shade` | 應用在前景後方的純色色鍵色調：broadcast_green（#00B140）、chroma_green（#00FF00）或 blue_screen（#0000FF） | STRING | 是 | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果皆非確定性（預設值：0） | INT | 是 | 0 至 2147483647 |

**注意：** 輸入影片的長度不得超過 60 秒。

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 已處理的影片，原始背景已被選定的色鍵色調取代 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/zh-TW.md)

---
**Source fingerprint (SHA-256):** `663b41bf51bd8d871a59e756f226e4bf6244bb616ebcd2e8ccfa426137f2a05b`
