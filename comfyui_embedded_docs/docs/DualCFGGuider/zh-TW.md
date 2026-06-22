# 雙 CFG 引導器

## 概述

DualCFGGuider 節點建立了一個用於雙重無分類器引導取樣的引導系統。它將兩個正向條件輸入與一個負向條件輸入結合，對每個條件配對應用不同的引導尺度，以控制每個提示對生成輸出的影響。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於引導的模型 | MODEL | 是 | - |
| `cond1` | 第一個正向條件輸入 | CONDITIONING | 是 | - |
| `cond2` | 第二個正向條件輸入 | CONDITIONING | 是 | - |
| `負面` | 負向條件輸入 | CONDITIONING | 是 | - |
| `cfg 條件` | 第一個正向條件的引導尺度（預設值：8.0） | FLOAT | 是 | 0.0 - 100.0 |
| `cfg cond2 負面` | 第二個正向與負向條件的引導尺度（預設值：8.0） | FLOAT | 是 | 0.0 - 100.0 |
| `風格` | 要套用的引導風格（預設值："regular"）。設為 "nested" 時，引導將以巢狀方式套用 | COMBO | 是 | "regular"<br>"nested" |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `GUIDER` | 一個已配置完成的引導系統，可供取樣使用 | GUIDER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/zh-TW.md)

---
**Source fingerprint (SHA-256):** `802e07f2e64dc2d55e86290db7e94dffd46079a9180480a560035d0bb6350325`
