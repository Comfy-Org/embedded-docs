> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/zh-TW.md)

## 概述

LoadLatent 節點會從輸入目錄中的 .latent 檔案載入先前儲存的潛在表示。它會從檔案中讀取潛在張量資料，並在將潛在資料傳回供其他節點使用之前，套用任何必要的縮放調整。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `潛在空間` | STRING | 是 | 輸入目錄中的所有 .latent 檔案 | 從輸入目錄中可用的檔案中，選擇要載入的 .latent 檔案 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `LATENT` | LATENT | 傳回從所選檔案載入的潛在表示資料 |

---
**Source fingerprint (SHA-256):** `020185a6066263b75b2417411f07af54d31a2a3a056d650eacfff188dc2cb87e`
