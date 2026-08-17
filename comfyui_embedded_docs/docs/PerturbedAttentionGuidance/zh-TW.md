# 擾動注意力引導

PerturbedAttentionGuidance 節點對擴散模型應用擾動注意力引導，以提升生成品質。它在採樣期間修改模型的自注意力機制，將其替換為專注於值投影的簡化版本。此技術透過調整條件去噪過程，有助於改善生成圖像的連貫性與品質。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用擾動注意力引導的擴散模型 | MODEL | 是 | - |
| `scale` | 擾動注意力引導效果的強度（預設值：3.0）。設定為 0 時，此節點不產生任何效果，並回傳原始去噪結果。 | FLOAT | 是 | 0.0 - 100.0 |

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用擾動注意力引導的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1cf824486ae695a9e563c70a4798aaf4c9c067ae3b53172c9767e3c5093d0096`
