此節點使用 Recraft V4 或 V4 Pro AI 模型，根據文字描述生成圖像。它會將您的提示詞發送到外部 API，並返回生成的圖像。您可以透過指定模型、圖像大小和要建立的圖像數量來控制輸出。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | 圖像生成的提示詞。最多 10,000 個字元。 | STRING | 是 | 不適用 |
| `negative_prompt` | 可選的負面提示詞，用於描述圖像中不希望出現的元素。 | STRING | 否 | 不適用 |
| `model` | 用於生成的模型。選擇模型會決定可用的圖像大小。 | COMBO | 是 | `"recraftv4"`<br>`"recraftv4_pro"` |
| `size` | 生成圖像的大小。可用選項取決於所選的模型。對於 `recraftv4`，預設值為 "1024x1024"。對於 `recraftv4_pro`，預設值為 "2048x2048"。 | COMBO | 是 | 依模型而異 |
| `n` | 要生成的圖像數量（預設值：1）。 | INT | 是 | 1 到 6 |
| `seed` | 用於決定節點是否應重新執行的種子；無論種子為何，實際結果都是非確定性的（預設值：0）。 | INT | 是 | 0 到 18446744073709551615 |
| `recraft_controls` | 透過 Recraft Controls 節點對生成過程進行可選的額外控制。 | CUSTOM | 否 | 不適用 |

**注意：** `size` 參數是一個動態輸入，其可用選項會根據所選的 `model` 而變化。`seed` 值無法保證可重現的圖像輸出。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的單張圖像或一批圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `77d549a43aeee670b6c42069654017fb6b202ed83ca330389573b790bad6ae6e`
