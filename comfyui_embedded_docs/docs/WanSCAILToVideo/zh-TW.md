# WanSCAILToVideo

WanSCAILToVideo 節點用於準備影片生成的條件化（conditioning）與空潛在空間。它處理可選輸入，如參考影像、姿態影片和 CLIP 視覺輸出，將它們嵌入到影片模型的正向與負向條件化中。此節點輸出修改後的條件化以及指定影片尺寸的空白潛在張量。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 正向條件化輸入。 | CONDITIONING | 是 | - |
| `負向` | 負向條件化輸入。 | CONDITIONING | 是 | - |
| `vae` | 用於編碼影像和影片幀的 VAE 模型。 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素），預設值：512。必須能被 8 整除。 | INT | 是 | 32 至 MAX_RESOLUTION |
| `高度` | 輸出影片的高度（像素），預設值：896。必須能被 8 整除。 | INT | 是 | 32 至 MAX_RESOLUTION |
| `長度` | 影片的幀數，預設值：81。必須能被 4 整除。 | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 每批次生成的影片數量，預設值：1。 | INT | 是 | 1 至 4096 |
| `clip_vision_output` | 可選的 CLIP 視覺輸出，用於條件化。 | CLIP_VISION_OUTPUT | 否 | - |
| `參考圖片` | 可選的參考影像，用於條件化。 | IMAGE | 否 | - |
| `姿勢影片` | 用於姿態條件化的影片。將被縮小至主影片解析度的一半。 | IMAGE | 否 | - |
| `姿勢強度` | 姿態潛在的強度，預設值：1.0。 | FLOAT | 是 | 0.0 至 10.0 |
| `姿勢起始步驟` | 開始使用姿態條件化的步驟，預設值：0.0。 | FLOAT | 是 | 0.0 至 1.0 |
| `姿勢結束步驟` | 結束使用姿態條件化的步驟，預設值：1.0。 | FLOAT | 是 | 0.0 至 1.0 |

**注意：** `pose_video` 輸入僅處理前 `length` 幀。`reference_image` 僅處理批次中的第一張影像。當提供了 `reference_image` 時，負向條件化會使用相同大小的零填充潛在。當提供了 `clip_vision_output` 時，它會同時應用於正向和負向條件化。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `正向` | 修改後的正向條件化，可能包含嵌入的參考影像潛在、CLIP 視覺輸出或姿態影片潛在。 | CONDITIONING |
| `負向` | 修改後的負向條件化，可能包含嵌入的參考影像潛在、CLIP 視覺輸出或姿態影片潛在。 | CONDITIONING |
| `latent` | 形狀為 `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]` 的空白潛在張量。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `63de4b6fe41fc23ea81c21965a2dbfc82120bb1bad6785b2130af824e015fbcb`
