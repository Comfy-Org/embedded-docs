# SamplerDPMPP_2M_SDE

SamplerDPMPP_2M_SDE 節點為擴散模型建立 DPM++ 2M SDE 取樣器。此取樣器將二階多步求解器與隨機微分方程（SDE）雜訊結合以生成樣本。它提供不同的求解器類型和雜訊處理選項來控制取樣過程。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `solver_type` | 取樣期間要使用的微分方程求解器類型：「midpoint」或「heun」（預設值：「midpoint」） | COMBO | 是 | "midpoint"<br>"heun" |
| `eta` | 控制取樣過程中的隨機性（randomness）程度（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `s_noise` | 控制取樣期間新增的雜訊量（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `noise_device` | 用於雜訊計算的裝置。「gpu」在 GPU 上執行雜訊生成，可能獲得較高效能；「cpu」使用 CPU（預設值：「gpu」） | COMBO | 是 | "gpu"<br>"cpu" |

注意：當 `noise_device` 設定為「cpu」時，節點建立 `dpmpp_2m_sde` 取樣器。設定為「gpu」時，則建立 `dpmpp_2m_sde_gpu` 變體，它會在 GPU 上執行與雜訊相關的計算。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `sampler` | 已設定的取樣器物件，可用於取樣管線中 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/zh-TW.md)

---
**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`
