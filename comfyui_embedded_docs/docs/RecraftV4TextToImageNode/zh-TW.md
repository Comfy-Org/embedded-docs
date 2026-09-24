# Recraft V4 文字轉圖像

使用 Recraft V4 與 V4.1 模型從文字提示詞生成圖像。它會將提示詞與選定設定傳送至 Recraft API，並傳回生成的圖像（單張或多張）。若使用風格參考圖像，也會一併傳回所建立的風格 ID。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於生成的模型。recraftv4_styles 模型是為了風格一致的生成而建構，且一律需要 `style_id` 或 `style_references`。`recraftv4_1_flash` 是最快且最便宜的模型，完全不支援風格。 | DYNAMIC_COMBO | 是 | "recraftv4_1"<br>"recraftv4_1_flash"<br>"recraftv4_1_utility"<br>"recraftv4_1_pro"<br>"recraftv4_1_utility_pro"<br>"recraftv4"<br>"recraftv4_pro"<br>"recraftv4_styles"<br>"recraftv4_styles_pro" |
| `prompt` | 用於圖像生成的提示詞。最多 10,000 個字元。 | STRING | 是 | 1 到 10000 個字元 |
| `negative_prompt` | 此輸入會被忽略：Recraft V4 與 V4.1 模型不支援負向提示詞。 | STRING | 是 | N/A |
| `n` | 要生成的圖像數量（預設值：1）。 | INT | 是 | 1 到 6 |
| `seed` | 用於決定節點是否應重新執行的種子；無論種子為何，實際結果都是不確定的（預設值：0）。 | INT | 是 | 0 到 18446744073709551615 |
| `recraft_controls` | 可透過 Recraft Controls 節點對生成進行額外控制的選用項目。 | CUSTOM | 否 | N/A |
| `style_id` | 要套用的 Recraft V4 風格 UUID，例如來自 Recraft V4 Create Style 節點，或先前執行的 `style_id` 輸出。不能與 `style_references` 合併使用（預設值：空）。 | STRING | 否 | 有效的 UUID 字串 |
| `style_match` | 遵循風格的程度：precise 會詳細重現風格，flexible 則符合整體外觀。僅在提供風格時使用（預設值："precise"）。 | COMBO | 否 | "precise"<br>"flexible" |

### recraftv4_1、recraftv4_1_flash、recraftv4_1_utility、recraftv4 與 recraftv4_styles 輸入

這些模型共用相同的 `size` 參數。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成圖像的尺寸（預設值："1024x1024"）。 | COMBO | 是 | 有多個選項可用（標準 Recraft V4 尺寸；包含 "1024x1024"） |

### recraftv4_1_pro、recraftv4_1_utility_pro、recraftv4_pro 與 recraftv4_styles_pro 輸入

這些模型共用相同的 `size` 參數。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成圖像的尺寸（預設值："2048x2048"）。 | COMBO | 是 | 有多個選項可用（pro Recraft V4 尺寸；包含 "2048x2048"） |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `style_references` | 用於即時建立風格的參考圖像，會於生成費用之外另行計費。建立的風格會以 `style_id` 傳回以供重複使用。不能與 `style_id` 合併使用。可擴充插槽：連接 1..N 張圖像（`style_reference_1`、`style_reference_2`、...）。 | IMAGE | 否 | 0 到 Recraft API 允許的參考圖像數量上限；總編碼大小不得超過 10 MB |

**注意：** `size` 參數是動態輸入，其可用選項會根據所選的 `model` 而改變。`recraftv4_styles` 與 `recraftv4_styles_pro` 模型一律需要風格：請連接風格參考圖像或提供 `style_id`。`style_id` 與 `style_references` 輸入互斥——只能提供其中一個。`style_id` 必須是有效的 UUID。`style_match` 輸入僅在提供風格時使用。風格參考圖像會於生成費用之外另行計費，且其總編碼大小不得超過 10 MB。`seed` 值不保證可重現圖像輸出。若你使用來自 Infinite Style Library 的風格 ID，請確認它不是 Vector art 風格，因為這可能會傳回 SVG 資料而非圖像。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的圖像或圖像批次。 | IMAGE |
| `style_id` | 此次生成所使用或建立的風格 ID。當提供風格參考圖像時，建立的風格會在此傳回以供重複使用；未使用風格時為空字串。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `690286e663f27b525e58f81a7f883e490dacd48c1a34ee7b8e9ad4efd9935ff1`
