# 儲存SVG節點

將 SVG 檔案儲存到磁碟。此節點接收 SVG 資料作為輸入，並將其寫入 ComfyUI 輸出目錄，自動處理帶有計數器後綴的檔案命名。當工作流程提示資訊可用時，它會直接嵌入 SVG 檔案中作為中繼資料元素。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `svg` | 要儲存到磁碟的 SVG 資料 | SVG | 是 | - |
| `檔案名稱前綴` | 要儲存的檔案前綴。這可能包含格式化資訊，例如 %date:yyyy-MM-dd% 或 %Empty Latent Image.width%，以包含來自節點的值。（預設值："svg/ComfyUI"） | STRING | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `svg` | 原始的 SVG 資料，在儲存後傳遞 | SVG |
| `ui` | 已儲存的檔案資訊，包括檔案名稱、子資料夾和類型，用於在 ComfyUI 介面中顯示 | DICT |

**注意：** 此節點會在可用時自動將工作流程中繼資料（提示和額外的 PNG 資訊）嵌入 SVG 檔案中。中繼資料會作為 CDATA 區段插入 SVG 的中繼資料元素內。檔案會使用模式 `filename_prefix_00001_.svg` 儲存；處理批次時，前綴中的 `%batch_num%` 會替換為目前批次項目的索引。此節點是輸出節點，因此即使檔案本身不會顯示為影像預覽，它也會在輸出資料夾中產生已儲存的結果。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
