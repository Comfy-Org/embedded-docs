> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/zh-TW.md)

T5TokenizerOptions 節點允許您為各種 T5 模型類型配置分詞器設定。它為多個 T5 模型變體（包括 t5xxl、pile_t5xl、t5base、mt5xl 和 umt5xxl）設定最小填充和最小長度參數。此節點接收一個 CLIP 輸入，並返回一個已套用指定分詞器選項的修改後 CLIP。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | - | 要為其配置分詞器選項的 CLIP 模型 |
| `最小填充` | INT | 否 | 0 至 10000 | 為所有 T5 模型類型設定的最小填充值（預設值：0） |
| `最小長度` | INT | 否 | 0 至 10000 | 為所有 T5 模型類型設定的最小長度值（預設值：0） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | CLIP | 已將更新的分詞器選項套用至所有 T5 變體的修改後 CLIP 模型 |

---
**Source fingerprint (SHA-256):** `bc05c714e4006786d0c948ed1de05324257472337397b0aa4ce574d7483929ff`
