> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/zh-TW.md)

此節點使用 Bria AI 服務移除影片的背景。它會處理輸入的影片，並將原始背景替換為您選擇的單一顏色。此操作透過外部 API 執行，結果將以新的影片檔案形式回傳。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | 是 | 不適用 | 將從中移除背景的輸入影片檔案。 |
| `background_color` | STRING | 是 | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` | 用作輸出影片新背景的單一顏色。 |
| `seed` | INT | 否 | 0 到 2147483647 | 控制節點是否應重新執行的種子值。無論種子值為何，結果都是非確定性的。（預設值：0） |

**注意：** 輸入影片的時長必須為 60 秒或更短。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 已移除背景並替換為所選顏色的處理後影片檔案。 |

---
**Source fingerprint (SHA-256):** `51499fc006d3fd3fd45f8aad686d92537d399255b3a583fd54b77c5a0698a068`
