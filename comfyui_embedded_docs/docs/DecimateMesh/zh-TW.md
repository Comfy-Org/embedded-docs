# 簡化網格

使用 QEM（quadric error metric，二次誤差度量）簡化，在作用中的運算裝置上執行計算，將 3D 網格簡化至目標面數。`"midpoint"` 放置模式是 cumesh-faithful 預設集，可提供最佳品質，同時保留頭髮等薄特徵；而 `"qem"` 則將頂點放置在 QEM 最佳位置，並提供可選的線與特徵邊控制。輸出網格保持焊接狀態。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `網格` | 要簡化的 3D 網格。 | MESH | 是 | - |
| `target_face_count` | 目標最大面數。0 表示停用。（預設值：200000） | INT | 是 | 0 至 50000000 |
| `placement_mode` | midpoint：cumesh-faithful（建議）。qem：QEM 最佳放置。（預設值：`"midpoint"`） | DYNAMIC_COMBO | 是 | `"midpoint"`<br>`"qem"` |

### Midpoint 輸入

`"midpoint"` 放置模式不會公開額外的子參數；它使用預設的 midpoint 放置預設集。

### QEM 輸入

下列子參數僅在 `placement_mode` 設為 `"qem"` 時才會顯示於介面中。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `line_quadric_weight` | 每條邊的線二次誤差權重；可保留銳利的脊線/谷線。0 = 關閉。（預設值：0.0） | FLOAT | 否 | 0.0 至 100.0 |
| `feature_edge_quadric_weight` | 二面角特徵邊（摺痕）上的額外二次誤差權重。0 = 關閉。（預設值：0.0） | FLOAT | 否 | 0.0 至 1000.0 |
| `feature_edge_min_dihedral_deg` | 將邊視為特徵邊的最小二面角（度）。（預設值：30.0） | FLOAT | 否 | 0.0 至 180.0 |
| `clamp_v_to_edge` | 將 QEM 最佳位置投影到塌縮的邊段上。（預設值：true） | BOOLEAN | 否 | `true`<br>`false` |

注意：當 `target_face_count` 為 0，或網格面數已不超過目標值時，會跳過簡化。此節點會在其自身上顯示面數縮減摘要，例如 `faces: 1.23M → 200K (-84%)`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `mesh` | 簡化後的網格，具有縮減後的面數；連接性保持焊接。 | MESH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/zh-TW.md)

---
**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`
