# SamplerSASolver

SamplerSASolver 節點會為擴散模型建立並配置自訂取樣器。它使用 "sa_solver" 取樣演算法，搭配可配置的預測器-校正器方案與隨機微分方程 (SDE) 設定，並傳回一個可插入取樣節點中使用的取樣器物件。`sde_start_percent` 與 `sde_end_percent` 值會使用所連接模型的取樣排程轉換為 sigma 值，以定義隨機元件套用的區間。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於建構取樣器的擴散模型，其取樣排程會被使用 | MODEL | 是 | - |
| `eta` | 控制 SDE 求解器的步長縮放因子（預設：1.0） | FLOAT | 否 | 0.0 - 10.0 |
| `sde_start_percent` | 取樣過程中隨機（SDE）元件開始的起始百分比；會使用模型的排程轉換為 sigma 值（預設：0.2） | FLOAT | 否 | 0.0 - 1.0 |
| `sde_end_percent` | 取樣過程中隨機（SDE）元件停止的結束百分比；會使用模型的排程轉換為 sigma 值（預設：0.8） | FLOAT | 否 | 0.0 - 1.0 |
| `s_noise` | 控制取樣期間加入的雜訊量（預設：1.0） | FLOAT | 否 | 0.0 - 100.0 |
| `predictor_order` | 求解器中預測器元件的階數（預設：3） | INT | 否 | 1 - 6 |
| `corrector_order` | 求解器中校正器元件的階數（預設：4） | INT | 否 | 0 - 6 |
| `use_pece` | 啟用 PECE（Predict-Evaluate-Correct-Evaluate）方法（預設：停用） | BOOLEAN | 否 | - |
| `simple_order_2` | 啟用簡化的二階計算（預設：停用） | BOOLEAN | 否 | - |

所有可選輸入在介面中都會標記為進階。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 已配置的取樣器物件（使用 `sa_solver` 演算法），可供取樣節點使用 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/zh-TW.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
