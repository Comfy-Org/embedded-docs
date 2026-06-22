# LTXVContextWindows

此節點在取樣期間為類似 LTXV 的模型設定上下文視窗。它將影片生成過程劃分為重疊的視窗，以管理記憶體使用並改善時間連貫性。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 在取樣期間要套用上下文視窗的模型。 | MODEL | 是 | - |
| `context_length` | 上下文視窗的長度，以實際幀為單位。必須為 8*n + 1。（預設值：145） | INT | 是 | 最小值：1<br>最大值：nodes.MAX_RESOLUTION<br>步長：8 |
| `context_overlap` | 上下文視窗的重疊部分，以實際幀為單位。（預設值：40） | INT | 是 | 最小值：0<br>步長：8 |
| `context_schedule` | 上下文視窗的依步驟排程演算法。（預設值：UNIFORM_STANDARD） | COMBO | 是 | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `context_stride` | 上下文視窗的步長；僅適用於均勻排程。（預設值：1） | INT | 否 | 最小值：1 |
| `closed_loop` | 是否閉合上下文視窗迴圈；僅適用於循環排程。（預設值：False） | BOOLEAN | 否 | True<br>False |
| `fuse_method` | 用於融合上下文視窗的方法。（預設值：PYRAMID） | COMBO | 是 | 選項來自 comfy.context_windows.ContextFuseMethods.LIST_STATIC |
| `freenoise` | 是否套用 FreeNoise 噪聲洗牌，可改善視窗混合效果。（預設值：True） | BOOLEAN | 否 | True<br>False |
| `retain_first_frame` | 在每個上下文視窗中保留第一個潛在幀（可能有助於保留初始參考）。（預設值：False） | BOOLEAN | 否 | True<br>False |
| `split_conds_to_windows` | 是否根據區域索引將多個條件（由 ConditionCombine 建立）分割到每個視窗。（預設值：False） | BOOLEAN | 否 | True<br>False |

**注意：** `context_length` 參數必須遵循公式 8*n + 1，其中 n 為正整數。節點會自動調整數值以滿足此要求，方法是將實際幀轉換為潛在幀。`context_overlap` 也會從實際幀轉換為潛在幀（除以 8）。

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `MODEL` | 已套用上下文視窗以供取樣使用的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ad0b8c54acaab1853f6fe98dbad675478f033caf867df954b40b7db5208f5ae4`
