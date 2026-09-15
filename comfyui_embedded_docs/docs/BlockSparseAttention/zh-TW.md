# 模型區塊稀疏注意力

**Block Sparse Attention** 節點會修改模型，使其注意力層只專注於輸入中最相關的部分，而非一次處理全部內容，藉此減少長序列所需的運算量。節省的幅度會隨序列長度增加而提升，因為短序列通常使用一般（稠密）注意力會更快。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要套用修補的模型。 | MODEL | 是 | N/A |
| `selection` | 用於挑選完整 token 層級注意力之關鍵區塊的方法（介面顯示為 `method`）。<br>`sol-attn`：Sparsifying Online Attention 會為每個注意力頭與查詢區塊使用免訓練的自適應閾值。<br>`sla`：Sparse-Linear Attention 會保留固定比例的最高分關鍵區塊；僅適用於以此模式訓練的模型權重。<br>`vsa`：Video Sparse Attention（FastVideo）使用 3D 影片立方體切分與學習式粗略注意力分支；需要 FastH3 模型權重。 | DYNAMIC_COMBO | 是 | `"sol-attn"`<br>`"sla"`<br>`"vsa"` |
| `start_percent` | 稀疏注意力開始的百分比位置。在此位置之前，注意力維持稠密。預設值：0.2。 | FLOAT | 否 | min: 0.0, max: 1.0, step: 0.01 |
| `end_percent` | 稀疏注意力結束的百分比位置。在此位置之後，注意力回到稠密。預設值：1.0。 | FLOAT | 否 | min: 0.0, max: 1.0, step: 0.01 |
| `dense_blocks` | 永遠以稠密方式執行的 Transformer 區塊，例如 '0, 1, 47-49'。預設值：""（空）。進階輸入。 | STRING | 否 | 預設值："" |
| `min_tokens` | 短於此值的序列維持稠密。預設值：12288。進階輸入。 | INT | 否 | min: 0, max: 1048576, step: 512 |
| `extra_tokens` | 每個查詢區塊在其選定區塊之外，額外關注的最高分 token 數量。數值越大越接近稠密，但注意力時間也越長；建議 256，設為 0 則停用。VSA 會忽略此參數。預設值：256。進階輸入。 | INT | 否 | min: 0, max: 256, step: 64 |
| `sink_conditioning` | 僅適用於 MiniMax-H3。`exact_kv`：每個查詢都會精確關注打包的文字／音訊／參考資料列（約 3% 成本）。`exact_kv_and_rows`：額外以稠密方式執行目標音訊查詢列（維持生成的音訊完整）。`off` 會停用此行為。預設值："exact_kv_and_rows"。進階輸入。 | COMBO | 否 | `"exact_kv"`<br>`"exact_kv_and_rows"`<br>`"off"` |
| `verbose` | 記錄每個注意力形狀使用稀疏注意力，或維持稠密的原因。預設值：False。進階輸入。 | BOOLEAN | 否 | 預設值：False |

### sol-attn 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `tau` | 分數分布標準差中的閾值。數值越高越稀疏：1.0 會保留約 16% 的關鍵區塊為精確，1.5 約 7%，2.0 約 2.7%。預設值：1.3。 | FLOAT | 否 | min: 0.0, max: 4.0, step: 0.05 |

### sla 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `keep_percent` | 每個查詢區塊精確保留的關鍵區塊百分比（sink 與對角線會額外附加其上）。SLA 風格的 LoRA 蒸餾即是針對此選擇；若無此類 LoRA，數值越高越接近稠密。預設值：10.0。 | FLOAT | 否 | min: 0.5, max: 95.0, step: 0.5 |

### vsa 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `keep_percent` | 每個查詢立方體保留的影片立方體百分比；FastH3-VSA 檢查點是以 10 進行訓練。若模型具有 `to_gate_compress` 層，粗略分支會使用這些層。預設值：10.0。 | FLOAT | 否 | min: 0.5, max: 95.0, step: 0.5 |

**注意：** 介面中僅會顯示屬於目前所選方法的參數。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `model` | 已套用區塊稀疏注意力的模型。 | MODEL |

## 限制與約束

- 短於 `min_tokens` 的序列、列於 `dense_blocks` 中的區塊，以及在 `start_percent` 到 `end_percent` 範圍之外的取樣步驟，都會退回使用由 Model Attention Backend 節點所選的稠密模型注意力後端。
- 選用 `vsa` 方法時會忽略 `extra_tokens`。此時會記錄一則訊息，因為 VSA 權重是針對其稀疏模式訓練的。
- `vsa` 方法需要 MiniMax-H3 模型；使用任何其他模型都會引發錯誤。若模型缺少 `to_gate_compress` 層，精細階段會在沒有粗略分支的情況下執行，並記錄一則警告。
- 對於未回報區塊索引的模型，`dense_blocks` 會被忽略；啟用 `verbose` 時，日誌中會註明此情況。
- `sink_conditioning` 僅適用於所回報配置與目前序列長度相符的 MiniMax-H3 模型。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0c34876b49a04db0ab265526e2bb5f784e150591aab631713ad2ab420a3327c4`
