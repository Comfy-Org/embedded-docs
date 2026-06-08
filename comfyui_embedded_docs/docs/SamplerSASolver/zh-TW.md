## 概述

SamplerSASolver 節點為擴散模型實現了自訂取樣演算法。它採用預測-校正方法，搭配可設定的階數設定與隨機微分方程（SDE）參數，從輸入模型生成樣本。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於取樣的擴散模型 | MODEL | 是 | - |
| `eta` | 控制步長縮放因子（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `sde_start_percent` | SDE 取樣的起始百分比（預設值：0.2） | FLOAT | 否 | 0.0 - 1.0 |
| `sde_end_percent` | SDE 取樣的結束百分比（預設值：0.8） | FLOAT | 否 | 0.0 - 1.0 |
| `s_noise` | 控制取樣過程中添加的噪聲量（預設值：1.0） | FLOAT | 否 | 0.0 - 100.0 |
| `predictor_order` | 求解器中預測元件的階數（預設值：3） | INT | 否 | 1 - 6 |
| `corrector_order` | 求解器中校正元件的階數（預設值：4） | INT | 否 | 0 - 6 |
| `use_pece` | 啟用或停用 PECE（預測-評估-校正-評估）方法 | BOOLEAN | 否 | - |
| `simple_order_2` | 啟用或停用簡化二階計算 | BOOLEAN | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sampler` | 一個已設定的取樣器物件，可與擴散模型搭配使用 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3de8834281c09d0bd1435e29f0c9ae540a2ea42db142277d07cb655ccf814873`
