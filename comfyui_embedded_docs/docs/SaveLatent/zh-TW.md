> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/zh-TW.md)

# SaveLatent 節點

SaveLatent 節點可將潛在張量儲存為磁碟上的檔案，以供後續使用或分享。它接收潛在樣本，並將其儲存到輸出目錄中，可選擇性地包含包含提示資訊的中繼資料。此節點會自動處理檔案命名與組織，同時保留潛在資料結構。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | 是 | - | 要儲存到磁碟的潛在樣本 |
| `檔名前綴` | STRING | 否 | - | 輸出檔案名稱的前綴（預設值："latents/ComfyUI"） |
| `prompt` | PROMPT | 否 | - | 要包含在中繼資料中的提示資訊（隱藏參數） |
| `extra_pnginfo` | EXTRA_PNGINFO | 否 | - | 要包含在中繼資料中的額外 PNG 資訊（隱藏參數） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `ui` | UI | 在 ComfyUI 介面中提供已儲存潛在檔案的檔案位置資訊 |

---
**Source fingerprint (SHA-256):** `dc7fd101c8dd93e2bcc39de64e0c39abe8e056c9e5932587fc6ce80e2fd143e8`
