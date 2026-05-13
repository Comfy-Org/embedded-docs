> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/zh-TW.md)

# OptimalStepsScheduler 節點

OptimalStepsScheduler 節點根據所選的模型類型和步數配置，計算擴散模型的噪聲調度 sigma 值。它會根據去噪參數調整總步數，並對噪聲級別進行插值以匹配所需的步數。該節點返回一系列 sigma 值，這些值決定了擴散採樣過程中使用的噪聲級別。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model_type` | COMBO | 是 | "FLUX"<br>"Wan"<br>"Chroma" | 用於噪聲級別計算的擴散模型類型 |
| `步驟數` | INT | 是 | 3-1000 | 要計算的總採樣步數（預設值：20） |
| `去雜訊強度` | FLOAT | 否 | 0.0-1.0 | 控制去噪強度，用於調整有效步數（預設值：1.0） |

**注意：** 當 `denoise` 設定為小於 1.0 時，節點會將有效步數計算為 `steps * denoise`。如果 `denoise` 設定為 0.0，節點將返回一個空張量。

## 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | 代表擴散採樣噪聲調度的 sigma 值序列 |

---
**Source fingerprint (SHA-256):** `4379171dc6d525a1ece514fdd11a95bfd92ed0c8b301f69ca718c1a3256b9590`
