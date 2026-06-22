# Grok 圖像

Grok 影像節點會使用 Grok AI 模型，根據文字描述生成一張或多張影像。它會將您的提示詞傳送至外部服務，並將生成的影像以張量形式回傳，以便在工作流程中使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影像生成的特定 Grok 模型。不同的模型可能提供不同的品質、速度或功能。 | COMBO | 是 | `"grok-imagine-image-quality"`<br>`"grok-imagine-image-pro"`<br>`"grok-imagine-image"`<br>`"grok-imagine-image-beta"` |
| `prompt` | 用於生成影像的文字提示詞。此描述會引導 AI 生成相應的內容。長度至少需為 1 個字元。 | STRING | 是 | 不適用 |
| `aspect_ratio` | 生成影像所需的寬高比。 | COMBO | 是 | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"9:16"`<br>`"16:9"`<br>`"9:19.5"`<br>`"19.5:9"`<br>`"9:20"`<br>`"20:9"`<br>`"1:2"`<br>`"2:1"` |
| `number_of_images` | 要生成的影像數量（預設值：1）。 | INT | 否 | 1 到 10 |
| `seed` | 用於決定節點是否應重新執行的種子值。實際影像結果是非確定性的，即使使用相同的種子，結果也會有所不同（預設值：0）。 | INT | 否 | 0 到 2147483647 |
| `解析度` | 生成影像所需的輸出解析度（預設值："1K"）。 | COMBO | 否 | `"1K"`<br>`"2K"` |

**注意：** `seed` 參數主要用於控制節點在工作流程中何時重新執行。由於外部 AI 服務的特性，即使使用相同的種子，每次執行所生成的影像也無法重現或完全相同。

**關於定價的注意事項：** 生成影像的成本取決於所選的 `model`、`resolution` 和 `number_of_images`。例如，使用 "grok-imagine-image-quality" 模型搭配 "1K" 解析度，每張影像成本為 0.05 美元，而 "2K" 解析度則為每張 0.07 美元。"grok-imagine-image-pro" 模型每張影像成本為 0.07 美元，其他模型則為每張 0.02 美元。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的單張影像或一批影像。如果 `number_of_images` 為 1，則回傳單個影像張量。如果大於 1，則回傳一批影像張量。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5c8a76d3636dea8bcc6ade0d8adb6e6d1610b518a31e15fc7fce3f107fe63953`
