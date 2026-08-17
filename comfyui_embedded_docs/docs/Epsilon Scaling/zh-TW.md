# Epsilon縮放

此節點實作了研究論文《Elucidating the Exposure Bias in Diffusion Models》（arxiv.org/abs/2308.15321v6）中的 Epsilon Scaling 方法。其運作方式是在取樣過程中縮放預測的雜訊，以幫助減少曝光偏差，從而提升生成圖像的品質。此實作採用了論文所推薦的「均勻排程」（uniform schedule），因為它兼具實用性與有效性。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 將套用 epsilon scaling 修補程式的模型。 | MODEL | 是 | - |
| `scaling_factor` | 預測雜訊的縮放因子。數值大於 1.0 會減少預測雜訊，而小於 1.0 則會增加（預設值：1.005）。 | FLOAT | 是 | 0.5 - 1.5 (step: 0.001) |

注意：`scaling_factor` 已防止數值為零，以避免除以零的情況。UI 會強制最小值為 0.5，因此在正常使用下不會發生此問題。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 輸入模型的修補副本，其取樣過程已套用 epsilon scaling 函式。原始模型保持不變。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`
