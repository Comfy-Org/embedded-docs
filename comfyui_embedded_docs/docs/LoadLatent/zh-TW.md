# LoadLatent

LoadLatent 節點從輸入目錄中的 .latent 檔案載入先前儲存的潛在表示。它會從選取的檔案讀取潛在張量資料，並在傳回潛在資料供其他節點使用之前，套用任何必要的縮放調整。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `潛在空間` | 從輸入目錄中可用的檔案選取要載入的 .latent 檔案 | COMBO | 是 | 輸入目錄中的所有 .latent 檔案（動態清單，依字母順序排列） |

注意：可用檔案清單是動態產生的，僅包含輸入目錄中副檔名為 .latent 的檔案。如果選取的檔案已不存在，節點會將其回報為無效的潛在檔案。

## 輸出

| 輸出名 | 說明 | 資料型別 |
| --- | --- | --- |
| LATENT | 傳回從選取檔案載入的潛在表示資料，作為浮點張量。如果檔案不包含 `latent_format_version_0` 標記，則張量在傳回前會以 1/0.18215 縮放；包含該標記的檔案則以其儲存的縮放比例傳回。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`
