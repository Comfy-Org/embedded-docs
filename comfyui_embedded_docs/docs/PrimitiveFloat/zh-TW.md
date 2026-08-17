# 浮點數

PrimitiveFloat 節點會建立一個可在您的工作流程中使用的浮點數值。它接受單一數值輸入並輸出相同的值，讓您可以在 ComfyUI 管線中的不同節點之間定義和傳遞浮點數值。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `value` | 要輸出的浮點數值（預設值：0.0） | FLOAT | 是 | -sys.maxsize 至 sys.maxsize（步長：0.1） |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 輸入的浮點數值 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/zh-TW.md)

---
**Source fingerprint (SHA-256):** `df57e5900e972e17da365fbbdb7b7db777dda6f9f938e1074f1a89451d4b7c73`
