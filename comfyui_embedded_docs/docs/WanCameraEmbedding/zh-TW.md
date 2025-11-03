> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/zh-TW.md)

WanCameraEmbedding 節點使用基於攝影機運動參數的 Plücker 嵌入來生成攝影機軌跡嵌入。它會創建一系列模擬不同攝影機運動的攝影機姿態，並將其轉換為適合影片生成流程的嵌入張量。

## 輸入參數

| 參數名稱 | 資料類型 | 是否必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `camera_pose` | COMBO | 是 | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" | 要模擬的攝影機運動類型（預設值："Static"） |
| `width` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出的寬度（單位：像素）（預設值：832，間隔：16） |
| `height` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出的高度（單位：像素）（預設值：480，間隔：16） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 攝影機軌跡序列的長度（預設值：81，間隔：4） |
| `speed` | FLOAT | 否 | 0.0 至 10.0 | 攝影機運動的速度（預設值：1.0，間隔：0.1） |
| `fx` | FLOAT | 否 | 0.0 至 1.0 | 焦距 x 參數（預設值：0.5，間隔：0.000000001） |
| `fy` | FLOAT | 否 | 0.0 至 1.0 | 焦距 y 參數（預設值：0.5，間隔：0.000000001） |
| `cx` | FLOAT | 否 | 0.0 至 1.0 | 主點 x 座標（預設值：0.5，間隔：0.01） |
| `cy` | FLOAT | 否 | 0.0 至 1.0 | 主點 y 座標（預設值：0.5，間隔：0.01） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `camera_embedding` | TENSOR | 生成的攝影機嵌入張量，包含軌跡序列 |
| `width` | INT | 用於處理的寬度數值 |
| `height` | INT | 用於處理的高度數值 |
| `length` | INT | 用於處理的長度數值 |