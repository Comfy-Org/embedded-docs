# MoGe 推論

對單一影像執行 MoGe 以估算深度與幾何。此節點會透過 MoGe 模型處理輸入影像，以產生 3D 點雲、深度圖、相機內部參數、遮罩及表面法向量。

## 輸入

| 參數 | 描述 | 資料型態 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `moge_model` | 用於推論的 MoGe 模型。 | MOGE_MODEL | 是 | N/A |
| `image` | 用於深度與幾何估算的輸入影像。僅使用 RGB 通道；任何 alpha 通道都會被忽略。 | IMAGE | 是 | N/A |
| `resolution_level` | 控制處理解析度。0 最快，9 提供最多細節。（預設值：9） | INT | 是 | 0 至 9 |
| `fov_x_degrees` | （進階）來源相機的水平視野，單位為度。設定用於將深度圖反投影至 3D 的焦距。設為 0.0 則自動從預測點還原視野。（預設值：0.0） | FLOAT | 是 | 0.0 至 170.0 |
| `batch_size` | 每次推論呼叫所處理的影像數量。若在處理長影片或大型影像集時記憶體不足，請調低此值。（預設值：4） | INT | 是 | 1 至 64 |
| `force_projection` | （進階）強制對預測點進行投影。（預設值：True） | BOOLEAN | 是 | True/False |
| `apply_mask` | （進階）啟用時，會將遮罩涵蓋的（天空或無效）像素在點雲與深度輸出中設為無限遠。這有助於網格化工具忽略這些區域。停用以保留所有位置的原始預測幾何；遮罩仍會單獨回傳。（預設值：True） | BOOLEAN | 是 | True/False |

注意：`image` 輸入可包含多張影像。此節點會以 `batch_size` 為一組進行處理，並將結果合併為單一輸出。

## 輸出

| 輸出名 | 描述 | 資料型態 |
| --- | --- | --- |
| `moge_geometry` | 包含估算幾何的字典。它永遠包含輸入的 `image`（僅 RGB 通道），並可能包含 `points`（3D 點雲）、`depth`（深度圖）、`intrinsics`（相機內部參數矩陣）、`mask`（標示有效像素的遮罩）及 `normal`（表面法向量）。 | MOGE_GEOMETRY |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/zh-TW.md)

---
**Source fingerprint (SHA-256):** `59f6b8b1ab65147a47f5dc7ebee7b965a5ab37c6a0843a2c80d50c767ad98db4`
