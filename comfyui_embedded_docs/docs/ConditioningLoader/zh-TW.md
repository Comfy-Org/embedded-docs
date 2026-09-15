# 載入條件

此節點會從 embeddings 資料夾載入先前使用 Save Conditioning 節點儲存的 conditioning，或任何包含 `conditioning` tensor 的 safetensors 檔案。它也會還原與該 conditioning 一起儲存的任何額外選項及編號清單值。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `conditioning_name` | 要從 embeddings 資料夾載入的檔案。選項清單會由該資料夾中目前可用的檔案建立。 | COMBO | 是 | embeddings 資料夾中的所有檔案 |

**注意：** 選取的檔案必須包含 `conditioning` tensor。檔案中儲存的任何額外鍵都會被還原：編號鍵（例如 `key.0`、`key.1`）會重新分組為有序清單，其他鍵則還原為一般選項。額外選項若存在，會從檔案的 `conditioning_options` 中繼資料讀取。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `CONDITIONING` | 從檔案載入的 conditioning，以及還原的選項。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `08fc58bcaa2309fcf03d4e4cc634b930aaf6ccf8097181fd3d45924abda144eb`
