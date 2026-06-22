# 儲存SVG節點

## 概述

將 SVG 檔案儲存至磁碟。此節點接收 SVG 資料作為輸入，並將其儲存至您的輸出目錄，可選擇嵌入中繼資料。節點會自動處理帶有計數器後綴的檔案命名，並能將工作流程提示資訊直接嵌入 SVG 檔案中。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `svg` | 要儲存至磁碟的 SVG 資料 | SVG | 是 | - |
| `檔案名稱前綴` | 要儲存檔案的檔案名稱前綴。可包含格式化資訊，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`，以納入來自節點的值。（預設值："svg/ComfyUI"） | STRING | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `ui` | 回傳檔案資訊，包含檔案名稱、子資料夾及類型，用於在 ComfyUI 介面中顯示 | DICT |

**注意：** 此節點會在有可用工作流程中繼資料（提示和額外 PNG 資訊）時，自動將其嵌入 SVG 檔案中。中繼資料會以 CDATA 區段的形式插入 SVG 的 metadata 元素內。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a294103d8d2306ce6765912a98c5572323bb5394909ee384591534b0b404ea70`
