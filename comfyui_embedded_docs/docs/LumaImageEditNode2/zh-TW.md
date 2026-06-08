## 概述

此節點使用文字提示來編輯現有圖像，由 Luma UNI-1 模型驅動。它接收來源圖像和所需變更的描述，然後生成編輯後的新圖像版本。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `來源` | 要編輯的來源圖像。 | IMAGE | 是 | - |
| `提示` | 所需編輯的描述。預設值：""（空字串）。 | STRING | 是 | 1–6000 個字元 |
| `模型` | 用於編輯的模型。 | MODEL | 是 | `"uni-1"`<br>`"uni-1-max"` |
| `種子` | 種子控制節點是否應重新執行；無論種子為何，結果皆為非確定性。預設值：0。 | INT | 是 | 0 到 2147483647 |

**參數限制：**
- `prompt` 的長度必須在 1 到 6000 個字元之間。
- `model` 參數是一個動態組合框，當設定為 `"uni-1"` 或 `"uni-1-max"` 時，會提供額外的子參數（例如 `style`、`web_search` 和 `image_ref`）。`image_ref` 子參數最多可接受 8 個圖像參考。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `image` | 由 Luma UNI-1 模型生成的編輯後圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7026e3ce818b0a9710624bd071fc2049950290f89c7d0365ff44236e9ad5eaed`
