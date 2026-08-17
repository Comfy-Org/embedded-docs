# T5 分詞器選項

T5TokenizerOptions 節點可讓您為各種 T5 模型類型設定分詞器選項。它會為多種 T5 模型變體設定最小填充與最小長度參數，包括 t5xxl、pile_t5xl、t5base、mt5xl 與 umt5xxl。此節點接受 CLIP 輸入，並回傳套用指定分詞器選項後的修改版 CLIP。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 要設定分詞器選項的 CLIP 模型 | CLIP | 是 | - |
| `min_padding` | 要為所有 T5 模型類型設定的最小填充值（預設值：0） | INT | 否 | 0 至 10000 |
| `min_length` | 要為所有 T5 模型類型設定的最小長度值（預設值：0） | INT | 否 | 0 至 10000 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 已將更新後的分詞器選項套用至所有 T5 變體的修改版 CLIP 模型 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`
