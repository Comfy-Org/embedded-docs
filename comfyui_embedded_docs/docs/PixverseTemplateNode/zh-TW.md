> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/zh-TW.md)

PixVerse 範本節點讓您可以從可用的 PixVerse 影片生成範本中進行選擇。它會將您選擇的範本名稱轉換為 PixVerse API 用於影片創建所需的對應範本 ID。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `範本` | STRING | 是 | 多個可用選項 | 用於 PixVerse 影片生成的範本。可用的選項對應於 PixVerse 系統中的預定義範本。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `pixverse_template` | STRING | 與所選範本名稱對應的範本 ID，可供其他 PixVerse 節點用於影片生成。 |

---
**Source fingerprint (SHA-256):** `d6ea1eb1cc9a7d33cf69f101990e601189726b9ef9e199fe211087f7070f35d0`
