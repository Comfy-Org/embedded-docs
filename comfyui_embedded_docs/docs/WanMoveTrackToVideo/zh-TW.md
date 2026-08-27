# WanMoveTrackToVideo

WanMoveTrackToVideo 節點準備影片生成的條件與潛在空間資料，並納入可選的運動追蹤資訊。它將起始影像序列編碼為潛在表示，並可混入物體軌跡的位置資料，以引導生成影片中的運動。此節點輸出修改後的正向與負向條件，以及一個可供影片模型使用的空潛在張量。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 要修改的正向條件輸入。 | CONDITIONING | 是 | - |
| `negative` | 要修改的負向條件輸入。 | CONDITIONING | 是 | - |
| `vae` | 用於將起始影像編碼到潛在空間的 VAE 模型。 | VAE | 是 | - |
| `軌跡` | 包含物體路徑的可選運動追蹤資料。 | TRACKS | 否 | - |
| `強度` | 軌跡條件的強度。（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `寬度` | 輸出影片的寬度。必須能被 16 整除。（預設值：832） | INT | 是 | 16 - MAX_RESOLUTION |
| `高度` | 輸出影片的高度。必須能被 16 整除。（預設值：480） | INT | 是 | 16 - MAX_RESOLUTION |
| `長度` | 影片序列中的幀數，以 4 為增量。（預設值：81） | INT | 是 | 1 - MAX_RESOLUTION |
| `批次大小` | 潛在輸出的批次大小。（預設值：1） | INT | 是 | 1 - 4096 |
| `起始影像` | 要編碼的起始影像或影像序列。 | IMAGE | 是 | - |
| `clip_vision_output` | 可選的 CLIP 視覺模型輸出，用於添加到條件中。 | CLIP_VISION_OUTPUT | 否 | - |

**注意：** `strength` 參數只有在提供了 `tracks` 且 `strength` 大於 0.0 時才有效；軌跡條件僅在同時提供 `start_image` 時才會套用。如果未提供 `tracks` 或 `strength` 為 0.0，則跳過軌跡混合。當軌跡混合啟用時，正向條件會接收軌跡混合後的潛在影像，而負向條件則接收未修改的潛在影像。如果未提供 `start_image`，則不會建立潛在影像與遮罩條件；正向與負向條件會原封不動地通過（除了仍會新增 `clip_vision_output`（若有的話）），且節點會輸出一個空的潛在張量。

**注意：** 當提供 `start_image` 時，影像序列會被調整為目標 `width` 與 `height`，並截斷為前 `length` 幀。如果序列比 `length` 短，剩餘的幀會在 VAE 編碼前以中性灰幀（數值 0.5）填充。產生的條件包含一個 `concat_mask`，其值在對應起始影像幀的時間位置為 0，在其他位置為 1。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 修改後的正向條件，可能包含 `concat_latent_image`、`concat_mask` 和 `clip_vision_output`。 | CONDITIONING |
| `negative` | 修改後的負向條件，可能包含 `concat_latent_image`、`concat_mask` 和 `clip_vision_output`。 | CONDITIONING |
| `latent` | 一個空的潛在張量，形狀為 `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`，由 `batch_size`、`length`、`height` 和 `width` 輸入決定。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
