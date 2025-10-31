> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DifferentialDiffusion/zh-TW.md)

{heading_overview}

Differential Diffusion 節點透過基於時間步閾值應用二值遮罩來修改去噪過程。它創建一個在原始去噪遮罩和基於閾值的二值遮罩之間混合的遮罩，從而允許對擴散過程強度進行受控調整。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `模型` | MODEL | 是 | - | 要修改的擴散模型 |
| `strength` | FLOAT | 否 | 0.0 - 1.0 | 控制原始去噪遮罩和二值閾值遮罩之間的混合強度（預設值：1.0） |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `模型` | MODEL | 帶有更新去噪遮罩功能的修改後擴散模型 |