# Recraft V4 文字轉圖像

Recraft V4 文字轉圖片

此節點使用 Recraft V4 與 V4.1 AI 模型，根據文字描述生成圖片。它會將您的提示詞傳送至外部 API，並返回生成的圖片。您可以透過指定模型、圖片尺寸、圖片數量，以及可選的樣式（以已儲存的樣式 ID 或參考圖片提供）來控制輸出。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於生成的模型。recraftv4_styles 模型專為樣式一致性生成而設計，且一律需要 style_id 或 style_references。 | DYNAMIC_COMBO | 是 | "recraftv4_1"<br>"recraftv4_1_utility"<br>"recraftv4_1_pro"<br>"recraftv4_1_utility_pro"<br>"recraftv4"<br>"recraftv4_pro"<br>"recraftv4_styles"<br>"recraftv4_styles_pro" |
| `prompt` | 圖片生成的提示詞。最多 10,000 個字元。 | STRING | 是 | 1 至 10000 個字元 |
| `negative_prompt` | 此輸入會被忽略：Recraft V4 與 V4.1 模型不支援負面提示詞。 | STRING | 是 | N/A |
| `n` | 要生成的圖片數量（預設值：1）。 | INT | 是 | 1 至 6 |
| `seed` | 用於決定節點是否重新執行的種子；無論種子為何，實際結果皆為非確定性（預設值：0）。 | INT | 是 | 0 至 18446744073709551615 |
| `recraft_controls` | 透過 Recraft Controls 節點對生成進行的可選額外控制。 | CUSTOM | 否 | N/A |
| `style_id` | 要套用的 Recraft V4 樣式 UUID，例如來自 Recraft V4 Create Style 節點，或先前執行產生的 style_id 輸出。不能與 style_references 同時使用（預設值：空）。 | STRING | 否 | 有效的 UUID 字串 |
| `style_match` | 遵循樣式的程度：precise 會精細地重現細節，flexible 則符合整體外觀。僅在提供樣式時使用（預設值："precise"）。 | COMBO | 否 | "precise"<br>"flexible" |

### recraftv4_1、recraftv4_1_utility、recraftv4 與 recraftv4_styles 輸入

這些模型共用相同的 `size` 參數。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成圖片的尺寸（預設值："1024x1024"）。 | COMBO | 是 | 提供多種選項（標準 Recraft V4 尺寸，包含 "1024x1024"） |

### recraftv4_1_pro、recraftv4_1_utility_pro、recraftv4_pro 與 recraftv4_styles_pro 輸入

這些模型共用相同的 `size` 參數。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成圖片的尺寸（預設值："2048x2048"）。 | COMBO | 是 | 提供多種選項（Pro 版 Recraft V4 尺寸，包含 "2048x2048"） |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `style_references` | 用於即時建立樣式的參考圖片，費用會額外加在生成費用之上。建立的樣式會以 style_id 回傳以供重複使用。不能與 style_id 同時使用。可擴充槽位：可連接 1..N 張圖片（style_reference_1、style_reference_2、...）。 | IMAGE | 否 | 0 至 Recraft API 允許的最大參考圖片數量；編碼後總大小不得超過 10 MB |

**注意：** `size` 參數是一個動態輸入，其可用選項會依所選的 `model` 而改變。`recraftv4_styles` 與 `recraftv4_styles_pro` 模型一律需要樣式：請連接樣式參考圖片或提供 `style_id`。`style_id` 與 `style_references` 輸入互斥——僅需提供其中一個。`style_id` 必須是有效的 UUID。`style_match` 輸入僅在提供樣式時使用。樣式參考圖片會額外計費，且編碼後總大小不得超過 10 MB。`seed` 值不保證能產生可重現的圖片輸出。如果您使用 Infinite Style Library 中的樣式 ID，請確認它不是向量藝術樣式，因為這可能會回傳 SVG 資料而非圖片。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的圖片或圖片批次。 | IMAGE |
| `style_id` | 本次生成所使用或建立的樣式 ID。當提供了樣式參考圖片時，建立的樣式會在此回傳以供重複使用；若未使用任何樣式，則為空字串。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `af5c1f68e59ca282cdca7c32cd50f0438b743fdda27d9d22e59b2d1343f45e26`
