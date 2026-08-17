# LoadLatent

LoadLatent 節點會載入先前在輸入目錄中儲存為 .latent 檔案的潛在表示。它會從所選檔案讀取潛在張量資料，並套用必要的縮放調整，然後傳回結果供其他節點使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `latent` | 從輸入目錄中的可用檔案中選擇要載入的 .latent 檔案 | COMBO | 是 | 輸入目錄中的所有 .latent 檔案 |

注意：對於不包含 `latent_format_version_0` 標記的 .latent 檔案，載入的潛在張量會乘以 1/0.18215，以便其縮放符合其他節點預期的格式。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 返回從所選檔案載入的潛在表示資料 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`
