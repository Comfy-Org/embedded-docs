> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/zh-TW.md)

將 SVG 檔案儲存至磁碟。此節點接收 SVG 資料作為輸入，並將其儲存至您的輸出目錄，同時可選擇嵌入中繼資料。該節點會自動處理帶有計數器後綴的檔案命名，並可將工作流程提示資訊直接嵌入 SVG 檔案中。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `svg` | SVG | 是 | - | 要儲存至磁碟的 SVG 資料 |
| `filename_prefix` | STRING | 是 | - | 儲存檔案的前綴名稱。可包含格式化資訊，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%` 以包含來自其他節點的數值。（預設值："svg/ComfyUI"） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `ui` | DICT | 回傳檔案資訊，包含檔案名稱、子資料夾和類型，用於在 ComfyUI 介面中顯示 |

**注意：** 此節點在可用時會自動將工作流程中繼資料（提示和額外的 PNG 資訊）嵌入 SVG 檔案中。中繼資料會以 CDATA 區段的形式插入至 SVG 的 metadata 元素內。