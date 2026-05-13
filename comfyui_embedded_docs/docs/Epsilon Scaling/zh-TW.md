> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon Scaling/zh-TW.md)

# Epsilon Scaling 節點

此節點實作了研究論文《Elucidating the Exposure Bias in Diffusion Models》（arxiv.org/abs/2308.15321v6）中的 Epsilon Scaling 方法。其運作原理是在取樣過程中對預測的噪聲進行縮放，以幫助減少曝光偏差，從而提升生成圖像的品質。此實作採用論文推薦的「統一排程」，兼具實用性與有效性。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 將套用 epsilon 縮放修補的模型。 |
| `scaling_factor` | FLOAT | 否 | 0.5 - 1.5 | 預測噪聲的縮放因子。數值大於 1.0 會減少噪聲，小於 1.0 則會增加噪聲（預設值：1.005）。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 輸入模型的修補版本，其取樣過程已套用 epsilon 縮放函數。 |

---
**Source fingerprint (SHA-256):** `85c464ce0b2ec2a031a01d9eef5d50fd300be3012499cc061705fb7964110882`
