## 概述

此節點使用 OpenAI 的 GPT 圖片 API 生成圖像。它支援多種模型，允許您提供輸入圖像進行編輯，並可使用遮罩指定要修改的圖像區域。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `提示詞` | GPT 圖像的文字提示（預設：""）。 | STRING | 是 | 不適用 |
| `模型` | 要使用的 OpenAI GPT 圖像模型。選擇模型會顯示該模型專屬的額外參數。 | COMBO | 是 | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `model.size` | 圖像尺寸。選擇「Custom」可使用自訂寬度和高度（預設："auto"）。僅適用於 `gpt-image-2`。 | COMBO | 是 | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | 僅在 `size` 設為「Custom」時使用。必須是 16 的倍數（預設：1024）。僅適用於 `gpt-image-2`。 | INT | 否 | 1024 至 3840 |
| `model.custom_height` | 僅在 `size` 設為「Custom」時使用。必須是 16 的倍數（預設：1024）。僅適用於 `gpt-image-2`。 | INT | 否 | 1024 至 3840 |
| `model.background` | 返回帶有或不帶背景的圖像（預設："auto"）。僅適用於 `gpt-image-2`。 | COMBO | 是 | `"auto"`<br>`"opaque"` |
| `model.quality` | 生成圖像的品質。僅適用於 `gpt-image-2`。 | COMBO | 是 | `"standard"`<br>`"hd"` |
| `model.images` | 用於編輯的輸入圖像。僅適用於 `gpt-image-2`。 | IMAGE | 否 | 不適用 |
| `model.mask` | 指定要編輯輸入圖像哪些部分的遮罩。僅適用於 `gpt-image-2`。 | MASK | 否 | 不適用 |
| `數量` | 要生成的圖像數量（預設：1）。 | INT | 是 | 1 至 8 |
| `種子` | 用於重現結果的種子（預設：0）。注意：後端尚未實作此功能。 | INT | 是 | 0 至 2147483647 |

**參數限制與注意事項：**

- 使用 `gpt-image-2` 且 `model.size` 設為「Custom」時，`custom_width` 和 `custom_height` 必須是 16 的倍數，最大邊長不得超過 3840，長寬比不得超過 3:1，且總像素數必須在 655,360 至 8,294,400 之間。
- 如果提供了 `mask`，則需要提供輸入圖像（`model.images`）。沒有輸入圖像就無法使用遮罩。
- 遮罩不能與多個輸入圖像同時使用。
- 提供遮罩時，遮罩尺寸必須與輸入圖像尺寸相符。
- `seed` 參數目前無法正常運作。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `image` | 生成的圖像或圖像集合。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a757208cf6cc151594599b35b0ef73f2caf7274189e948799211c0714a6a8f89`
