> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/zh-TW.md)

SamplerER_SDE 節點為擴散模型提供專門的取樣方法，提供不同的求解器類型，包括 ER-SDE、反向時間 SDE 和 ODE 方法。它允許控制取樣過程的隨機行為和計算階段。該節點會根據所選的求解器類型自動調整參數以確保正常功能。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `solver_type` | COMBO | 是 | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" | 用於取樣的求解器類型。決定擴散過程的數學方法。 |
| `max_stage` | INT | 是 | 1-3 | 取樣過程的最大階段數（預設值：3）。控制計算複雜度和品質。 |
| `eta` | FLOAT | 是 | 0.0-100.0 | 反向時間 SDE 的隨機強度（預設值：1.0）。當 eta=0 時，會簡化為確定性 ODE。此設定不適用於 ER-SDE 求解器類型。 |
| `s_noise` | FLOAT | 是 | 0.0-100.0 | 取樣過程的噪聲縮放因子（預設值：1.0）。控制取樣過程中應用的噪聲量。 |

**參數約束：**

- 當 `solver_type` 設定為 "ODE" 或使用 "Reverse-time SDE" 且 `eta`=0 時，無論用戶輸入值為何，`eta` 和 `s_noise` 都會自動設定為 0。
- `eta` 參數僅影響 "Reverse-time SDE" 求解器類型，對 "ER-SDE" 求解器類型沒有影響。

## 輸出參數

| 輸出名稱 | 資料類型 | 參數說明 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 一個配置好的取樣器物件，可在取樣流程中使用指定的求解器設定。 |