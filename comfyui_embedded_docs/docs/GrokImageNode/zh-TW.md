# Grok 圖像

**說明：**  
Grok Image 節點使用 Grok AI 影像模型，根據文字提示產生一張或多張圖像。它會將提示與設定傳送至外部服務，並將產生的圖像以張量形式回傳，以供工作流程中的其他部分使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於圖像生成的特定 Grok 模型。不同的模型可能提供不同的品質、速度或功能。 | COMBO | 是 | `"grok-imagine-image-2.0"`<br>`"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `prompt` | 用於生成圖像的文字提示。此描述引導 AI 決定要建立的內容。必須至少包含 1 個非空白字元。 | STRING | 是 | N/A |
| `aspect_ratio` | 所需生成圖像的寬高比。 | COMBO | 是 | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `number_of_images` | 要生成的圖像數量（預設值：1）。 | INT | 是 | 1 到 10 |
| `seed` | 決定節點是否應重新執行的種子；無論種子為何，實際結果皆不確定（預設值：0）。 | INT | 是 | 0 到 2147483647 |
| `resolution` | 生成圖像所需的輸出解析度（預設值：\""1K\""）。 | COMBO | 否 | `"1K"`<br>`"2K"` |
| `quality` | 品質等級，僅由 grok-imagine-image-2.0 模型支援（預設值：\""medium\""）。 | COMBO | 否 | 多種選項可用 |

**注意：** `quality` 參數僅在 `model` 設定為 \""grok-imagine-image-2.0\"" 時才會套用。對於所有其他模型，此設定會被忽略。

**注意：** `seed` 參數主要用於控制節點在工作流程中重新執行的時機。由於外部 AI 服務的性質，即便使用相同的種子，產生的圖像也無法跨執行重現。

**定價說明：** 生成圖像的成本取決於所選的 `model`、`resolution`、`quality` 和 `number_of_images`；總價格為每張圖像的費率乘以 `number_of_images`。對於 \""grok-imagine-image-2.0\"" 模型，在 \""1K\"" 解析度下每張圖像費率為 $0.04，在 \""2K\"" 且品質為 \""low\"" 時為 $0.06；或在 \""1K\"" 時為 $0.06，在 \""2K\"" 且其他品質等級時為 $0.08。\""grok-imagine-image-quality\"" 模型在 \""1K\"" 時每張圖像 $0.05，在 \""2K\"" 時每張圖像 $0.07。\""grok-imagine-image-pro\"" 模型每張圖像 $0.07。其他模型每張圖像 $0.02。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的圖像或一批圖像。如果 `number_of_images` 為 1，則回傳單一圖像張量。如果大於 1，則回傳一批圖像張量。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`
