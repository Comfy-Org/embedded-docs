# Recraft V4 文字轉向量圖

以下是將 Recraft V4 Text to Vector 節點文檔翻譯為繁體中文的結果：

---

Recraft V4 Text to Vector 節點會根據文字描述產生可縮放向量圖形（SVG）影像。此節點連接外部 API，使用 Recraft V4 與 V4.1 模型來產生影像。節點會根據您的提示輸出一個或多個 SVG 影像。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於產生影像的模型。選擇模型會變更可用的 `size` 選項。 | DYNAMIC_COMBO | 是 | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | 影像生成的提示詞。最多 10,000 個字元。 | STRING | 是 | N/A |
| `negative_prompt` | 此輸入會被忽略：Recraft V4 與 V4.1 模型不支援負面提示詞。 | STRING | 是 | N/A |
| `n` | 要產生的影像數量（預設值：1）。 | INT | 是 | 1 至 6 |
| `seed` | 用來決定節點是否應重新執行的種子；無論種子為何，實際結果都是非確定性的（預設值：0）。 | INT | 是 | 0 至 18446744073709551615 |
| `recraft_controls` | 透過 Recraft Controls 節點對產生過程的額外控制選項。 | CUSTOM | 否 | N/A |

### recraftv4_1_vector、recraftv4_1_utility_vector 與 recraftv4 輸入

這三個模型共享相同的 `size` 選項。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size` | 產生影像的大小（預設值：`"1024x1024"`）。 | COMBO | 是 | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### recraftv4_1_pro_vector、recraftv4_1_utility_pro_vector 與 recraftv4_pro 輸入

這三個模型共享相同的 `size` 選項。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size` | 產生影像的大小（預設值：`"2048x2048"`）。 | COMBO | 是 | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

**注意：** `size` 參數是動態輸入，其可用選項會根據所選的 `model` 而變更。`seed` 值不保證可從外部 API 獲得可重現的結果。`negative_prompt` 輸入會被忽略，因為 Recraft V4 與 V4.1 模型不支援負面提示詞。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 產生的可縮放向量圖形（SVG）影像。 | SVG |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `822f6b9fef67ef6beb1eba099c41c72570a1f79e316612201c81f6e5eb91408d`
