# Meshy: Image to Model (Smart Topology)

此節點使用 Meshy T2.5，從參考影像生成可直接用於遊戲的三角網格，並達到目標面數。拓撲會依所請求的多邊形數量建構，而不是事後再進行面數削減，因此結果可直接用於遊戲引擎，無需另外執行重拓撲處理。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要用於生成的 Meshy 模型版本。 | COMBO | 是 | `"meshy-t2.5"` |
| `image` | 用於生成模型的參考影像。 | IMAGE | 是 | - |
| `target_polycount` | 生成網格中三角形的近似數量。預設：15000。 | INT | 是 | 100 至 30000 |
| `should_texture` | 決定是否產生貼圖。`"false"` 會略過貼圖階段並傳回未貼圖的網格。 | DYNAMIC_COMBO | 是 | `"true"`<br>`"false"` |
| `enable_pbr` | 除了基礎顏色外，還產生 PBR 貼圖（金屬度、粗糙度、法線）。只有在 `should_texture` 設為 `"true"` 時，此輸入才可用。預設：`False`。 | BOOLEAN | 否 | - |
| `texture_prompt` | 用於引導貼圖流程的文字提示。最多 800 個字元。不能與 `texture_image` 同時使用。只有在 `should_texture` 設為 `"true"` 時，此輸入才可用。預設：`""`（空字串）。 | STRING | 否 | 1 至 800 個字元 |
| `texture_image` | 貼圖流程的參考影像。同一時間只能使用 `texture_image` 或 `texture_prompt` 其中之一。只有在 `should_texture` 設為 `"true"` 時，此輸入才可用。 | IMAGE | 否 | - |
| `texture_resolution` | 貼圖解析度。較高解析度可捕捉更多表面細節。只有在 `should_texture` 設為 `"true"` 時，此輸入才可用。 | COMBO | 否 | `"2k"`<br>`"4k"`<br>`"8k"` |
| `pose_mode` | 生成角色的姿勢。空字串表示不指定特定姿勢。這是進階設定。預設：`""`（空字串）。 | COMBO | 是 | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果都是非確定性的。預設：42。 | INT | 是 | 0 至 2147483647 |

**注意：** `enable_pbr`、`texture_prompt`、`texture_image` 與 `texture_resolution` 輸入只有在 `should_texture` 設為 `"true"` 時才可用。

**限制條件：**

* `target_polycount` 是建構網格時使用的三角形數量，而不是生成後再套用的限制。
* 當 `should_texture` 設為 `"true"` 時，`texture_prompt` 與 `texture_image` 不能同時使用。若同時提供兩者，節點會引發錯誤。
* `texture_prompt` 的最大長度為 800 個字元。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `meshy_task_id` | Meshy API 任務的唯一識別碼。 | MESHY_TASK_ID |
| `GLB` | 以 GLB 格式產生的 3D 模型。 | FILE3DGLB |
| `FBX` | 以 FBX 格式產生的 3D 模型。 | FILE3DFBX |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelSmartTopologyNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e78034a591825ec6e105df1942cf501e882ac780cc2584bfa04b424ecc34a02e`
