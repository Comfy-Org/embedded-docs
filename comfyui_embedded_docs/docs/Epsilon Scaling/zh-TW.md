# Epsilon縮放

此節點實作了研究論文《Elucidating the Exposure Bias in Diffusion Models》（arxiv.org/abs/2308.15321v6）中的 Epsilon Scaling 方法。其運作原理是在取樣過程中縮放預測的噪聲，以幫助減少曝光偏差，從而提升生成圖像的品質。此實作採用論文所建議的「均勻調度」（uniform schedule），因其具備實用性與有效性。

## 輸入

| 參數 | 描述 | 資料類型 | 必需 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 將套用 epsilon scaling 修補的模型。 | MODEL | 是 | - |
| `縮放係數` | 縮放預測噪聲的因子。大於 1.0 的值會減少噪聲，小於 1.0 的值則會增加噪聲（預設值：1.005）。這是進階參數。 | FLOAT | 否 | 0.5 - 1.5 (step: 0.001) |

注意：如果 `scaling_factor` 設定為 0，節點會自動將其替換為一個非常小的值（1e-9），以防止除以零。UI 的最小值 0.5 通常可以防止這種情況發生。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 輸入模型的修補版本，其取樣過程已套用 epsilon scaling 函數。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`
