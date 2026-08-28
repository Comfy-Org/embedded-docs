# OpenAI GPT 圖像 2

此節點使用 OpenAI 的 GPT Image API 生成影像。它支援多個模型（`gpt-image-2`、`gpt-image-1.5` 和 `gpt-image-1`），可讓您提供參考影像進行編輯，並可使用遮罩指定要修改影像的哪些部分。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要使用的 OpenAI GPT Image 模型。選擇模型後，會顯示該模型專屬的其他參數。 | DYNAMIC_COMBO | 是 | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `提示詞` | GPT Image 的文字提示（預設值：`""`）。 | STRING | 是 | N/A |
| `數量` | 要生成的影像數量（預設值：`1`）。 | INT | 是 | 1 至 8 |
| `種子` | 用於重現結果的種子（預設值：`0`）。後端尚未實作。 | INT | 是 | 0 至 2147483647 |

### gpt-image-2 輸入

當 `model` 設定為 `gpt-image-2` 時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `尺寸` | 影像尺寸。選擇「Custom」以使用自訂寬度與高度（預設值：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `自訂寬度` | 僅在 `model.size` 為「Custom」時使用。必須是 16 的倍數（預設值：`1024`）。 | INT | 否 | 1024 至 3840 |
| `自訂高度` | 僅在 `model.size` 為「Custom」時使用。必須是 16 的倍數（預設值：`1024`）。 | INT | 否 | 1024 至 3840 |
| `背景` | 傳回帶有或不帶背景的影像（預設值：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"opaque"` |
| `品質` | 影像品質，會影響成本與生成時間（預設值：`"low"`）。 | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | 可選的參考影像，用於影像編輯。最多 16 張影像。詳細資訊請參閱「參考輸入」。 | IMAGE | 否 | 0 至 16 |
| `model.mask` | 用於修補的可選遮罩（白色區域將被替換）。需要正好一張參考影像。 | MASK | 否 | N/A |

### gpt-image-1.5 與 gpt-image-1 輸入

當 `model` 設定為 `gpt-image-1.5` 或 `gpt-image-1` 時，會顯示這些輸入。兩個模型共用相同的參數集。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `尺寸` | 影像尺寸（預設值：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `背景` | 傳回帶有或不帶背景的影像（預設值：`"auto"`）。 | COMBO | 是 | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `品質` | 影像品質，會影響成本與生成時間（預設值：`"low"`）。 | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | 可選的參考影像，用於影像編輯。最多 16 張影像。詳細資訊請參閱「參考輸入」。 | IMAGE | 否 | 0 至 16 |
| `model.mask` | 用於修補的可選遮罩（白色區域將被替換）。需要正好一張參考影像。 | MASK | 否 | N/A |

### 參考輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.images` | 可擴充插槽：可連接 1..N 個項目（例如 `image_1`...`image_16`）；所有模型最多可有 16 張參考影像。 | IMAGE | 否 | 1 至 16 |
| `model.mask` | 用於修補的可選遮罩（白色區域將被替換）。需要正好一張參考影像。 | MASK | 否 | N/A |

**參數限制與注意事項：**

- 當 `model.size` 為「Custom」時（僅限 gpt-image-2），`model.custom_width` 和 `model.custom_height` 都必須是 16 的倍數，最長邊不得超過 3840，長寬比不得超過 3:1，且總像素數必須介於 655,360 到 8,294,400 之間。
- `model.mask` 需要在 `model.images` 中有正好一張參考影像：沒有影像時無法使用，多於一張影像時也無法使用。
- 使用 `model.mask` 時，其尺寸必須與參考影像的尺寸相符。
- 當提供 `model.images` 時，節點會以影像編輯模式執行；若未提供 `model.images`，則僅根據提示生成影像。
- 參考影像在傳送至 API 前會先縮小。
- `seed` 目前尚未在後端實作。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `image` | 生成的影像。所有傳回的影像會堆疊成一個批次；如果尺寸不同，會調整大小以符合第一張影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fb3491f949151fbd3f5825ec9f9ae124019767d083f56966ef34af278aef50c0`
