> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/zh-TW.md)

Rodin 3D Smooth 節點透過 Rodin API 處理輸入圖像並將其轉換為平滑的 3D 模型，從而生成 3D 資產。該節點以多張圖像作為輸入，並產生可下載的 3D 模型檔案。此節點會自動處理整個生成流程，包括任務建立、狀態輪詢和檔案下載。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | 是 | - | 用於 3D 模型生成的輸入圖像 |
| `Seed` | INT | 是 | - | 用於生成一致性的隨機種子值 |
| `Material_Type` | STRING | 是 | - | 應用於 3D 模型的材質類型 |
| `Polygon_count` | STRING | 是 | - | 生成 3D 模型的目標多邊形數量 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | 已下載 3D 模型的檔案路徑 |