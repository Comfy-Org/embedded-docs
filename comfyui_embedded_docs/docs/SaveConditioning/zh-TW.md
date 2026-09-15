# 儲存條件

此節點會將單一 conditioning 儲存到輸出資料夾，格式為 safetensors 檔案。儲存的檔案可以移動到 models/embeddings 資料夾，之後使用 Load Conditioning 載入，例如用來跳過文字編碼器。此節點會將 conditioning 原樣傳遞，因此之後仍可在工作流程中使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | 要儲存的 conditioning。僅支援單一 conditioning 項目。 | CONDITIONING | 是 | - |
| `filename_prefix` | 用於建立輸出檔名的前綴。檔案會寫入輸出資料夾，並附加數字計數器。預設：`conditioning/ComfyUI` | STRING | 是 | - |

**備註：**

- 如果 `conditioning` 輸入包含超過一個項目（例如在合併 conditioning 之後），此節點會引發錯誤：「Save Conditioning supports a single conditioning entry, save it before combining.」
- 屬於 tensor、tensor 的 list/tuple、boolean、integer、float 或 string 的 conditioning 選項，會與 conditioning 一併儲存。值為 `None` 的選項會被略過。任何其他選項類型會引發錯誤，表示該選項無法儲存。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `conditioning` | 傳入的同一個 conditioning，維持不變。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `07b7d2be5262c4782f237138d034b130322507e62ae8775b9c94634df8e7a3fa`
