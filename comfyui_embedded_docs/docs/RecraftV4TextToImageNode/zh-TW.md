# Recraft V4 文字轉圖像

使用 Recraft V4 和 V4.1 模型從文字提示生成圖像。它會將提示與所選設定傳送至 Recraft API，並傳回生成的一張或多張圖像。若使用樣式參考圖像，也會傳回建立的樣式 ID。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於生成的模型。recraftv4_styles 模型專為樣式一致的生成而設計，並且一律需要 `style_id` 或 `style_references`。 | DYNAMIC_COMBO | 是 | "recraftv4_1"<br>"recraftv4_1_utility"<br>"recraftv4_1_pro"<br>"recraftv4_1_utility_pro"<br>"recraftv4"<br>"recraftv4_pro"<br>"recraftv4_styles"<br>"recraftv4_styles_pro" |
| `prompt` | 用於圖像生成的提示。最多 10,000 個字元。 | STRING | 是 | 1 到 10000 個字元 |
| `negative_prompt` | 此輸入會被忽略：Recraft V4 和 V4.1 模型不支援負面提示。 | STRING | 是 | N/A |
| `n` | 要生成的圖像數量（預設值：1）。 | INT | 是 | 1 到 6 |
| `seed` | 用於決定節點是否應重新執行的種子；無論種子為何，實際結果皆不具確定性（預設值：0）。 | INT | 是 | 0 到 18446744073709551615 |
| `recraft_controls` | 透過 Recraft Controls 節點對生成作業進行可選的額外控制。 | CUSTOM | 否 | N/A |
| `style_id` | 要套用的 Recraft V4 樣式 UUID，例如來自 Recraft V4 Create Style 節點，或先前執行之 `style_id` 輸出。不能與 `style_references` 合併使用（預設值：空）。 | STRING | 否 | 有效的 UUID 字串 |
| `style_match` | 遵循樣式的緊密程度：`precise` 會詳細重現樣式，`flexible` 則符合整體外觀。僅在提供樣式時使用（預設值："precise"）。 | COMBO | 否 | "precise"<br>"flexible" |

### recraftv4_1、recraftv4_1_utility、recraftv4 和 recraftv4_styles 輸入

這些模型共用相同的 `size` 參數。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成圖像的大小（預設值："1024x1024"）。 | COMBO | 是 | 有多個可用選項（標準 Recraft V4 尺寸；包含 "1024x1024"） |

### recraftv4_1_pro、recraftv4_1_utility_pro、recraftv4_pro 和 recraftv4_styles_pro 輸入

這些模型共用相同的 `size` 參數。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成圖像的大小（預設值："2048x2048"）。 | COMBO | 是 | 有多個可用選項（pro Recraft V4 尺寸；包含 "2048x2048"） |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `style_references` | 用於即時建立樣式的參考圖像，會在生成費用之外另行計費。建立的樣式會以 `style_id` 傳回以供重複使用。不能與 `style_id` 合併使用。可擴充槽位：連接 1..N 張圖像（`style_reference_1`、`style_reference_2`、...）。 | IMAGE | 否 | 0 到 Recraft API 允許的參考圖像數量上限；總編碼大小不得超過 10 MB |

**注意：** `size` 參數是動態輸入，其可用選項會根據所選的 `model` 而改變。`recraftv4_styles` 和 `recraftv4_styles_pro` 模型一律需要樣式：連接樣式參考圖像或提供 `style_id`。`style_id` 與 `style_references` 輸入互斥——只能提供其中一個。`style_id` 必須是有效的 UUID。`style_match` 輸入僅在提供樣式時使用。樣式參考圖像會在生成費用之外另行計費，且其總編碼大小不得超過 10 MB。`seed` 值不保證可重現的圖像輸出。若您使用來自 Infinite Style Library 的樣式 ID，請確認它不是 Vector art 樣式，因為這可能會傳回 SVG 資料而非圖像。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的圖像或一批圖像。 | IMAGE |
| `style_id` | 此生成所使用的或建立的樣式 ID。當提供樣式參考圖像時，建立的樣式會在此傳回以供重複使用；未使用樣式時為空字串。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `af5c1f68e59ca282cdca7c32cd50f0438b743fdda27d9d22e59b2d1343f45e26`
