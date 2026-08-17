# 上下文視窗（手動）

Context Windows (Manual) 節點可讓您在取樣期間手動設定模型的上下文窗口。它會以指定的長度、重疊和排程模式建立重疊的上下文區段，以便在維持區段間連續性的同時，以可管理的大小區塊處理資料。此節點提供進階選項來控制上下文窗口的套用方式，包括雜訊重新排列、條件保留、雜訊潛在變量保留，以及因果窗口修正。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用上下文窗口的模型（於取樣期間）。 | MODEL | 是 | - |
| `context_length` | 上下文窗口的長度（預設值：16）。 | INT | 否 | 1+ |
| `context_overlap` | 上下文窗口的重疊量（預設值：4）。 | INT | 否 | 0+ |
| `context_schedule` | 上下文窗口的步驟依賴排程演算法（預設值：STATIC_STANDARD）。 | COMBO | 否 | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | 上下文窗口的步幅；僅適用於均勻排程（預設值：1）。 | INT | 否 | 1+ |
| `closed_loop` | 是否封閉上下文窗口循環；僅適用於循環排程（預設值：False）。 | BOOLEAN | 否 | - |
| `fuse_method` | 用於融合上下文窗口的方法（預設值：PYRAMID）。 | COMBO | 否 | `"PYRAMID"`<br>`"LIST_STATIC"` |
| `dim` | 要套用上下文窗口的維度（預設值：0）。 | INT | 否 | 0-5 |
| `freenoise` | 是否套用 FreeNoise 雜訊重新排列，可改善窗口混合效果（預設值：False）。 | BOOLEAN | 否 | - |
| `cond_retain_index_list` | 要在每個窗口的條件張量中保留的潛在索引清單。對於 concat 風格的 I2V 模型（例如 Wan I2V、HunyuanVideo I2V、Cosmos I2V、SVD），編碼後的起始影像位於 c_concat 條件通道中；將此設為 '0' 將在每個窗口的子位置 0 保留該起始影像內容（預設值：""）。 | STRING | 否 | - |
| `split_conds_to_windows` | 是否根據區域索引將多個條件（由 ConditionCombine 建立）拆分到每個窗口（預設值：False）。 | BOOLEAN | 否 | - |
| `latent_retain_index_list` | 要在每個窗口的雜訊潛在變量本身中保留的潛在索引清單。適用於參考內容（例如起始影像）直接存在於雜訊潛在變量中，而非單獨的條件通道中的工作流程（例如 LTXV、AnimateDiff 這類 inplace 風格的 I2V）。與 `cond_retain_index_list` 無關（預設值：""）。 | STRING | 否 | - |
| `causal_window_fix` | 是否為非 0 索引的上下文窗口加入因果修正幀（預設值：True）。 | BOOLEAN | 否 | - |

**參數限制：**

- `context_stride` 僅在選擇均勻排程時使用
- `closed_loop` 僅適用於循環排程
- `dim` 必須介於 0 到 5（含）之間
- `cond_retain_index_list` 預期一個以逗號分隔的整數索引字串（例如 "0,1,2"）
- `latent_retain_index_list` 預期一個以逗號分隔的整數索引字串（例如 "0,1,2"），且獨立於 `cond_retain_index_list`

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 在取樣期間套用了上下文窗口的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/zh-TW.md)

---
**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`
