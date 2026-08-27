# WanCamera嵌入

WanCameraEmbedding 節點會根據相機運動參數，使用 Plücker 嵌入來產生相機軌跡嵌入。它建立一系列模擬不同相機運動的相機姿態，並將其轉換為適合影片生成管線的嵌入張量。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `相機姿勢` | 要模擬的相機運動類型（預設值："Static"） | COMBO | 是 | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" |
| `寬度` | 輸出寬度（像素，預設值：832，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 輸出高度（像素，預設值：480，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `長度` | 相機軌跡序列的長度（預設值：81，步長：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `速度` | 相機運動的速度（預設值：1.0，步長：0.1） | FLOAT | 否 | 0.0 至 10.0 |
| `fx` | 焦距 x 參數（預設值：0.5，步長：0.000000001） | FLOAT | 否 | 0.0 至 1.0 |
| `fy` | 焦距 y 參數（預設值：0.5，步長：0.000000001） | FLOAT | 否 | 0.0 至 1.0 |
| `cx` | 主點 x 座標（預設值：0.5，步長：0.01） | FLOAT | 否 | 0.0 至 1.0 |
| `cy` | 主點 y 座標（預設值：0.5，步長：0.01） | FLOAT | 否 | 0.0 至 1.0 |

注意：`fx`、`fy`、`cx` 和 `cy` 是先進的相機內部參數。`speed` 參數會縮放所選相機運動的旋轉角度與平移距離。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `攝影機嵌入` | 包含軌跡序列的已產生相機嵌入張量 | TENSOR |
| `寬度` | 處理時使用的寬度值 | INT |
| `高度` | 處理時使用的高度值 | INT |
| `長度` | 處理時使用的長度值 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`
