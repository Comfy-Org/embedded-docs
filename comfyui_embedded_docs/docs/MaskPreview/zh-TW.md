# MaskPreview

MaskPreview 節點會直接在 ComfyUI 介面中顯示遮罩資料的視覺化預覽，而不會將其儲存到輸出目錄。這讓您可以在工作流程的任何階段檢查遮罩，同時遮罩也會原樣通過此節點，因此可繼續在下游使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `遮罩` | 要預覽的遮罩資料 | MASK | 是 | - |
| `filename_prefix` | 用於預覽的檔案名稱前綴（預設值："ComfyUI"） | STRING | 否 | - |
| `prompt` | 用於中繼資料的提示資訊（自動提供） | PROMPT | 否 | - |
| `extra_pnginfo` | 用於中繼資料的額外 PNG 資訊（自動提供） | EXTRA_PNGINFO | 否 | - |

只有 `mask` 是可見且需要連接的輸入。`filename_prefix`、`prompt` 和 `extra_pnginfo` 參數由系統提供：`filename_prefix` 會回退至其預設值，而 `prompt` 和 `extra_pnginfo` 則是隱藏的，並由 ComfyUI 執行環境自動提供。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `mask` | 與所預覽相同的遮罩資料，會原樣回傳，以便可在工作流程中的其他位置使用 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fb7abe8cb6b5ac8a6a38e88ef90a146d16caf41d24c5de95309a94bc3c371d75`
