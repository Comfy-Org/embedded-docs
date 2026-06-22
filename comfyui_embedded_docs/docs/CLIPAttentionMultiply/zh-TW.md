# CLIPAttentionMultiply

CLIPAttentionMultiply 節點允許您透過對自注意力層的不同元件套用乘法因子，來調整 CLIP 模型中的注意力機制。其運作方式是修改 CLIP 模型注意力機制中的查詢、鍵、值及輸出投影的權重與偏差。此實驗性節點會建立輸入 CLIP 模型的修改副本，並套用指定的縮放因子。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `clip` | 要修改的 CLIP 模型 | CLIP | 是 | - |
| `q` | 查詢投影權重與偏差的乘法因子（預設值：1.0） | FLOAT | 是 | 0.0 - 10.0 |
| `k` | 鍵投影權重與偏差的乘法因子（預設值：1.0） | FLOAT | 是 | 0.0 - 10.0 |
| `v` | 值投影權重與偏差的乘法因子（預設值：1.0） | FLOAT | 是 | 0.0 - 10.0 |
| `out` | 輸出投影權重與偏差的乘法因子（預設值：1.0） | FLOAT | 是 | 0.0 - 10.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `CLIP` | 回傳一個已套用指定注意力縮放因子的修改後 CLIP 模型 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/zh-TW.md)

---
**Source fingerprint (SHA-256):** `43dab83ecfc928f3359eb7560658f43235bf3faa62c81084a2b4f482e3a4638f`
