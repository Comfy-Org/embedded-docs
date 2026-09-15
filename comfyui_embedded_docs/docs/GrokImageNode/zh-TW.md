# Grok 圖像

Grok Image 節點使用 Grok AI 模型，根據文字描述生成一張或多張圖像。它會將您的提示傳送至外部服務，並以張量形式傳回生成的圖像，這些張量可在您的工作流程中使用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於圖像生成的特定 Grok 模型。不同模型可能提供不同的品質、速度或功能。 | COMBO | 是 | `"grok-imagine-image-2.0"`<br>`"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"` |
| `prompt` | 用於生成圖像的文字提示。此描述會引導 AI 建立什麼內容。長度必須至少為 1 個字元（不接受僅含空白字元的文字）。 | STRING | 是 | N/A |
| `aspect_ratio` | 生成圖像所需的寬高比。 | COMBO | 是 | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `number_of_images` | 要生成的圖像數量（預設值：1）。 | INT | 是 | 1 到 10 |
| `seed` | 用於決定節點是否應重新執行的種子；無論種子為何，實際結果皆不具確定性（預設值：0）。 | INT | 是 | 0 到 2147483647 |
| `解析度` | 生成圖像所需的輸出解析度（預設值："1K"）。 | COMBO | 否 | `"1K"`<br>`"2K"` |
| `品質` | 品質等級，僅由 `grok-imagine-image-2.0` 模型支援（預設值："medium"；"low" 是可用選項之一）。對於所有其他模型，此設定會被忽略。 | COMBO | 否 | 提供多個選項 |

**注意：** `seed` 參數主要用於控制節點在工作流程中何時重新執行。由於外部 AI 服務的特性，即使使用相同的種子，生成的圖像在每次執行之間也無法重現或完全相同。

**定價注意事項：** 生成圖像的成本取決於所選的 `model`、`resolution`、`quality` 和 `number_of_images`。對於 `grok-imagine-image-2.0` 模型，"low" 品質在 1K 解析度下每張圖像為 $0.04，在 2K 解析度下每張圖像為 $0.06；其他品質等級在 1K 下每張圖像為 $0.06，在 2K 下每張圖像為 $0.08。`grok-imagine-image-quality` 模型在 1K 解析度下每張圖像為 $0.05，在 2K 解析度下每張圖像為 $0.07。`grok-imagine-image-pro` 模型每張圖像為 $0.07。`grok-imagine-image` 模型每張圖像為 $0.02。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的圖像或一批圖像。如果 `number_of_images` 為 1，則傳回單一圖像張量。如果大於 1，則傳回一批圖像張量。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`
