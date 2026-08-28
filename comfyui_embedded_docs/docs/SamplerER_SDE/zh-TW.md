# SamplerER_SDE

SamplerER_SDE 節點為擴散模型提供專門的取樣方法，支援不同的求解器類型：ER-SDE、Reverse-time SDE 和 ODE。它讓您控制取樣過程的隨機行為和計算階段數量。該節點會根據所選的求解器類型自動調整設定，以確保取樣器正常運作。

## 輸入

| 參數 | 描述 | 資料型態 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `solver_type` | 用於取樣的求解器類型。決定擴散過程的數學方法（預設值："ER-SDE"）。 | COMBO | 是 | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" |
| `max_stage` | 取樣過程的最大階段數（預設值：3）。控制計算複雜度和品質。 | INT | 是 | 1-3 |
| `eta` | SDE 的隨機強度。<br>當 eta=0 時，它們會簡化為確定性 ODE。<br>較大的 eta 可能導致無效輸出。若發生此情況，請嘗試調低此值。（預設值：1.0） | FLOAT | 是 | 0.0-10.0 (step: 0.01) |
| `s_noise` | 取樣過程的雜訊縮放因子（預設值：1.0）。控制取樣期間套用的雜訊量。 | FLOAT | 是 | 0.0-100.0 (step: 0.01) |

**參數約束：**

- 當 `solver_type` 設定為「ODE」或 `eta` 為 0 時，節點會切換至 ODE 模式，並將 `s_noise` 設定為 0.0，無論為 `s_noise` 輸入的值為何。
- `eta` 參數控制「ER-SDE」和「Reverse-time SDE」兩種求解器類型的隨機強度。當求解器以 ODE 模式執行時，此參數不產生效果。

## 輸出

| 輸出名稱 | 描述 | 資料型態 |
| --- | --- | --- |
| `sampler` | 一個已設定的取樣器物件，可在取樣管線中使用，內含指定的求解器設定。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5299ae9b45444cdc7c36bcb3c5e5a0600f9f904e57ae614554033434afdffd30`
