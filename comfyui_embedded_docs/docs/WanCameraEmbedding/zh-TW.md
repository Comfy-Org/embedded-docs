# WanCamera嵌入

此節點會使用 Plücker embeddings 為您選擇的相機路徑生成相機軌跡嵌入。它會建立一系列相機姿態，以模擬平移、縮放或旋轉等運動，並將它們轉換為可用於影片生成管線的嵌入張量。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `相機姿勢` | 要模擬的相機運動類型（預設："Static"） | COMBO | 是 | "Static"<br>"Pan Up"<br>"Pan Down"<br>"Pan Left"<br>"Pan Right"<br>"Zoom In"<br>"Zoom Out"<br>"Anti Clockwise (ACW)"<br>"ClockWise (CW)" |
| `寬度` | 輸出的寬度，單位為像素（預設：832，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 輸出的高度，單位為像素（預設：480，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `長度` | 相機軌跡序列的長度（預設：81，步長：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `速度` | 相機移動速度（預設：1.0，步長：0.1） | FLOAT | 否 | 0.0 至 10.0 |
| `fx` | 焦距 x 參數（預設：0.5，步長：0.000000001） | FLOAT | 否 | 0.0 至 1.0 |
| `fy` | 焦距 y 參數（預設：0.5，步長：0.000000001） | FLOAT | 否 | 0.0 至 1.0 |
| `cx` | 主點 x 座標（預設：0.5，步長：0.01） | FLOAT | 否 | 0.0 至 1.0 |
| `cy` | 主點 y 座標（預設：0.5，步長：0.01） | FLOAT | 否 | 0.0 至 1.0 |

注意：`fx`、`fy`、`cx` 和 `cy` 是進階相機內參參數。`speed` 參數會縮放所選相機運動的旋轉角度與平移距離。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `camera_embedding` | 生成的相機嵌入張量，包含軌跡序列 | TENSOR |
| `width` | 用於處理的寬度值 | INT |
| `height` | 用於處理的高度值 | INT |
| `length` | 用於處理的長度值 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraEmbedding/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1a2f98d83d18033581823dee61b5a3686d560c749c55223f81febca89654a29f`
