# SamplerER_SDE

SamplerER_SDE 節點為擴散模型提供了專用的取樣方法，內含三種求解器類型：ER-SDE、Reverse-time SDE 和 ODE。此節點可控制取樣過程中的隨機行為及計算階段數量。當選用 ODE 求解器或確定性配置（`eta`=0）時，節點會自動調整雜訊設定。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `solver_type` | 用於取樣的求解器類型。決定擴散過程的雜訊縮放行為（預設值："ER-SDE"）。 | COMBO | 是 | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" |
| `max_stage` | 取樣過程的最大階段數（預設值：3）。控制計算複雜度與品質。進階參數。 | INT | 是 | 1-3 |
| `eta` | SDE 的隨機強度。<br>當 eta=0 時，它們會簡化為確定性 ODE。<br>較大的 eta 可能導致無效輸出。如果發生這種情況，請嘗試降低此值。（預設值：1.0）。進階參數。 | FLOAT | 是 | 0.0-10.0 |
| `s_noise` | 取樣過程的雜訊縮放因子（預設值：1.0）。控制取樣期間套用的雜訊量。進階參數。 | FLOAT | 是 | 0.0-100.0 |

**參數限制：**

- 當 `solver_type` 為 "ODE" 或 `eta` 為 0 時，節點會強制將 `s_noise` 設為 0.0，並將求解器切換為 "ODE"。
- `eta` 同時影響 "ER-SDE" 和 "Reverse-time SDE" 求解器類型。較大的值可能導致無效輸出。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `sampler` | 一個已配置的取樣器物件，可在取樣管線中搭配指定的求解器設定使用。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5299ae9b45444cdc7c36bcb3c5e5a0600f9f904e57ae614554033434afdffd30`
