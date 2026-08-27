# SamplerSASolver

SamplerSASolver 節點為擴散模型實現了自訂採樣演算法。它使用可配置階數設定的預測-校正方法，以及隨機微分方程（SDE）參數，從輸入模型生成樣本。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於採樣的擴散模型 | MODEL | 是 | - |
| `eta` | 控制步長縮放因子（預設值：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `sde_start_percent` | SDE 採樣的起始百分比（預設值：0.2） | FLOAT | 否 | 0.0 - 1.0 |
| `sde_end_percent` | SDE 採樣的結束百分比（預設值：0.8） | FLOAT | 否 | 0.0 - 1.0 |
| `s_noise` | 控制採樣過程中新增的雜訊量（預設值：1.0） | FLOAT | 否 | 0.0 - 100.0 |
| `predictor_order` | 求解器中預測元件的階數（預設值：3） | INT | 否 | 1 - 6 |
| `corrector_order` | 求解器中校正元件的階數（預設值：4） | INT | 否 | 0 - 6 |
| `use_pece` | 啟用或停用 PECE（預測-評估-校正-評估）方法 | BOOLEAN | 否 | - |
| `simple_order_2` | 啟用或停用簡化的二階計算 | BOOLEAN | 否 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 一個已設定的採樣器物件，可與擴散模型一起使用 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/zh-TW.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
