> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/zh-TW.md)

## 概述

此節點使用 OpenAI 的 GPT 圖片 API 生成圖像。它支援多種模型，允許您提供輸入圖像進行編輯，並可使用遮罩指定要修改的圖像區域。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `提示詞` | STRING | 是 | 不適用 | GPT 圖像的文字提示（預設：""）。 |
| `模型` | COMBO | 是 | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` | 要使用的 OpenAI GPT 圖像模型。選擇模型會顯示該模型專屬的額外參數。 |
| `model.size` | COMBO | 是 | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` | 圖像尺寸。選擇「Custom」可使用自訂寬度和高度（預設："auto"）。僅適用於 `gpt-image-2`。 |
| `model.custom_width` | INT | 否 | 1024 至 3840 | 僅在 `size` 設為「Custom」時使用。必須是 16 的倍數（預設：1024）。僅適用於 `gpt-image-2`。 |
| `model.custom_height` | INT | 否 | 1024 至 3840 | 僅在 `size` 設為「Custom」時使用。必須是 16 的倍數（預設：1024）。僅適用於 `gpt-image-2`。 |
| `model.background` | COMBO | 是 | `"auto"`<br>`"opaque"` | 返回帶有或不帶背景的圖像（預設："auto"）。僅適用於 `gpt-image-2`。 |
| `model.quality` | COMBO | 是 | `"standard"`<br>`"hd"` | 生成圖像的品質。僅適用於 `gpt-image-2`。 |
| `model.images` | IMAGE | 否 | 不適用 | 用於編輯的輸入圖像。僅適用於 `gpt-image-2`。 |
| `model.mask` | MASK | 否 | 不適用 | 指定要編輯輸入圖像哪些部分的遮罩。僅適用於 `gpt-image-2`。 |
| `數量` | INT | 是 | 1 至 8 | 要生成的圖像數量（預設：1）。 |
| `種子` | INT | 是 | 0 至 2147483647 | 用於重現結果的種子（預設：0）。注意：後端尚未實作此功能。 |

**參數限制與注意事項：**

- 使用 `gpt-image-2` 且 `model.size` 設為「Custom」時，`custom_width` 和 `custom_height` 必須是 16 的倍數，最大邊長不得超過 3840，長寬比不得超過 3:1，且總像素數必須在 655,360 至 8,294,400 之間。
- 如果提供了 `mask`，則需要提供輸入圖像（`model.images`）。沒有輸入圖像就無法使用遮罩。
- 遮罩不能與多個輸入圖像同時使用。
- 提供遮罩時，遮罩尺寸必須與輸入圖像尺寸相符。
- `seed` 參數目前無法正常運作。

## 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 生成的圖像或圖像集合。 |

---
**Source fingerprint (SHA-256):** `a757208cf6cc151594599b35b0ef73f2caf7274189e948799211c0714a6a8f89`
