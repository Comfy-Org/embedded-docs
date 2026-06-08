# Recraft V4 文字轉向量節點

Recraft V4 文字轉向量節點可根據文字描述生成可縮放向量圖形（SVG）插圖。此節點連接到外部 API，使用 Recraft V4 或 Recraft V4 Pro 模型進行圖像生成。節點會根據您的提示輸出一個或多個 SVG 圖像。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | 圖像生成的提示詞。最多 10,000 個字元。 | STRING | 是 | 不適用 |
| `negative_prompt` | 可選的負面提示詞，用於描述圖像中不希望出現的元素。 | STRING | 否 | 不適用 |
| `model` | 用於生成的模型。選擇模型會改變可用的 `size` 選項。 | COMBO | 是 | `"recraftv4"`<br>`"recraftv4_pro"` |
| `size` | 生成圖像的尺寸。可用選項取決於所選的 `model`。`recraftv4` 的預設值為 `"1024x1024"`，`recraftv4_pro` 的預設值為 `"2048x2048"`。 | COMBO | 是 | 對於 `recraftv4`：`"1024x1024"`、`"1152x896"`、`"896x1152"`、`"1216x832"`、`"832x1216"`、`"1344x768"`、`"768x1344"`、`"1536x640"`、`"640x1536"`<br>對於 `recraftv4_pro`：`"2048x2048"`、`"2304x1792"`、`"1792x2304"`、`"2432x1664"`、`"1664x2432"`、`"2688x1536"`、`"1536x2688"`、`"3072x1280"`、`"1280x3072"` |
| `n` | 要生成的圖像數量（預設值：1）。 | INT | 是 | 1 到 6 |
| `seed` | 用於決定節點是否應重新執行的種子值；無論種子為何，實際結果均為非確定性。 | INT | 是 | 0 到 18446744073709551615 |
| `recraft_controls` | 可選的額外控制項，可透過 Recraft Controls 節點對生成過程進行控制。 | CUSTOM | 否 | 不適用 |

**注意：** `size` 參數是一個動態輸入，其可用選項會根據所選的 `model` 而改變。`seed` 值無法保證從外部 API 獲得可重現的結果。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的 Scalable Vector Graphics (SVG) 圖像。 | SVG |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ffab67555923cea29b50ae71e3ffaad13340aead4d01973a70244468fae4420d`
