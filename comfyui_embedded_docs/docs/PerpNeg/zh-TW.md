> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNeg/zh-TW.md)

{heading_overview}

PerpNeg 節點對模型的取樣過程應用垂直負向引導。此節點修改模型的配置函數，以使用負向條件和縮放因子來調整噪聲預測。該節點已被棄用，並由 PerpNegGuider 節點取代以提供更佳功能。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要應用垂直負向引導的模型 |
| `empty_conditioning` | CONDITIONING | 是 | - | 用於負向引導計算的空條件 |
| `neg_scale` | FLOAT | 否 | 0.0 - 100.0 | 負向引導的縮放因子（預設值：1.0） |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用垂直負向引導的修改後模型 |

**注意**：此節點已被棄用，並由 PerpNegGuider 取代。它被標記為實驗性節點，不應在生產工作流程中使用。