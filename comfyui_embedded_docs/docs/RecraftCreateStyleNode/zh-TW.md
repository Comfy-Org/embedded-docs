> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreateStyleNode/zh-TW.md)

此節點透過上傳參考影像來建立用於影像生成的自訂風格。您可以上傳 1 到 5 張影像來定義新風格，節點將回傳一個獨特的風格 ID，可與其他 Recraft 節點搭配使用。所有上傳影像的總檔案大小不得超過 5 MB。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `風格` | STRING | 是 | `"realistic_image"`<br>`"digital_illustration"` | 生成影像的基礎風格。 |
| `圖片` | IMAGE | 是 | 1 到 5 張影像 | 用於建立自訂風格的一組參考影像，數量為 1 到 5 張。 |

**注意：** `images` 輸入中所有影像的總檔案大小必須小於 5 MB。若超過此限制，節點將會執行失敗。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `style_id` | STRING | 新建立的自訂風格的獨特識別碼。 |

---
**Source fingerprint (SHA-256):** `36340e64d90b3edbbecedf15ac123adaabb5bc0c950183d2df6627dc873da61c`
