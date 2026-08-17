# 儲存圖片

SaveImage 節點會將接收到的圖像儲存至您的 `ComfyUI/output` 目錄。它會將每張圖像儲存為 PNG 檔案，並可將工作流程中繼資料（例如提示詞）嵌入儲存的檔案中，以供日後參考。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 要儲存的圖像。 | IMAGE | 是 | - |
| `filename_prefix` | 要儲存之檔案的檔名前綴。可包含格式化資訊，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`，以納入來自節點的值（預設值："ComfyUI"）。 | STRING | 是 | - |
| `prompt` | 隱藏輸入，由 ComfyUI 自動提供：作為中繼資料嵌入於儲存之 PNG 檔案中的提示詞資料。 | PROMPT | 否 | - |
| `extra_pnginfo` | 隱藏輸入，由 ComfyUI 自動提供：作為中繼資料嵌入於儲存之 PNG 檔案中的額外工作流程資訊。 | EXTRA_PNGINFO | 否 | - |

每張圖像皆會儲存為 PNG 檔案。在儲存的檔案名稱中，前綴中的 `%batch_num%` 會替換為該圖像的批次編號，並附加一個補零計數器。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `images` | 已儲存的相同圖像，直接傳遞輸出以供其他節點使用。 | IMAGE |
| `ui` | UI 結果，包含已儲存圖像的清單及其檔案名稱、子資料夾與類型，並顯示於 ComfyUI 介面中。 | UI_RESULT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
