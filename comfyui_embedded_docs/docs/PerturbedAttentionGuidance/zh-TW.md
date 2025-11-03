> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerturbedAttentionGuidance/zh-TW.md)

{heading_overview}

PerturbedAttentionGuidance 節點對擴散模型應用擾動注意力引導，以提升生成品質。它在採樣過程中修改模型的自注意力機制，將其替換為專注於值投影的簡化版本。此技術透過調整條件去噪過程，有助於改善生成圖像的連貫性和品質。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要應用擾動注意力引導的擴散模型 |
| `scale` | FLOAT | 否 | 0.0 - 100.0 | 擾動注意力引導效果的強度（預設值：3.0） |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用擾動注意力引導的修改後模型 |