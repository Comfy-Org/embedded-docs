# WanMoveVisualizeTracks

WanMoveVisualizeTracks 節點會將運動追蹤資料繪製到一系列影像或視訊影格上。它會在每個追蹤點的目前位置放置一個圓圈，並繪製一條漸淡的軌跡線，顯示該點在最近幾個影格中的移動路徑。如果未提供任何追蹤資料，輸入影像將原樣回傳，不作變更。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 將在其上視覺化顯示追蹤軌跡的輸入影像或視訊影格序列。 | IMAGE | 是 | - |
| `tracks` | 包含點位置和可見性資訊的運動追蹤資料。若未提供，輸入影像將原樣直接通過，不作變更。 | TRACKS | 否 | - |
| `line_resolution` | 繪製每個追蹤點軌跡線時要使用的先前影格數（預設值：24）。 | INT | 是 | 1 - 1024 |
| `circle_size` | 在每個追蹤點的目前位置繪製的圓圈大小（預設值：12）。 | INT | 是 | 1 - 128 |
| `opacity` | 繪製的追蹤疊加層的不透明度（預設值：0.75）。 | FLOAT | 是 | 0.0 - 1.0 |
| `line_width` | 用於繪製追蹤路徑的線條寬度（預設值：16）。 | INT | 是 | 1 - 128 |

**注意：** 若輸入影像的數量與所提供的 `tracks` 資料中的影格數不符，輸入影像序列會重複以對齊追蹤資料。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 包含運動追蹤資料作為疊加層繪製的影像序列。若未提供任何 `tracks`，則會直接回傳原始輸入影像，不作變更。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d94bfde28dfdad682edcc81b1c63408f1352e0dbc94af4d043d750e8cd4c099b`
