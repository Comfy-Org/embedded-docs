> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/zh-TW.md)

Rodin3D_Gen2 節點使用 Rodin API 來生成 3D 資產。它接收輸入圖像並將其轉換為具有各種材質類型和多邊形數量的 3D 模型。此節點會自動處理整個生成過程，包括任務建立、狀態輪詢和檔案下載。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | 是 | - | 用於 3D 模型生成的輸入圖像 |
| `Seed` | INT | 否 | 0-65535 | 用於生成的隨機種子值（預設值：0） |
| `Material_Type` | COMBO | 否 | "PBR"<br>"Shaded" | 應用於 3D 模型的材質類型（預設值："PBR"） |
| `Polygon_count` | COMBO | 否 | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" | 生成 3D 模型的目標多邊形數量（預設值："500K-Triangle"） |
| `TAPose` | BOOLEAN | 否 | - | 是否應用 TAPose 處理（預設值：False） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | 生成的 3D 模型的檔案路徑 |