# SenseNova Conditioning

為影像生成或交錯文字與影像輸出準備 SenseNova 條件資料。`task` 選擇器會設定提示詞模板與停止行為，且節點會回報模型是否需要影像，讓迴圈知道何時執行取樣器。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `clip` | SenseNova CLIP 模型，從 CLIP Text Encode 連接。除了傳入的條件資料已完成的情況外，所有任務皆需要此項。 | CLIP | 否 | - |
| `conditioning` | 來自 CLIP Text Encode 的 SenseNova 文字條件資料。 | CONDITIONING | 是 | - |
| `negative` | 選用的負向條件資料。在 `interleave` 與 `self-correction` 任務中會更新並回傳。 | CONDITIONING | 否 | - |
| `task` | 要執行的任務。`"image"` 會為標準取樣器編碼提示詞，`"image thinking"` 會讓模型在回答前先思考，`"interleave"` 會在一次處理中產生文字與影像，`"self-correction"` 會讓模型修正自己先前的輸出。 | DYNAMIC_COMBO | 是 | `"image"`<br>`"image thinking"`<br>`"interleave"`<br>`"self-correction"` |
| `max_tokens` | 本次呼叫期間產生的最大 token 數。預設：1024。 | INT | 是 | 1 至 8192 |

### `interleave` 輸入

當 `task` 設為 `"interleave"` 時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `thinking` | 讓模型在回答前先思考。預設：True。 | BOOLEAN | 是 | True<br>False |
| `samples` | 先前的取樣器輸出，在影像請求後繼續時連接。 | LATENT | 否 | - |

### `self-correction` 輸入

當 `task` 設為 `"self-correction"` 時，會顯示這些輸入。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `samples` | 先前的取樣器輸出，在影像請求後繼續時連接。 | LATENT | 否 | - |

**限制與行為：**

* `clip` 輸入需要 CLIP Text Encode 的 SenseNova CLIP 輸出；其他任何 CLIP 都會引發錯誤。
* `"image thinking"` 需要恰好一個正向條件項目；`"interleave"` 與 `"self-correction"` 需要一個正向與一個負向項目。
* 當模型正在等待影像時，將前一個取樣器的 LATENT 輸出連接到 `samples`。在尚未請求影像前傳入 `samples` 會造成錯誤。
* 當傳入的條件資料已完成時，節點會原樣回傳，其中 `generated_text` 為空，且 `image_requested` 設為 False。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `conditioning` | 供取樣器使用的條件資料，並擴充了本次呼叫產生的文字。 | CONDITIONING |
| `generated_text` | 本次呼叫產生的文字。若要取得完整結果，請使用 SenseNova Interleave Decode。 | STRING |
| `negative` | 用於 `interleave` 與 `self-correction` 任務的更新後負向條件資料。 | CONDITIONING |
| `image_requested` | 當模型要求影像時為 True：執行取樣器，然後將迴圈回饋至此節點。 | BOOLEAN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaConditioning/zh-TW.md)

---
**Source fingerprint (SHA-256):** `97fcdc26ccf80f48c5628f695a4ae8231b065b67414c93dec9bced6bb8d4c77c`
