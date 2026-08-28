# 雙 CFG 引導器

The DualCFGGuider 節點會建立用於雙重無分類器引導取樣（dual classifier-free guidance sampling）的引導系統。它將兩個正向 conditioning 輸入與一個負向 conditioning 輸入結合，並套用兩個獨立的引導尺度（guidance scale），以控制每個 conditioning 對生成輸出的影響強度。它支援兩種結合這些引導尺度的樣式：「regular」與「nested」。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於引導的模型 | MODEL | 是 | - |
| `cond1` | 第一個正向 conditioning 輸入 | CONDITIONING | 是 | - |
| `cond2` | 第二個 conditioning 輸入，用作第一個正向 conditioning 與負向 conditioning 之間的參考 | CONDITIONING | 是 | - |
| `負面` | 負向 conditioning 輸入 | CONDITIONING | 是 | - |
| `cfg 條件` | 套用於第一個正向 conditioning 的引導尺度（預設：8.0） | FLOAT | 是 | 0.0 - 100.0 |
| `cfg cond2 負面` | 套用於第二個 conditioning 與負向 conditioning 之間的引導尺度（預設：8.0） | FLOAT | 是 | 0.0 - 100.0 |
| `風格` | 要套用的引導樣式（預設："regular"）。設為 "nested" 時，引導會以巢狀方式套用 | COMBO | 是 | "regular"<br>"nested" |

注意：在 `regular` 樣式中，`cfg_cond2_negative` 套用於 `cond2` 與 `negative` 之間，而 `cfg_conds` 套用於 `cond1` 與 `cond2` 之間。在 `nested` 樣式中，`cfg_conds` 先套用於 `cond1` 與 `cond2` 之間，然後使用 `cfg_cond2_negative` 將結果預測引導遠離 `negative`。

## 輸出
| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `GUIDER` | 已設定好的引導系統，可用於取樣 | GUIDER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ef28d109149cb545bcd76215fd99535905c1d395222149a029c1c210e2912e97`
