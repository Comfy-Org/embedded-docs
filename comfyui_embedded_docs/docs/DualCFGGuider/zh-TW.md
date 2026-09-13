# 雙 CFG 引導器

Dual CFG Guider 節點會建立一個用於取樣的引導系統，使用兩個條件輸入及一個負向條件輸入。它會套用兩個獨立的引導尺度，以控制每個條件對生成結果的影響強度，並支援兩種結合這些尺度的方式：`"regular"` 和 `"nested"`。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於引導的模型 | MODEL | 是 | - |
| `cond1` | 第一個正向條件輸入 | CONDITIONING | 是 | - |
| `cond2` | 第二個條件輸入，用作第一個正向條件與負向條件之間的參考 | CONDITIONING | 是 | - |
| `負面` | 負向條件輸入 | CONDITIONING | 是 | - |
| `cfg 條件` | 套用於第一個正向條件的引導尺度（預設值：8.0） | FLOAT | 是 | 0.0 - 100.0 |
| `cfg cond2 負面` | 套用於第二個條件與負向條件之間的引導尺度（預設值：8.0） | FLOAT | 是 | 0.0 - 100.0 |
| `風格` | 要套用的引導風格（預設值："regular"）。設為 "nested" 時，引導會以巢狀方式套用 | COMBO | 是 | "regular"<br>"nested" |

注意：在 `regular` 風格中，`cfg_cond2_negative` 會套用在 `cond2` 與 `negative` 之間，而 `cfg_conds` 會套用在 `cond1` 與 `cond2` 之間。在 `nested` 風格中，`cfg_conds` 會先套用在 `cond1` 與 `cond2` 之間，然後使用 `cfg_cond2_negative` 將產生的預測引導遠離 `negative`。

注意：在 `regular` 風格中，當 `cfg_cond2_negative` 等於 1.0 時，會跳過負向條件；而當 `cfg_conds` 也等於 1.0 時，第二個條件也會被跳過。這會減少所執行的模型評估次數。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `GUIDER` | 已配置的引導系統，可供取樣使用 | GUIDER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
