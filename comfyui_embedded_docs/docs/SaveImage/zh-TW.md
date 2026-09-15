# 儲存圖片

SaveImage 節點會將輸入影像儲存為 PNG 檔案至你的 ComfyUI 輸出目錄。它可將工作流中繼資料（例如提示詞）嵌入每個儲存的檔案中，並會原樣傳回影像，因此這些影像仍可供其他節點使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要儲存的影像。 | IMAGE | 是 | - |
| `檔名前綴` | 要儲存檔案的前綴。這可以包含格式化資訊，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`，以納入來自節點的值（預設值："ComfyUI"）。 | STRING | 是 | - |

此節點也會接收兩個隱藏輸入：`prompt` 與 `extra_pnginfo`，這些輸入會由 ComfyUI 自動填入工作流提示詞與額外 PNG 資訊。當啟用中繼資料時，這些資訊會以文字中繼資料的形式嵌入每個儲存的 PNG 檔案中。

每個儲存影像的檔案名稱由 `filename_prefix`、可選的 `%batch_num%` 預留位置（會替換為該影像在批次中的位置），以及一個五位數計數器組成，例如 `ComfyUI_00001_.png`。影像會以 PNG 壓縮層級 4 寫入。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `images` | 原始輸入影像，在儲存至磁碟後會原樣傳回。 | IMAGE |
| `ui` | 僅供 UI 使用的結果，包含已儲存影像檔案的清單（檔案名稱、子資料夾與類型），用於前端顯示。 | UI_RESULT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
