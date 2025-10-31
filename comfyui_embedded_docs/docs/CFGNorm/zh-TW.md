> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/zh-TW.md)

{heading_overview}

CFGNorm 節點在擴散模型中對分類器自由引導（CFG）過程應用一種標準化技術。它透過比較條件輸出和無條件輸出的範數來調整去噪預測的尺度，然後應用強度乘數來控制效果。這有助於通過防止引導縮放中的極端值來穩定生成過程。

{heading_inputs}

| 參數 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | 必填 | - | - | 要應用 CFG 標準化的擴散模型 |
| `strength` | FLOAT | 必填 | 1.0 | 0.0 - 100.0 | 控制應用於 CFG 縮放的標準化效果的強度 |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `patched_model` | MODEL | 返回已在其採樣過程中應用 CFG 標準化的修改後模型 |