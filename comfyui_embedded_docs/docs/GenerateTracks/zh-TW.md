> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GenerateTracks/zh-TW.md)

`GenerateTracks` 節點會為影片生成建立多條平行運動路徑。它定義一條從起點到終點的主要路徑，然後生成一組與此路徑平行、間距均勻的軌道。您可以控制路徑的形狀（直線或貝茲曲線）、沿路徑移動的速度，以及軌道在哪些影格中可見。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | 是 | 16 - 4096 | 影片影格的寬度（像素）。預設值為 832。 |
| `height` | INT | 是 | 16 - 4096 | 影片影格的高度（像素）。預設值為 480。 |
| `start_x` | FLOAT | 是 | 0.0 - 1.0 | 起點位置的標準化 X 座標 (0-1)。預設值為 0.0。 |
| `start_y` | FLOAT | 是 | 0.0 - 1.0 | 起點位置的標準化 Y 座標 (0-1)。預設值為 0.0。 |
| `end_x` | FLOAT | 是 | 0.0 - 1.0 | 終點位置的標準化 X 座標 (0-1)。預設值為 1.0。 |
| `end_y` | FLOAT | 是 | 0.0 - 1.0 | 終點位置的標準化 Y 座標 (0-1)。預設值為 1.0。 |
| `num_frames` | INT | 是 | 1 - 1024 | 要生成軌道位置的總影格數。預設值為 81。 |
| `num_tracks` | INT | 是 | 1 - 100 | 要生成的平行軌道數量。預設值為 5。 |
| `track_spread` | FLOAT | 是 | 0.0 - 1.0 | 軌道之間的標準化距離。軌道垂直於運動方向展開。預設值為 0.025。 |
| `bezier` | BOOLEAN | 是 | True / False | 啟用使用中點作為控制點的貝茲曲線路徑。預設值為 False。 |
| `mid_x` | FLOAT | 是 | 0.0 - 1.0 | 貝茲曲線的標準化 X 控制點。僅在啟用 `bezier` 時使用。預設值為 0.5。 |
| `mid_y` | FLOAT | 是 | 0.0 - 1.0 | 貝茲曲線的標準化 Y 控制點。僅在啟用 `bezier` 時使用。預設值為 0.5。 |
| `interpolation` | COMBO | 是 | `"linear"`<br>`"ease_in"`<br>`"ease_out"`<br>`"ease_in_out"`<br>`"constant"` | 控制沿路徑移動的時間/速度。預設值為 "linear"。 |
| `track_mask` | MASK | 否 | - | 可選的遮罩，用於指示可見影格。 |

**注意：** `mid_x` 和 `mid_y` 參數僅在 `bezier` 參數設定為 `True` 時使用。當 `bezier` 為 `False` 時，路徑是從起點到終點的直線。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `TRACKS` | TRACKS | 一個軌道物件，包含所有影格中所有軌道的生成路徑座標和可見性資訊。 |
| `track_length` | INT | 生成軌道的影格數，與輸入的 `num_frames` 相符。 |

---
**Source fingerprint (SHA-256):** `3dca1cabaee8738e2a68acafed47ad347019d03c9b7f0d1392b3fdf97d0e8add`
