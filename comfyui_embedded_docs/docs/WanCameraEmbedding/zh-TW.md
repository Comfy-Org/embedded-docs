# WanCamera嵌入

WanCameraEmbedding 節點根據相機運動參數，使用 Plücker 嵌入生成相機軌跡嵌入。它建立一系列模擬不同相機運動的相機姿態，並將其轉換為適合影片生成管線的嵌入張量。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `camera_pose` | 要模擬的相機運動類型（預設值："Static"） | COMBO | 是 | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" |
| `width` | 輸出的寬度（像素）（預設值：832，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 輸出的高度（像素）（預設值：480，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `length` | 相機軌跡序列的長度（預設值：81，步長：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `speed` | 相機移動的速度（預設值：1.0，步長：0.1） | FLOAT | 否 | 0.0 to 10.0 |
| `fx` | 焦距 x 參數（預設值：0.5，步長：0.000000001） | FLOAT | 否 | 0.0 to 1.0 |
| `fy` | 焦距 y 參數（預設值：0.5，步長：0.000000001） | FLOAT | 否 | 0.0 to 1.0 |
| `cx` | 主點 x 座標（預設值：0.5，步長：0.01） | FLOAT | 否 | 0.0 to 1.0 |
| `cy` | 主點 y 座標（預設值：0.5，步長：0.01） | FLOAT | 否 | 0.0 to 1.0 |

注意：`fx`、`fy`、`cx` 和 `cy` 是進階參數。`length` 參數使用步長 4，因為第一個相機幀會在內部重複，所以實際處理的序列長度變為 `length + 3`。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `camera_embedding` | 包含軌跡序列的生成相機嵌入張量 | TENSOR |
| `width` | 用於處理的寬度值 | INT |
| `height` | 用於處理的高度值 | INT |
| `length` | 用於處理的長度值 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`
