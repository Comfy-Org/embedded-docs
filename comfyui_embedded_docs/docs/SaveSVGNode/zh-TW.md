# 儲存SVG節點

將 SVG 檔案儲存到磁碟。此節點接收 SVG 資料作為輸入，並將其儲存到您的輸出目錄，可選擇嵌入中繼資料。此節點自動處理帶有計數器後綴的檔案命名，並可直接將工作流程提示資訊嵌入 SVG 檔案中。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `svg` | 要儲存到磁碟的 SVG 資料 | SVG | 是 | - |
| `檔案名稱前綴` | 要儲存檔案的前置詞。可包含格式資訊，例如 %date:yyyy-MM-dd% 或 %Empty Latent Image.width%，以納入來自節點的值。（預設："svg/ComfyUI"） | STRING | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `svg` | 原始的 SVG 資料，在儲存後原樣傳出 | SVG |
| `ui` | 已儲存檔案資訊，包括檔案名稱、子資料夾和型別，用於在 ComfyUI 介面中顯示 | DICT |

**注意：** 此節點會在工作流程中繼資料可用時，自動將其（提示詞和額外的 PNG 資訊）嵌入 SVG 檔案中。中繼資料會以 CDATA 區段的形式插入 SVG 的 metadata 元素中。檔案會依照 `filename_prefix_00001_.svg` 的模式儲存；處理批次時，前置詞中的 `%batch_num%` 會替換為目前批次項目的索引。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
