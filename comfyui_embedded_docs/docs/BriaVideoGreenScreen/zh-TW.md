# Bria Video 綠幕

此節點使用 Bria API 將影片背景替換為純色色鍵（chroma-key）畫面。它會處理輸入影片，並回傳一個新影片，其中原始背景已被移除，並替換為均勻的綠色或藍色畫面。

## 輸入

| 參數 | 說明 | 資料型態 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 要處理的輸入影片 | VIDEO | 是 | 影片檔案 |
| `green_shade` | 應用於前景後方的純色色鍵色調：broadcast_green (#00B140)、chroma_green (#00FF00) 或 blue_screen (#0000FF) | COMBO | 是 | `"broadcast_green"`<br>`"chroma_green"`<br>`"blue_screen"` |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果都不具確定性（預設值：0） | INT | 是 | 0 到 2147483647 |

**注意：** 輸入影片的時長不得超過 60 秒。

## 輸出

| 輸出名稱 | 說明 | 資料型態 |
|-------------|-------------|-----------|
| `video` | 處理後的影片，原始背景已替換為所選的色鍵色調，以 MP4（H.264）影片格式回傳 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/zh-TW.md)

---
**Source fingerprint (SHA-256):** `70d2951d0adbbe7492b2bc97d04be6591b65f040ca4b414754ad6365c5db45cf`
