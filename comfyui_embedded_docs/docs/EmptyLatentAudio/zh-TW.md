> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/zh-TW.md)

{heading_overview}

EmptyLatentAudio 節點為音訊處理建立空的潛在張量。它會生成具有指定持續時間和批次大小的空白音訊潛在表示，可用作音訊生成或處理工作流程的輸入。該節點會根據音訊持續時間和取樣率計算適當的潛在維度。

{heading_inputs}

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `秒數` | FLOAT | 是 | 1.0 - 1000.0 | 音訊的持續時間（單位：秒，預設值：47.6） |
| `批次大小` | INT | 是 | 1 - 4096 | 批次中的潛在影像數量（預設值：1） |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `LATENT` | LATENT | 返回具有指定持續時間和批次大小的空音訊處理潛在張量 |