# WanMoveTrackToVideo

WanMoveTrackToVideo 節點為影片生成準備 conditioning 與潛在資料。它使用 VAE 將起始影像序列編碼到潛在空間，並可選擇性地納入運動追蹤資訊，以引導生成影片中的物體移動。此節點輸出修改後的正向與負向 conditioning，以及準備好供影片生成模型使用的空潛在張量。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 要修改的正向 conditioning 輸入。 | CONDITIONING | 是 | - |
| `negative` | 要修改的負向 conditioning 輸入。 | CONDITIONING | 是 | - |
| `vae` | 用於將起始影像編碼到潛在空間的 VAE 模型。 | VAE | 是 | - |
| `tracks` | 選用的運動追蹤資料，包含物體路徑。 | TRACKS | 否 | - |
| `strength` | 軌跡 conditioning 的強度。僅在提供 `tracks` 且數值大於 0.0 時有效。（預設值：1.0） | FLOAT | 是 | 0.0 - 100.0 |
| `width` | 輸出影片的寬度。以 16 的倍數設定。（預設值：832） | INT | 是 | 16 - MAX_RESOLUTION |
| `height` | 輸出影片的高度。以 16 的倍數設定。（預設值：480） | INT | 是 | 16 - MAX_RESOLUTION |
| `length` | 影片序列的影格數。以 4 的倍數設定。（預設值：81） | INT | 是 | 1 - MAX_RESOLUTION |
| `batch_size` | 潛在輸出的批次大小。（預設值：1） | INT | 是 | 1 - 4096 |
| `start_image` | 要用 VAE 編碼的起始影像或影像序列。 | IMAGE | 是 | - |
| `clip_vision_output` | 選用的 CLIP 視覺模型輸出，用於加入 conditioning。 | CLIP_VISION_OUTPUT | 否 | - |

注意：基於軌跡的運動僅在提供 `tracks` 且 `strength` 大於 0.0 時才會套用。否則，conditioning 會接收未修改的已編碼起始影像。`start_image` 用於建立潛在影像與 conditioning 遮罩；若 `start_image` 無法取得，此節點僅會傳遞 conditioning 並輸出空的潛在張量。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 修改後的正向 conditioning，可能包含 `concat_latent_image`、`concat_mask` 與 `clip_vision_output`。 | CONDITIONING |
| `negative` | 修改後的負向 conditioning，可能包含 `concat_latent_image`、`concat_mask` 與 `clip_vision_output`。 | CONDITIONING |
| `latent` | 一個空的潛在張量，其維度由 `batch_size`、`length`、`height` 與 `width` 輸入決定。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
