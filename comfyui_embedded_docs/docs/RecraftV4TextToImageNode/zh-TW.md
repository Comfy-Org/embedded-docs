# Recraft V4 文字轉圖像

此節點使用 Recraft V4 與 V4.1 AI 模型，根據文字描述生成影像。它會將提示詞與生成設定傳送至 Recraft 影像生成服務，並傳回產生的單張或多張影像。您可以選擇模型、影像尺寸，以及要生成的影像數量。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於生成的模型。選取模型會決定可用的 `size` 選項。 | DYNAMIC_COMBO | 是 | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | 影像生成的提示詞。最多 10,000 個字元。 | STRING | 是 | 1 至 10000 個字元 |
| `negative_prompt` | 此輸入會被忽略：Recraft V4 與 V4.1 模型不支援負面提示詞。 | STRING | 是 | N/A |
| `n` | 要生成的影像數量（預設：1）。 | INT | 是 | 1 至 6 |
| `seed` | 決定節點是否應重新執行的種子；無論種子為何，實際結果都是非確定性的（預設：0）。 | INT | 是 | 0 至 18446744073709551615 |
| `recraft_controls` | 透過 Recraft Controls 節點對生成過程進行的選用額外控制。 | CUSTOM | 否 | N/A |

### recraftv4_1、recraftv4_1_utility 與 recraftv4 的輸入

由 `recraftv4_1`、`recraftv4_1_utility` 與 `recraftv4` 模型共用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成影像的大小（預設：1024x1024）。 | COMBO | 是 | 多種選項可用（標準 Recraft V4 尺寸） |

### recraftv4_1_pro、recraftv4_1_utility_pro 與 recraftv4_pro 的輸入

由 `recraftv4_1_pro`、`recraftv4_1_utility_pro` 與 `recraftv4_pro` 模型共用。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size` | 生成影像的大小（預設：2048x2048）。 | COMBO | 是 | 多種選項可用（Pro Recraft V4 尺寸） |

**注意事項：**

- 當選取模型時，`size` 輸入會出現，其可用選項取決於模型：標準模型（`recraftv4_1`、`recraftv4_1_utility`、`recraftv4`）共用一組尺寸，而 Pro 模型（`recraftv4_1_pro`、`recraftv4_1_utility_pro`、`recraftv4_pro`）共用另一組尺寸。
- `negative_prompt` 輸入會在 UI 中顯示，但不會傳送給模型；Recraft V4 與 V4.1 模型不支援負面提示詞。
- `seed` 值僅決定當數值變更時節點是否重新執行；無論種子為何，實際影像結果都是非確定性的。
- 如果您透過 Recraft Controls 輸入使用 Infinite Style Library 的樣式 ID，請確保它不是向量藝術（Vector art）樣式，因為這可能會回傳 SVG 資料而非影像。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的單張影像或影像批次。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`
