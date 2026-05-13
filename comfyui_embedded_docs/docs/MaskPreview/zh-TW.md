> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/zh-TW.md)

MaskPreview 節點會將遮罩資料儲存為預覽圖片至您的 ComfyUI 輸出目錄，讓您在工作流程執行期間能直觀地檢查遮罩資料。它會將輸入的遮罩轉換為適合圖片顯示的格式，並使用可設定的檔案名稱前綴進行儲存。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `遮罩` | MASK | 是 | - | 要預覽並儲存為圖片的遮罩資料 |
| `filename_prefix` | STRING | 否 | - | 輸出檔案名稱的前綴（預設值："ComfyUI"） |
| `prompt` | PROMPT | 否 | - | 用於中繼資料的提示資訊（自動提供） |
| `extra_pnginfo` | EXTRA_PNGINFO | 否 | - | 用於中繼資料的額外 PNG 資訊（自動提供） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `ui` | DICT | 包含預覽圖片資訊及用於 UI 顯示的中繼資料 |

---
**Source fingerprint (SHA-256):** `9f64adf4a0130368618fc1ca3655192686815ab10b4153f9552ef23149928e3f`
