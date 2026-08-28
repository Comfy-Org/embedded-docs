# 模型取樣 Stable Cascade

The ModelSamplingStableCascade 節點透過使用 shift 值調整取樣參數，將穩定級聯取樣套用至模型。它會建立輸入模型的修補副本，並帶有自訂的穩定級聯取樣設定，而原始模型保持不變。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用穩定級聯取樣的輸入模型 | MODEL | 是 | - |
| `偏移` | 要套用於取樣參數的 shift 值（預設：2.0） | FLOAT | 是 | 0.0 - 100.0 (step 0.01) |

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
| --- | --- | --- |
| `model` | 已套用穩定級聯取樣之修改後的模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/zh-TW.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
