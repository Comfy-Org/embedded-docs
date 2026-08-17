# WanAnimateToVideo

此實驗性節點透過結合參考影像與可選的姿勢、臉部及背景影片，來準備 Wan 影片生成。它會建立 conditioning 資料與空的潛在影片張量，以供後續生成使用，並回傳幀偏移資訊，協助以分塊方式擴展現有影片。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 用於引導生成朝向期望內容的正向 conditioning。 | CONDITIONING | 是 | - |
| `negative` | 用於引導生成避開不需要內容的負向 conditioning。 | CONDITIONING | 是 | - |
| `vae` | 用於編碼與解碼影像資料的 VAE 模型。 | VAE | 是 | - |
| `width` | 輸出影片寬度（像素）（預設值：832，間距：16）。 | INT | 是 | 16 至 MAX_RESOLUTION |
| `height` | 輸出影片高度（像素）（預設值：480，間距：16）。 | INT | 是 | 16 至 MAX_RESOLUTION |
| `length` | 要生成的幀數（預設值：77，間距：4）。 | INT | 是 | 1 至 MAX_RESOLUTION |
| `batch_size` | 一個批次中要生成的影片數量（預設值：1）。 | INT | 是 | 1 至 4096 |
| `clip_vision_output` | 可選的 CLIP vision 模型輸出，用作正向與負向 conditioning 的額外條件。 | CLIP_VISION_OUTPUT | 否 | - |
| `reference_image` | 用作生成起點的參考影像。若未提供，則使用黑色影像（全零）。 | IMAGE | 否 | - |
| `face_video` | 提供臉部表情引導的影片。處理時會調整為 512x512，並正規化至 -1.0 至 1.0 的範圍。 | IMAGE | 否 | - |
| `pose_video` | 提供姿勢與動作引導的影片。若其長度短於 `length`，則以最後一幀填補。 | IMAGE | 否 | - |
| `continue_motion_max_frames` | 從先前動作繼續的最大幀數。僅使用 `continue_motion` 的最後這些幀數（預設值：5，間距：4）。 | INT | 是 | 1 至 MAX_RESOLUTION |
| `background_video` | 要與生成內容合成的背景影片。 | IMAGE | 否 | - |
| `character_mask` | 定義角色區域以進行選擇性處理的遮罩。若遮罩只有一幀，則會重複套用至所有幀。 | MASK | 否 | - |
| `continue_motion` | 用於在擴展影片時維持時間一致性的先前動作序列。僅使用最後 `continue_motion_max_frames` 幀。 | IMAGE | 否 | - |
| `video_frame_offset` | 在所有輸入影片中要跳過的幀數。用於分塊生成較長影片。若要擴展影片，請連接到前一個節點的 video_frame_offset 輸出。（預設值：0，間距：1） | INT | 是 | 0 至 MAX_RESOLUTION |

**參數限制：**

- 當提供 `pose_video` 時，較短的姿勢影片會以最後一幀填補，以符合 `length`。原始碼包含一個 `trim_to_pose_video` 旗標，目前為停用；若啟用，則會縮短輸出以符合姿勢影片長度。
- `face_video` 會調整為 512x512，並正規化至 -1.0 至 1.0 的範圍。
- `continue_motion` 僅限於最後 `continue_motion_max_frames` 幀。使用 `continue_motion` 時，`video_frame_offset` 會減去所取的幀數，但不會低於 0。
- 輸入影片（`face_video`、`pose_video`、`background_video`、`character_mask`）會以 `video_frame_offset` 偏移。若偏移量等於或大於其長度，則忽略該輸入，但單幀的 `character_mask` 除外，它會被重複使用。
- 當提供 `clip_vision_output` 時，它會套用至正向與負向 conditioning。
- 若未提供 `reference_image`，則使用黑色影像（全零）作為參考。
- 若未提供 `continue_motion`，動作部分會使用像素值 0.5 的灰色幀。
- `width` 與 `height` 使用 16 的間距；對應的潛在維度為 `width / 8` 與 `height / 8`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `positive` | 修改後的正向 conditioning，一律包含拼接後的潛在影像與拼接後的遮罩。若提供了 `clip_vision_output`、`pose_video` 或 `face_video`，其數值也會一併加入。 | CONDITIONING |
| `negative` | 修改後的負向 conditioning，一律包含拼接後的潛在影像與拼接後的遮罩。若提供了 `clip_vision_output`、`pose_video` 或 `face_video`，其數值也會一併加入；臉部影片像素會設為 -1.0。 | CONDITIONING |
| `latent` | 初始化為零的空潛在張量，形狀為 `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]`。 | LATENT |
| `trim_latent` | 要從開頭修剪的潛在幀數，對應於參考影像的潛在幀。 | INT |
| `trim_image` | 要從開頭修剪的影像幀數，對應於參考動作幀。 | INT |
| `video_frame_offset` | 更新後的幀偏移，用於分塊影片生成，等於調整後的輸入偏移加上生成的長度。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
