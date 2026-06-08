## 概述

ModelMergeAuraflow 節點允許您透過調整各個模型元件的特定混合權重，將兩個不同的模型融合在一起。它提供了從初始層到最終輸出的精細控制，讓您能夠精確掌控模型不同部分的合併方式。此節點特別適合用於建立自訂模型組合，並對合併過程進行精確控制。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型 1` | 要合併的第一個模型 | MODEL | 是 | - |
| `模型 2` | 要合併的第二個模型 | MODEL | 是 | - |
| `init_x_linear.` | 初始線性轉換的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `positional_encoding` | 位置編碼元件的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `cond_seq_linear.` | 條件序列線性層的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `register_tokens` | 令牌註冊元件的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `t_embedder.` | 時間嵌入元件的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `double_layers.0.` | 雙層群組 0 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `double_layers.1.` | 雙層群組 1 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `double_layers.2.` | 雙層群組 2 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `double_layers.3.` | 雙層群組 3 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.0.` | 單層 0 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.1.` | 單層 1 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.2.` | 單層 2 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.3.` | 單層 3 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.4.` | 單層 4 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.5.` | 單層 5 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.6.` | 單層 6 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.7.` | 單層 7 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.8.` | 單層 8 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.9.` | 單層 9 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.10.` | 單層 10 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.11.` | 單層 11 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.12.` | 單層 12 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.13.` | 單層 13 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.14.` | 單層 14 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.15.` | 單層 15 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.16.` | 單層 16 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.17.` | 單層 17 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.18.` | 單層 18 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.19.` | 單層 19 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.20.` | 單層 20 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.21.` | 單層 21 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.22.` | 單層 22 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.23.` | 單層 23 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.24.` | 單層 24 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.25.` | 單層 25 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.26.` | 單層 26 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.27.` | 單層 27 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.28.` | 單層 28 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.29.` | 單層 29 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.30.` | 單層 30 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `single_layers.31.` | 單層 31 的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `modF.` | modF 元件的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |
| `final_linear.` | 最終線性轉換的混合權重（預設值：1.0） | FLOAT | 是 | 0.0 - 1.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 根據指定的混合權重，結合兩個輸入模型特徵的合併模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c4959321bba252eb24c945343198d72f50d6021d4dac9945f94e3eb28f1bc3c9`
