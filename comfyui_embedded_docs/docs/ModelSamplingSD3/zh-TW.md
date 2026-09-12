# 模型取樣 SD3

此節點會將 Stable Diffusion 3 風格的取樣設定套用到模型。它會複製模型，並將其取樣方法替換為基於 flow 的取樣設定；此設定會使用指定的 `shift` 值，而該值可控制取樣分佈的形狀。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 SD3 取樣參數的輸入模型 | MODEL | 是 | - |
| `偏移` | 控制取樣偏移參數（預設值：3.0） | FLOAT | 是 | 0.0 - 100.0 (step: 0.01) |

注意：`shift` 值會與固定的內部乘數 1000 一起套用。如果原始模型有 noise scale 設定，該值會沿用至修改後的模型。原始模型不會被變更；會回傳一個經過複製並修補的副本。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 SD3 取樣參數的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a77e38c2cebf6f21f841a953ec5c59096eaf60ffc205c24f34f635e54c5718cb`
