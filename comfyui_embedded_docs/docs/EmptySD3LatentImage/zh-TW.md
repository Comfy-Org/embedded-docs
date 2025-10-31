> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/zh-TW.md)

EmptySD3LatentImage 節點會建立一個專為 Stable Diffusion 3 模型格式化的空白潛在影像張量。它會生成一個填滿零值的張量，該張量具有 SD3 流程所需的正確維度和結構。這通常用作影像生成工作流程的起點。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `寬度` | INT | 是 | 16 至 MAX_RESOLUTION (間隔: 16) | 輸出潛在影像的寬度，單位為像素 (預設值: 1024) |
| `高度` | INT | 是 | 16 至 MAX_RESOLUTION (間隔: 16) | 輸出潛在影像的高度，單位為像素 (預設值: 1024) |
| `批次大小` | INT | 是 | 1 至 4096 | 批次中要生成的潛在影像數量 (預設值: 1) |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `LATENT` | LATENT | 包含具有 SD3 相容維度的空白樣本的潛在張量 |