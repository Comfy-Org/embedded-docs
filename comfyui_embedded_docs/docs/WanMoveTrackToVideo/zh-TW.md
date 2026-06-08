## 概述

WanMoveTrackToVideo 節點為影片生成準備條件化（conditioning）與潛在空間（latent space）資料，並可整合選擇性的運動追蹤資訊。它會將起始影像序列編碼為潛在表示，並可將來自物體軌跡的位置資料混合進來，以引導生成影片中的運動。該節點會輸出修改後的正向與負向條件化資料，以及一個準備好供影片模型使用的空潛在張量。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 待修改的正向條件化輸入。 | CONDITIONING | 是 | - |
| `negative` | 待修改的負向條件化輸入。 | CONDITIONING | 是 | - |
| `vae` | 用於將起始影像編碼至潛在空間的 VAE 模型。 | VAE | 是 | - |
| `軌跡` | 選擇性的運動追蹤資料，包含物體路徑。 | TRACKS | 否 | - |
| `強度` | 軌跡條件化的強度。（預設值：1.0） | FLOAT | 否 | 0.0 - 100.0 |
| `寬度` | 輸出影片的寬度。必須能被 16 整除。（預設值：832） | INT | 否 | 16 - MAX_RESOLUTION |
| `高度` | 輸出影片的高度。必須能被 16 整除。（預設值：480） | INT | 否 | 16 - MAX_RESOLUTION |
| `長度` | 影片序列的影格數。（預設值：81） | INT | 否 | 1 - MAX_RESOLUTION |
| `批次大小` | 潛在輸出的批次大小。（預設值：1） | INT | 否 | 1 - 4096 |
| `起始影像` | 要編碼的起始影像或影像序列。 | IMAGE | 是 | - |
| `clip_vision_output` | 選擇性的 CLIP 視覺模型輸出，用於添加到條件化資料中。 | CLIPVISIONOUTPUT | 否 | - |

**注意：** `strength` 參數僅在提供 `tracks` 時才有效。如果未提供 `tracks` 或 `strength` 為 0.0，則不會套用軌跡條件化。`start_image` 用於建立條件化所需的潛在影像與遮罩；如果未提供，該節點僅會傳遞條件化資料並輸出一個空的潛在張量。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `negative` | 修改後的正向條件化資料，可能包含 `concat_latent_image`、`concat_mask` 與 `clip_vision_output`。 | CONDITIONING |
| `latent` | 修改後的負向條件化資料，可能包含 `concat_latent_image`、`concat_mask` 與 `clip_vision_output`。 | CONDITIONING |
| `latent` | 一個空的潛在張量，其維度由 `批次大小`、`長度`、`高度` 與 `寬度` 輸入決定。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9677addf5b94b42efd3015f51380c1fa9b16d4a5105cc7f24de0be34c0042bbc`
