> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/zh-TW.md)

WanCameraEmbedding 節點根據相機運動參數，使用 Plücker 嵌入生成相機軌跡嵌入。它會建立一系列模擬不同相機運動的相機姿態，並將其轉換為適用於影片生成管線的嵌入張量。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `相機姿勢` | COMBO | 是 | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" | 要模擬的相機運動類型（預設值："Static"） |
| `寬度` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影像的寬度，單位為像素（預設值：832，步進值：16） |
| `高度` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影像的高度，單位為像素（預設值：480，步進值：16） |
| `長度` | INT | 是 | 1 至 MAX_RESOLUTION | 相機軌跡序列的長度（預設值：81，步進值：4） |
| `速度` | FLOAT | 否 | 0.0 至 10.0 | 相機運動的速度（預設值：1.0，步進值：0.1） |
| `fx` | FLOAT | 否 | 0.0 至 1.0 | 焦距 x 參數（預設值：0.5，步進值：0.000000001） |
| `fy` | FLOAT | 否 | 0.0 至 1.0 | 焦距 y 參數（預設值：0.5，步進值：0.000000001） |
| `cx` | FLOAT | 否 | 0.0 至 1.0 | 主點 x 座標（預設值：0.5，步進值：0.01） |
| `cy` | FLOAT | 否 | 0.0 至 1.0 | 主點 y 座標（預設值：0.5，步進值：0.01） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `寬度` | TENSOR | 生成的相機嵌入張量，包含軌跡序列 |
| `高度` | INT | 用於處理的寬度值 |
| `長度` | INT | 用於處理的高度值 |
| `長度` | INT | 用於處理的長度值 |

---
**Source fingerprint (SHA-256):** `422c4a1fdfb6fd403afac26a609f80cbdbaa87f2c115068de9d7a33c756e71fd`
