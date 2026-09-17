# MoGe 推論

在單一影像上執行 MoGe，以估算深度與幾何。此節點會透過 MoGe 模型處理輸入影像，以產生 3D 點雲、深度圖、相機內參、遮罩與表面法線。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `moge_model` | 用於推論的 MoGe 模型。 | MOGE_MODEL | 是 | N/A |
| `image` | 用於深度與幾何估算的輸入影像。僅使用前三個色彩通道（RGB）。 | IMAGE | 是 | N/A |
| `resolution_level` | 控制處理解析度。0 = 最快，9 = 最精細。（預設值：9） | INT | 是 | 0 至 9 |
| `fov_x_degrees` | （進階）來源相機的水平視野。設定用於將深度圖反投影至 3D 的焦距。0 = 從預測點自動還原。（預設值：0.0） | FLOAT | 是 | 0.0 至 170.0 (步進值 0.1) |
| `batch_size` | 每次推論呼叫的影像數量。若在長時間影片／影像集上遇到 OOM，請降低此值。（預設值：4） | INT | 是 | 1 至 64 |
| `force_projection` | （進階）強制投影預測點。（預設值：True） | BOOLEAN | 是 | True/False |
| `apply_mask` | （進階）將被遮罩（天空／無效）的像素在 points 和 depth 中設為 inf，以便網格化時將它們剔除。停用此選項可保留各處的原始預測幾何；遮罩仍會單獨回傳。（預設值：True） | BOOLEAN | 是 | True/False |
| `refine_steps` | （進階）僅限 MoGe-3：對預測深度執行稀疏體積細化迭代。更多迭代會以大致線性的成本銳化細節與邊緣。0 會停用細化。MoGe-1 / MoGe-2 會忽略此參數。（預設值：3） | INT | 是 | 0 至 8 |

注意：當輸入 `image` 包含的影格數多於 `batch_size` 時，此節點會以多次推論呼叫處理它們，並將結果合併為單一輸出幾何。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `moge_geometry` | 包含估算幾何的字典。它包含原始 `image`，並可能包含 `points`（3D 點雲）、`depth`（深度圖）、`intrinsics`（相機內參矩陣）、`mask`（識別有效像素的遮罩）與 `normal`（表面法線）。 | MOGE_GEOMETRY |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/zh-TW.md)

---
**Source fingerprint (SHA-256):** `10f3399d9b6bc4ff8a940c940f538a8ec8f38a15e7d65f162499c5ab264fad65`
