> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/zh-TW.md)

## 概述

上下文視窗（手動）節點允許您在取樣過程中手動為模型配置上下文視窗。它會建立具有指定長度、重疊和排程模式的重疊上下文區段，以便在區段之間保持連續性的同時，將資料處理成可管理的區塊。此節點提供進階選項來控制上下文視窗的應用方式，包括雜訊洗牌、條件保留和因果視窗修正。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `模型` | MODEL | 是 | - | 在取樣期間要套用上下文視窗的模型。 |
| `上下文長度` | INT | 否 | 1+ | 上下文視窗的長度（預設值：16）。 |
| `上下文重疊` | INT | 否 | 0+ | 上下文視窗的重疊量（預設值：4）。 |
| `上下文排程` | COMBO | 否 | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` | 上下文視窗的步幅。 |
| `上下文步幅` | INT | 否 | 1+ | 上下文視窗的步幅；僅適用於均勻排程（預設值：1）。 |
| `閉環` | BOOLEAN | 否 | - | 是否閉合上下文視窗迴圈；僅適用於循環排程（預設值：False）。 |
| `融合方法` | COMBO | 否 | `PYRAMID`<br>`LIST_STATIC` | 用於融合上下文視窗的方法（預設值：PYRAMID）。 |
| `維度` | INT | 否 | 0-5 | 要套用上下文視窗的維度（預設值：0）。 |
| `自由雜訊` | BOOLEAN | 否 | - | 是否套用 FreeNoise 雜訊洗牌，可改善視窗混合效果（預設值：False）。 |
| `cond_retain_index_list` | STRING | 否 | - | 要在每個視窗的條件張量中保留的潛在索引列表，例如設定為 '0' 將對每個視窗使用初始起始影像（預設值：""）。 |
| `split_conds_to_windows` | BOOLEAN | 否 | - | 是否根據區域索引將多個條件（由 ConditionCombine 建立）分割到每個視窗（預設值：False）。 |
| `causal_window_fix` | BOOLEAN | 否 | - | 是否為非 0 索引的上下文視窗添加因果修正幀（預設值：True）。 |

**參數限制：**

- `context_stride` 僅在選擇均勻排程時使用
- `closed_loop` 僅適用於循環排程
- `dim` 必須介於 0 到 5 之間（含）
- `cond_retain_index_list` 預期為字串形式的逗號分隔整數索引列表（例如 "0,1,2"）

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `模型` | MODEL | 在取樣期間已套用上下文視窗的模型。 |

---
**Source fingerprint (SHA-256):** `b05ddda0ba38588305e6f733cd218c8b462268c39d16226ca961d09054187261`
