# T5 分詞器選項

## 概覽

T5TokenizerOptions 節點會為各種 T5 模型類型配置分詞器設定。它會為多個 T5 模型變體設定最小填充與最小長度參數，包括 t5xxl、pile_t5xl、t5base、mt5xl 與 umt5xxl。此節點接受一個 CLIP 輸入，將設定套用到其副本，並傳回修改後的 CLIP。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 要為其設定分詞器選項的 CLIP 模型 | CLIP | 是 | - |
| `最小填充` | 要為所有 T5 模型類型設定的最小填充值（預設：0） | INT | 是 | 0 至 10000 |
| `最小長度` | 要為所有 T5 模型類型設定的最小長度值（預設：0） | INT | 是 | 0 至 10000 |

注意：此節點在 ComfyUI 中標記為實驗性。這些設定會一次套用到所有支援的 T5 變體：t5xxl、pile_t5xl、t5base、mt5xl 與 umt5xxl。輸入 `clip` 在修改前會被複製，因此原始 CLIP 不會被變更。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 已將更新後的分詞器選項套用到所有 T5 變體的修改後 CLIP 模型 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`
