# GenerateTracks

`GenerateTracks` 節點會為影片生成建立多條平行運動路徑。它定義一條從起點到終點的主要路徑，然後生成一組與此路徑平行、間距均勻的軌道。您可以控制路徑的形狀（直線或貝茲曲線）、沿路徑移動的速度，以及軌道在哪些影格中可見。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `width` | 影片影格的寬度（像素）。預設值為 832。 | INT | 是 | 16 - 4096 |
| `height` | 影片影格的高度（像素）。預設值為 480。 | INT | 是 | 16 - 4096 |
| `start_x` | 起點位置的標準化 X 座標 (0-1)。預設值為 0.0。 | FLOAT | 是 | 0.0 - 1.0 |
| `start_y` | 起點位置的標準化 Y 座標 (0-1)。預設值為 0.0。 | FLOAT | 是 | 0.0 - 1.0 |
| `end_x` | 終點位置的標準化 X 座標 (0-1)。預設值為 1.0。 | FLOAT | 是 | 0.0 - 1.0 |
| `end_y` | 終點位置的標準化 Y 座標 (0-1)。預設值為 1.0。 | FLOAT | 是 | 0.0 - 1.0 |
| `num_frames` | 要生成軌道位置的總影格數。預設值為 81。 | INT | 是 | 1 - 1024 |
| `num_tracks` | 要生成的平行軌道數量。預設值為 5。 | INT | 是 | 1 - 100 |
| `track_spread` | 軌道之間的標準化距離。軌道垂直於運動方向展開。預設值為 0.025。 | FLOAT | 是 | 0.0 - 1.0 |
| `bezier` | 啟用使用中點作為控制點的貝茲曲線路徑。預設值為 False。 | BOOLEAN | 是 | True / False |
| `mid_x` | 貝茲曲線的標準化 X 控制點。僅在啟用 `bezier` 時使用。預設值為 0.5。 | FLOAT | 是 | 0.0 - 1.0 |
| `mid_y` | 貝茲曲線的標準化 Y 控制點。僅在啟用 `bezier` 時使用。預設值為 0.5。 | FLOAT | 是 | 0.0 - 1.0 |
| `interpolation` | 控制沿路徑移動的時間/速度。預設值為 "linear"。 | COMBO | 是 | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` |
| `track_mask` | 可選的遮罩，用於指示可見影格。 | MASK | 否 | - |

**注意：** `mid_x` 和 `mid_y` 參數僅在 `bezier` 參數設定為 `True` 時使用。當 `bezier` 為 `False` 時，路徑是從起點到終點的直線。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `track_length` | 一個軌道物件，包含所有影格中所有軌道的生成路徑座標和可見性資訊。 | TRACKS |
| `track_length` | 生成軌道的影格數，與輸入的 `num_frames` 相符。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3dca1cabaee8738e2a68acafed47ad347019d03c9b7f0d1392b3fdf97d0e8add`
