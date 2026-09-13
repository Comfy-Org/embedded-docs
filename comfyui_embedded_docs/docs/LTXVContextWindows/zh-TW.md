# LTXV 上下文視窗

此節點會在取樣期間為類似 LTXV 的模型設定上下文視窗。它會將生成過程分割為重疊視窗，以協助管理記憶體使用量並改善時序一致性。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要在取樣期間套用上下文視窗的模型。 | MODEL | 是 | - |
| `context_length` | 上下文視窗的長度，以實際影格為單位。必須為 8*n + 1。（預設值：145） | INT | 是 | 最小值：1<br>最大值：nodes.MAX_RESOLUTION<br>步長：8 |
| `context_overlap` | 上下文視窗的重疊量，以實際影格為單位。（預設值：40） | INT | 是 | 最小值：0<br>步長：8 |
| `context_schedule` | 取決於步驟的上下文視窗排程演算法。（預設值："UNIFORM_STANDARD"） | COMBO | 是 | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | 上下文視窗的步幅；僅適用於均勻排程。（預設值：1） | INT | 是 | 最小值：1 |
| `closed_loop` | 是否關閉上下文視窗迴圈；僅適用於循環排程。（預設值：False） | BOOLEAN | 是 | True<br>False |
| `fuse_method` | 用於融合上下文視窗的方法。可用選項由 `ContextFuseMethods.LIST_STATIC` 定義。（預設值："PYRAMID"） | COMBO | 是 | 由 `ContextFuseMethods.LIST_STATIC` 定義 |
| `freenoise` | 是否套用 FreeNoise 雜訊重排；可改善視窗混合。（預設值：True） | BOOLEAN | 是 | True<br>False |
| `retain_first_frame` | 在每個上下文視窗中保留第一個潛在影格（可能有助於保留初始參考）。（預設值：False） | BOOLEAN | 是 | True<br>False |
| `split_conds_to_windows` | 是否根據區域索引，將多個條件（由 ConditionCombine 建立）拆分到每個視窗。（預設值：False） | BOOLEAN | 是 | True<br>False |

**注意：** `context_length` 的值以實際影格提供，並在內部使用公式 `((context_length - 1) // 8) + 1` 轉換為潛在影格，最小值為 1。`context_overlap` 的值同樣以實際影格提供，並透過整數除以 8 轉換為潛在影格，最小值為 0。`context_length` 的工具提示指出其必須遵循 8*n + 1 的模式。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 已套用上下文視窗以供取樣使用的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/zh-TW.md)

---
**Source fingerprint (SHA-256):** `148649d0a938e08c932a163f5d7614332626fba37b8f79db7f92bbcf422e692f`
