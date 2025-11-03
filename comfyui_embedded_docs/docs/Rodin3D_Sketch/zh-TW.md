> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/zh-TW.md)

此節點使用 Rodin API 來生成 3D 資產。它接收輸入圖像並透過外部服務將其轉換為 3D 模型。該節點處理從任務創建到下載最終 3D 模型檔案的整個流程。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | 是 | - | 要轉換為 3D 模型的輸入圖像 |
| `Seed` | INT | 否 | 0-65535 | 用於生成的隨機種子值（預設值：0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | 生成的 3D 模型檔案路徑 |