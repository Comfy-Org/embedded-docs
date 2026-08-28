# SamplerDPMPP_2M_SDE

SamplerDPMPP_2M_SDE 節點為擴散模型建立一個 DPM++ 2M SDE 取樣器。此取樣器使用二階微分方程求解器與隨機微分方程式來生成樣本。它提供不同的求解器類型和雜訊處理選項，以控制取樣過程。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `solver_type` | 取樣過程所使用的微分方程求解器類型（預設值："midpoint"） | COMBO | 是 | `"midpoint"`<br>`"heun"` |
| `eta` | 控制取樣過程的隨機性（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `s_noise` | 控制取樣期間添加的雜訊量（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `noise_device` | 執行雜訊計算的裝置。設定為 "cpu" 時，取樣器使用基於 CPU 的雜訊生成；設定為 "gpu" 時，使用基於 GPU 的雜訊生成，可能獲得更高的效能（預設值："gpu"） | COMBO | 是 | `"gpu"`<br>`"cpu"` |

注意：`eta`、`s_noise` 和 `noise_device` 被標記為進階參數，並顯示在節點介面的進階區段中。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 一個已配置的取樣器物件，可直接用於取樣流程 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/zh-TW.md)

---
**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`
