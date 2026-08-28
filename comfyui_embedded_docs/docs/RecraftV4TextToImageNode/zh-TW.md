# Recraft V4 文字轉圖像

此節點使用 Recraft V4 和 V4.1 AI 模型，根據文字描述產生影像。它會將您的提示詞傳送至外部 API，並回傳產生的影像。您可以透過指定模型、影像尺寸和要建立的影像數量來控制輸出。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於生成所採用的模型。 | DYNAMIC_COMBO | 是 | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | 影像生成的提示詞。上限為 10,000 個字元。 | STRING | 是 | N/A |
| `negative_prompt` | 此輸入會被忽略：Recraft V4 和 V4.1 模型不支援負面提示詞。 | STRING | 是 | N/A |
| `n` | 要生成的影像數量（預設：1）。 | INT | 是 | 1 到 6 |
| `seed` | 用於決定節點是否應重新執行的種子；實際結果不具確定性，與種子無關（預設：0）。 | INT | 是 | 0 到 18446744073709551615 |
| `recraft_controls` | 透過 Recraft Controls 節點對生成過程進行的額外控制（選用）。 | CUSTOM | 否 | N/A |

### recraftv4_1、recraftv4_1_utility 與 recraftv4 輸入

由 `recraftv4_1`、`recraftv4_1_utility` 和 `recraftv4` 共用。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size` | 產生的影像尺寸（預設："1024x1024"）。 | COMBO | 是 | 多種選項（標準 Recraft V4 尺寸，包含 "1024x1024"） |

### recraftv4_1_pro、recraftv4_1_utility_pro 與 recraftv4_pro 輸入

由 `recraftv4_1_pro`、`recraftv4_1_utility_pro` 和 `recraftv4_pro` 共用。

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size` | 產生的影像尺寸（預設："2048x2048"）。 | COMBO | 是 | 多種選項（pro Recraft V4 尺寸，包含 "2048x2048"） |

**注意：** `size` 參數是動態輸入，可用的選項會依所選的 `model` 而改變。`seed` 值不保證能重現相同的影像輸出。如果您使用 Infinite Style Library 中的樣式 ID，請確認它不是向量藝術樣式，因為這可能會回傳 SVG 資料而非影像。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 產生的單張影像或一批影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`
