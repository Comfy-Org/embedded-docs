> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Detail/zh-TW.md)

Rodin 3D Detail 節點使用 Rodin API 生成詳細的 3D 資產。它接收輸入圖像並透過 Rodin 服務進行處理，以創建具有精細幾何結構和材質的高品質 3D 模型。該節點處理從任務創建到最終 3D 模型檔案下載的完整工作流程。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | 是 | - | 用於 3D 模型生成的輸入圖像 |
| `Seed` | INT | 是 | - | 用於可重現結果的隨機種子值 |
| `Material_Type` | STRING | 是 | - | 應用於 3D 模型的材質類型 |
| `Polygon_count` | STRING | 是 | - | 生成 3D 模型的目標多邊形數量 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | 生成的 3D 模型檔案路徑 |