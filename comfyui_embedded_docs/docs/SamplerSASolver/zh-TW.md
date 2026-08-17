# SamplerSASolver

SamplerSASolver 節點實作了用於擴散模型的自訂取樣演算法。它使用帶有可設定階數設定的預測-校正方法，以及隨機微分方程（SDE）參數，從輸入模型生成樣本。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於取樣的擴散模型 | MODEL | Yes | - |
| `eta` | 控制步長縮放因子（預設值：1.0） | FLOAT | No | 0.0 - 10.0 |
| `sde_start_percent` | 去噪過程中SDE取樣開始的起始百分比，使用模型的取樣排程轉換為sigma值（預設值：0.2） | FLOAT | No | 0.0 - 1.0 |
| `sde_end_percent` | 去噪過程中SDE取樣結束的結束百分比，使用模型的取樣排程轉換為sigma值（預設值：0.8） | FLOAT | No | 0.0 - 1.0 |
| `s_noise` | 控制取樣期間添加的雜訊量（預設值：1.0） | FLOAT | No | 0.0 - 100.0 |
| `predictor_order` | 求解器中預測元件的階數（預設值：3） | INT | No | 1 - 6 |
| `corrector_order` | 求解器中校正元件的階數（預設值：4） | INT | No | 0 - 6 |
| `use_pece` | 啟用或停用 PECE（預測-評估-校正-評估）方法 | BOOLEAN | No | - |
| `simple_order_2` | 啟用或停用簡化的二階計算 | BOOLEAN | No | - |

注意：所有輸入參數（`model` 除外）皆為進階參數，在節點介面中預設為隱藏。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `sampler` | 可與擴散模型搭配使用的已設定取樣器物件 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/zh-TW.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
