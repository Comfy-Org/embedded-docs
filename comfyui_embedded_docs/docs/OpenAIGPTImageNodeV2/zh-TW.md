# OpenAI GPT Image 2.6

此節點使用 OpenAI 的 GPT Image API 生成影像。它支援六種模型 — `gpt-image-2.6-flare`、`gpt-image-2.6-sunburst`、`gpt-image-2.5-flare`、`gpt-image-2.5-sunburst`、`gpt-image-2` 與 `gpt-image-1.5` — 可讓你附加參考影像以進行影像編輯，並可使用遮罩來指定要替換影像的哪些部分。

## 輸入

### 通用輸入

這些輸入一律可見。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要使用的 OpenAI GPT Image 模型。選擇模型後會顯示該模型專屬的額外參數。 | DYNAMIC_COMBO | 是 | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"`<br>`"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"`<br>`"gpt-image-2"`<br>`"gpt-image-1.5"` |
| `提示詞` | GPT Image 的文字提示詞（預設：`""`）。 | STRING | 是 | N/A |
| `數量` | 要生成多少張影像（預設：`1`）。 | INT | 是 | 1 至 8 |
| `種子` | 用於重現結果的種子值（預設：`0`）。後端尚未實作。 | INT | 是 | 0 至 2147483647 |

### gpt-image-2.6-flare 與 gpt-image-2.6-sunburst 輸入

當 `model` 設為 `gpt-image-2.6-flare` 或 `gpt-image-2.6-sunburst` 時會顯示這些輸入。兩個模型共用同一組參數。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `尺寸` | 影像尺寸。選擇 "Custom" 以使用自訂寬度與高度（預設：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `自訂寬度` | 僅當 `model.size` 為 "Custom" 時使用。必須是 16 的倍數（預設：`1024`）。 | INT | 否 | 480 至 3840（步進值：16） |
| `自訂高度` | 僅當 `model.size` 為 "Custom" 時使用。必須是 16 的倍數（預設：`1024`）。 | INT | 否 | 480 至 3840（步進值：16） |
| `背景` | 傳回含背景或不含背景的影像（預設：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `品質` | 影像品質，會影響成本與生成時間（預設：`"low"`）。 | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | 用於影像編輯的選用參考影像。最多 16 張影像。詳見「參考輸入」。 | IMAGE | 否 | 0 至 16 |
| `model.mask` | 用於內繪（inpainting）的選用遮罩（白色區域會被替換）。必須恰好有一張參考影像。 | MASK | 否 | N/A |
| `model.complexity` | 模型在算繪前規劃影像的程度。較低的值回應較快，較高的值則規劃更多。預設：`"high"`。 | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |

### gpt-image-2 輸入

當 `model` 設為 `gpt-image-2` 時會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `尺寸` | 影像尺寸。選擇 "Custom" 以使用自訂寬度與高度（預設：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `自訂寬度` | 僅當 `model.size` 為 "Custom" 時使用。必須是 16 的倍數（預設：`1024`）。 | INT | 否 | 480 至 3840（步進值：16） |
| `自訂高度` | 僅當 `model.size` 為 "Custom" 時使用。必須是 16 的倍數（預設：`1024`）。 | INT | 否 | 480 至 3840（步進值：16） |
| `背景` | 傳回含背景或不含背景的影像（預設：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"opaque"` |
| `品質` | 影像品質，會影響成本與生成時間（預設：`"low"`）。 | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | 用於影像編輯的選用參考影像。最多 16 張影像。詳見「參考輸入」。 | IMAGE | 否 | 0 至 16 |
| `model.mask` | 用於內繪（inpainting）的選用遮罩（白色區域會被替換）。必須恰好有一張參考影像。 | MASK | 否 | N/A |

### gpt-image-1.5 輸入

當 `model` 設為 `gpt-image-1.5` 時會顯示這些輸入。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `尺寸` | 影像尺寸（預設：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `背景` | 傳回含背景或不含背景的影像（預設：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `品質` | 影像品質，會影響成本與生成時間（預設：`"low"`）。 | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | 用於影像編輯的選用參考影像。最多 16 張影像。詳見「參考輸入」。 | IMAGE | 否 | 0 至 16 |
| `model.mask` | 用於內繪（inpainting）的選用遮罩（白色區域會被替換）。必須恰好有一張參考影像。 | MASK | 否 | N/A |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.images` | 可擴充插槽：連接 1..N 個項目（例如 `image_1`...`image_16`）；所有模型最多支援 16 張參考影像。 | IMAGE | 否 | 0 至 16 |
| `model.mask` | 用於內繪（inpainting）的選用遮罩（白色區域會被替換）。必須恰好有一張參考影像。 | MASK | 否 | N/A |

**參數限制與條件：**

- 當 `model.size` 為 "Custom" 時（僅限 `gpt-image-2.6-flare`、`gpt-image-2.6-sunburst`、`gpt-image-2.5-flare`、`gpt-image-2.5-sunburst` 與 `gpt-image-2`），`model.custom_width` 與 `model.custom_height` 都必須是 16 的倍數，最長邊不得超過 3840，長寬比不得超過 3:1，且總像素數必須介於 655,360 與 8,294,400 之間。
- `model.mask` 需要 `model.images` 中恰好有一張參考影像：沒有影像時無法使用，且影像超過一張時也無法使用。
- 使用 `model.mask` 時，其高度與寬度必須與參考影像的高度與寬度相符。
- 提供 `model.images` 時，節點會以影像編輯模式執行；未提供 `model.images` 時，則僅根據提示詞生成影像。
- 參考影像與遮罩在傳送至 API 前會先縮小。
- `"xhigh"` 與 `"max"` 品質等級僅適用於 `gpt-image-2.6-flare`、`gpt-image-2.6-sunburst`、`gpt-image-2.5-flare` 與 `gpt-image-2.5-sunburst`。
- `model.complexity` 僅適用於 `gpt-image-2.6-flare` 與 `gpt-image-2.6-sunburst`；其他模型使用固定的規劃深度。
- `seed` 目前尚未在後端實作。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `image` | 生成的一張或多張影像。所有傳回的影像會堆疊成單一批次；若尺寸不同，會調整大小以符合第一張影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `effc65978ac1cca52a8d8c85230784c23c9eb2afffd7f057aba9f9627e784a15`
