> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/zh-TW.md)

此節點使用 Recraft V4 或 V4 Pro AI 模型，根據文字描述生成圖像。它會將您的提示發送到外部 API 並返回生成的圖像。您可以透過指定模型、圖像尺寸和要創建的圖像數量來控制輸出。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | N/A | 圖像生成的提示。最多 10,000 個字元。 |
| `negative_prompt` | STRING | 否 | N/A | 圖像上不希望出現元素的選用文字描述。 |
| `model` | COMBO | 是 | `"recraftv4"`<br>`"recraftv4_pro"` | 用於生成的模型。選擇的模型決定了可用的圖像尺寸。 |
| `size` | COMBO | 是 | 依模型而異 | 生成圖像的尺寸。可用選項取決於所選模型。對於 `recraftv4`，預設為 "1024x1024"。對於 `recraftv4_pro`，預設為 "2048x2048"。 |
| `n` | INT | 是 | 1 到 6 | 要生成的圖像數量（預設值：1）。 |
| `seed` | INT | 是 | 0 到 18446744073709551615 | 用於決定節點是否應重新執行的種子值；無論種子為何，實際結果都是非確定性的（預設值：0）。 |
| `recraft_controls` | CUSTOM | 否 | N/A | 透過 Recraft Controls 節點對生成過程進行選用的額外控制。 |

**注意：** `size` 參數是一個動態輸入，其可用選項會根據所選的 `model` 而改變。`seed` 值並不能保證圖像輸出的可重現性。

## 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | IMAGE | 生成的單張圖像或圖像批次。 |