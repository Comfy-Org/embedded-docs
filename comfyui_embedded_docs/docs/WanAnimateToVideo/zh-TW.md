# WanAnimateToVideo

WanAnimateToVideo 準備條件資料與初始潛在張量，用於透過 Wan 生成動畫影片。它使用參考影像、姿態、臉部、背景以及可選的先前區塊動作作為輸入。此外，它也支援透過讀取並更新 `video_frame_offset` 數值，以分塊方式生成更長的影片。此節點標記為實驗性。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正面提示詞` | 正向條件，用於引導生成朝向期望內容。 | CONDITIONING | 是 | - |
| `負面提示` | 負向條件，用於引導生成避開不希望出現的內容。 | CONDITIONING | 是 | - |
| `VAE` | 用於將影像與影片輸入編碼至潛在空間的 VAE 模型。 | VAE | 是 | - |
| `寬度` | 生成影片的寬度，單位為像素（預設：832，間距：16）。 | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 生成影片的高度，單位為像素（預設：480，間距：16）。 | INT | 是 | 16 至 MAX_RESOLUTION |
| `長度` | 要生成的幀數（預設：77，間距：4）。 | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 一次批次生成的影片數量（預設：1）。 | INT | 是 | 1 至 4096 |
| `CLIP視覺輸出` | 可選的 CLIP 視覺輸出，會加入正向與負向條件中。 | CLIP_VISION_OUTPUT | 否 | - |
| `參考圖像` | 作為生成影片外觀起點的參考影像。若未提供，則使用黑色影像。 | IMAGE | 否 | - |
| `臉部影片` | 提供臉部表情引導的影片輸入。內部會調整為 512x512，並縮放至 -1.0 至 1.0 的範圍。 | IMAGE | 否 | - |
| `姿勢影片` | 提供姿態與動作引導的影片輸入。 | IMAGE | 否 | - |
| `連續動作最大幀數` | 從先前動作序列延續的最大幀數（預設：5，間距：4）。 | INT | 是 | 1 至 MAX_RESOLUTION |
| `背景影片` | 用於填補幀中非角色部分的背景影片。 | IMAGE | 否 | - |
| `角色遮罩` | 定義角色區域的遮罩，用於將角色與背景分離。 | MASK | 否 | - |
| `連續動作` | 要延續的先前動作幀，用於保持與先前生成區塊的時間一致性。 | IMAGE | 否 | - |
| `影片幀偏移` | 在所有輸入影片中要跳過的幀數偏移量。用於以分塊方式生成更長的影片。連接到前一個節點的 `video_frame_offset` 輸出即可延長影片。（預設：0，間距：1） | INT | 是 | 0 至 MAX_RESOLUTION |

**參數限制：**

- 當提供 `continue_motion` 時，僅使用其最後的 `continue_motion_max_frames` 幀。
- 輸入影片（`face_video`、`pose_video`、`background_video`、`character_mask`）在使用前會依 `video_frame_offset` 進行偏移。若偏移量大於或等於輸入的幀數，則該輸入會被忽略，但單幀 `character_mask` 除外。
- 若 `character_mask` 只有一幀，則該幀會重複用於輸出的每一幀。
- 當 `pose_video` 比 `length` 短時，其最後一幀會重複以填補剩餘幀數；輸出長度不會改變。
- 若提供了 `clip_vision_output`，它會同時加入正向與負向條件。
- 若未提供 `reference_image`，則使用黑色影像（全零值）作為預設參考。
- 若未提供 `continue_motion`，則初始動作幀會以常數灰色（強度 0.5）幀填充。
- 使用 `continue_motion` 時，`video_frame_offset` 會在計算下一個區塊偏移量前先減去已延續的幀數，以避免重複處理重疊幀。
- `background_video` 會填補參考動作部分之後的動作幀；它不會取代參考影像或已延續的 `continue_motion` 幀。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `正面提示` | 修改後的正向條件，包含額外的影片上下文，包括 CLIP 視覺輸出、姿態影片潛在張量、臉部影片像素、串接後的潛在影像以及串接後的遮罩。 | CONDITIONING |
| `負面提示` | 修改後的負向條件，包含額外的影片上下文，包括 CLIP 視覺輸出、姿態影片潛在張量、空白臉部像素、串接後的潛在影像以及串接後的遮罩。 | CONDITIONING |
| `潛在空間` | 生成影片的初始潛在張量（全零樣本），形狀為 `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]`。 | LATENT |
| `修剪潛在空間` | 要從潛在張量開頭裁掉的潛在幀數，對應於參考影像幀。 | INT |
| `修剪圖像` | 要從開頭裁掉的影像幀數，對應於參考動作幀。 | INT |
| `影片幀偏移` | 更新後的幀偏移量，用於下一個區塊，根據輸入偏移量與已處理的幀數計算。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
