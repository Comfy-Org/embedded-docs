# DecimateMesh

DecimateMesh 會使用二次誤差度量（QEM）簡化方式，將 3D 網格簡化至目標面數，並在作用中的運算裝置上執行。`"midpoint"` 放置模式是 cumesh-faithful 預設，能在保留頭髮等纖細特徵的同時提供最佳品質；而 `"qem"` 則會將頂點放置在 QEM 最佳位置，並可選用線與特徵邊控制。輸出網格會維持焊接狀態。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mesh` | 要簡化的 3D 網格。 | MESH | 是 | - |
| `target_face_count` | 目標最大面數。設為 0 則停用簡化。（預設：200000） | INT | 是 | 0 到 50000000 |
| `placement_mode` | midpoint：cumesh-faithful（建議）。qem：QEM 最佳位置放置。（預設：`"midpoint"`） | DYNAMIC_COMBO | 是 | `"midpoint"`<br>`"qem"` |

### Midpoint 輸入

`"midpoint"` 放置模式不會顯示額外的子參數，而是使用預設的 midpoint 放置預設。

### QEM 輸入

以下子參數僅在 `placement_mode` 設定為 `"qem"` 時才會出現在介面中。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `line_quadric_weight` | 每條邊的線性二次型權重；保留銳利的稜線與谷線。0 為關閉。（預設：0.0） | FLOAT | 否 | 0.0 到 100.0 |
| `feature_edge_quadric_weight` | 二面角特徵邊（摺痕）上的額外二次型權重。0 為關閉。（預設：0.0） | FLOAT | 否 | 0.0 到 1000.0 |
| `feature_edge_min_dihedral_deg` | 將邊視為特徵邊所需的最小二面角（度數）。（預設：30.0） | FLOAT | 否 | 0.0 到 180.0 |
| `clamp_v_to_edge` | 將 QEM 最佳位置投影到坍縮後的邊線段上。（預設：true） | BOOLEAN | 否 | `true`<br>`false` |

注意：當 `target_face_count` 為 0，或網格的面數已少於目標值時，將跳過簡化。節點會顯示面數減少的摘要，例如 `faces: 1.23M → 200K (-84%)`。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `mesh` | 簡化後的網格，面數已減少；連通性保持焊接狀態。 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`
