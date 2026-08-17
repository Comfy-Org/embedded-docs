# 儲存SVG節點

將 SVG 檔案儲存至磁碟。此節點接收 SVG 資料作為輸入，並將其儲存到您的輸出目錄，可選擇嵌入中繼資料。節點會自動以計數器後綴處理檔案命名，並可將工作流程提示資訊直接嵌入 SVG 檔案中。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `svg` | 要儲存至磁碟的 SVG 資料 | SVG | 是 | - |
| `filename_prefix` | 要儲存檔案的字首。可包含格式化資訊，例如 %date:yyyy-MM-dd% 或 %Empty Latent Image.width%，以納入來自節點的值。（預設值："svg/ComfyUI"） | STRING | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `svg` | 已儲存至磁碟的 SVG 資料 | SVG |
| `ui` | 傳回包含檔案名稱、子資料夾和型別的檔案資訊，以供 ComfyUI 介面顯示 | DICT |

**注意事項：** 此節點會在可用時自動將工作流程中繼資料（提示與額外的 PNG 資訊）嵌入 SVG 檔案中。中繼資料會作為 CDATA 區段插入 SVG 的 metadata 元素內。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
