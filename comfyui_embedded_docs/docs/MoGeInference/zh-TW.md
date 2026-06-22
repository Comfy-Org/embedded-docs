# MoGe 推論

## 概述

對單張影像執行 MoGe 模型以估算深度與幾何結構。此節點透過 MoGe 模型處理輸入影像，生成 3D 點雲、深度圖、相機內參、遮罩以及表面法向量。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `moge_model` | 用於推論的 MoGe 模型。 | MOGE_MODEL | 是 | 不適用 |
| `image` | 用於深度與幾何估算的輸入影像。 | IMAGE | 是 | 不適用 |
| `resolution_level` | 控制處理解析度。0 為最快，9 提供最多細節。（預設值：9） | INT | 是 | 0 至 9 |
| `fov_x_degrees` | 來源相機的水平視野角度（度）。設定用於將深度圖反投影至 3D 的焦距。設為 0.0 可從預測點自動還原視野。（預設值：0.0） | FLOAT | 是 | 0.0 至 170.0 |
| `batch_size` | 每次推論呼叫處理的影像數量。若處理長影片或大型影像集時記憶體不足，請調低此值。（預設值：4） | INT | 是 | 1 至 64 |
| `force_projection` | （進階）強制投影預測點。（預設值：True） | BOOLEAN | 是 | True/False |
| `apply_mask` | 啟用時，將遮罩區域（天空或無效區域）的像素設為點雲與深度輸出中的無限遠值。這有助於網格工具忽略這些區域。停用則保留所有位置的原始預測幾何；遮罩仍會單獨回傳。（預設值：True） | BOOLEAN | 是 | True/False |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `moge_geometry` | 包含估算幾何結構的字典。其中包括原始 `image`，並可能包含 `points`（3D 點雲）、`depth`（深度圖）、`intrinsics`（相機內參矩陣）、`mask`（標示有效像素的遮罩）以及 `normal`（表面法向量）。 | MOGE_GEOMETRY |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGeInference/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5213b280513850eeef2e22ae723ebb015789109435e28ddd79f91f9a4b4a1e79`
