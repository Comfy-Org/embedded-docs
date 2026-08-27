# 上下文視窗（手動）

Context Windows (Manual) 節點可讓您在採樣期間手動設定模型的上下文視窗，建立具有指定長度、重疊量與排程模式的重疊上下文區段，以便在維持區段之間連續性的同時，將資料以可管理的區塊進行處理。它提供了進階選項來控制上下文視窗的套用方式，包括雜訊洗牌、conditioning 保留與因果視窗修正。此節點為實驗性功能。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 在採樣期間要套用上下文視窗的模型。 | MODEL | 是 | - |
| `上下文長度` | 上下文視窗的長度（預設值：16）。 | INT | 是 | 1+ |
| `上下文重疊` | 上下文視窗的重疊量（預設值：4）。 | INT | 是 | 0+ |
| `上下文排程` | 上下文視窗的依步驟排程演算法（預設值：STATIC_STANDARD）。 | COMBO | 是 | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `上下文步幅` | 上下文視窗的步幅；僅適用於均勻排程（預設值：1）。 | INT | 是 | 1+ |
| `閉環` | 是否關閉上下文視窗迴圈；僅適用於循環排程（預設值：False）。 | BOOLEAN | 是 | - |
| `融合方法` | 用於融合上下文視窗的方法（預設值：PYRAMID）。 | COMBO | 是 | 靜態融合方法（參見 `ContextFuseMethods.LIST_STATIC`） |
| `維度` | 要套用上下文視窗的維度（預設值：0）。 | INT | 是 | 0-5 |
| `自由雜訊` | 是否套用 FreeNoise 雜訊洗牌，可改善視窗混合效果（預設值：False）。 | BOOLEAN | 是 | - |
| `cond_retain_index_list` | 要在每個視窗的 conditioning 張量中保留的 latent 索引清單。對於 concat 風格的 I2V 模型（例如 Wan I2V、HunyuanVideo I2V、Cosmos I2V、SVD），編碼後的起始影像位於 c_concat conditioning 通道中；將此設定為 '0' 會在每個視窗的 sub-pos 0 保留該起始影像內容（預設值：""）。 | STRING | 否 | - |
| `split_conds_to_windows` | 是否根據區域索引將多個 conditioning（由 ConditionCombine 建立）拆分到每個視窗（預設值：False）。 | BOOLEAN | 否 | - |
| `latent_retain_index_list` | 要在每個視窗的雜訊 latent 本身中保留的 latent 索引清單。適用於參考內容（例如起始影像）直接存在於雜訊 latent 中，而非獨立 conditioning 通道中的工作流程（例如 LTXV、AnimateDiff 等 inplace 風格 I2V）。與 cond_retain_index_list 無關（預設值：""）。 | STRING | 否 | - |
| `causal_window_fix` | 是否對非 0 索引的上下文視窗加入因果修正幀（causal fix frame）（預設值：True）。 | BOOLEAN | 否 | - |

**參數限制：**

- `context_stride` 僅在選擇均勻排程（`UNIFORM_STANDARD` 或 `UNIFORM_LOOPED`）時使用。
- `closed_loop` 僅適用於循環排程（`UNIFORM_LOOPED`）。
- `dim` 必須介於 0 到 5（含）之間。
- `cond_retain_index_list` 和 `latent_retain_index_list` 預期使用字串形式的逗號分隔整數索引清單（例如 "0,1,2"）。
- `latent_retain_index_list` 與 `cond_retain_index_list` 無關。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 在採樣期間套用了上下文視窗的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/zh-TW.md)

---
**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`
