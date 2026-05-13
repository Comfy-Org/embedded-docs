> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/zh-TW.md)

## 概述

SamplerSASolver 節點為擴散模型實現了自訂取樣演算法。它採用預測-校正方法，搭配可設定的階數設定與隨機微分方程（SDE）參數，從輸入模型生成樣本。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 用於取樣的擴散模型 |
| `eta` | FLOAT | 否 | 0.0 - 10.0 | 控制步長縮放因子（預設值：1.0） |
| `sde_start_percent` | FLOAT | 否 | 0.0 - 1.0 | SDE 取樣的起始百分比（預設值：0.2） |
| `sde_end_percent` | FLOAT | 否 | 0.0 - 1.0 | SDE 取樣的結束百分比（預設值：0.8） |
| `s_noise` | FLOAT | 否 | 0.0 - 100.0 | 控制取樣過程中添加的噪聲量（預設值：1.0） |
| `predictor_order` | INT | 否 | 1 - 6 | 求解器中預測元件的階數（預設值：3） |
| `corrector_order` | INT | 否 | 0 - 6 | 求解器中校正元件的階數（預設值：4） |
| `use_pece` | BOOLEAN | 否 | - | 啟用或停用 PECE（預測-評估-校正-評估）方法 |
| `simple_order_2` | BOOLEAN | 否 | - | 啟用或停用簡化二階計算 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 一個已設定的取樣器物件，可與擴散模型搭配使用 |

---
**Source fingerprint (SHA-256):** `3de8834281c09d0bd1435e29f0c9ae540a2ea42db142277d07cb655ccf814873`
