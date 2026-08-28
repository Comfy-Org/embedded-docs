# DecimateMesh

DecimateMesh 使用二次誤差度量（QEM）簡化技術，將 3D 網格簡化為目標面數，並在目前啟用的計算設備上執行運算。`"midpoint"` 放置模式是 cumesh-faithful 預設，可在保留頭髮等細微特徵的同時提供最佳品質；而 `"qem"` 模式則將頂點放置在 QEM 最佳位置，並提供可選的線條與特徵邊緣控制。輸出的網格保持焊接（welded）狀態。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `網格` | 要簡化的 3D 網格。 | MESH | 是 | - |
| `target_face_count` | 目標最大面數。設為 0 會停用此功能。（預設：200000） | INT | 是 | 0 至 50000000 |
| `placement_mode` | midpoint：cumesh-faithful（建議）。qem：QEM 最佳放置。（預設：`"midpoint"`） | DYNAMIC_COMBO | 是 | `"midpoint"`<br>`"qem"` |

### Midpoint 輸入

`"midpoint"` 放置模式不會顯示額外的子參數；它使用預設的 midpoint 放置預設。

### QEM 輸入

下列子參數僅在 `placement_mode` 設定為 `"qem"` 時才會出現在介面中。

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `line_quadric_weight` | 每條邊的線性二次（line-quadric）權重；可保留銳利的山脊與山谷。0 = 關閉。（預設：0.0） | FLOAT | 否 | 0.0 至 100.0 |
| `feature_edge_quadric_weight` | 二面角特徵邊緣（摺痕）上的額外二次權重。0 = 關閉。（預設：0.0） | FLOAT | 否 | 0.0 至 1000.0 |
| `feature_edge_min_dihedral_deg` | 將邊緣視為特徵邊緣的最小二面角（度數）。（預設：30.0） | FLOAT | 否 | 0.0 至 180.0 |
| `clamp_v_to_edge` | 將 QEM 最佳位置投影到坍縮後的邊緣線段上。（預設：true） | BOOLEAN | 否 | `true`<br>`false` |

注意：當 `target_face_count` 為 0，或網格的面數已少於目標值時，將跳過簡化（Decimation）操作。節點會在其上顯示面數減少摘要，例如 `faces: 1.23M → 200K (-84%)`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `網格` | 面數減少後的簡化網格；連通性保持焊接狀態。 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`
