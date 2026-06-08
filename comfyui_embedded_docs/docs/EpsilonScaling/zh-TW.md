實作了研究論文《Elucidating the Exposure Bias in Diffusion Models》中的 Epsilon Scaling 方法。此方法透過在取樣過程中縮放預測的雜訊來改善樣本品質。它使用均勻排程來減輕擴散模型中的曝光偏差。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 epsilon 縮放的模型 | MODEL | 是 | - |
| `scaling_factor` | 用於縮放預測雜訊的因子（預設值：1.005） | FLOAT | 否 | 0.5 - 1.5 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 epsilon 縮放的模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/zh-TW.md)
