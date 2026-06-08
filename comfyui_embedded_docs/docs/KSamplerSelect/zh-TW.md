KSamplerSelect 節點旨在根據提供的取樣器名稱來選擇特定的取樣器。它抽象化了取樣器選擇的複雜性，讓使用者能夠輕鬆地在不同的取樣策略之間切換，以完成其任務。

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `取樣器名稱` | 指定要選擇的取樣器名稱。此參數決定了將使用哪種取樣策略，進而影響整體的取樣行為與結果。 | COMBO[STRING] |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `sampler` | 傳回所選取的取樣器物件，準備好用於取樣任務。 | `SAMPLER` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerSelect/zh-TW.md)
