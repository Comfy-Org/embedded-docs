> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/zh-TW.md)

# ByteDance Seedream 節點

ByteDance Seedream 4.5 和 5.0 節點提供統一的文字轉圖像生成功能，以及高達 4K 解析度的精確單句編輯能力。它可以根據文字提示建立新圖像，或使用文字指令編輯現有圖像。該節點支援單張圖像生成和多張相關圖像的序列生成。

## 輸入

| 參數 | 資料類型 | 必填 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | STRING | 是 | 請參閱說明 | 用於生成的 Seedream 模型。可用的模型包括 seedream-4-0、seedream-4-5 和 seedream-5-0 變體。 |
| `prompt` | STRING | 是 | - | 用於建立或編輯圖像的文字提示。長度必須至少為 1 個字元。 |
| `image` | IMAGE | 否 | - | 用於圖像到圖像生成的輸入圖像。用於單一或多重參考生成的參考圖像。大多數模型最多 10 張參考圖像，seedream-5-0-260128 最多 14 張。 |
| `size_preset` | STRING | 否 | 多個選項可用 | 選擇建議的尺寸。選擇「自訂」以使用下方的寬度和高度。預設值：RECOMMENDED_PRESETS_SEEDREAM_4 中的第一個預設值。 |
| `width` | INT | 否 | 1024 至 6240（步長 2） | 圖像的自訂寬度。僅當 `size_preset` 設定為「自訂」時，此值才有效。預設值：2048。 |
| `height` | INT | 否 | 1024 至 4992（步長 2） | 圖像的自訂高度。僅當 `size_preset` 設定為「自訂」時，此值才有效。預設值：2048。 |
| `sequential_image_generation` | STRING | 否 | "disabled"<br>"auto" | 群組圖像生成模式。「disabled」生成單張圖像。「auto」讓模型決定是否生成多張相關圖像（例如故事場景、角色變體）。預設值："disabled"。 |
| `max_images` | INT | 否 | 1 至 15（步長 1） | 當 sequential_image_generation='auto' 時生成的最大圖像數量。總圖像數量（輸入 + 生成）不得超過 15。預設值：1。 |
| `seed` | INT | 否 | 0 至 2147483647（步長 1） | 用於生成的種子值。預設值：0。 |
| `watermark` | BOOLEAN | 否 | - | 是否在圖像上添加「AI 生成」浮水印。預設值：False。 |
| `fail_on_partial` | BOOLEAN | 否 | - | 如果啟用，當任何請求的圖像缺失或返回錯誤時，中止執行。預設值：True。 |

**參數限制說明：**
- 最小圖像解析度取決於所選模型：seedream-4-5 和 seedream-5-0 模型為 3.68MP，seedream-4-0 模型為 0.92MP。
- 最大圖像解析度：seedream-5-0 模型為 10.4MP，其他模型為 16.78MP。
- 參考圖像的長寬比必須在 1:3 到 3:1 之間。
- 當 `sequential_image_generation` 設定為 "auto" 時，輸入圖像總數加上 `max_images` 不得超過 15。
- `width` 和 `height` 參數僅在 `size_preset` 設定為「自訂」時使用。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 根據輸入參數和提示生成的圖像。如果生成多張圖像，則返回單個圖像張量或一批圖像張量。 |

---
**Source fingerprint (SHA-256):** `ce130246026e0f5036e137bea4e193f51097e0812459586dcbeb87ef01975630`
