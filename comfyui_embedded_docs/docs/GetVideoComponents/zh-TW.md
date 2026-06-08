「取得影片元件」節點會從影片檔案中提取所有主要元素。它將影片分割為單獨的影格、提取音軌，並提供影片的幀率資訊。這讓您可以獨立處理每個元件，以便進行後續處理或分析。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影片` | 要從中提取元件的影片。 | VIDEO | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `音訊` | 從影片中提取的個別影格，作為獨立的影像。 | IMAGE |
| `每秒影格數` | 從影片中提取的音軌。 | AUDIO |
| `fps` | 影片的幀率，以每秒影格數表示。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7b8419d6614d5be0ec15ccfeb48ee9813c74b28b0b405d62c03496c133c92f53`
