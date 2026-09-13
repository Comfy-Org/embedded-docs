# 模型取樣 Stable Cascade

ModelSamplingStableCascade 節點透過對取樣參數套用位移值，將穩定串聯（stable cascade）取樣設定套用至模型。它會回傳一個套用了自訂穩定串聯取樣配置的輸入模型修補副本，原始模型保持不變。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用穩定串聯取樣的輸入模型 | MODEL | 是 | - |
| `偏移` | 套用至取樣參數的位移值（預設：2.0） | FLOAT | 是 | 0.0 - 100.0 （步進值：0.01） |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 套用了穩定串聯取樣的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/zh-TW.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
