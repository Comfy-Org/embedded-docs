# MoGe 推論

在單張影像上執行 MoGe 以估計深度與幾何形狀。此節點透過 MoGe 模型處理輸入影像，以產生 3D 點雲、深度圖、相機內參、遮罩以及表面法向量。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `moge_model` | 用於推論的 MoGe 模型。 | MOGE_MODEL | 是 | N/A |
| `image` | 用於深度與幾何形狀估計的輸入影像。僅使用前三個色彩通道（RGB）。 | IMAGE | 是 | N/A |
| `resolution_level` | 控制處理解析度。0 最快，9 提供最多細節。（預設值：9） | INT | 是 | 0 至 9 |
| `fov_x_degrees` | （進階）來源相機的水平視野（以度為單位）。設定用於將深度圖反投影至 3D 的焦距。設定為 0.0 可從預測點自動恢復視野。（預設值：0.0） | FLOAT | 是 | 0.0 至 170.0 |
| `batch_size` | 每次推論呼叫的影像數量。若在長影片或大量影像集上記憶體不足，請降低此值。（預設值：4） | INT | 是 | 1 至 64 |
| `force_projection` | （進階）強制投影預測的點。（預設值：True） | BOOLEAN | 是 | True/False |
| `apply_mask` | （進階）將遮罩區域（天空或無效）的像素在點與深度輸出中設為無限大，以便網格化工具忽略它們。停用則在所有位置保留原始預測幾何；遮罩仍會單獨回傳。（預設值：True） | BOOLEAN | 是 | True/False |

注意：當輸入 `image` 包含的幀數多於 `batch_size` 時，節點會以多次推論呼叫處理這些幀，並將結果合併為單一輸出幾何。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `moge_geometry` | 包含估計幾何的字典。其中包含原始 `image`，並可能包含 `points`（3D 點雲）、`depth`（深度圖）、`intrinsics`（相機內參矩陣）、`mask`（識別有效像素的遮罩）以及 `normal`（表面法向量）。 | MOGE_GEOMETRY |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/zh-TW.md)

---
**Source fingerprint (SHA-256):** `59f6b8b1ab65147a47f5dc7ebee7b965a5ab37c6a0843a2c80d50c767ad98db4`
