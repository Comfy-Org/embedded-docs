# 雙 CFG 引導器

DualCFGGuider 節點建立一個用於雙重無分類器引導取樣的引導系統。它將兩個正向條件輸入與一個負向條件輸入結合，對每個條件對套用不同的引導比例，以控制每個提示對生成輸出的影響強度。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於引導的模型。 | MODEL | 是 | - |
| `cond1` | 第一個正向條件輸入。 | CONDITIONING | 是 | - |
| `cond2` | 第二個正向條件輸入，作為中間條件處理。 | CONDITIONING | 是 | - |
| `negative` | 負向條件輸入。 | CONDITIONING | 是 | - |
| `cfg_conds` | 套用於 `cond1` 和 `cond2` 之間的引導比例（預設值：8.0）。 | FLOAT | 是 | 0.0 - 100.0 |
| `cfg_cond2_negative` | 套用於 `cond2` 和負向條件之間的引導比例（預設值：8.0）。 | FLOAT | 是 | 0.0 - 100.0 |
| `style` | 要套用的引導樣式（預設值："regular"）。"regular" 在一步中結合兩個引導比例；"nested" 先套用 `cfg_conds`，然後相對於負向條件，使用 `cfg_cond2_negative` 對結果進行縮放。 | COMBO | 是 | "regular"<br>"nested" |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `GUIDER` | 已配置的引導系統，可直接用於取樣。 | GUIDER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
