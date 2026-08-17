# OpenAI GPT 圖像 2

此節點使用 OpenAI 的 GPT Image API 生成影像。它支援多種 GPT Image 模型、可選的參考影像以進行編輯，以及可選的遮罩以進行局部重繪（inpainting）。當提供參考影像時，節點會向 API 傳送編輯請求；否則會傳送一般的生成請求。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 OpenAI GPT Image 模型。選取模型會顯示該模型專屬的額外參數。 | DYNAMIC_COMBO | 是 | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | GPT Image 的文字提示（預設值：""）。 | STRING | 是 | N/A |
| `n` | 要生成的影像數量（預設值：1）。 | INT | 是 | 1 至 8 |
| `seed` | 用於重現結果的種子（預設值：0）。後端尚未實作。 | INT | 是 | 0 至 2147483647 |

### gpt-image-2 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.size` | 影像尺寸。選取「Custom」可使用自訂寬度與高度（預設值："auto"）。 | COMBO | 是 | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | 僅在 `size` 為「Custom」時使用。必須為 16 的倍數（預設值：1024）。 | INT | 否 | 1024 至 3840 |
| `model.custom_height` | 僅在 `size` 為「Custom」時使用。必須為 16 的倍數（預設值：1024）。 | INT | 否 | 1024 至 3840 |
| `model.background` | 傳回含背景或不含背景的影像（預設值："auto"）。 | COMBO | 是 | `"auto"`<br>`"opaque"` |
| `model.quality` | 影像品質，影響成本與生成時間（預設值："low"）。 | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |

### gpt-image-1.5 與 gpt-image-1 輸入

這兩個模型共用同一組模型專屬參數。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.size` | 影像尺寸（預設值："auto"）。 | COMBO | 是 | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | 傳回含背景或不含背景的影像（預設值："auto"）。 | COMBO | 是 | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | 影像品質，影響成本與生成時間（預設值："low"）。 | COMBO | 是 | `"low"`<br>`"medium"`<br>`"high"` |

### 參考輸入

以下輸入適用於所有模型。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model.images` | 用於影像編輯的選用參考影像。可擴充插槽：最多可連接 16 張影像（`image_1` 至 `image_16`）。 | IMAGE | 否 | 0 至 16 張影像 |
| `model.mask` | 用於局部重繪的選用遮罩（白色區域將被替換）。需要恰好一張參考影像。 | MASK | 否 | N/A |

**參數限制與注意事項：**

- 當 `model.size` 為「Custom」（僅限 gpt-image-2）時，`model.custom_width` 和 `model.custom_height` 必須是 16 的倍數，最長邊不得超過 3840 像素，長寬比不得超過 3:1，且總像素數必須介於 655,360 與 8,294,400 之間。
- 遮罩需要恰好一張參考影像。遮罩不能沒有輸入影像而使用，也不能與多張輸入影像同時使用。
- 提供遮罩時，遮罩的高度與寬度必須符合輸入影像的高度與寬度。
- 參考影像在傳送至 API 前會縮小至總像素最多 2048 x 2048。
- `seed` 參數尚未在後端實作。
- 若 API 在單一回應中傳回不同尺寸的影像，所有影像會調整大小，以符合第一張影像的尺寸。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `image` | 生成的單張或多張影像，堆疊成單一批次張量，形狀為 (N, H, W, C)。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fb3491f949151fbd3f5825ec9f9ae124019767d083f56966ef34af278aef50c0`
