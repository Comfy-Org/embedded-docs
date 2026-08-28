# 儲存圖片

SaveImage 節點會將輸入的影像儲存為 PNG 檔案，並輸出至您的 ComfyUI 輸出目錄。它可以將工作流程中繼資料（例如提示詞）嵌入每個儲存的檔案中，並原封不動地回傳影像，以便其他節點繼續使用。

## 輸入
| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `影像` | 要儲存的影像。 | IMAGE | 是 | - |
| `檔名前綴` | 要儲存檔案的檔名前置詞。可包含格式化資訊，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`，以從節點取得值（預設值："ComfyUI"）。 | STRING | 是 | - |

此節點還接收兩個隱藏輸入 `prompt` 和 `extra_pnginfo`，ComfyUI 會自動以工作流程提示詞及額外的 PNG 資訊填入這些輸入。當啟用中繼資料時，此資訊會以文字中繼資料的形式嵌入每個儲存的 PNG 檔案中。

## 輸出
| Output Name | Description | Data Type |
| --- | --- | --- |
| `images` | 原始的輸入影像，在儲存至磁碟後原封不動地回傳。 | IMAGE |
| `ui` | 僅供 UI 使用的結果，包含已儲存影像檔案的清單（檔名、子資料夾與類型），供前端顯示。 | UI_RESULT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
