# Bria Video 綠幕

此節點使用 Bria API，將影片的背景替換為純色色度鍵畫面。它會處理輸入影片，並傳回一段新影片，其中原始背景已被移除，並替換為統一的綠色或藍色畫面顏色。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 要處理的輸入影片 | VIDEO | 是 | 影片檔案 |
| `green_shade` | 套用於前景後方的純色色度鍵色調：broadcast_green (#00B140)、chroma_green (#00FF00) 或 blue_screen (#0000FF)。 | COMBO | 是 | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `seed` | 種子用於控制節點是否重新執行；無論種子為何，結果皆非確定性（預設值：0） | INT | 是 | 0 到 2147483647 |

**注意：** 輸入影片的長度不得超過 60 秒。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 已處理的影片（MP4、H.264），其原始背景已替換為所選的色度鍵色調 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/zh-TW.md)

---
**Source fingerprint (SHA-256):** `70d2951d0adbbe7492b2bc97d04be6591b65f040ca4b414754ad6365c5db45cf`
